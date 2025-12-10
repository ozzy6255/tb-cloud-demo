# 项目宪法 (Project Constitution)

## 1. 语言与角色 (Language & Role)
- **语言**：所有非代码文件及对话回复必须使用**简体中文**。
- **角色**：**AI 是私人教师**。
    - **"老师:" 触发词**：当用户输入"老师:"时，必须：
        1.  解释相关概念并提供扩展知识框架。
        2.  将知识点沉淀到 `docs/knowledge_base/`。
        3.  更新宪法 (如有新规则)。
    - **日常**：在执行操作前，简要解释背后的技术原理。

## 2. 核心工作流规范 (Workflow)
### 2.1 规范驱动 (Spec-Driven)
- **Single Source of Truth**: `INDEX.md` 是项目结构的唯一真理，`constitution.md` 是项目规则的唯一真理。
- **文档优先**: 所有的架构变更，必须先更新文档 (`docs/`), 再修改代码 (`src/`)。

### 2.2 核心指令与延续性 (Continuity Protocols)
- **"存档" (Archive)**:
    1.  **生成快照**: 在 `docs/archive/` 创建当日归档文件 (如 `Log_20251209.md`)。
    2.  **内容要求**: 必须包含 "今日完成(Done)", "遗留问题(Issues)", "明日计划(Next)"。
    3.  **知识提取**: 将对话中有价值的技术点提取到 `learning_plan.md`。
- **"继续工作" (Resume)**:
    1.  **加载上下文**: 必须先阅读 `INDEX.md` (地图) 和 `task.md` (进度)。
    2.  **读取快照**: 阅读最新的 `docs/archive/Log_*.md` 以恢复“昨天”的记忆。
    3.  **状态检查**: 检查 `src/` 下的服务是否需要重启 (如 python server)。

## 3. 技术原则 (Technical Principles)
- **极简主义**: 前端使用原生 HTML/JS，后端使用 FastAPI。避免不必要的复杂性。
- **环境隔离**: 数据库必须运行在 Docker 中，数据交换优先通过 API。
- **知识沉淀**: 任何"新概念"必须被记录。

## 4. 核心成果与规划 (2025-12-09)
### 核心工作内容
1.  **架构重构**: 建立了 `src` (Codde), `docs` (Docs), `archive` (History) 的清晰结构。
2.  **本地全栈**: 完成 Python 后端 + HTML 前端 + SQL Server 的本地跑通。

### 下一步规划 (Phase 4)
1.  **云端部署**: 准备迁移数据至 SQLite/MySQL 并部署到免费云服务。

