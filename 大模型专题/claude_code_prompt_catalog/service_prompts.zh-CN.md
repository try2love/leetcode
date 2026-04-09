# 后台与辅助 Prompt

本文档整理 Claude Code 在总结、记忆、文档维护、提示建议及旁路能力中使用的 prompt 摘录。

## 1. 对话压缩 / 总结 Prompt
来源：
- `restored-src/src/services/compact/prompt.ts`

变体：
- `BASE_COMPACT_PROMPT`
- `PARTIAL_COMPACT_PROMPT`
- `PARTIAL_COMPACT_UP_TO_PROMPT`

核心摘录：
- 只能输出纯文本。
- 输出结构必须包含 `<analysis>` 和 `<summary>`。
- 摘要必须保留：
  - 用户请求与意图
  - 技术概念
  - 文件和代码片段
  - 错误与修复
  - 待办事项
  - 当前工作 / 下一步
- partial 变体只总结最近一段对话，或只总结即将被压缩掉的前缀部分。

## 2. Session Memory 模板与更新 Prompt
来源：
- `restored-src/src/services/SessionMemory/prompts.ts`

核心模板分区：
- Session Title
- Current State
- Task specification
- Files and Functions
- Workflow
- Errors & Corrections
- Codebase and System Documentation
- Learnings
- Key results
- Worklog

更新 prompt 摘录：
- 这条记笔记指令不是用户真实对话的一部分。
- 只能用 Edit 更新会话笔记文件。
- 必须原样保留 section header 和斜体模板说明。
- 内容要高密度、具体、可操作。
- “Current State” 必须始终反映最新状态。

## 3. Magic Docs 更新 Prompt
来源：
- `restored-src/src/services/MagicDocs/prompts.ts`

摘录：
- 只有在确实出现了有价值的新信息时，才更新 Magic Doc。
- 文档应始终反映代码库“当前状态”。
- 应就地更新，而不是追加变更历史。
- 重点写架构、入口点、设计动机、模式和导航价值。
- 不要写成穷举式函数说明文档。

## 4. 记忆提取 Prompt
来源：
- `restored-src/src/services/extractMemories/prompts.ts`

变体：
- `buildExtractAutoOnlyPrompt(...)`
- `buildExtractCombinedPrompt(...)`

摘录：
- 扮演记忆提取 subagent。
- 只能根据最近几条消息来更新持久化 memory。
- 不要跳出去做额外调查。
- 优先更新已有 memory 文件，不要制造重复项。
- 必须遵守 memory 类型与 frontmatter 规范。
- 启用 team memory 时，要谨慎选择 private / team 范围，且绝不能把敏感信息写入共享 memory。

## 5. Away Summary Prompt
来源：
- `restored-src/src/services/awaySummary.ts`

摘录：
- 用户离开后回来时，用 1-3 句短句做 recap。
- 先说明高层任务是什么。
- 再说明下一步具体要做什么。
- 不要写流水账式状态汇报，也不要复述 commit 记录。

## 6. Agent 进度摘要 Prompt
来源：
- `restored-src/src/services/AgentSummary/agentSummary.ts`

摘录：
- 用 3-5 个词描述最近动作。
- 使用现在进行式 / `-ing`。
- 说文件名或函数名，不要说分支名。
- 不要调用工具。
- 如果已经有上一条摘要，新摘要必须带来新信息。

## 7. Tool-Use Summary Prompt
来源：
- `restored-src/src/services/toolUseSummary/toolUseSummaryGenerator.ts`

摘录：
- 生成一条单行短标签，概括最近工具调用做成了什么。
- 主要服务于移动端列表，长度大约 30 字以内。
- 使用过去式和最有辨识度的名词。

## 8. Prompt Suggestion Prompt
来源：
- `restored-src/src/services/PromptSuggestion/promptSuggestion.ts`

摘录：
- 猜测用户“下一句自然会输入什么”。
- 目标是预测用户真的会打什么，而不是 Claude 希望用户做什么。
- 长度控制在 2-12 个词。
- 不要用评价性语言、Claude 口吻、凭空发散的新想法，也不要多句输出。
- 只能返回建议本身，或返回空。

## 9. Dream / 记忆整合 Prompt
来源：
- `restored-src/src/services/autoDream/consolidationPrompt.ts`

摘录：
- 对 memory 文件做一轮反思式整理。
- 先熟悉 memory 目录和最近 transcript。
- 把近期值得保留的信息整合成稳定的 topic memory。
- 删除冲突或过期信息。
- 保持 memory index 精简且便于导航。

## 10. Claude-in-Chrome Prompt 家族
来源：
- `restored-src/src/utils/claudeInChrome/prompt.ts`

### Base Chrome Prompt
摘录：
- 使用 Chrome 浏览器自动化工具执行网页交互。
- 对多步骤流程，在合适时录 GIF。
- 读取 console 时要尽量带过滤模式。
- 避免触发会阻塞扩展的浏览器模态框。
- 每次浏览器自动化会话开始时，先读取 tab 上下文。
- 如果自动化过程连续失败或越走越偏，应停止并向用户确认下一步。

### Chrome ToolSearch Instructions
摘录：
- 在调用任意 `mcp__claude-in-chrome__*` 工具之前，必须先通过 ToolSearch 把它加载出来。

### Claude-in-Chrome Skill Hints
摘录：
- 如果扩展存在，系统可能会在启动时追加一个 hint，提醒模型先调用 `claude-in-chrome` skill。
- 当 WebBrowser 也可用时，该 hint 会把开发回路任务导向 WebBrowser，而把 claude-in-chrome 留给需要真实登录态的用户 Chrome 会话。
