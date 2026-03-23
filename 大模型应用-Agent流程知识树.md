可以把它当成：

- 复习提纲
- 模拟面试题库
- 项目深挖提纲
- 自我查漏补缺清单

------

# Agent 面试题清单

## 一、Agent 基础认知

### 1. 概念与边界

-  什么是 Agent？
-  Agent 和普通 Chatbot 的区别是什么？
-  Agent 和 Workflow 的区别是什么？
-  Agent 和 RAG 的区别与联系是什么？
-  为什么说 RAG 是能力模块，而 Agent 是任务执行框架？
-  什么任务适合做成 Agent，什么任务不适合？
-  为什么不是所有场景都应该 Agent 化？
-  单轮 Agent 和多轮 Agent 的区别是什么？
-  开环系统和闭环系统的区别是什么？
-  Agent 的最小工作闭环是什么？

### 2. 高频追问

-  你如何用一句话定义 Agent？
-  你觉得 Agent 的核心不是“会调用工具”，而是什么？
-  一个系统只要用了 function calling，就一定算 Agent 吗？
-  如果一个系统只有固定分支判断，没有动态决策，它算 Agent 吗？
-  为什么“可执行性”是 Agent 和普通对话系统的重要分界线？

------

## 二、Agent 核心组成

### 1. 基本模块

-  一个 Agent 系统通常由哪些模块组成？
-  目标、状态、策略、工具、记忆、反馈分别起什么作用？
-  为什么 state 对 Agent 很重要？
-  为什么工具对 Agent 很重要？
-  为什么 memory 对 Agent 很重要？
-  为什么 planning 对复杂任务很重要？
-  observation 在 Agent 中是什么意思？
-  success condition 和 stop condition 分别是什么？

### 2. 高频追问

-  如果没有 memory，Agent 还能工作吗？
-  如果没有 planning，Agent 会出现什么问题？
-  如果没有 observation，Agent 还能称为闭环吗？
-  如果 state 设计不好，会带来哪些连锁问题？
-  工具很多一定更好吗？为什么？

------

## 三、任务理解与目标建模

### 1. 任务理解

-  Agent 如何从用户输入中抽取目标、约束和成功条件？
-  用户问题模糊时，Agent 应该直接执行还是先澄清？
-  如何判断用户输入是“信息查询任务”还是“操作执行任务”？
-  如何区分主目标和子目标？
-  如何识别隐含约束，比如时间、预算、权限、格式要求？
-  用户给出的目标本身不合理时怎么办？
-  用户在执行过程中修改目标怎么办？

### 2. 高频追问

-  你会如何给 Agent 设计 success criteria？
-  为什么成功条件不明确会导致 Agent 反复兜圈子？
-  如果用户目标本身是冲突的，系统如何处理？
-  “帮我整理一下资料”和“帮我发出去”在系统设计上有什么本质差别？
-  用户意图识别错误会如何传导到后续模块？

------

## 四、状态 State 与上下文管理

### 1. State 设计

-  Agent 的 state 一般包含哪些内容？
-  当前任务状态和长期用户记忆应该如何区分？
-  中间推理结果是否应该写入 state？
-  工具调用历史是否应该进入 state？
-  state 太大有什么问题？
-  如何控制 state 的大小与信息密度？
-  如何避免 state 污染？
-  如何处理过时状态、脏状态和冲突状态？

### 2. 高频追问

-  为什么很多 Agent 失败不是因为模型不够强，而是因为 state 管理混乱？
-  多轮任务中，哪些信息必须保留，哪些可以摘要？
-  state summary 会带来什么信息损失？
-  如何保证状态更新的一致性？
-  如果 state 中混入错误信息，后续会发生什么？

------

## 五、记忆 Memory

### 1. 记忆分类

-  Agent 为什么需要 memory？
-  working memory、short-term memory、long-term memory 有什么区别？
-  episodic memory 和 semantic memory 有什么区别？
-  会话历史和长期用户画像记忆有什么区别？
-  RAG 知识库和 Agent memory 的边界是什么？

### 2. 记忆写入与检索

-  什么样的信息应该写入长期记忆？
-  什么样的信息不应该写入长期记忆？
-  记忆是每轮都写，还是按阈值写？
-  如何检索与当前任务最相关的记忆？
-  记忆检索错误会造成什么问题？
-  如何处理记忆冲突、记忆过期和错误记忆？
-  如何设计 memory update 策略？
-  如何做 memory pruning 和 forgetting？

### 3. 高频追问

