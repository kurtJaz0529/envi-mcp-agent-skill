# 复用 ENVI Modeler 流程

[ExampleModels](https://github.com/envi-idl/ExampleModels) 提供任务、参数连线、循环和嵌套流程的例子。`.model` 是可阅读的流程定义；无需把它当作原生二进制反编译。

读取 `nodes`、`envitask.name`、静态参数、`edges` 和嵌套 metatask 的参数映射。区分处理任务与 iterator、aggregator、arrayextractor、view、datamanager 等辅助节点。任务名不在 Task Engine 目录中时，先判断其是否属于 Modeler 辅助行为，不能直接断言整个模型无法运行。

迁移到 MCP/Python 时：

- 严格解析原文件；记录语法错误，不静默修改来源。需要修复占位符时使用明确标注的派生副本。
- 检查节点连接、输入文件、精确 Task 名称、参数与版本；名称匹配不等于模型已验证。
- 将迭代、聚合和数组索引作为显式控制逻辑实现；多维索引和顺序按实际 ENVI/IDL 语义核对。
- 替换作者机器上的示例路径。一般模型、ENVI Server 和 Deep Learning 各自有不同环境要求。
- 用小型合成输入验证节点结果与完整流程，再应用到用户数据。

可优先研究的流程：指数变化检测、逐波段 RasterMath、多时相指数计算、分类方法比较、波段堆叠。指数变化示例先统一目标网格，再分别计算指数、差分、阈值分类、平滑和聚合；这不替代云影处理或真实几何配准。

如果使用 [envi-mcp-server](https://github.com/Di0105/envi-mcp-server) 的状态恢复框架，应补查实际上游产物和参数，不仅检查 `state.json` 是否存在输出键。
