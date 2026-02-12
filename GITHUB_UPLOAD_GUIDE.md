# 📤 GitHub 上传指南 (GitHub Upload Guide)

## 中文版本

### 需要上传的文件

上传到 GitHub 时，**不需要**上传以下文件：

❌ **不上传：**
- `.env` - 包含敏感的 API 密钥
- `__pycache__/` - Python 缓存文件
- `venv/` 或 `env/` - 虚拟环境
- `.streamlit/` - Streamlit 缓存
- `*.log` - 日志文件
- `.DS_Store` - macOS 系统文件

✅ **需要上传的文件：**

| 文件 | 说明 |
|------|------|
| `app.py` | 中文版本的主应用 |
| `app_en.py` | 英文版本的应用 |
| `requirements.txt` | Python 依赖列表 |
| `.env.example` | 环境变量模板（不含真实密钥） |
| `.gitignore` | Git 忽略规则 |
| `README.md` | 中文文档 |
| `README_EN.md` | 英文文档 |
| `QUICK_START.md` | 中文快速开始 |
| `QUICK_START_EN.md` | 英文快速开始 |
| `SETUP_GUIDE.md` | 详细设置指南 |
| `TROUBLESHOOTING.md` | 故障排除指南 |
| `CONTRIBUTING.md` | 贡献指南 |
| `LICENSE` | MIT 许可证 |
| `GITHUB_README.md` | GitHub 主页 README |
| `setup_database.py` | 数据库设置辅助脚本 |
| `run.sh` | 启动脚本 |

### 上传步骤

#### 第一步：创建 GitHub 账户和仓库

