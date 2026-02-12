# 🎨 Facebook 广告创意管理系统

一个完整的、基于 Streamlit 和 Supabase 的 Facebook 广告创意管理平台。帮助您集中管理、追踪和分析所有的广告创意和素材。

## ✨ 功能特性

### 📊 仪表板
- 实时显示关键指标（总创意数、运行中的创意、草稿数量等）
- 性能概览（展示、点击、转化、花费）
- 最近创建的创意列表
- 快速访问最佳表现创意

### ✏️ 创建创意
- 创建新的广告创意
- 记录创意名称、描述、目标受众
- 支持多种创意类型（图片、视频、轮播、文本等）
- 一次上传多个素材文件
- 为每个素材添加文案和行动号召（CTA）
- 自动保存到 Supabase

### 🎨 创意库
- 浏览所有已创建的创意
- 按名称搜索创意
- 按状态和类型筛选
- 查看创意的详细信息
- 更新创意状态（草稿、运行中、暂停、已结束）
- 预览上传的素材（图片和视频）
- 查看文案和 CTA 文本

### 📈 数据分析
- 创意类型分布饼图
- 创意状态分布柱状图
- 创意创建时间线
- 性能指标汇总
- CTR 趋势分析

### 📊 效果追踪
- 为每个创意添加广告效果数据
- 记录展示、点击、转化、花费
- 自动计算 CTR、转化率、ROI
- 查看效果数据历史

## 🚀 快速开始

### 前置要求
- Python 3.8+
- Supabase 账户
- 互联网连接

### 安装步骤

1. **克隆或下载项目**
```bash
cd /home/ubuntu/fb-ads-creative-manager
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **配置 Supabase**
   - 在 Supabase 中创建以下表：
     - `creatives` - 存储创意信息
     - `materials` - 存储素材信息
     - `performance` - 存储效果数据
   - 创建 Storage bucket：`ad-creatives`
   - 复制您的 Supabase URL 和 API Key

4. **更新配置**
   - 打开 `app.py`
   - 替换以下变量：
     ```python
     SUPABASE_URL = "your_supabase_url"
     SUPABASE_KEY = "your_supabase_key"
     ```

5. **运行应用**
```bash
streamlit run app.py
```

6. **访问应用**
   - 打开浏览器访问 `http://localhost:8501`

## 📊 数据库结构

### creatives 表
存储所有广告创意的基本信息

| 字段 | 类型 | 描述 |
|------|------|------|
| id | BIGINT | 创意 ID（自动生成） |
| name | VARCHAR | 创意名称 |
| description | TEXT | 创意描述 |
| creative_type | VARCHAR | 创意类型（图片、视频等） |
| account_name | VARCHAR | 广告账户名称 |
| campaign_name | VARCHAR | 广告活动名称 |
| target_audience | TEXT | 目标受众描述 |
| status | VARCHAR | 状态（draft、running、paused、ended） |
| created_at | TIMESTAMP | 创建时间 |
| published_at | TIMESTAMP | 发布时间 |
| ended_at | TIMESTAMP | 结束时间 |
| tags | TEXT | 标签（逗号分隔） |
| notes | TEXT | 备注 |
| updated_at | TIMESTAMP | 更新时间 |

### materials 表
存储上传的素材文件信息

| 字段 | 类型 | 描述 |
|------|------|------|
| id | BIGINT | 素材 ID |
| creative_id | BIGINT | 关联的创意 ID |
| file_name | VARCHAR | 文件名 |
| file_path | VARCHAR | 文件在 Storage 中的路径 |
| file_type | VARCHAR | 文件类型（MIME type） |
| file_size | BIGINT | 文件大小（字节） |
| copy_text | TEXT | 广告文案 |
| cta_text | VARCHAR | 行动号召文本 |
| uploaded_at | TIMESTAMP | 上传时间 |

### performance 表
存储广告效果数据

| 字段 | 类型 | 描述 |
|------|------|------|
| id | BIGINT | 记录 ID |
| creative_id | BIGINT | 关联的创意 ID |
| impressions | BIGINT | 展示次数 |
| clicks | BIGINT | 点击次数 |
| conversions | BIGINT | 转化次数 |
| spend | DECIMAL | 花费金额 |
| ctr | DECIMAL | 点击率（%） |
| conversion_rate | DECIMAL | 转化率（%） |
| roi | DECIMAL | 投资回报率（%） |
| recorded_date | DATE | 记录日期 |
| updated_at | TIMESTAMP | 更新时间 |

## 💡 使用指南

### 创建新创意

1. 点击左侧菜单的 **✏️ 创建创意**
2. 填写创意基本信息：
   - 创意名称（必填）
   - 创意类型（必填）
   - 描述、账户、活动等可选信息
3. 上传素材文件（支持图片和视频）
4. 为每个素材添加文案和 CTA
5. 点击 **💾 保存创意**

### 管理创意

1. 点击 **🎨 创意库**
2. 使用搜索框和筛选器查找创意
3. 点击创意名称展开详情
4. 可以：
   - 查看创意信息
   - 更新创意状态
   - 预览上传的素材
   - 查看文案和 CTA

### 追踪效果

1. 点击 **📊 效果追踪**
2. 选择要追踪的创意
3. 输入广告效果数据：
   - 展示次数
   - 点击次数
   - 转化次数
   - 花费金额
4. 点击 **💾 保存效果数据**
5. 系统会自动计算 CTR、转化率和 ROI

### 查看分析

1. 点击 **📈 数据分析**
2. 查看各种可视化图表：
   - 创意类型分布
   - 创意状态分布
   - 创意创建时间线
   - 性能指标
   - CTR 趋势

## 🔧 配置选项

### 支持的文件类型

**图片：**
- JPG / JPEG
- PNG
- GIF

**视频：**
- MP4
- MOV
- WebM

### 创意类型

- 图片
- 视频
- 轮播
- 文本
- 其他

### 创意状态

- **draft** - 草稿（未发布）
- **running** - 运行中（正在投放）
- **paused** - 暂停（已暂停投放）
- **ended** - 已结束（投放结束）

## 📱 响应式设计

应用支持多种设备：
- 💻 桌面浏览器
- 📱 平板设备
- 📲 手机浏览器

## 🔒 数据安全

- 所有数据存储在 Supabase 云端
- 自动备份和版本控制
- 支持访问权限管理
- 素材文件存储在 Supabase Storage

## 📈 性能优化

- 使用缓存减少数据库查询
- 图片和视频自动优化
- 分页加载大数据集
- 实时数据更新

## 🐛 故障排除

### 连接问题
- 检查 Supabase URL 和 API Key 是否正确
- 确保网络连接正常
- 检查 Supabase 项目是否正在运行

### 文件上传失败
- 检查文件大小是否过大
- 确保文件格式被支持
- 检查 Storage bucket 是否已创建

### 数据未显示
- 刷新页面
- 检查数据库连接
- 查看浏览器控制台是否有错误

## 📞 支持

如有问题或建议，请：
1. 检查本文档
2. 查看错误消息
3. 检查 Supabase 日志

## 📝 更新日志

### v1.0.0 (2024-02-12)
- ✅ 初始版本发布
- ✅ 完整的创意管理功能
- ✅ 素材上传和预览
- ✅ 效果追踪
- ✅ 数据分析和可视化

## 📄 许可证

本项目为个人使用项目。

## 🙏 致谢

感谢 Streamlit 和 Supabase 提供的优秀服务！

---

**祝您使用愉快！** 🚀
