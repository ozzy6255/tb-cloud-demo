# 数据流程图

## 完整的数据旅程

```mermaid
graph TB
    subgraph "本地环境"
        A[SQL Server Docker<br/>TB_Restored 数据库] -->|ETL 脚本| B[migrate_logistics.py]
        B -->|SELECT 2025数据| C[app.db SQLite<br/>10k 物流记录]
    end
    
    subgraph "版本控制"
        C -->|git add| D[Git 本地仓库]
        D -->|git push| E[GitHub 远程仓库]
    end
    
    subgraph "Render 云端"
        E -->|Webhook 触发| F[Render Builder]
        F -->|docker build| G[Docker 镜像构建]
        
        subgraph "Docker 多阶段构建"
            G1[Stage 1: Node.js<br/>编译 Vue 前端] -->|dist/| G2[Stage 2: Python<br/>复制后端 + app.db]
        end
        
        G --> G1
        G1 --> G2
        G2 -->|docker run| H[运行中的容器<br/>FastAPI + SQLite]
    end
    
    subgraph "用户访问"
        H -->|HTTPS| I[全球用户<br/>浏览器访问]
    end
    
    style C fill:#90EE90
    style E fill:#87CEEB
    style H fill:#FFD700
```

## 关键节点说明

### 1. ETL 过程 (本地)
- **输入**: SQL Server 分区表 `TBOutCodeRelation25xxxx`
- **处理**: Python 脚本连接两个数据库,执行 JOIN 查询
- **输出**: `app.db` (单文件,10MB)

### 2. Git 版本控制
- **作用**: 不仅管理代码,也管理数据库文件
- **注意**: `.gitignore` 中**没有**排除 `app.db`

### 3. Docker 构建
- **阶段 1**: 用 Node.js 编译 Vue (生成静态文件)
- **阶段 2**: 用 Python 运行后端,同时服务前端静态文件

### 4. 数据持久化
- **问题**: Docker 容器重启后数据会丢失吗?
- **答**: 不会! `app.db` 被打包进**镜像**,每次启动都会恢复
- **但**: 如果在云端修改了数据,重新部署会覆盖 (因为镜像是只读的)
