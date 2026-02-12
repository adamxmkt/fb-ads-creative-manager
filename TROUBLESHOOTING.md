# 🔧 故障排除指南

## 常见问题和解决方案

### 应用启动问题

#### Q: 应用无法启动，显示 "ModuleNotFoundError"

**症状：**
```
ModuleNotFoundError: No module named 'streamlit'
```

**解决方案：**
```bash
pip install -r requirements.txt
```

或者单独安装：
```bash
pip install streamlit supabase python-dotenv pandas plotly pillow
```

---

#### Q: 应用启动很慢

**原因：** Streamlit 首次启动需要时间

**解决方案：**
- 第一次启动会比较慢，之后会快一些
- 确保网络连接正常
- 关闭其他占用资源的应用

---

### 数据库连接问题

#### Q: 显示 "Connection refused" 或 "Failed to connect to Supabase"

**症状：**
```
Error: Failed to connect to Supabase
```

**解决方案：**

1. **检查 Supabase 凭证**
   - 打开 `app.py`
   - 确保 `SUPABASE_URL` 和 `SUPABASE_KEY` 正确
   - 检查是否有多余的空格或特殊字符

2. **检查网络连接**
   ```bash
   ping supabase.com
   ```

3. **检查 Supabase 项目状态**
   - 登录 Supabase 控制面板
   - 确保项目处于 "Active" 状态

4. **检查 API Key 权限**
   - 在 Supabase 中，确保使用的是 "anon public" key
   - 不要使用 "service_role" key

---

#### Q: 数据无法保存到数据库

**症状：**
- 创建创意后没有保存
- 显示 "Error saving creative"

**解决方案：**

1. **检查表是否存在**
   - 登录 Supabase
   - 点击 "Table Editor"
   - 确保 `creatives`, `materials`, `performance` 表存在

2. **检查表结构**
   - 确保表的列名和类型正确
   - 参考 README.md 中的数据库结构

3. **查看 Supabase 日志**
   - 在 Supabase 控制面板点击 "Logs"
   - 查看是否有错误信息

---

### 文件上传问题

#### Q: 文件上传失败

**症状：**
```
Error uploading file
```

**解决方案：**

1. **检查 Storage Bucket**
   - 登录 Supabase
   - 点击 "Storage"
   - 确保 `ad-creatives` bucket 存在
   - 确保 bucket 被标记为 "Public"

2. **检查文件大小**
   - 确保文件不超过 100MB
   - 对于视频，建议不超过 50MB

3. **检查文件格式**
   - 支持的格式：JPG, PNG, GIF, MP4, MOV, WebM
   - 确保文件扩展名正确

4. **检查网络连接**
   - 大文件上传需要稳定的网络连接
   - 尝试上传一个小文件测试

---

#### Q: 上传的图片/视频无法显示

**症状：**
- 创意库中看不到上传的素材
- 显示空白或加载中

**解决方案：**

1. **检查 Bucket 权限**
   - 确保 `ad-creatives` bucket 是 "Public"
   - 如果不是，编辑 bucket 设置

2. **检查文件路径**
   - 在 Supabase Storage 中查看文件是否存在
   - 文件应该在 `ad-creatives/creative_id/filename` 路径下

3. **刷新页面**
   - 按 F5 或 Ctrl+R 刷新浏览器
   - 清除浏览器缓存

4. **检查浏览器控制台**
   - 按 F12 打开开发者工具
   - 查看 "Console" 标签中是否有错误

---

### 数据显示问题

#### Q: 创意库中看不到创建的创意

**症状：**
- 创意库为空
- 或者看不到最近创建的创意

**解决方案：**

1. **刷新页面**
   ```
   按 F5 或 Ctrl+R
   ```

2. **检查数据库**
   - 登录 Supabase
   - 点击 "Table Editor"
   - 点击 `creatives` 表
   - 确保数据存在

