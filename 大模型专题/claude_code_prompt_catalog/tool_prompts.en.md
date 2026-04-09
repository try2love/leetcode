# Tool Prompts

This file excerpts the prompt text used to describe Claude Code tools to the model.

Note:
- `AgentTool` is summarized in `agent_prompts.en.md`.
- `MCPTool` itself has an empty prompt because concrete MCP tool descriptions come from MCP servers dynamically.

## 1. File and Code Tools

### Read
Source:
- `restored-src/src/tools/FileReadTool/prompt.ts`

Extract:
- Read a file from the local filesystem using an absolute path.
- Can read normal files, images, PDFs (with page constraints), and Jupyter notebooks.
- Only reads files, not directories.
- If the user gives a screenshot path, always use Read to inspect it.

### Write
Source:
- `restored-src/src/tools/FileWriteTool/prompt.ts`

Extract:
- Write a file to the local filesystem.
- If rewriting an existing file, Read it first.
- Prefer Edit for modifying existing files.
- Do not create markdown/README files unless explicitly requested.

### Edit
Source:
- `restored-src/src/tools/FileEditTool/prompt.ts`

Extract:
- Performs exact string replacements in files.
- Requires at least one prior Read in the conversation.
- Preserve indentation exactly.
- Use the smallest clearly unique `old_string`.
- Prefer editing existing files over creating new ones.

### Glob
Source:
- `restored-src/src/tools/GlobTool/prompt.ts`

Extract:
- Fast file-pattern matching tool.
- Supports patterns like `**/*.js` or `src/**/*.ts`.
- Use for finding files by name patterns.

### Grep
Source:
- `restored-src/src/tools/GrepTool/prompt.ts`

Extract:
- A powerful search tool built on ripgrep.
- Use for content search across files.
- Intended for exact and regex-style code/text searching.

### NotebookEdit
Source:
- `restored-src/src/tools/NotebookEditTool/prompt.ts`

Extract:
- Replaces or inserts/deletes a specific cell in a Jupyter notebook.
- Uses absolute notebook path and 0-based `cell_number`.

### LSP
Source:
- `restored-src/src/tools/LSPTool/prompt.ts`

Extract:
- Provides LSP-based code intelligence.
- Supports definition, references, hover, symbols, implementations, and call hierarchy.
- Requires file path, line, and character position.

## 2. Shell, Web, and Environment Tools

### Bash
Source:
- `restored-src/src/tools/BashTool/prompt.ts`

Extract:
- Use for terminal/system commands, not for file reads/writes when dedicated tools exist.
- Supports optional background execution.
- Includes detailed git safety rules:
  - do not skip hooks
  - avoid destructive git commands
  - do not amend unless explicitly asked
  - commit only when asked
- Includes a full PR-creation workflow using `gh`.

### PowerShell
Source:
- `restored-src/src/tools/PowerShellTool/prompt.ts`

Extract:
- Use for terminal work in PowerShell, not file operations.
- Includes PowerShell edition-specific syntax guidance.
- Supports optional background execution.
- Warns against interactive/blocking cmdlets and unsafe command forms.
- Repeats the dedicated-tool preference for file operations.

### WebFetch
Source:
- `restored-src/src/tools/WebFetchTool/prompt.ts`

Extract:
- Fetch a URL, convert HTML to markdown, and run a small fast model over it.
- Takes both a URL and a prompt.
- Prefer MCP-provided web fetch when available.
- Prefer `gh` via Bash for GitHub URLs.

### WebSearch
Source:
- `restored-src/src/tools/WebSearchTool/prompt.ts`

Extract:
- Search the web for up-to-date information.
- Mandatory rule: after using web search, include a `Sources:` section with markdown links.
- Use the current year/month context in search queries for recent information.

### ToolSearch
Source:
- `restored-src/src/tools/ToolSearchTool/prompt.ts`

Extract:
- Loads full schemas for deferred tools so they become callable.
- Supports exact select form and keyword-search form.
- Explains that deferred tools may appear first only by name, without schemas.

### Sleep
Source:
- `restored-src/src/tools/SleepTool/prompt.ts`

Extract:
- Wait for a duration.
- Prefer this over `Bash(sleep ...)`.
- Can be used while waiting for other work or user-directed pauses.

### Config
Source:
- `restored-src/src/tools/ConfigTool/prompt.ts`

Extract:
- Get or set Claude Code configuration settings.
- Explains get vs set usage.
- Enumerates global and project settings plus model options.

### RemoteTrigger
Source:
- `restored-src/src/tools/RemoteTriggerTool/prompt.ts`

Extract:
- Manage scheduled remote Claude Code triggers via the claude.ai API.
- Use this instead of curl because auth is handled in-process.
- Supports list/get/create/update/run actions.

### ListMcpResources
Source:
- `restored-src/src/tools/ListMcpResourcesTool/prompt.ts`

Extract:
- List available resources from configured MCP servers.
- Each resource includes which server it belongs to.

### ReadMcpResource
Source:
- `restored-src/src/tools/ReadMcpResourceTool/prompt.ts`

Extract:
- Read a specific MCP resource by server name and URI.

### MCPTool
Source:
- `restored-src/src/tools/MCPTool/prompt.ts`

