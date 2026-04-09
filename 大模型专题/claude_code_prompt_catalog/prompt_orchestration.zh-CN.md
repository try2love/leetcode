# Claude Code 提示词应用编排

本文档说明这个仓库里的提示词是如何被选择、拼装、注入和运行的。

## 1. 先区分四种“提示词”

Claude Code 里并不是只有一种 prompt。至少要分清下面几层：

1. 主 system prompt
- 决定 Claude Code 主线程的人格、行为边界、工具使用原则、输出风格。
- 主要来自：
  - `restored-src/src/constants/system.ts`
  - `restored-src/src/constants/prompts.ts`
  - `restored-src/src/constants/outputStyles.ts`

2. 工具 prompt / 工具描述
- 不是 system prompt。
- 它们会随着工具 schema 一起提供给模型，用于告诉模型“这个工具什么时候用、怎么用”。
- 主要来自 `restored-src/src/tools/*/prompt.ts`

3. agent / subagent prompt
- 当 Claude Code 启动子代理时，子代理会有自己的 system prompt。
- 可能是默认 agent prompt，也可能是某个内置 agent 的专属 system prompt。
- 主要来自：
  - `restored-src/src/tools/AgentTool/prompt.ts`
  - `restored-src/src/tools/AgentTool/built-in/*.ts`
  - `restored-src/src/constants/prompts.ts` 中的 `DEFAULT_AGENT_PROMPT`

4. 后台 side-query / 辅助 prompt
- 这些不是主对话 system prompt，而是后台任务或旁路功能用的 prompt。
- 例如：
  - 对话压缩总结
  - Session Memory 更新
  - Magic Docs 更新
  - 提示建议
  - agent 进度摘要
  - away summary

## 2. 主线程 system prompt 的生成链路

交互式主线程的 system prompt 生成链路大致如下：

1. `screens/REPL.tsx`
- 每轮 query 前调用 `getSystemPrompt(...)` 生成默认 system prompt 片段。
- 同时还会加载 userContext 和 systemContext。

2. `utils/systemPrompt.ts`
- `buildEffectiveSystemPrompt(...)` 决定最终采用哪套 system prompt。
- 优先级如下：
  1. `overrideSystemPrompt`
  2. coordinator mode prompt
  3. main-thread agent prompt
  4. `customSystemPrompt`
  5. 默认 `getSystemPrompt(...)`

3. `services/api/claude.ts`
- 在真正发 API 之前，再在最前面拼接：
  - attribution header
  - CLI 身份前缀（`getCLISyspromptPrefix(...)`）
  - advisor tool instructions（如果开启）
  - chrome tool search instructions（如果需要）
- 然后通过 `buildSystemPromptBlocks(...)` 变成真正送给模型的 system blocks。

换句话说，主线程 system prompt 不是某一个文件里的单独长字符串，而是“多段拼装后的结果”。

## 3. 主线程 system prompt 的选择逻辑

### 3.1 默认模式

默认情况下，主线程 system prompt 来自 `constants/prompts.ts -> getSystemPrompt(...)`。

它会包含这些层：
- 身份与总目标
- 系统行为规则
- 做任务的规则
- 风险操作的处理原则
- 工具使用原则
- 语气和输出规则
- 动态段落（语言、output style、MCP、环境信息等）

### 3.2 Coordinator Mode

如果开启 coordinator mode：
- `buildEffectiveSystemPrompt(...)` 会改用 `coordinatorMode.ts -> getCoordinatorSystemPrompt()`
- 此时主线程不再走普通默认 system prompt 作为主干，而是使用协调者专用 prompt
- 这也是为什么 `coordinate_prompt.md` 是一份完整、独立、可读性很强的 prompt

### 3.3 Main-thread Agent

如果当前主线程不是普通 Claude Code，而是某个 agent definition：
- `buildEffectiveSystemPrompt(...)` 会使用该 agent 的 `getSystemPrompt()`

在 proactive 模式下还有一个特殊规则：
- agent prompt 不是替换默认 prompt
- 而是作为 `# Custom Agent Instructions` 追加到默认 prompt 之后

### 3.4 Custom / Append Prompt

还有两类运行时附加：
- `customSystemPrompt`
  - 直接替换默认主提示逻辑中的默认部分
- `appendSystemPrompt`
  - 追加到最终 prompt 末尾

`appendSystemPrompt` 的典型来源之一：
- `main.tsx` 在自动启用 `claude-in-chrome` 时，会把 skill hint 追加进去

