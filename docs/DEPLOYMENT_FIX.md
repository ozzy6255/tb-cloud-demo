# Render 部署修复说明

## 问题诊断
初次部署只显示了后端 API,Vue 前端未被服务。

## 解决方案
采用**多阶段 Docker 构建**:

### Stage 1: 编译 Vue 前端
```dockerfile
FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend
COPY src/frontend_vite/package*.json ./
RUN npm install
COPY src/frontend_vite/ ./
RUN npm run build  # 生成 dist/ 目录
```

### Stage 2: Python 后端 + 静态文件
```dockerfile
FROM python:3.9-slim
# ... 安装依赖 ...
COPY --from=frontend-builder /app/frontend/dist /app/static
```

### FastAPI 配置
- API 端点: `/api/products`, `/api/logistics`
- 静态文件: `/assets/*` (Vue 编译后的 CSS/JS)
- SPA 路由: `/*` (所有其他路径返回 `index.html`)

## 验证步骤
1.  访问 `https://tb-cloud-demo.onrender.com` - 应显示 Vue 界面
2.  访问 `https://tb-cloud-demo.onrender.com/api` - 应显示 API 信息
3.  测试物流查询功能

## 预计部署时间
首次构建: **8-12 分钟** (需要安装 Node.js 和编译前端)
后续更新: **3-5 分钟**
