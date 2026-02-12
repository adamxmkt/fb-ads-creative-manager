# 🚀 详细设置指南

本指南将帮助您一步步设置 Facebook 广告创意管理系统。

## 📋 目录

1. [Supabase 设置](#supabase-设置)
2. [本地环境设置](#本地环境设置)
3. [运行应用](#运行应用)
4. [常见问题](#常见问题)

---

## Supabase 设置

### 第一步：创建 Supabase 账户

1. 访问 [https://supabase.com](https://supabase.com)
2. 点击 **Sign Up** 注册
3. 使用邮箱或 GitHub 账户注册
4. 验证邮箱

### 第二步：创建新项目

1. 登录 Supabase 控制面板
2. 点击 **New Project**
3. 填写项目信息：
   - **Project name**: `fb-ads-creative-manager`
   - **Database password**: 设置一个强密码（保存好！）
   - **Region**: 选择离您最近的区域
4. 点击 **Create new project**
5. 等待项目创建完成（约 1-2 分钟）

### 第三步：创建数据库表

1. 在 Supabase 控制面板左侧，点击 **SQL Editor**
2. 点击 **New Query**
3. 复制以下 SQL 代码到编辑器：

```sql
-- Create creatives table
CREATE TABLE creatives (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    creative_type VARCHAR(50) NOT NULL,
    account_name VARCHAR(255),
    campaign_name VARCHAR(255),
    target_audience TEXT,
    status VARCHAR(50) DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT NOW(),
    published_at TIMESTAMP,
    ended_at TIMESTAMP,
    tags TEXT,
    notes TEXT,
    created_by VARCHAR(255),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create materials table
CREATE TABLE materials (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    creative_id BIGINT NOT NULL REFERENCES creatives(id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(500) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size BIGINT,
    copy_text TEXT,
    cta_text VARCHAR(255),
    uploaded_at TIMESTAMP DEFAULT NOW(),
    created_by VARCHAR(255)
);

-- Create performance table
CREATE TABLE performance (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    creative_id BIGINT NOT NULL REFERENCES creatives(id) ON DELETE CASCADE,
    impressions BIGINT DEFAULT 0,
    clicks BIGINT DEFAULT 0,
    conversions BIGINT DEFAULT 0,
    spend DECIMAL(10, 2) DEFAULT 0,
    ctr DECIMAL(5, 2),
    conversion_rate DECIMAL(5, 2),
    roi DECIMAL(5, 2),
    recorded_date DATE DEFAULT CURRENT_DATE,
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes
CREATE INDEX idx_creatives_status ON creatives(status);
CREATE INDEX idx_creatives_created_at ON creatives(created_at);
CREATE INDEX idx_materials_creative_id ON materials(creative_id);
CREATE INDEX idx_performance_creative_id ON performance(creative_id);
```

4. 点击 **Run** 执行 SQL
5. 等待执行完成（应该看到 "Success" 消息）

### 第四步：创建 Storage Bucket

1. 在左侧菜单点击 **Storage**
2. 点击 **Create a new bucket**
3. 输入 bucket 名称：`ad-creatives`
4. **重要**：勾选 **Public bucket**（这样可以公开访问文件）
5. 点击 **Create bucket**

### 第五步：获取 API 凭证

1. 在左侧菜单点击 **Settings**
2. 点击 **API**
3. 复制以下信息：
   - **Project URL** - 看起来像 `https://xxxxx.supabase.co`
   - **anon public** - 这是您的 API Key

**保存这两个信息，接下来会用到！**

---

## 本地环境设置

### 第一步：准备项目文件

项目文件已经在以下位置：
```
/home/ubuntu/fb-ads-creative-manager/
```

### 第二步：安装 Python 依赖

打开终端，运行：

```bash
cd /home/ubuntu/fb-ads-creative-manager
pip install -r requirements.txt
```

### 第三步：配置凭证

**方法 A：直接编辑代码（简单）**

1. 打开 `app.py` 文件
2. 找到这两行（大约在第 20-21 行）：
   ```python
   SUPABASE_URL = "https://lrvezjcycxixmtxqqclh.supabase.co"
   SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
   ```
3. 替换为您从 Supabase 复制的值：
   ```python
   SUPABASE_URL = "your_project_url"
   SUPABASE_KEY = "your_api_key"
   ```
4. 保存文件

**方法 B：使用环境变量（推荐）**

1. 复制 `.env.example` 为 `.env`：
   ```bash
   cp .env.example .env
   ```

2. 编辑 `.env` 文件，填入您的凭证：
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-anon-public-key
   ```

3. 在 `app.py` 中添加以下代码（在导入部分）：
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   
   SUPABASE_URL = os.getenv("SUPABASE_URL")
   SUPABASE_KEY = os.getenv("SUPABASE_KEY")
   ```

---

## 运行应用

### 启动 Streamlit 应用

在项目目录中运行：

```bash
streamlit run app.py
```

您应该会看到类似的输出：

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### 访问应用

1. 打开浏览器
2. 访问 `http://localhost:8501`
3. 应该看到应用的首页

---

## 常见问题

### Q: 我看到 "ModuleNotFoundError" 错误

**A:** 这意味着某些依赖没有安装。运行：
```bash
pip install -r requirements.txt
```

### Q: 连接到 Supabase 失败

**A:** 检查以下几点：
1. 确保 SUPABASE_URL 和 SUPABASE_KEY 正确
2. 确保网络连接正常
3. 检查 Supabase 项目是否在运行
4. 查看浏览器控制台（F12）的错误信息

### Q: 文件上传失败

**A:** 检查以下几点：
1. 确保 `ad-creatives` bucket 已创建
2. 确保 bucket 被标记为 "Public"
3. 文件大小不超过 100MB
4. 文件格式被支持（JPG, PNG, MP4 等）

### Q: 我看不到上传的图片/视频

**A:** 可能的原因：
1. 文件还在上传中，请等待
2. Storage bucket 不是 public
3. 文件路径不正确
4. 浏览器缓存，尝试刷新页面

### Q: 如何停止应用？

**A:** 在终端中按 `Ctrl + C`

### Q: 如何重新启动应用？

**A:** 再次运行：
```bash
streamlit run app.py
```

### Q: 如何修改应用配置？

**A:** 编辑 `app.py` 文件中的配置部分（第 15-20 行）

---

## 下一步

应用启动后，您可以：

1. **创建第一个创意**
   - 点击 "✏️ 创建创意"
   - 填写创意信息
   - 上传素材
   - 保存

2. **浏览创意库**
   - 点击 "🎨 创意库"
   - 查看所有创意
   - 搜索和筛选

3. **追踪效果**
   - 点击 "📊 效果追踪"
   - 添加广告效果数据
   - 查看历史记录

4. **查看分析**
   - 点击 "📈 数据分析"
   - 查看各种图表和统计

---

## 需要帮助？

如果遇到问题：

1. 查看 README.md 中的故障排除部分
2. 检查 Supabase 文档：https://supabase.com/docs
3. 检查 Streamlit 文档：https://docs.streamlit.io

---

**祝您使用愉快！** 🎉