-  为什么长期记忆系统很容易把临时信息误当成长期事实？
-  用户明确否认过的旧记忆该怎么处理？
-  如何防止错误记忆反复被召回强化？
-  你会如何设计“是否写入记忆”的 gating？
-  如果 memory 和当前检索证据冲突，优先信哪个？

------

## 六、规划 Planning 与推理 Reasoning

### 1. Planning

-  什么是 planning？
-  复杂任务为什么要做 planning？
-  一次性全局规划和逐步规划分别适合什么场景？
-  plan-and-execute 架构是什么？
-  子任务拆分的依据是什么？
-  子任务粒度太粗和太细分别有什么问题？
-  如何识别哪些步骤可以并行？
-  执行到一半发现计划错误怎么办？
-  什么时候需要 re-plan？
-  如何设置计划终止条件？

### 2. Reasoning

-  Agent 中的 reasoning 和普通 CoT 有什么区别？
-  为什么推理链不是越长越好？
-  长推理可能带来哪些问题？
-  如何控制 reasoning budget？
-  如何避免模型在中间推理阶段自我强化错误？
-  什么时候应该让模型显式输出步骤，什么时候不应该？
-  结构化推理和自由推理各有什么优缺点？

### 3. 高频追问

-  planning 的价值体现在哪些任务中最明显？
-  如果任务很简单，还要不要规划？
-  为什么过度规划会拖慢系统？
-  为什么“先规划再执行”通常比“边想边做”更稳？
-  reasoning 和 planning 的边界在哪里？

------

## 七、ReAct、反思与纠错

### 1. 执行循环

-  ReAct 是什么？
-  为什么 Thought-Act-Observation 这种模式有效？
-  反思 reflection 在 Agent 中起什么作用？
-  self-critique 和 verifier 有什么区别？
-  反思应该每一步都做，还是结束后做？
-  如何判断当前步骤需要反思？
-  什么时候反思会适得其反？

### 2. 纠错与回退

-  Agent 如何发现自己做错了？
-  如何设计执行失败后的 retry 机制？
-  重试和重规划的区别是什么？
-  如何避免重复犯同一个错误？
-  如何防止 Agent 进入死循环？
-  如何设计 step limit、budget limit 和 timeout？

### 3. 高频追问

-  reflection 为什么有时能提升效果，有时却会让结果更差？
-  如何区分“当前工具坏了”还是“上一步思路错了”？
-  如果 Agent 一直在尝试但没有进展，怎么判定该终止？
-  如果反思模块本身也不稳定，怎么办？
-  verifier 比 self-reflection 更稳的原因是什么？

------

## 八、工具调用与 Function Calling

### 1. Tool Use 基础

-  Agent 为什么需要工具，而不能只靠模型参数？
-  function calling 的本质是什么？
-  tool schema 为什么重要？
-  工具描述应该包含哪些关键信息？
-  工具输入输出为什么需要结构化？
-  工具返回值如何反馈给模型继续决策？

### 2. 工具选择与路由

-  多个工具都能完成任务时如何选择？
-  tool router 可以怎么做？
-  基于规则、分类器、LLM 决策的工具路由各有什么优缺点？
-  tool selection 错误会如何影响后续链路？
-  如何做 fallback 和兜底？

### 3. 工具健壮性

-  工具超时、失败、返回空值怎么办？
-  工具结果部分成功怎么办？
-  如何做 retry、timeout、熔断和降级？
-  如何验证工具输出是否合法？
-  工具返回错误事实时，Agent 如何发现？

### 4. 高频追问

-  为什么 API Agent 通常比 UI Agent 更稳定？
-  为什么浏览器操作型 Agent 更容易失败？
-  参数抽取错误通常发生在哪些地方？
-  工具描述写得过长或过短会有什么问题？
-  你如何减少“明明有工具却不用”或者“没必要却乱调用工具”的问题？

------

## 九、环境交互与执行控制

### 1. 环境交互

-  Agent 中的 environment 指什么？
-  observation 的本质是什么？
-  部分可观测环境对 Agent 有什么挑战？
-  环境动态变化时，Agent 如何保持鲁棒？
-  外部系统延迟或异步返回时怎么办？
-  为什么说环境反馈决定了 Agent 是否真正闭环？

### 2. 执行控制

-  如何决定下一步是继续执行还是终止？
-  如何避免无效重复操作？
-  如何做 checkpoint？
-  长任务如何实现暂停、恢复、回滚？
-  什么情况下需要 human-in-the-loop？
-  如何设计用户确认点？

### 3. 高频追问

