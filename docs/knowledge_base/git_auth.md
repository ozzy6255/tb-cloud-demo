# Git Authentication: 密码 vs 令牌

## 核心概念
自 2021 年起，GitHub 废除通过 HTTPS 使用**账户密码**进行身份验证的方式，改为强制使用 **Personal Access Token (PAT)**。

### 为什么变了？
- **安全性 (Security)**:
    - **密码**: 权限太大（一旦泄露，黑客可以删除账号、修改邮箱）。
    - **Token**: 权限可控（您可以限制它只能读写代码，不能改密码），且由于是随机生成的字符串，随时可以像“换把锁”一样废除旧 Token 重新生成，而不影响您的登录密码。

## 实际操作
当 Git 提示输入 Password 时：
- **不要输入**: 您的 GitHub 网站登录密码。
- **必须输入**: 您生成的 Personal Access Token (以 `ghp_` 开头)。

## 知识延展
- **SSH Key**: 除了 HTTPS + Token，另一种常见认证方式是 SSH。它通过非对称加密（公钥/私钥）实现免密登录。这属于更进阶的用法。
- **Credential Helper**: 您的电脑（Mac Keychain 或 Windows Credential Manager）通常会记住您第一次输入的密码。如果您输入错了，它记住了错误的，下次可能直接报错而不询问。这时需要去系统设置里清除旧凭据。
