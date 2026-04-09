# Claude Code Prompt Catalog

本目录用于整理这个仓库中与 Claude Code 行为直接相关的提示词。

说明：
- 这里采用“按类型聚合”的方式整理，而不是“一条 prompt 一个文件”。
- 内容以“摘录+整理”为主，重点保留真正影响模型行为的核心指令。
- 对于已经单独提取的协调者提示词，直接沿用仓库根目录已有文件：
  - `coordinate_prompt.md`
  - `coordinate_prompt.zh-CN.md`

目录结构：
- `system_prompts.en.md`
  - 主系统提示词、CLI 前缀、输出风格提示词等英文摘录
- `system_prompts.zh-CN.md`
  - 上述内容的中文翻译
- `agent_prompts.en.md`
  - AgentTool、本地内置 agent、子代理补充提示的英文摘录
- `agent_prompts.zh-CN.md`
  - 上述内容的中文翻译
- `tool_prompts.en.md`
  - 各类工具提示词的英文摘录
- `tool_prompts.zh-CN.md`
  - 上述内容的中文翻译
- `service_prompts.en.md`
  - 压缩总结、会话记忆、Magic Docs、提示建议等后台 prompt 的英文摘录
- `service_prompts.zh-CN.md`
  - 上述内容的中文翻译
- `prompt_orchestration.zh-CN.md`
  - Claude Code 对提示词的注入、选择、编排链路说明

分类范围：

1. 系统提示词
- `restored-src/src/constants/system.ts`
- `restored-src/src/constants/prompts.ts`
- `restored-src/src/constants/outputStyles.ts`
- `restored-src/src/coordinator/coordinatorMode.ts`（已单独提取）

2. Agent / Subagent 提示词
- `restored-src/src/tools/AgentTool/prompt.ts`
- `restored-src/src/tools/AgentTool/built-in/generalPurposeAgent.ts`
- `restored-src/src/tools/AgentTool/built-in/exploreAgent.ts`
- `restored-src/src/tools/AgentTool/built-in/planAgent.ts`
- `restored-src/src/tools/AgentTool/built-in/verificationAgent.ts`
- `restored-src/src/tools/AgentTool/built-in/claudeCodeGuideAgent.ts`
- `restored-src/src/tools/AgentTool/built-in/statuslineSetup.ts`
- `restored-src/src/constants/prompts.ts` 中的 `DEFAULT_AGENT_PROMPT` 与 `enhanceSystemPromptWithEnvDetails`

3. 工具提示词
- `restored-src/src/tools/*/prompt.ts`

4. 后台 / 辅助 prompt
- `restored-src/src/services/compact/prompt.ts`
- `restored-src/src/services/SessionMemory/prompts.ts`
- `restored-src/src/services/MagicDocs/prompts.ts`
- `restored-src/src/services/extractMemories/prompts.ts`
- `restored-src/src/services/awaySummary.ts`
- `restored-src/src/services/AgentSummary/agentSummary.ts`
- `restored-src/src/services/toolUseSummary/toolUseSummaryGenerator.ts`
- `restored-src/src/services/PromptSuggestion/promptSuggestion.ts`
- `restored-src/src/services/autoDream/consolidationPrompt.ts`
- `restored-src/src/utils/claudeInChrome/prompt.ts`
- `restored-src/src/buddy/prompt.ts`
