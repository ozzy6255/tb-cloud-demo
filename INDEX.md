# 数据孤岛项目总索引 (Project Plumbing Diagram)

> **"水电暖图" (Plumbing Diagram)** - 通过索引快速定位所有文件、代码、配置和进展信息。

## 1. 📂 目录结构 (Directory Structure)

```text
/Users/ozzymini/Documents/legacy_source/
├── src/                      # 🏗️ 源代码 (Source Code)
│   ├── backend/              #     🐍 后端 (Python/FastAPI)
│   └── frontend_new/         #     🌐 前端 (HTML/JS)
│
├── docs/                     # 📚 文档中心 (Documentation)
│   ├── archive/              #     🗄️ 归档资料 (Old Logs/Memos)
│   ├── knowledge_base/       #     🧠 知识库 (Learning & Concepts)
│   ├── 00_知识体系图谱.md     #     🗺️ 知识图谱 (Knowledge Graph)
│   ├── architecture.md       #     🏗️ 架构文档
│   └── ROADMAP.md            #     🛣️ 路线图
│
├── .specify/                 # ⚙️ Spec-Kit 配置
│   ├── memory/               #     📜 记忆库 (Constitution)
│   └── specs/                #     📝 规格说明书
│
└── venv/                     # 🐍 Python 虚拟环境
```

## 2. 🚀 快速入口 (Quick Access)

- **项目宪法 (Rules)**: `.specify/memory/constitution.md` (唯一法则文件)
- **当前任务 (Tasks)**: `.gemini/antigravity/brain/.../task.md` (请在 Agent 侧边栏查看)

### 开发环境
- **启动后端**: `source venv/bin/activate && cd src/backend && uvicorn main:app --reload`
- **启动前端**: `cd src/frontend_new && python3 -m http.server 8080`

## 3. 📅 工作流 (Workflows)

### 存档 (Archive)
当执行 "存档" 操作时：
1. 更新 `docs/archive/` 中的日志。
2. 提取知识点到 `docs/knowledge_base/`。

### 继续工作 (Continue)
当执行 "继续工作" 操作时：
1. 读取 `docs/ROADMAP.md` 或 `task.md`。
2. 读取 `.specify/memory/constitution.md`。