-  为什么同一个 Agent 在实验环境中表现很好，上线后却容易崩？
-  执行环境变化对 Agent 的影响通常体现在哪些地方？
-  为什么 UI 微小变动会导致 Agent 大面积失败？
-  如何让 Agent 对环境不确定性更鲁棒？
-  为什么执行控制是工程成败的关键？

------

## 十、常见 Agent 架构

### 1. 单 Agent

-  单 Agent 架构的优点是什么？
-  单 Agent 架构的瓶颈是什么？
-  什么情况下单 Agent 就足够？

### 2. Planner-Executor

-  planner-executor 架构是什么？
-  为什么把规划和执行拆开通常更稳？
-  planner 输出什么格式更合适？
-  executor 如何保证忠实执行？
-  如果 planner 出错，executor 是否应该纠正？

### 3. Router + Specialist

-  router-specialist 架构是什么？
-  为什么多专家架构常用于复杂任务？
-  specialist 应该如何划分边界？
-  router 错分怎么办？
-  specialist 输出冲突怎么办？

### 4. Multi-Agent

-  多 Agent 架构的优势是什么？
-  多 Agent 的代价是什么？
-  planner、researcher、executor、critic、verifier 这些角色分别做什么？
-  多 Agent 如何通信？
-  如何避免多 Agent 重复劳动？
-  如何避免多 Agent 互相强化错误？
-  leader/coordinator 为什么重要？

### 5. 高频追问

-  为什么多 Agent 不一定比单 Agent 更强？
-  什么时候多 Agent 是伪需求？
-  多 Agent 最大的问题是性能、成本还是稳定性？
-  如果让你设计一个多 Agent 系统，你会如何拆角色？
-  为什么 planner-executor 往往比“一把梭大 prompt”更可控？

------

## 十一、Agent 与 RAG 结合

### 1. Agent + RAG 的作用

-  Agent 为什么经常和 RAG 一起出现？
-  RAG 在 Agent 中扮演什么角色？
-  Agent 检索和普通问答检索有什么区别？
-  Agent 中的检索对象有哪些？
-  检索失败会如何影响后续决策？

### 2. 检索在 Agent 中的特殊问题

-  Agent 如何决定什么时候检索、检索什么、检索几次？
-  一次检索不够怎么办？
-  多跳检索在 Agent 中如何实现？
-  如何防止检索结果把 Agent 带偏？
-  如何判断需要 re-retrieve？
-  memory retrieval 和 knowledge retrieval 的边界是什么？

### 3. 高频追问

-  Agent 里为什么更需要 query rewrite 和 query planning？
-  为什么 Agent 的检索错误比普通 RAG 更危险？
-  如果 RAG 返回了冲突证据，Agent 应该怎么处理？
-  如果检索不到信息，Agent 应该停还是继续尝试别的路径？
-  Agent 中如何平衡检索成本与任务成功率？

------

## 十二、生成结果与结果校验

### 1. 最终输出

-  Agent 如何保证最终答案与用户目标一致？
-  如何做 structured output？
-  JSON schema 输出失败如何修复？
-  最终输出前为什么需要 post-check？
-  如何判断应该给答案、继续执行还是拒答？

### 2. 校验机制

-  结果校验可以在哪些层次做？
-  verifier 如何设计？
-  如何做生成后校验与回退？
-  如何判断最终结果是否 grounded？
-  如何防止“看起来合理但其实没有完成任务”的假成功？

### 3. 高频追问

-  为什么 Agent 的“最终答对”不代表执行过程正确？
-  你会如何定义 task success 和 answer quality？
-  为什么有些 Agent 能生成非常漂亮的解释，但实际上没完成任务？
-  如何避免模型在结果总结时夸大执行成功？
-  结果校验失败后，应该重试、重规划还是让用户确认？

------

## 十三、Agent 安全

### 1. Prompt Injection

-  为什么 Agent 比普通问答系统更怕 prompt injection？
-  prompt injection 在 Agent 里主要有哪些来源？
-  来自网页、邮件、文档、数据库内容的注入如何处理？
-  instruction hierarchy 应该如何设计？
-  什么是 untrusted content？

### 2. 权限控制

-  为什么 Agent 必须做权限隔离？
-  只读工具和可写工具为什么要分开？
-  高风险工具为什么需要二次确认？
-  最小权限原则如何落地？
-  如何防止越权访问？

### 3. 数据安全与审计

-  Agent 为什么容易泄漏敏感信息？
-  如何做脱敏？
-  如何做租户隔离？
-  如何做审计日志和操作追踪？
-  如何记录“谁在什么时间访问了什么数据并触发了什么动作”？