3. **检查筛选条件**
   - 在创意库中检查是否设置了筛选
   - 尝试清除所有筛选条件

4. **检查搜索框**
   - 清除搜索框中的文本
   - 尝试重新搜索

---

#### Q: 仪表板显示的数据不正确

**症状：**
- 统计数字不对
- 图表显示异常

**解决方案：**

1. **刷新页面**
   ```
   按 F5 或 Ctrl+R
   ```

2. **清除缓存**
   - Streamlit 使用缓存来加速
   - 点击右上角菜单 → "Clear cache"

3. **检查数据**
   - 确保数据已正确保存到数据库
   - 在 Supabase 中检查 `performance` 表

---

### 性能问题

#### Q: 应用运行很慢

**症状：**
- 页面加载缓慢
- 操作响应延迟

**解决方案：**

1. **检查网络连接**
   - 确保网络速度正常
   - 尝试用其他网络测试

2. **减少数据量**
   - 如果有很多创意，尝试使用筛选和搜索
   - 只加载必要的数据

3. **清除浏览器缓存**
   - 按 Ctrl+Shift+Delete
   - 清除缓存和 Cookie

4. **重启应用**
   - 按 Ctrl+C 停止应用
   - 重新运行 `streamlit run app.py`

---

#### Q: 图表加载很慢

**症状：**
- 分析页面加载缓慢
- 图表显示延迟

**解决方案：**

1. **减少数据范围**
   - 尝试只查看最近的数据
   - 使用日期筛选

2. **关闭其他标签页**
   - 减少浏览器占用的资源

3. **更新 Plotly**
   ```bash
   pip install --upgrade plotly
   ```

---

### 其他问题

#### Q: 应用崩溃

**症状：**
- 应用突然停止
- 显示红色错误信息

**解决方案：**

1. **查看错误信息**
   - 记下完整的错误信息
   - 查看是否有特定的错误代码

2. **检查日志**
   - 在终端中查看错误输出
   - 复制完整的错误信息

3. **重启应用**
   ```bash
   # 按 Ctrl+C 停止
   # 然后重新运行
   streamlit run app.py
   ```

4. **检查依赖版本**
   ```bash
   pip list
   ```

---

#### Q: 无法登录或权限问题

**症状：**
- 显示 "Permission denied"
- 无法访问某些功能

**解决方案：**

1. **检查 API Key**
   - 确保使用的是 "anon public" key
   - 不要使用 "service_role" key

2. **检查 Supabase 权限**
   - 登录 Supabase
   - 点击 "Authentication"
   - 检查 RLS (Row Level Security) 设置

3. **重新生成 API Key**
   - 如果 key 可能被泄露，生成新的 key
   - 在 Supabase 中点击 "Settings" → "API"

---

## 获取帮助

### 收集信息

遇到问题时，请收集以下信息：

1. **错误信息**
   - 完整的错误文本
   - 错误代码（如果有）

2. **系统信息**
   ```bash
   python --version
   pip list
   ```

3. **Streamlit 日志**
   - 终端中的完整输出

4. **浏览器信息**
   - 浏览器类型和版本
   - 按 F12 打开开发者工具，查看 Console 标签

### 常用命令

**查看 Python 版本**
```bash
python --version
```

**查看已安装的包**
```bash
pip list
```

**重新安装依赖**
```bash
pip install -r requirements.txt --force-reinstall
```

**清除 Streamlit 缓存**
```bash
streamlit cache clear
```

**查看 Streamlit 配置**
```bash
streamlit config show
```

---

## 联系支持

如果问题仍未解决：

1. **查看官方文档**
   - Streamlit: https://docs.streamlit.io
   - Supabase: https://supabase.com/docs

2. **查看项目文档**
   - README.md
   - SETUP_GUIDE.md

3. **检查社区**
   - Streamlit 论坛
   - Supabase 社区

---

**祝您使用愉快！** 🚀
