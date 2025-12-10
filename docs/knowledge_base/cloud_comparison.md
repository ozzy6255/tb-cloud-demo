# 云服务对比: Render vs Google Cloud vs Tencent

## 1. 免运维 (PaaS) vs 基础设施 (IaaS)

### PaaS (Platform as a Service) - 如 Render, Heroku, Vercel
- **比喻**: 住全服务酒店。
- **特点**: 您只需给前台（平台）一把钥匙（代码仓库），房间打扫、水电网络（环境配置、扩容、HTTPS）全部自动搞定。
- **适用**: 初创项目、个人开发者、快速验证想法。
- **缺点**: 自定义程度低，价格随规模指数级增长。

### IaaS (Infrastructure as a Service) - 如 AWS EC2, Google Compute Engine, 阿里云 ECS
- **比喻**: 租毛坯房。
- **特点**: 給您四面墙（服务器），装修、水电、家具（操作系统、Python、Nginx、防火墙）都要自己动手。
- **适用**: 企业级应用、需要极致性能调优、特殊环境需求。
- **优点**: 极高的控制权，大规模下成本更低。

### CaaS / Serverless (混合态) - 如 Google Cloud Run, Tencent SCF
- **比喻**: 胶囊旅馆 / 共享单车。
- **特点**: 介于两者之间。您打包好一个容器（Docker），平台负责运行。按秒/次收费，没人用时不收钱。

## 2. 选型建议

| 维度 | Render (PaaS) | Google Cloud Run (Serverless) | 腾讯云 (IaaS/Serverless) |
| :--- | :--- | :--- | :--- |
| **上手难度** | ⭐ (小白首选) | ⭐⭐⭐ (需要了解 IAM/Gcloud) | ⭐⭐⭐⭐ (备案是最大门槛) |
| **中国访问** | 慢/不稳定 | 被墙 | **极快** |
| **微信小程序** | **不兼容** (无备案) | **不兼容** (无备案) | **兼容** (可备案) |
| **免费额度** | 长期免费 (休眠) | 长期免费 (需绑卡) | 短期试用 / 按量付费 |
