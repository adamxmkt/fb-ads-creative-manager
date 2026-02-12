# 🎨 Facebook Ads Creative Manager

A comprehensive, Streamlit-based and Supabase-powered Facebook ads creative management platform. Centrally manage, track, and analyze all your ad creatives and materials.

## ✨ Key Features

### 📊 Dashboard
- Real-time display of key metrics (total creatives, active creatives, drafts, etc.)
- Performance overview (impressions, clicks, conversions, spend)
- Recent creatives list
- Quick access to top-performing creatives

### ✏️ Create Creative
- Create new ad creatives
- Record creative name, description, target audience
- Support multiple creative types (image, video, carousel, text, etc.)
- Upload multiple material files at once
- Add copy and call-to-action (CTA) for each material
- Auto-save to Supabase

### 🎨 Creative Library
- Browse all created creatives
- Search creatives by name
- Filter by status and type
- View detailed creative information
- Update creative status (draft, running, paused, ended)
- Preview uploaded materials (images and videos)
- View copy and CTA text

### 📈 Data Analytics
- Creative type distribution pie chart
- Creative status distribution bar chart
- Creative creation timeline
- Performance metrics summary
- CTR trend analysis

### 📊 Performance Tracking
- Add ad performance data for each creative
- Record impressions, clicks, conversions, spend
- Auto-calculate CTR, conversion rate, ROI
- View performance data history

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Supabase account
- Internet connection

### Installation Steps

1. **Clone or download the project**
```bash
cd /home/ubuntu/fb-ads-creative-manager
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Supabase**
   - Create the following tables in Supabase:
     - `creatives` - Store creative information
     - `materials` - Store material information
     - `performance` - Store performance data
   - Create Storage bucket: `ad-creatives`
   - Copy your Supabase URL and API Key

4. **Update configuration**
   - Open `app_en.py`
   - Replace the following variables:
     ```python
     SUPABASE_URL = "your_supabase_url"
     SUPABASE_KEY = "your_supabase_key"
     ```

5. **Run the application**
```bash
streamlit run app_en.py
```

6. **Access the application**
   - Open your browser and visit `http://localhost:8501`

## 📊 Database Structure

### creatives table
Stores basic information about all ad creatives

| Field | Type | Description |
|-------|------|-------------|
| id | BIGINT | Creative ID (auto-generated) |
| name | VARCHAR | Creative name |
| description | TEXT | Creative description |
| creative_type | VARCHAR | Creative type (image, video, etc.) |
| account_name | VARCHAR | Ad account name |
| campaign_name | VARCHAR | Ad campaign name |
| target_audience | TEXT | Target audience description |
| status | VARCHAR | Status (draft, running, paused, ended) |
| created_at | TIMESTAMP | Creation time |
| published_at | TIMESTAMP | Publication time |
| ended_at | TIMESTAMP | End time |
| tags | TEXT | Tags (comma-separated) |
| notes | TEXT | Notes |
| updated_at | TIMESTAMP | Update time |

### materials table
Stores uploaded material file information

| Field | Type | Description |
|-------|------|-------------|
| id | BIGINT | Material ID |
| creative_id | BIGINT | Associated creative ID |
| file_name | VARCHAR | File name |
| file_path | VARCHAR | File path in Storage |
| file_type | VARCHAR | File type (MIME type) |
| file_size | BIGINT | File size (bytes) |
| copy_text | TEXT | Ad copy |
| cta_text | VARCHAR | Call-to-action text |
| uploaded_at | TIMESTAMP | Upload time |

### performance table
Stores ad performance data

| Field | Type | Description |
|-------|------|-------------|
| id | BIGINT | Record ID |
| creative_id | BIGINT | Associated creative ID |
| impressions | BIGINT | Impressions |
| clicks | BIGINT | Clicks |
| conversions | BIGINT | Conversions |
| spend | DECIMAL | Spend amount |
| ctr | DECIMAL | Click-through rate (%) |
| conversion_rate | DECIMAL | Conversion rate (%) |
| roi | DECIMAL | Return on investment (%) |
| recorded_date | DATE | Record date |
| updated_at | TIMESTAMP | Update time |

## 💡 Usage Guide

### Creating a New Creative

1. Click **✏️ Create Creative** in the left menu
2. Fill in the creative information:
   - Creative name (required)
   - Creative type (required)
   - Description, account, campaign, etc. (optional)
3. Upload material files (supports images and videos)
4. Add copy and CTA for each material
5. Click **💾 Save Creative**

### Managing Creatives

1. Click **🎨 Creative Library**
2. Use the search box and filters to find creatives
3. Click on creative name to expand details
4. You can:
   - View creative information
   - Update creative status
   - Preview uploaded materials
   - View copy and CTA

### Tracking Performance

1. Click **📊 Performance Tracking**
2. Select the creative to track
3. Enter ad performance data:
   - Impressions
   - Clicks
   - Conversions
   - Spend amount
4. Click **💾 Save Performance Data**
5. System will auto-calculate CTR, conversion rate, and ROI

### Viewing Analytics

1. Click **📈 Data Analytics**
2. View various visualization charts:
   - Creative type distribution
   - Creative status distribution
   - Creative creation timeline
   - Performance metrics
   - CTR trends

## 🔧 Configuration Options

### Supported File Types

**Images:**
- JPG / JPEG
- PNG
- GIF

**Videos:**
- MP4
- MOV
- WebM

### Creative Types

- Image
- Video
- Carousel
- Text
- Other

### Creative Status

- **draft** - Draft (not published)
- **running** - Running (actively delivering)
- **paused** - Paused (delivery paused)
- **ended** - Ended (delivery completed)

## 📱 Responsive Design

The application supports multiple devices:
- 💻 Desktop browsers
- 📱 Tablets
- 📲 Mobile browsers

## 🔒 Data Security

- All data stored in Supabase cloud
- Auto backup and version control
- Support for access permission management
- Material files stored in Supabase Storage

## 📈 Performance Optimization

- Use caching to reduce database queries
- Auto optimize images and videos
- Paginated loading for large datasets
- Real-time data updates

## 🐛 Troubleshooting

### Connection Issues
- Check if Supabase URL and API Key are correct
- Ensure network connection is stable
- Check if Supabase project is running

### File Upload Failures
- Check if file size is too large
- Ensure file format is supported
- Check if Storage bucket is created

### Data Not Displaying
- Refresh the page
- Check database connection
- Check browser console for errors

## 📞 Support

If you encounter issues:
1. Check this documentation
2. Review error messages
3. Check Supabase logs

## 📝 Changelog

### v1.0.0 (2024-02-12)
- ✅ Initial release
- ✅ Complete creative management functionality
- ✅ Material upload and preview
- ✅ Performance tracking
- ✅ Data analytics and visualization

## 📄 License

This project is for personal use.

## 🙏 Acknowledgments

Thanks to Streamlit and Supabase for providing excellent services!

---

**Happy using!** 🚀
