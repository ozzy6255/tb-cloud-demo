# 老师: 部署问题诊断 - 前端文件缺失

## 问题现象
用户访问 `https://tb-cloud-demo.onrender.com` 只看到:
```json
{"message":"Welcome to TBAnti Query API. Visit /docs for Swagger UI."}
```

## 根本原因

### 代码逻辑分析
```python
# main.py 第 53-59 行
@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
    index_file = static_dir / "index.html"  # /app/static/index.html
    if index_file.exists():
        return FileResponse(index_file)
    return {"message": "Frontend not deployed. API available at /api"}  # ← 返回这个
```

**结论**: `/app/static/index.html` **不存在**!

### Docker 构建流程检查

#### Stage 1: 编译 Vue
```dockerfile
FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend
COPY src/frontend_vite/ ./
RUN npm run build  # 生成 dist/ 目录
```

**问题**: Vite 默认输出到 `dist/`,所以文件在 `/app/frontend/dist/`

#### Stage 2: 复制前端
```dockerfile
COPY --from=frontend-builder /app/frontend/dist /app/static
```

**理论上**: 应该把 `dist/` 内容复制到 `/app/static/`

### 可能的失败原因

1.  **npm run build 失败**
    - Node.js 依赖安装失败
    - Vite 编译错误
    - 构建日志中应该有错误信息

2.  **路径不匹配**
    - Vite 配置的 `outDir` 不是 `dist`
    - 或者 `dist` 目录为空

3.  **文件权限问题**
    - Docker COPY 失败但没报错

## 诊断步骤

### 1. 检查 Render 构建日志
在 Render Dashboard 查看最近一次部署的完整日志,搜索:
- `npm run build` - 是否成功?
- `COPY --from=frontend-builder` - 是否有警告?
- `ERROR` 或 `WARN` 关键词

### 2. 本地验证 Docker 构建
```bash
cd /Users/ozzymini/Documents/legacy_source
docker build -t test-build .
docker run -it test-build ls -la /app/static
```

如果 `/app/static` 为空或不存在,说明 Dockerfile 有问题。

### 3. 检查 package.json
```bash
cat src/frontend_vite/package.json | grep "build"
```

确认 `build` 脚本是 `vite build`。

## 临时解决方案

### 方案 A: 添加构建日志
修改 Dockerfile,增加调试输出:
```dockerfile
RUN npm run build
RUN ls -la dist/  # 查看构建产物
```

### 方案 B: 显式指定输出目录
修改 `vite.config.js`:
```javascript
export default defineConfig({
  plugins: [vue()],
  base: '/',
  build: {
    outDir: 'dist',  // 显式指定
    emptyOutDir: true
  }
})
```

## 知识延展

### Vite 构建输出结构
```
dist/
├── index.html
├── assets/
│   ├── index-abc123.js
│   ├── index-def456.css
│   └── vue-xyz789.svg
└── vite.svg
```

### FastAPI 静态文件服务
```python
app.mount("/assets", StaticFiles(directory="/app/static/assets"))
# 这会服务 /app/static/assets/ 下的所有文件
# 访问 /assets/index-abc123.js 会返回该文件
```

### SPA 路由原理
```
用户访问 /logistics
    ↓
FastAPI catch-all 路由匹配
    ↓
返回 index.html
    ↓
浏览器加载 Vue
    ↓
Vue Router 解析 /logistics
    ↓
显示物流追溯页面
```
