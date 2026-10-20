# ENVI MCP Agent Skill

可复用的本机 ENVI MCP 调用技能：按任务选择 Task Engine 或 Classic GUI，查询真实参数，执行并核验遥感结果，按需要组织真实实验截图与报告证据。

技能入口：`$envi-workflows`。界面显示名：**ENVI MCP Agent**。

## 本地安装

从仓库根目录运行：

```powershell
python tools/install_skill.py
```

安装程序使用 `CODEX_HOME`，未设置时使用当前用户的 `.codex` 目录。已存在的同名技能先备份，再更新；不会安装 MCP 服务、ENVI、SDK 或修改 MCP 连接配置。

先检查计划：

```powershell
python tools/install_skill.py --dry-run
```

手动安装也可以：将 `skills/envi-workflows` 文件夹复制到自己的 Codex 技能目录。现有同名技能应先备份。若当前会话尚未发现新内容，在新会话中使用该技能。

## 调用示例

- `使用 $envi-workflows 检查本机 ENVI 接入，报告能用的接口和限制。`
- `使用 $envi-workflows 对我的影像执行波段计算，先查真实任务参数，再验证输出。`
- `使用 $envi-workflows 按指导书完成 ENVI 实验，每一步保留真实截图。`
- `使用 $envi-workflows 评估这个 Modeler 模型能否在本机迁移为批处理。`

## 能力与依赖

后台计算使用已连接的 ENVI Task Engine MCP；原生界面任务使用已连接的 Classic MCP。完整实验报告可组合 `envi-classic-lab-automation` 与 `remote-sensing-report` 技能。若这些依赖缺失，技能会区分当前能做和未完成的环节。

普通计算不要求报告模板或全套截图。Classic 原生 GUI 可能占用桌面；纯计算优先 Task Engine 后台执行。

本仓库只分发调用规则、原创安装工具和脱敏的验证结论。ENVI/SARScape、SDK、许可、输入数据和厂商代码需要在用户环境中提供。

## 完成情况

参见 [验证记录与限制](skills/envi-workflows/references/validation-state.md)。已验证接入与一项小型真实波段计算；完整 InSAR 链、全部 Modeler 模型和正式实验报告没有因此被视为完成。

## 目录

```text
skills/envi-workflows/
  SKILL.md
  agents/openai.yaml
  references/
    task-engine.md
    classic.md
    modeler.md
    validation-state.md
tools/install_skill.py
```

## 来源与相关项目

- [ENVI/SARScape MCP Server](https://github.com/Di0105/envi-mcp-server)
- [ENVI Classic MCP](https://github.com/xuedai-mayi/envi-classic-remote-sensing)
- [官方 envipyengine](https://github.com/envi-idl/envipyengine)
- [ENVI Modeler 示例](https://github.com/envi-idl/ExampleModels)

本技能整理了本地集成经验，独立于上述项目；没有把上游完整源码或厂商反编译代码打包进来。