## 4. 非交互模式与 print/headless 的差异

在 `main.tsx` 里可以看到：
- 非交互模式下，如果指定了 main-thread custom agent，而且不是 built-in agent
- 会直接把 agent 的 `getSystemPrompt()` 塞进 `systemPrompt`

也就是说：
- 交互式模式更依赖 `buildEffectiveSystemPrompt(...)`
- 非交互式模式有一部分路径会更早地直接设置 system prompt

## 5. 工具 prompt 是怎么注入的

工具 prompt 不会进入主 system prompt 正文。

它们的注入方式是：

1. `tools.ts` / tool pool 组装工具列表
2. 每个工具对象暴露出自己的 description / prompt
3. `services/api/claude.ts` 在发请求时把工具 schema 一起送给模型

因此模型同时看到两类东西：
- system prompt：告诉它“应该怎么当 Claude Code”
- tool schema / tool prompt：告诉它“某个工具是什么、什么时候用、怎么用”

这也是为什么：
- `BashTool/prompt.ts`
- `FileReadTool/prompt.ts`
- `SkillTool/prompt.ts`
- `EnterPlanModeTool/prompt.ts`

这些文件不会直接出现在主 system prompt 里，但仍然强烈影响模型行为。

## 6. Deferred Tools 与 ToolSearch 的特殊机制

不是所有工具一开始都带完整 schema。

当工具被标记为 deferred 时：
- 初始阶段模型可能只知道这个工具“存在”
- 但并不知道它的完整参数 schema
- 这时需要先调用 `ToolSearch`

对应链路：
- `tools/ToolSearchTool/prompt.ts`
- `services/toolSearch` 相关逻辑

典型例子：
- 某些 MCP 工具
- Claude in Chrome 工具

这就形成了一条两阶段注入链：

1. 先在上下文里告诉模型：“有这些延迟工具存在”
2. 再通过 ToolSearch 把具体 schema 拉进来

## 7. Attachment 形式的“软提示”

Claude Code 还有一批不是 system prompt、也不是 tool schema 的提示，会通过 attachment / reminder 注入：

### 7.1 agent listing delta

来源：
- `utils/attachments.ts`
- `tools/AgentTool/prompt.ts`

作用：
- 把当前可用 agent 列表作为 attachment 提醒给模型
- 避免 agent 列表频繁变化导致主 prompt cache 被打爆

### 7.2 MCP instructions delta

来源：
- `utils/attachments.ts`

作用：
- 把 MCP server 的 instructions 增量注入为 attachment
- 某些 chrome tool-search 指令也会走这里，而不是直接塞进 system prompt

### 7.3 output style attachment / reminder

输出风格除了在 system prompt 中体现，还可能以附件或上下文形式提示模型当前风格已激活。

### 7.4 companion intro

来源：
- `buddy/prompt.ts`

作用：
- 如果启用 companion/buddy，会插入 companion intro attachment
- 这不是新的主 prompt，而是补充行为提醒

## 8. 子代理 prompt 的编排

子代理主要走 `tools/AgentTool/runAgent.ts`。

### 8.1 普通 subagent

`runAgent(...)` 里会决定 agent 的 system prompt：

优先级：
1. `override.systemPrompt`
2. `getAgentSystemPrompt(...)`
3. 默认 `DEFAULT_AGENT_PROMPT`

然后再通过 `enhanceSystemPromptWithEnvDetails(...)` 追加：
- 绝对路径规则
- 不要 emoji
- 环境信息
- 语言 / output style / discover-skills 等补充

### 8.2 Fresh agent

如果是 fresh agent：
- 它看不到父对话
- 因此 prompt 必须完整自包含

这也是 `AgentTool/prompt.ts` 一直强调：
- 不能写“based on your findings”
- 不能把“理解工作”外包给 agent

### 8.3 Fork agent

如果是 fork：
- 它继承父上下文
- 更关键的是，它会继承父线程“已经渲染好的 system prompt”

这样做的目的：
- 让 fork 与主线程共享 prompt cache
- 避免因为重新构造 prompt 导致 cache key 不一致

因此 fork 不是“另一个 fresh subagent”，而是“带着原 prompt 上下文分叉出去的一条支线”

## 9. 后台 prompt 的编排方式

后台 prompt 大多不替换主线程 system prompt，而是通过“fork / side-query”运行。

### 9.1 Compact Prompt