Extract:
- Empty placeholder prompt.
- Real MCP tool descriptions come from connected MCP servers.

## 3. Workflow and Communication Tools

### AskUserQuestion
Source:
- `restored-src/src/tools/AskUserQuestionTool/prompt.ts`

Extract:
- Ask the user multiple-choice questions during execution.
- Use for preferences, clarifying ambiguity, and implementation decisions.
- In plan mode, use for clarifying requirements before finalizing the plan.
- Do not use it to ask for plan approval; use ExitPlanMode instead.

### Skill
Source:
- `restored-src/src/tools/SkillTool/prompt.ts`

Extract:
- Invoke a skill in the main conversation.
- If a visible skill matches the user's request, invoking it is a blocking requirement before any other response.
- Do not mention a skill without actually calling the Skill tool.
- Do not use it for built-in CLI commands.

### SendMessage
Source:
- `restored-src/src/tools/SendMessageTool/prompt.ts`

Extract:
- Send a message to another agent.
- Also supports cross-session targets when that feature is enabled.
- Used to continue an existing worker with preserved context.

### Brief / SendUserMessage
Source:
- `restored-src/src/tools/BriefTool/prompt.ts`

Extract:
- Send the user-facing message through the Brief channel.
- The real answer should live in this tool when Brief is enabled.
- If immediate answer is not possible, first acknowledge, then work, then send the result.

### EnterPlanMode
Source:
- `restored-src/src/tools/EnterPlanModeTool/prompt.ts`

Extract:
- Enter plan mode before non-trivial implementation work.
- External prompt strongly prefers planning for multi-file, ambiguous, or architectural tasks.
- Ant/internal prompt is stricter and uses plan mode only for genuine ambiguity or high-impact restructuring.

### ExitPlanMode
Source:
- `restored-src/src/tools/ExitPlanModeTool/prompt.ts`

Extract:
- Use when planning is complete and ready for user approval.
- The tool reads the plan from the plan file; it does not take the plan body directly.
- Do not use it for pure research tasks.

### EnterWorktree
Source:
- `restored-src/src/tools/EnterWorktreeTool/prompt.ts`

Extract:
- Use only when the user explicitly asks for worktree-based work.
- Creates an isolated worktree and switches the session into it.
- Do not use it just because the user wants another branch.

### ExitWorktree
Source:
- `restored-src/src/tools/ExitWorktreeTool/prompt.ts`

Extract:
- Exit a worktree session created by EnterWorktree.
- Only affects worktrees created by EnterWorktree in the current session.
- Supports `keep` or `remove`, with an extra `discard_changes` safeguard.

## 4. Task, Todo, Team, and Scheduling Tools

### TodoWrite
Source:
- `restored-src/src/tools/TodoWriteTool/prompt.ts`

Extract:
- Maintain a structured todo list for the current session.
- Use proactively for multi-step or non-trivial tasks.
- Avoid it for trivial one-step work.
- Keep at least one task `in_progress` while actively working.

### TaskCreate
Source:
- `restored-src/src/tools/TaskCreateTool/prompt.ts`

Extract:
- Create a structured task entry.
- Use proactively for complex work, plan mode, or multi-task requests.
- In swarm/team mode, include enough detail for another agent to execute it.

### TaskGet
Source:
- `restored-src/src/tools/TaskGetTool/prompt.ts`

Extract:
- Retrieve a task by ID with full details, dependencies, and context.

### TaskList
Source:
- `restored-src/src/tools/TaskListTool/prompt.ts`

Extract:
- List all tasks in the task list.
- In teammate mode, use it to find available work and prefer lower task IDs first when multiple are open.

### TaskUpdate
Source:
- `restored-src/src/tools/TaskUpdateTool/prompt.ts`

Extract:
- Update an existing task in the task list.
- Used to mark progress, assign ownership, and complete tasks.

### TaskStop
Source:
- `restored-src/src/tools/TaskStopTool/prompt.ts`

Extract:
- Stop a running background task by `task_id`.

### TeamCreate
Source:
- `restored-src/src/tools/TeamCreateTool/prompt.ts`

Extract:
- Create a team/swarm and its paired task list.
- Use proactively when the user asks for multiple agents or when the task benefits from parallelized teamwork.
- Explains teammate coordination, task ownership, automatic message delivery, and team config discovery.

### TeamDelete
Source:
- `restored-src/src/tools/TeamDeleteTool/prompt.ts`

Extract:
- Remove team and task directories after swarm work is complete.
- Fails if active teammates still exist.

### ScheduleCron / CronCreate
Source:
- `restored-src/src/tools/ScheduleCronTool/prompt.ts`

Extract:
- Schedule a future one-shot reminder or recurring prompt.
- Uses standard 5-field cron in the user's local timezone.
- Distinguishes durable jobs from session-only jobs.

### CronDelete
Source:
- `restored-src/src/tools/ScheduleCronTool/prompt.ts`

Extract:
- Cancel a previously scheduled cron job.

### CronList
Source:
- `restored-src/src/tools/ScheduleCronTool/prompt.ts`

Extract:
- List scheduled cron jobs for the current session, and durable jobs when that mode is enabled.
