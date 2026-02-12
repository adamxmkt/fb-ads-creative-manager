# 🎨 Facebook Ads Creative Manager

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/supabase-2.4+-green.svg)](https://supabase.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, full-featured creative management system for Facebook ads built with **Streamlit** and **Supabase**. Centrally manage, track, and analyze all your ad creatives and materials in one powerful dashboard.

## 📸 Features

### 🎯 Core Functionality

- **📊 Dashboard** - Real-time metrics and performance overview
- **✏️ Create Creative** - Easy creative creation with multi-file upload support
- **🎨 Creative Library** - Browse, search, filter, and manage all creatives
- **📈 Data Analytics** - Visual insights with interactive charts and trends
- **📊 Performance Tracking** - Record and analyze ad performance metrics

### 💪 Advanced Capabilities

- ✅ Multi-language support (Chinese & English)
- ✅ Real-time data synchronization with Supabase
- ✅ Media preview (images and videos)
- ✅ Automatic performance metrics calculation (CTR, conversion rate, ROI)
- ✅ Advanced filtering and search capabilities
- ✅ Responsive design for all devices
- ✅ Secure cloud storage with Supabase

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Supabase account (free tier available)
- Git (for cloning)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/fb-ads-creative-manager.git
cd fb-ads-creative-manager
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up Supabase**
   - Create a free account at [supabase.com](https://supabase.com)
   - Create a new project
   - Run the SQL setup script (see [SETUP_GUIDE.md](SETUP_GUIDE.md))
   - Create a storage bucket named `ad-creatives`

5. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your Supabase credentials
```

6. **Run the application**

For **Chinese version**:
```bash
streamlit run app.py
```

For **English version**:
```bash
streamlit run app_en.py
```

The app will open at `http://localhost:8501`

## 📁 Project Structure

```
fb-ads-creative-manager/
├── app.py                    # Main app (Chinese)
├── app_en.py                # English version
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── README.md                # Chinese documentation
├── README_EN.md             # English documentation
├── QUICK_START.md           # Chinese quick start
├── QUICK_START_EN.md        # English quick start
├── SETUP_GUIDE.md           # Detailed setup guide
├── TROUBLESHOOTING.md       # Common issues & solutions
└── setup_database.py        # Database setup helper
```

## 📊 Database Schema

### Tables

- **creatives** - Stores creative information
- **materials** - Stores uploaded media files
- **performance** - Stores ad performance metrics

See [README.md](README.md) or [README_EN.md](README_EN.md) for detailed schema documentation.

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-public-key
STORAGE_BUCKET=ad-creatives
```

### Supported File Types

**Images:** JPG, PNG, GIF  
**Videos:** MP4, MOV, WebM

## 📖 Documentation

- **[README.md](README.md)** - Chinese version with full feature documentation
- **[README_EN.md](README_EN.md)** - English version with full feature documentation
- **[QUICK_START.md](QUICK_START.md)** - 5-minute quick start (Chinese)
- **[QUICK_START_EN.md](QUICK_START_EN.md)** - 5-minute quick start (English)
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup instructions
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues and solutions

## 🎯 Usage Examples

### Create a Creative

1. Click "✏️ Create Creative"
2. Fill in creative details
3. Upload images/videos
4. Add copy and CTA
5. Save

### Track Performance

1. Click "📊 Performance Tracking"
2. Select a creative
3. Enter performance metrics
4. System auto-calculates CTR, conversion rate, ROI

### View Analytics

1. Click "📈 Data Analytics"
2. View distribution charts
3. Analyze trends and patterns

## 🔒 Security & Privacy

- All data stored securely in Supabase
- API keys should never be committed to git
- Use `.env` file for sensitive credentials
- `.gitignore` prevents accidental commits

## 🐛 Troubleshooting

Common issues and solutions are documented in [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

### Quick Fixes

**Connection error?**
```bash
# Check your .env file
cat .env

# Verify Supabase project is active
# Verify API key is correct
```

**Module not found?**
```bash
pip install -r requirements.txt
```

**Port already in use?**
```bash
streamlit run app.py --server.port 8502
```

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - Amazing framework for data apps
- [Supabase](https://supabase.com/) - Open source Firebase alternative
- [Plotly](https://plotly.com/) - Interactive visualization library

## 📞 Support

For issues and questions:
1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Review the documentation
3. Open an issue on GitHub

## 🚀 Roadmap

- [ ] User authentication
- [ ] Team collaboration features
- [ ] Advanced reporting
- [ ] API integration with Facebook Ads Manager
- [ ] Scheduled reports
- [ ] Mobile app version

---

**Made with ❤️ for Facebook ads managers**

⭐ If you find this project helpful, please consider giving it a star!