来源：
- `services/compact/prompt.ts`

用途：
- 当上下文需要压缩时，生成一段高保真摘要

特点：
- 这是一个独立的 summarization prompt
- 不是主线程 system prompt 的一部分

### 9.2 Session Memory Prompt

来源：
- `services/SessionMemory/prompts.ts`
- 调用点：`services/SessionMemory/sessionMemory.ts`

特点：
- 使用当前对话上下文
- 构造一个“请更新 session notes 文件”的 user prompt
- 通过 forked agent 执行
- 工具权限被限制为只允许改指定 memory 文件

### 9.3 Magic Docs Prompt

来源：
- `services/MagicDocs/prompts.ts`
- 调用点：`services/MagicDocs/magicDocs.ts`

特点：
- 根据当前 Magic Doc 内容生成更新 prompt
- 以异步 subagent 运行
- 工具权限只允许 Edit 那个 Magic Doc 文件

### 9.4 Extract Memories Prompt

来源：
- `services/extractMemories/prompts.ts`
- 调用点：`services/extractMemories/extractMemories.ts`

特点：
- 作为 memory extraction subagent 运行
- 使用 forked agent
- turn 数被硬性限制
- 只允许在 memory 目录内做受限读写

### 9.5 Away Summary Prompt

来源：
- `services/awaySummary.ts`

特点：
- 不是 system prompt
- 它直接作为一条额外 user message 插到 recent messages 后面
- 再调用小模型生成“用户离开回来时的简短 recap”

### 9.6 Agent Summary Prompt

来源：
- `services/AgentSummary/agentSummary.ts`

特点：
- 周期性 fork 子代理自己的上下文
- 用一句极短 prompt 生成“最近在干什么”的进度摘要

### 9.7 Prompt Suggestion Prompt

来源：
- `services/PromptSuggestion/promptSuggestion.ts`

特点：
- 作为 forked agent 的 user prompt 运行
- 不允许调用工具
- 只负责预测用户下一句自然输入

### 9.8 Tool Use Summary Prompt

来源：
- `services/toolUseSummary/toolUseSummaryGenerator.ts`

特点：
- 这是少数直接用“专门 system prompt”来做一类极小任务的例子
- 目标是生成移动端友好的短标签

### 9.9 Dream / Consolidation Prompt

来源：
- `services/autoDream/consolidationPrompt.ts`

特点：
- 用于 memory consolidation 场景
- 强调回看 memory 目录、近期 transcript，并整合成更持久的记忆文件

## 10. Claude in Chrome 提示词的注入位置

这套提示词比较特殊，有三种进入路径：

1. 启动时 hint
- `main.tsx`
- 自动启用扩展时，会把 `CLAUDE_IN_CHROME_SKILL_HINT` 或其 WebBrowser 变体追加到 `appendSystemPrompt`

2. request-time system append
- `services/api/claude.ts`
- 如果启用了 tool search 且当前有 chrome MCP 工具，而 MCP delta 附件没开
- 就把 `CHROME_TOOL_SEARCH_INSTRUCTIONS` 直接拼进 system prompt

3. attachment delta
- `utils/attachments.ts`
- 当 MCP instruction delta 开启时，chrome 的工具搜索指导会作为 attachment 注入，而不是 system prompt 正文

## 11. 一个核心结论：Claude Code 是“多层 prompt 编排”，不是“单 prompt 应用”

如果只盯着某一个 `prompt.ts` 文件，很容易误判行为来源。

Claude Code 的真实行为通常由下面几层共同决定：
- 主 system prompt
- CLI 前缀
- output style
- tool schema / tool prompt
- attachments / reminders
- subagent system prompt
- 某次 side-query 的 user prompt

所以你后续如果要做个性化改造，最好先判断你想改的是哪一层：

1. 想改主人格 / 主行为规则
- 主要看 `constants/prompts.ts`、`constants/system.ts`、`utils/systemPrompt.ts`

2. 想改某个工具什么时候被选中
- 主要看 `tools/*/prompt.ts`

3. 想改子代理行为
- 主要看 `AgentTool/prompt.ts`、`AgentTool/built-in/*.ts`

4. 想改压缩总结 / 记忆提取 / 文档维护
- 主要看 `services/*/prompts.ts` 及其调用点

5. 想改 chrome / MCP / attachment 提示
- 主要看 `utils/claudeInChrome/prompt.ts`、`utils/attachments.ts`
