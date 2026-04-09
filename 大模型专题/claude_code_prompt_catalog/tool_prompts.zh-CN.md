# 工具提示词

本文档整理 Claude Code 各类工具在模型侧看到的提示词摘录。

说明：
- `AgentTool` 已在 `agent_prompts.zh-CN.md` 中单独整理。
- `MCPTool` 本身是空提示，占位而已；真正的 MCP 工具描述来自运行时连接到的 MCP server。

## 1. 文件与代码工具

### Read
来源：
- `restored-src/src/tools/FileReadTool/prompt.ts`

摘录：
- 用绝对路径读取本地文件。
- 可读取普通文件、图片、PDF（带页码限制）和 Jupyter notebook。
- 只能读文件，不能读目录。
- 如果用户给的是截图路径，应优先用 Read 查看。

### Write
来源：
- `restored-src/src/tools/FileWriteTool/prompt.ts`

摘录：
- 向本地文件系统写文件。
- 如果是改已有文件，必须先 Read。
- 修改已有文件时优先用 Edit，而不是 Write。
- 非明确要求，不要创建 markdown / README 文件。

### Edit
来源：
- `restored-src/src/tools/FileEditTool/prompt.ts`

摘录：
- 对文件执行精确字符串替换。
- 对话中至少先有一次 Read 才能 Edit。
- 必须严格保留原有缩进。
- `old_string` 要尽量短，但又必须足够唯一。
- 优先修改已有文件，不要轻易新建文件。

### Glob
来源：
- `restored-src/src/tools/GlobTool/prompt.ts`

摘录：
- 快速文件模式匹配工具。
- 支持 `**/*.js`、`src/**/*.ts` 这类 glob 模式。
- 适合按文件名模式查找文件。

### Grep
来源：
- `restored-src/src/tools/GrepTool/prompt.ts`

摘录：
- 基于 ripgrep 的强力文本搜索工具。
- 用于跨文件做内容搜索。
- 适合精确匹配和正则匹配。

### NotebookEdit
来源：
- `restored-src/src/tools/NotebookEditTool/prompt.ts`

摘录：
- 替换 / 插入 / 删除 Jupyter notebook 中的特定 cell。
- 使用绝对 notebook 路径和从 0 开始的 `cell_number`。

### LSP
来源：
- `restored-src/src/tools/LSPTool/prompt.ts`

摘录：
- 提供基于 LSP 的代码智能能力。
- 支持跳转定义、查引用、hover、符号、实现、调用层级等。
- 需要文件路径、行号和字符位置。

## 2. Shell、Web 与环境工具

### Bash
来源：
- `restored-src/src/tools/BashTool/prompt.ts`

摘录：
- 用于终端 / 系统命令，不应用来替代专用的文件读写工具。
- 支持后台运行。
- 含有大量 git 安全规则：
  - 不要跳过 hooks
  - 避免破坏性 git 命令
  - 不要默认 amend
  - 只有用户明确要求时才 commit
- 还包含使用 `gh` 创建 PR 的完整流程说明。

### PowerShell
来源：
- `restored-src/src/tools/PowerShellTool/prompt.ts`

摘录：
- 用于 PowerShell 下的终端工作，而不是文件操作。
- 会根据 PowerShell 版本注入不同语法指导。
- 支持后台执行。
- 明确禁止交互式 / 阻塞式 cmdlet。
- 再次强调：文件类操作优先用专用工具。

### WebFetch
来源：
- `restored-src/src/tools/WebFetchTool/prompt.ts`

摘录：
- 抓取 URL，把 HTML 转成 markdown，再交给一个小而快的模型分析。
- 输入包括 URL 和分析 prompt。
- 如果有 MCP 提供的 web fetch，应优先使用 MCP 版本。
- 对 GitHub URL，优先用 Bash + `gh`。

### WebSearch
来源：
- `restored-src/src/tools/WebSearchTool/prompt.ts`

摘录：
- 用于获取最新网页信息。
- 强制要求：回答后必须带 `Sources:` 段，并列出 markdown 链接。
- 搜索近期内容时必须用当前年月上下文。

### ToolSearch
来源：
- `restored-src/src/tools/ToolSearchTool/prompt.ts`

摘录：
- 为延迟加载工具补齐完整 schema，使其可调用。
- 支持精确选择和关键字搜索两种查询方式。
- 说明某些工具初始只会显示名字，没有参数 schema。

### Sleep
来源：
- `restored-src/src/tools/SleepTool/prompt.ts`

摘录：
- 等待一段时间。
- 应优先使用它，而不是 `Bash(sleep ...)`。
- 适合等待、休眠、或者配合其他后台工作。

### Config
来源：
- `restored-src/src/tools/ConfigTool/prompt.ts`

摘录：
- 获取或修改 Claude Code 配置项。
- 区分“查看当前值”和“设置新值”。
- 会列出全局配置、项目配置和模型选项。

### RemoteTrigger
来源：
- `restored-src/src/tools/RemoteTriggerTool/prompt.ts`

摘录：
- 通过 claude.ai API 管理远程触发器。
- 应优先用它，不要自己 curl，因为鉴权在进程内完成。
- 支持 list/get/create/update/run。

### ListMcpResources
来源：
- `restored-src/src/tools/ListMcpResourcesTool/prompt.ts`

摘录：
- 列出配置好的 MCP server 暴露出的资源。
- 每个资源都带所属 server 信息。

### ReadMcpResource
来源：
- `restored-src/src/tools/ReadMcpResourceTool/prompt.ts`

摘录：
- 按 server 名称和 URI 读取指定 MCP 资源。

