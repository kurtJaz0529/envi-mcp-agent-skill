---
name: envi-workflows
description: 使用本机 ENVI MCP 完成任务发现、参数化遥感计算、Classic 界面操作与结果验收，并复用 ENVI Modeler 流程。适用于调用 ENVI、检查接入状态、批处理或组织实验步骤；仅在用户需要实验截图或报告时进入完整证据流程。
metadata:
  version: "1.0.0"
---

# ENVI MCP Agent

先识别用户需要的是计算结果、界面操作、实验报告还是接口研究。按实际可用工具和本机任务定义执行；历史记录只能帮助定位，不能替代当前运行证据。

## 按任务选择入口

| 任务 | 入口与需要读取的参考 |
|---|---|
| 指数、分类、裁剪、重投影、可重复批处理 | `envi-task-engine` MCP；读取 [Task Engine 调用规则](references/task-engine.md) |
| Classic 菜单、参数对话框、查看结果、真实截图 | `envi-classic` MCP；读取 [Classic 与报告规则](references/classic.md) |
| 按指导书完成实验并交付报告 | Classic 证据流程，再使用可用的 `envi-classic-lab-automation` 与 `remote-sensing-report` 技能；依赖缺失时说明尚不能交付的环节 |
| 复用 ENVI Modeler `.model` 流程 | 读取 [Modeler 迁移规则](references/modeler.md)，再按实际任务参数逐项验证 |
| 查询本机接入经验、历史完成情况 | 读取 [验证记录与限制](references/validation-state.md)，需要当前状态时再做相应健康检查 |

用户明确指定的操作方式优先。普通计算不自动要求指导书、模板和逐步截图。优先使用 Task Engine 的后台计算；Classic 是原生桌面界面，真实 GUI 操作可能占用屏幕，不能承诺通过浏览器隔离 ENVI 桌面窗口。

## 共同执行约定

1. **区分连接与完成。** 分别报告服务是否可见、引擎是否可启动、任务是否存在、请求是否成功、产物是否通过核验。配置已注册不等于本轮工具已加载。
2. **精确任务与参数。** 从实际目录查询任务名与参数；近似名称和 SAR 关键词只用于发现，不用于证明算法等价或模块许可。
3. **保留原始数据。** 新输出使用独立运行目录，记录真实输入、任务、参数、输出和验证结果。复核 CRS、网格、像元大小、波段顺序、比例因子、NoData 和掩膜；面积使用适合的投影与单位。
4. **按失败证据恢复。** 先读错误和部分输出，再决定后续动作。超时不代表底层计算已经终止，不能立即对同一输出重发计算。
5. **保留本机 SDK 修复。** 如果升级服务，先检查现有差异。官方 `envipyengine` 的 `Task.execute(parameters)` 与部分包装的无参 `execute()` 不同；不能用测试适配器的行为推断真实 SDK。
6. **用结果验收。** 成功返回、任务名称匹配、模拟测试通过都不能替代数值与地理信息验证。完整实验报告还需要对应的真实步骤证据。

## 本机定位与复用

先使用已连接的 MCP 检查工具发现安装路径；确实没有服务时，再检查用户已有的本地配置和项目说明，不盲目重装。常见安装为 ENVI 5.6 / IDL 8.8，其路径可以不同。

任务引擎常用工具：`check_envi_connectivity`、`find_envi_taskengine`、`list_envi_tasks`、`get_envi_task_info`、`run_envi_task`。

Classic 常用工具：`envi_classic_health_check`、`envi_classic_launch`、`envi_classic_list_menu_items`、`envi_classic_invoke_menu`、`envi_classic_run_recipe`。先看当前会话广告的参数 schema，再调用。

本技能不附带 ENVI、SARScape、SDK、许可文件、遥感数据或厂商反编译代码。跨机器复用时重新发现安装、环境和任务，不复制历史可用性结论。