1. 访问 [github.com](https://github.com)
2. 点击 "Sign up" 创建账户
3. 创建新仓库：
   - 仓库名：`fb-ads-creative-manager`
   - 描述：`Facebook Ads Creative Manager - Streamlit + Supabase`
   - 选择 "Public" 或 "Private"
   - 不要初始化 README（我们已经有了）

#### 第二步：本地初始化 Git

```bash
cd /home/ubuntu/fb-ads-creative-manager

# 初始化 Git 仓库
git init

# 添加所有文件（.gitignore 会自动排除不需要的文件）
git add .

# 检查将要提交的文件
git status

# 提交
git commit -m "Initial commit: Facebook Ads Creative Manager"
```

#### 第三步：连接到 GitHub 仓库

```bash
# 添加远程仓库（替换 yourusername 和 your-repo）
git remote add origin https://github.com/yourusername/fb-ads-creative-manager.git

# 重命名分支为 main（如果需要）
git branch -M main

# 推送到 GitHub
git push -u origin main
```

#### 第四步：验证上传

1. 访问 GitHub 仓库页面
2. 确认所有文件都已上传
3. 检查 `.gitignore` 是否正常工作（不应该看到 `.env` 或 `__pycache__`）

### 使用 GitHub Desktop（图形界面方式）

如果您不熟悉命令行，可以使用 GitHub Desktop：

1. 下载 [GitHub Desktop](https://desktop.github.com/)
2. 登录您的 GitHub 账户
3. 点击 "File" → "Clone Repository"
4. 选择您的仓库
5. 选择本地路径
6. 点击 "Clone"

然后：
1. 打开本地仓库文件夹
2. 将项目文件复制到该文件夹
3. 在 GitHub Desktop 中，您会看到所有更改
4. 输入提交信息
5. 点击 "Commit to main"
6. 点击 "Push origin"

### 更新仓库

当您进行更改时：

```bash
# 查看更改
git status

# 添加更改
git add .

# 提交
git commit -m "描述您的更改"

# 推送到 GitHub
git push origin main
```

### 重要：保护敏感信息

**永远不要提交以下内容：**
- `.env` 文件（包含 API 密钥）
- 任何包含密码或令牌的文件
- 个人信息

`.gitignore` 文件已经配置好了，会自动排除这些文件。

---

## English Version

### Files to Upload

When uploading to GitHub, **do NOT** upload:

❌ **Do NOT upload:**
- `.env` - Contains sensitive API keys
- `__pycache__/` - Python cache files
- `venv/` or `env/` - Virtual environments
- `.streamlit/` - Streamlit cache
- `*.log` - Log files
- `.DS_Store` - macOS system files

✅ **Files to upload:**

| File | Description |
|------|-------------|
| `app.py` | Chinese version of main app |
| `app_en.py` | English version of app |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment variables template |
| `.gitignore` | Git ignore rules |
| `README.md` | Chinese documentation |
| `README_EN.md` | English documentation |
| `QUICK_START.md` | Chinese quick start |
| `QUICK_START_EN.md` | English quick start |
| `SETUP_GUIDE.md` | Detailed setup guide |
| `TROUBLESHOOTING.md` | Troubleshooting guide |
| `CONTRIBUTING.md` | Contributing guide |
| `LICENSE` | MIT license |
| `GITHUB_README.md` | GitHub main README |
| `setup_database.py` | Database setup helper |
| `run.sh` | Startup script |

### Upload Steps

#### Step 1: Create GitHub Account and Repository

1. Visit [github.com](https://github.com)
2. Click "Sign up" to create an account
3. Create a new repository:
   - Repository name: `fb-ads-creative-manager`
   - Description: `Facebook Ads Creative Manager - Streamlit + Supabase`
   - Choose "Public" or "Private"
   - Don't initialize README (we already have one)

#### Step 2: Initialize Git Locally

```bash
cd /home/ubuntu/fb-ads-creative-manager

# Initialize Git repository
git init

# Add all files (.gitignore will automatically exclude unnecessary files)
git add .

# Check files to be committed
git status

# Commit
git commit -m "Initial commit: Facebook Ads Creative Manager"
```

#### Step 3: Connect to GitHub Repository

```bash
# Add remote repository (replace yourusername and your-repo)
git remote add origin https://github.com/yourusername/fb-ads-creative-manager.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

#### Step 4: Verify Upload

1. Visit your GitHub repository page
2. Confirm all files are uploaded
3. Check that `.gitignore` is working (you shouldn't see `.env` or `__pycache__`)

### Using GitHub Desktop (GUI Method)

If you're not comfortable with command line:

1. Download [GitHub Desktop](https://desktop.github.com/)
2. Sign in with your GitHub account
3. Click "File" → "Clone Repository"
4. Select your repository
5. Choose local path
6. Click "Clone"

Then:
1. Open the local repository folder
2. Copy project files to that folder
3. In GitHub Desktop, you'll see all changes
4. Enter a commit message
5. Click "Commit to main"
6. Click "Push origin"

### Updating the Repository

When you make changes:

```bash
# Check changes
git status

# Add changes
git add .

# Commit
git commit -m "Description of your changes"

# Push to GitHub
git push origin main
```

### Important: Protect Sensitive Information

**Never commit:**
- `.env` file (contains API keys)
- Any files with passwords or tokens
- Personal information

The `.gitignore` file is already configured to automatically exclude these files.

---

## 常见问题 (FAQ)

### Q: 我不小心提交了 `.env` 文件怎么办？

**A:** 立即从 GitHub 中删除：
```bash
git rm --cached .env
git commit -m "Remove .env file"
git push origin main
```

然后重新生成您的 API 密钥（因为它们已经被暴露）。

### Q: 如何更新已上传的文件？

**A:** 
```bash
# 修改文件
# 然后：
git add .
git commit -m "Update: description"
git push origin main
```

### Q: 如何删除已上传的文件？

**A:**
```bash
git rm filename
git commit -m "Remove: filename"
git push origin main
```

### Q: 我可以让仓库私有吗？

**A:** 可以。在 GitHub 仓库设置中：
1. 点击 "Settings"
2. 找到 "Danger Zone"
3. 点击 "Change repository visibility"
4. 选择 "Private"

---

**祝您上传愉快！** 🚀