### MCPTool
来源：
- `restored-src/src/tools/MCPTool/prompt.ts`

摘录：
- 空占位 prompt。
- 真正的 MCP 工具描述来自运行时连接的 MCP 服务器。

## 3. 工作流与沟通工具

### AskUserQuestion
来源：
- `restored-src/src/tools/AskUserQuestionTool/prompt.ts`

摘录：
- 在执行过程中向用户发起多选问题。
- 用于收集偏好、澄清歧义、让用户做实现决策。
- 在 plan mode 中，应用于“最终计划成形前”的澄清。
- 不要用它请求计划批准；计划批准应使用 ExitPlanMode。

### Skill
来源：
- `restored-src/src/tools/SkillTool/prompt.ts`

摘录：
- 在主对话中执行一个 skill。
- 如果当前可见 skill 明显匹配用户请求，那么先调用 Skill 是强制要求。
- 不要只提 skill 名字而不实际调用它。
- 不能用它执行内建 CLI 命令。

### SendMessage
来源：
- `restored-src/src/tools/SendMessageTool/prompt.ts`

摘录：
- 向另一个 agent 发送消息。
- 在某些模式下也支持跨 session 消息。
- 主要用于延续已有 worker，使其保留上下文继续工作。

### Brief / SendUserMessage
来源：
- `restored-src/src/tools/BriefTool/prompt.ts`

摘录：
- 当 Brief 可用时，真正给用户看的答复应走这个工具。
- 如果暂时不能直接回答，应先简短确认，再执行工作，最后通过 Brief 返回结果。

### EnterPlanMode
来源：
- `restored-src/src/tools/EnterPlanModeTool/prompt.ts`

摘录：
- 在进入复杂实现前切入 plan mode。
- external 版本更倾向于对多文件、歧义大、涉及架构决策的任务先规划。
- ant/internal 版本更克制，只在“确有明显歧义或高影响重构”时建议进入 plan mode。

### ExitPlanMode
来源：
- `restored-src/src/tools/ExitPlanModeTool/prompt.ts`

摘录：
- 当计划写完并准备交给用户审批时使用。
- 该工具会读取计划文件，不直接接收计划正文。
- 不应用于纯调研任务。

### EnterWorktree
来源：
- `restored-src/src/tools/EnterWorktreeTool/prompt.ts`

摘录：
- 只有当用户明确要求“使用 worktree”时才能调用。
- 会创建隔离 worktree 并切换当前会话进入其中。
- 不能因为用户只是想切分支就使用它。

### ExitWorktree
来源：
- `restored-src/src/tools/ExitWorktreeTool/prompt.ts`

摘录：
- 退出由 EnterWorktree 创建的 worktree 会话。
- 只作用于当前会话里由 EnterWorktree 创建的 worktree。
- 支持 `keep` 或 `remove`，并用 `discard_changes` 做保护。

## 4. 任务、Todo、团队与调度工具

### TodoWrite
来源：
- `restored-src/src/tools/TodoWriteTool/prompt.ts`

摘录：
- 维护当前会话的结构化 todo 列表。
- 对多步骤或非平凡任务应主动使用。
- 对极其简单的一步任务则不应使用。
- 工作进行中应始终保持至少一个 `in_progress` 项。

### TaskCreate
来源：
- `restored-src/src/tools/TaskCreateTool/prompt.ts`

摘录：
- 创建结构化任务项。
- 复杂工作、plan mode 或多任务请求下应主动使用。
- 在 swarm/team 模式下，描述必须足够详细，以便其他 agent 接手。

### TaskGet
来源：
- `restored-src/src/tools/TaskGetTool/prompt.ts`

摘录：
- 按 ID 获取任务的完整详情、依赖和上下文。

### TaskList
来源：
- `restored-src/src/tools/TaskListTool/prompt.ts`

摘录：
- 列出任务清单中的全部任务。
- 在 teammate 模式下，可用来寻找可领取的任务，并优先取较小 ID 的任务。

### TaskUpdate
来源：
- `restored-src/src/tools/TaskUpdateTool/prompt.ts`

摘录：
- 更新已有任务。
- 用于标记进度、分配 owner 和完成状态。

### TaskStop
来源：
- `restored-src/src/tools/TaskStopTool/prompt.ts`

摘录：
- 按 `task_id` 停止一个正在运行的后台任务。

### TeamCreate
来源：
- `restored-src/src/tools/TeamCreateTool/prompt.ts`

摘录：
- 创建 team/swarm 及其配套 task list。
- 用户明确提出多 agent 协作，或任务明显适合并行拆分时，应主动使用。
- prompt 中详细说明了 teammate 协作、任务 ownership、自动消息投递和 team config 发现流程。

### TeamDelete
来源：
- `restored-src/src/tools/TeamDeleteTool/prompt.ts`

摘录：
- 在 swarm 工作完成后移除 team 和 task 目录。
- 如果还有活跃 teammate，会删除失败。

### ScheduleCron / CronCreate
来源：
- `restored-src/src/tools/ScheduleCronTool/prompt.ts`

摘录：
- 安排未来一次性提醒或周期性 prompt。
- 使用用户本地时区下的标准 5 段 cron。
- 明确区分 durable job 和 session-only job。

### CronDelete
来源：
- `restored-src/src/tools/ScheduleCronTool/prompt.ts`

摘录：
- 取消之前调度的 cron 任务。

### CronList
来源：
- `restored-src/src/tools/ScheduleCronTool/prompt.ts`

摘录：
- 列出当前 session 的 cron 任务；启用 durable 时，也会包含持久化任务。