### 4. 高频追问

-  为什么“工具 + 外部内容 + 长链路”会显著放大安全风险？
-  仅靠 prompt 提示能防住注入吗？
-  如何识别高风险操作并拦截？
-  如果模型坚持认为某个高危操作合理，系统层面怎么兜底？
-  你会如何设计一个安全优先的 Agent 系统？

------

## 十四、评估与 Benchmark

### 1. 评估维度

-  为什么 Agent 评估比普通 LLM 更难？
-  Agent 评估应该看哪些指标？
-  task success rate、step success rate、tool success rate 分别反映什么？
-  latency、token cost、tool cost 分别如何衡量？
-  stability、recovery rate、human override rate 如何理解？

### 2. 评估方法

-  如何设计 Agent benchmark？
-  离线评测和在线评测的区别是什么？
-  为什么 Agent 需要轨迹级评估而不是只看最终答案？
-  如何构造 failure case 集？
-  如何评估多步任务中的误差累积？
-  仿真环境评估有什么价值？

### 3. 高频追问

-  为什么“一次成功”不能说明 Agent 稳定？
-  你如何评估一个 Agent 是否值得上线？
-  如果任务成功率提升了，但成本翻倍，你怎么看？
-  如果最终成功率不变，但步骤数明显下降，是否说明系统优化有效？
-  Agent 评估中最难定义的指标是什么？

------

## 十五、工程落地与系统设计

### 1. 服务架构

-  一个可上线的 Agent 系统一般如何分层？
-  orchestrator 的职责是什么？
-  planner、executor、memory、tool layer 如何协作？
-  为什么 Agent 系统通常需要比 RAG 更强的 orchestration？
-  如何实现模块解耦？

### 2. 性能与成本

-  Agent 为什么通常更慢、更贵？
-  latency 主要来自哪些部分？
-  如何控制 step 数、token 数和工具调用次数？
-  哪些内容可以缓存？
-  工具结果缓存、检索缓存、计划缓存分别适用于什么场景？
-  缓存会带来哪些一致性问题？

### 3. 稳定性与降级

-  某个工具服务挂了怎么办？
-  planner 挂了怎么办？
-  如何从 Agent 模式降级为 workflow 或单轮问答？
-  如何做重试、限流、熔断、超时控制？
-  如何设计 fallback 策略？
-  如何避免单点故障拖垮整条链路？

### 4. 可观测性

-  Agent 系统应该记录哪些日志？
-  为什么需要 step-level trace？
-  如何快速定位是 planner、tool、memory 还是 prompt 的问题？
-  什么是 trajectory logging？
-  为什么 Agent 的 observability 比普通 LLM 应用更重要？

### 5. 高频追问

-  如果线上出现“成功率下降但延迟不变”，你先查什么？
-  如果“延迟飙升但 QPS 没变”，你先查什么？
-  如果“平均步骤数突然增加”，通常意味着什么？
-  如果“某类任务大量失败”，排查顺序是什么？
-  如果“用户投诉 Agent 绕圈子”，你会从哪些模块定位？

------

## 十六、故障排查与失败模式

### 1. 常见失败模式

-  Agent 常见失败模式有哪些？
-  目标理解错、计划错、工具选错、参数填错、观察误读、状态污染分别会产生什么表现？
-  什么是 hallucinated action？
-  什么是 premature stop？
-  什么是 loop failure？

### 2. 排查方法

-  如果 Agent 一直调用无关工具，怎么排查？
-  如果 Agent 经常提前结束，怎么排查？
-  如果 Agent 最终答案看起来合理但任务没完成，怎么排查？
-  如果 Agent 在复杂任务上表现差，在简单任务上正常，可能是哪类问题？
-  如果工具成功率很高但最终成功率很低，说明问题可能在哪？

### 3. 高频追问

-  你如何区分“模型能力不足”和“系统设计缺陷”？
-  为什么很多失败表面看是生成问题，本质却是规划问题？
-  如何利用轨迹日志做错误归因？
-  如何定义一个 failure taxonomy？
-  你会优先优化哪类失败模式？为什么？

------

## 十七、训练与优化

### 1. 可训练模块

-  Agent 哪些部分可以训练？
-  router 可以如何训练？
-  tool selection 可以如何训练？
-  planning 可以如何训练？
-  memory write/read policy 可以如何训练？
-  verifier 可以如何训练？

### 2. 数据与学习方法

