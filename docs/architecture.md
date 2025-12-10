# TBAnti 系统架构图 (System Architecture)

**最后更新**: 2025-12-09
**状态**: 本地开发完成 (Logic Verified)

## 1. 目录结构 (Directory Structure)

```text
/Users/ozzymini/Documents/legacy_source/
├── src/                      # 🏗️ 源代码
│   ├── backend/              #     后端 (FastAPI)
│   │   ├── main.py           #         API 入口 (含 CORS)
│   │   ├── database.py       #         DB 连接 (SQLAlchemy)
│   │   └── models.py         #         数据模型 (TBProduct)
│   └── frontend_new/         #     前端 (Static Web)
│       └── index.html        #         查询主页
│
├── docs/                     # 📚 文档中心
│   ├── archive/              #     归档资料
│   ├── knowledge_base/       #     知识库
│   └── INDEX.md              #     全项目索引 (水电图)
│
├── .specify/                 # ⚙️ Spec-Kit 配置
│   └── memory/constitution.md #    项目宪法
│
└── venv/                     # 🐍 Python 虚拟环境
```

## 2. 技术栈 (Tech Stack)

### 后端 (Backend)
- **语言**: Python 3.x
- **框架**: FastAPI
- **ORM**: SQLAlchemy
- **驱动**: pyodbc (连接 SQL Server)

### 前端 (Frontend)
- **技术**: 原生 HTML5 / JavaScript (Fetch API)
- **服务器**: `python -m http.server` (简单的静态文件服务)

### 数据库 (Database)
- **当前**: Docker 容器 (`mssql-server`)
    - 数据库名: `TB_Restored`
- **目标**: 云端数据库 (SQLite 或 Managed SQL)

## 3. 数据流 (Data Flow)
1. **用户** -> **浏览器** (`localhost:8080`) -> 打开 `index.html`
2. **浏览器** -> JS `fetch()` -> **API** (`localhost:8000/products`)
3. **API (FastAPI)** -> **SQLAlchemy** -> **Docker SQL Server** (`localhost:1433`)
4. **SQL Server** -> 返回数据 -> **API** -> JSON 响应 -> **浏览器渲染**

## 4. 关键配置
- **数据库连接**: `mssql+pyodbc://sa:MyNewPass123@localhost:1433/TB_Restored...`
- **CORS**: 后端已配置 `CORSMiddleware` 允许跨域访问。