-  什么是 trajectory data？
-  如何构造高质量 Agent 轨迹数据？
-  imitation learning 在 Agent 中怎么用？
-  reinforcement learning 在 Agent 中适合优化什么？
-  reward 应该如何设计？
-  为什么 Agent 的 reward 设计很难？
-  preference optimization 在 Agent 中有哪些应用？

### 3. 高频追问

-  为什么 Agent 训练通常比普通 SFT 更难？
-  轨迹数据中的哪一部分最有价值？
-  如何从线上日志中挖掘高质量训练样本？
-  你会优先训练 router、planner 还是 verifier？为什么？
-  为什么“最终结果正确”不代表轨迹可以直接拿来训练？

------

## 十八、面试最爱问的对比题

-  Agent vs RAG
-  Agent vs Workflow
-  Agent vs Function Calling
-  Single-Agent vs Multi-Agent
-  Planner-Executor vs ReAct
-  API Agent vs UI Agent
-  Memory vs Knowledge Base
-  Reflection vs Verifier
-  Rule-based Router vs LLM Router
-  Global Planning vs Step-by-step Planning
-  Long Reasoning vs Short Reasoning
-  Tool Use vs Parametric Knowledge

### 常见追问

-  为什么 Multi-Agent 不一定更优？
-  为什么 Planner-Executor 更容易调试？
-  为什么 Memory 不能简单等同于 RAG？
-  为什么 UI Agent 更脆弱？
-  为什么 verifier 常常比 self-reflection 更可靠？

------

## 十九、项目深挖型问题

这类题最适合面试官顺着你的项目继续追问。

### 1. 系统设计题

-  如果让你从零设计一个 Agent 系统，你会怎么拆模块？
-  如果用户目标是“帮我查资料并生成报告”，你会怎么设计链路？
-  如果用户目标是“帮我完成一个多步线上操作”，你会怎么设计链路？
-  你会如何选择单 Agent 还是多 Agent？
-  你会如何引入 RAG、memory 和 tools？

### 2. 优化题

-  如果成功率低，你会优先优化哪个模块？
-  如果成本太高，你会如何降本？
-  如果延迟太高，你会如何加速？
-  如果工具调用太频繁，你会如何控制？
-  如果多轮执行很不稳定，你会如何稳住？

### 3. 安全题

-  如果 Agent 能访问外部网页，你如何防止 prompt injection？
-  如果 Agent 可以写数据库，你如何做权限控制？
-  如果 Agent 会处理敏感数据，你如何做审计与追踪？
-  如果工具返回恶意内容，你如何避免被带偏？
-  如果用户诱导 Agent 做危险操作，你如何拦截？

### 4. 评估题

-  你会如何评估一个 Agent 系统是否达到了上线标准？
-  你会如何构造 benchmark？
-  你如何做错误归因？
-  你如何判断一个优化真的有效，而不是评测偶然波动？
-  你如何做线上 A/B？

------

## 二十、最高频必会题

如果时间有限，下面这些建议你优先准备到能流畅回答。

-  什么是 Agent？和 RAG、Workflow 的区别是什么？
-  Agent 的最小闭环是什么？
-  Agent 为什么需要 planning、memory、tools？
-  ReAct 和 planner-executor 的区别是什么？
-  Single-Agent 和 Multi-Agent 怎么选？
-  API Agent 和 UI Agent 的差别是什么？
-  Memory 和 RAG 的区别是什么？
-  Agent 为什么比普通 LLM 应用更难评估？
-  Agent 的核心失败模式有哪些？
-  Agent 的安全风险为什么更高？
-  你会如何设计一个可上线的 Agent 系统？
-  如果效果下降、延迟升高、成本飙升，排查顺序是什么？

------

## 二十一、适合你背诵的“总纲式提问框架”

如果面试官让你系统讲 Agent，你可以按这套问题顺序准备：

### 1. 基础定义

-  Agent 是什么？
-  和 RAG / Workflow 的区别是什么？
-  适用边界是什么？

### 2. 核心机制

-  怎么理解任务？
-  怎么表示 state？
-  怎么做 planning？
-  怎么做 tool use？
-  怎么做 memory？
-  怎么根据 observation 闭环修正？

### 3. 架构设计

-  单 Agent 还是多 Agent？
-  ReAct 还是 planner-executor？
-  如何接 RAG？
-  如何做 verifier 和 safety layer？

### 4. 工程落地

-  怎么控制成本和时延？
-  怎么做缓存、降级、熔断？
-  怎么做 trace 和 observability？
-  怎么做评估和排障？

### 5. 安全治理

-  如何防注入？
-  如何做权限控制？
-  如何做审计与追踪？

------

