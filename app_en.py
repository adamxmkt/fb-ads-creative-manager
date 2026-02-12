"""
Facebook Ads Creative Manager - Streamlit Application (English Version)
A comprehensive system for managing, tracking, and analyzing Facebook ad creatives
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from supabase import create_client, Client
import os
from PIL import Image
import io
import base64

# ============================================================================
# CONFIGURATION
# ============================================================================

SUPABASE_URL = "https://lrvezjcycxixmtxqqclh.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxydmV6amN5Y3hpeG10eHFxY2xoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzA4NjE4MDYsImV4cCI6MjA4NjQzNzgwNn0.TG047KRptzFhALcS62BZ9tJblD9FTqjKrfoom2bL2Bk"
STORAGE_BUCKET = "ad-creatives"

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="FB Ads Creative Manager",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# INITIALIZE SUPABASE CLIENT
# ============================================================================

@st.cache_resource
def init_supabase():
    """Initialize Supabase client"""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase: Client = init_supabase()

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def upload_file_to_supabase(file, file_path):
    """Upload file to Supabase Storage"""
    try:
        file_data = file.read()
        response = supabase.storage.from_(STORAGE_BUCKET).upload(
            path=file_path,
            file=file_data,
            file_options={"content-type": file.type}
        )
        return True, file_path
    except Exception as e:
        return False, str(e)

def get_file_url(file_path):
    """Get public URL for a file in Supabase Storage"""
    try:
        url = supabase.storage.from_(STORAGE_BUCKET).get_public_url(file_path)
        return url
    except:
        return None

def save_creative(name, description, creative_type, account_name, campaign_name, 
                 target_audience, status, tags, notes):
    """Save creative to database"""
    try:
        data = {
            "name": name,
            "description": description,
            "creative_type": creative_type,
            "account_name": account_name,
            "campaign_name": campaign_name,
            "target_audience": target_audience,
            "status": status,
            "tags": tags,
            "notes": notes,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = supabase.table("creatives").insert(data).execute()
        return True, response.data[0]["id"]
    except Exception as e:
        return False, str(e)

def save_material(creative_id, file_name, file_path, file_type, file_size, copy_text, cta_text):
    """Save material information to database"""
    try:
        data = {
            "creative_id": creative_id,
            "file_name": file_name,
            "file_path": file_path,
            "file_type": file_type,
            "file_size": file_size,
            "copy_text": copy_text,
            "cta_text": cta_text,
            "uploaded_at": datetime.now().isoformat()
        }
        response = supabase.table("materials").insert(data).execute()
        return True, response.data[0]["id"]
    except Exception as e:
        return False, str(e)

def get_creatives(status=None, creative_type=None, limit=100):
    """Fetch creatives from database"""
    try:
        query = supabase.table("creatives").select("*").order("created_at", desc=True)
        
        if status:
            query = query.eq("status", status)
        if creative_type:
            query = query.eq("creative_type", creative_type)
        
        response = query.limit(limit).execute()
        return response.data
    except Exception as e:
        st.error(f"Error fetching creatives: {str(e)}")
        return []

def get_materials_for_creative(creative_id):
    """Fetch materials for a specific creative"""
    try:
        response = supabase.table("materials").select("*").eq("creative_id", creative_id).execute()
        return response.data
    except Exception as e:
        st.error(f"Error fetching materials: {str(e)}")
        return []

def get_performance_for_creative(creative_id):
    """Fetch performance data for a specific creative"""
    try:
        response = supabase.table("performance").select("*").eq("creative_id", creative_id).execute()
        return response.data
    except Exception as e:
        st.error(f"Error fetching performance: {str(e)}")
        return []

def update_creative_status(creative_id, status):
    """Update creative status"""
    try:
        data = {
            "status": status,
            "updated_at": datetime.now().isoformat()
        }
        supabase.table("creatives").update(data).eq("id", creative_id).execute()
        return True
    except Exception as e:
        return False

def save_performance_data(creative_id, impressions, clicks, conversions, spend):
    """Save performance data"""
    try:
        ctr = (clicks / impressions * 100) if impressions > 0 else 0
        conversion_rate = (conversions / clicks * 100) if clicks > 0 else 0
        roi = ((conversions - spend) / spend * 100) if spend > 0 else 0
        
        data = {
            "creative_id": creative_id,
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "spend": spend,
            "ctr": round(ctr, 2),
            "conversion_rate": round(conversion_rate, 2),
            "roi": round(roi, 2),
            "recorded_date": datetime.now().date().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = supabase.table("performance").insert(data).execute()
        return True, response.data[0]["id"]
    except Exception as e:
        return False, str(e)

def get_dashboard_stats():
    """Get statistics for dashboard"""
    try:
        creatives = supabase.table("creatives").select("*").execute()
        total_creatives = len(creatives.data)
        
        active_creatives = len([c for c in creatives.data if c["status"] == "running"])
        draft_creatives = len([c for c in creatives.data if c["status"] == "draft"])
        
        # Get performance data
        performance = supabase.table("performance").select("*").execute()
        total_impressions = sum([p["impressions"] for p in performance.data])
        total_clicks = sum([p["clicks"] for p in performance.data])
        total_conversions = sum([p["conversions"] for p in performance.data])
        total_spend = sum([p["spend"] for p in performance.data])
        
        return {
            "total_creatives": total_creatives,
            "active_creatives": active_creatives,
            "draft_creatives": draft_creatives,
            "total_impressions": total_impressions,
            "total_clicks": total_clicks,
            "total_conversions": total_conversions,
            "total_spend": total_spend
        }
    except Exception as e:
        st.error(f"Error getting dashboard stats: {str(e)}")
        return None

# ============================================================================
# PAGE CONTENT
# ============================================================================

def page_dashboard():
    """Dashboard page"""
    st.title("📊 Creative Management System")
    st.markdown("---")
    
    stats = get_dashboard_stats()
    
    if stats:
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Creatives", stats["total_creatives"])
        
        with col2:
            st.metric("Active", stats["active_creatives"])
        
        with col3:
            st.metric("Drafts", stats["draft_creatives"])
        
        with col4:
            st.metric("Total Impressions", f"{stats['total_impressions']:,}")
        
        st.markdown("---")
        
        # Performance metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Clicks", f"{stats['total_clicks']:,}")
        
        with col2:
            st.metric("Total Conversions", f"{stats['total_conversions']:,}")
        
        with col3:
            st.metric("Total Spend", f"${stats['total_spend']:,.2f}")
        
        with col4:
            if stats['total_clicks'] > 0:
                ctr = (stats['total_clicks'] / stats['total_impressions'] * 100) if stats['total_impressions'] > 0 else 0
                st.metric("Average CTR", f"{ctr:.2f}%")
        
        st.markdown("---")
        
        # Recent creatives
        st.subheader("📝 Recent Creatives")
        creatives = get_creatives(limit=10)
        
        if creatives:
            df = pd.DataFrame(creatives)
            df["created_at"] = pd.to_datetime(df["created_at"]).dt.strftime("%Y-%m-%d %H:%M")
            
            display_df = df[["name", "creative_type", "status", "account_name", "created_at"]]
            st.dataframe(display_df, use_container_width=True)
        else:
            st.info("No creatives yet. Create your first creative!")

def page_create_creative():
    """Create new creative page"""
    st.title("✏️ Create New Creative")
    st.markdown("---")
    
    with st.form("create_creative_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Creative Name *", placeholder="e.g., Summer Sale - Image Version A")
            creative_type = st.selectbox("Creative Type *", ["Image", "Video", "Carousel", "Text", "Other"])
        
        with col2:
            account_name = st.text_input("Ad Account", placeholder="e.g., My Facebook Account")
            campaign_name = st.text_input("Campaign", placeholder="e.g., February Spring Campaign")
        
        description = st.text_area("Description", placeholder="Describe the creative idea and objectives")
        target_audience = st.text_area("Target Audience", placeholder="e.g., Women aged 18-25 interested in fashion")
        
        col1, col2 = st.columns(2)
        
        with col1:
            status = st.selectbox("Status", ["draft", "running", "paused", "ended"])
            tags = st.text_input("Tags (comma-separated)", placeholder="e.g., summer, sale, women")
        
        with col2:
            notes = st.text_area("Notes", placeholder="Additional notes")
        
        st.markdown("---")
        st.subheader("📤 Upload Materials")
        
        uploaded_files = st.file_uploader(
            "Upload media files (images or videos)",
            type=["jpg", "jpeg", "png", "gif", "mp4", "mov", "webm"],
            accept_multiple_files=True
        )
        
        if uploaded_files:
            st.info(f"Selected {len(uploaded_files)} file(s)")
            
            for idx, file in enumerate(uploaded_files):
                st.write(f"**File {idx + 1}: {file.name}**")
                
                col1, col2 = st.columns(2)
                with col1:
                    copy_text = st.text_area(f"Copy {idx + 1}", placeholder="Ad copy text", key=f"copy_{idx}")
                with col2:
                    cta_text = st.text_input(f"Call-to-Action {idx + 1}", placeholder="e.g., Shop Now", key=f"cta_{idx}")
        
        st.markdown("---")
        
        submit_button = st.form_submit_button("💾 Save Creative", use_container_width=True)
        
        if submit_button:
            if not name:
                st.error("Please enter a creative name")
            else:
                # Save creative
                success, creative_id = save_creative(
                    name=name,
                    description=description,
                    creative_type=creative_type,
                    account_name=account_name,
                    campaign_name=campaign_name,
                    target_audience=target_audience,
                    status=status,
                    tags=tags,
                    notes=notes
                )
                
                if success:
                    st.success(f"✅ Creative saved! ID: {creative_id}")
                    
                    # Upload files
                    if uploaded_files:
                        for idx, file in enumerate(uploaded_files):
                            file_path = f"{creative_id}/{file.name}"
                            upload_success, upload_msg = upload_file_to_supabase(file, file_path)
                            
                            if upload_success:
                                # Save material info
                                copy_text = st.session_state.get(f"copy_{idx}", "")
                                cta_text = st.session_state.get(f"cta_{idx}", "")
                                
                                mat_success, mat_id = save_material(
                                    creative_id=creative_id,
                                    file_name=file.name,
                                    file_path=file_path,
                                    file_type=file.type,
                                    file_size=file.size,
                                    copy_text=copy_text,
                                    cta_text=cta_text
                                )
                                
                                if mat_success:
                                    st.success(f"✅ Material uploaded: {file.name}")
                                else:
                                    st.error(f"❌ Failed to save material info: {mat_id}")
                            else:
                                st.error(f"❌ Upload failed: {upload_msg}")
                    
                    st.balloons()
                else:
                    st.error(f"❌ Save failed: {creative_id}")

def page_creative_library():
    """Creative library page"""
    st.title("🎨 Creative Library")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_name = st.text_input("Search creative name")
    
    with col2:
        filter_status = st.selectbox("Filter by status", ["All", "draft", "running", "paused", "ended"])
    
    with col3:
        filter_type = st.selectbox("Filter by type", ["All", "Image", "Video", "Carousel", "Text", "Other"])
    
    st.markdown("---")
    
    # Fetch creatives
    status_filter = None if filter_status == "All" else filter_status
    type_filter = None if filter_type == "All" else filter_type
    
    creatives = get_creatives(status=status_filter, creative_type=type_filter)
    
    # Filter by name
    if search_name:
        creatives = [c for c in creatives if search_name.lower() in c["name"].lower()]
    
    if creatives:
        for creative in creatives:
            with st.expander(f"📌 {creative['name']} ({creative['creative_type']})"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Description:** {creative['description']}")
                    st.write(f"**Account:** {creative['account_name']}")
                    st.write(f"**Campaign:** {creative['campaign_name']}")
                    st.write(f"**Target Audience:** {creative['target_audience']}")
                    st.write(f"**Tags:** {creative['tags']}")
                    st.write(f"**Notes:** {creative['notes']}")
                
                with col2:
                    st.write(f"**Status:** {creative['status']}")
                    st.write(f"**Created:** {creative['created_at'][:10]}")
                    
                    new_status = st.selectbox(
                        "Update Status",
                        ["draft", "running", "paused", "ended"],
                        index=["draft", "running", "paused", "ended"].index(creative["status"]),
                        key=f"status_{creative['id']}"
                    )
                    
                    if st.button("Save Status", key=f"save_status_{creative['id']}"):
                        if update_creative_status(creative["id"], new_status):
                            st.success("✅ Status updated")
                        else:
                            st.error("❌ Update failed")
                
                # Show materials
                st.markdown("---")
                st.subheader("📁 Materials")
                
                materials = get_materials_for_creative(creative["id"])
                
                if materials:
                    for material in materials:
                        st.write(f"**File:** {material['file_name']}")
                        st.write(f"**Copy:** {material['copy_text']}")
                        st.write(f"**CTA:** {material['cta_text']}")
                        
                        # Try to display media
                        file_url = get_file_url(material['file_path'])
                        if file_url:
                            if material['file_type'].startswith('image'):
                                st.image(file_url, use_column_width=True)
                            elif material['file_type'].startswith('video'):
                                st.video(file_url)
                        
                        st.write(f"Uploaded: {material['uploaded_at'][:10]}")
                        st.markdown("---")
                else:
                    st.info("No materials uploaded yet")
    else:
        st.info("No creatives found")

def page_analytics():
    """Analytics page"""
    st.title("📈 Data Analytics")
    st.markdown("---")
    
    creatives = get_creatives()
    
    if not creatives:
        st.info("No creative data available")
        return
    
    # Creative type distribution
    st.subheader("Creative Type Distribution")
    
    creative_types = {}
    for creative in creatives:
        ct = creative["creative_type"]
        creative_types[ct] = creative_types.get(ct, 0) + 1
    
    if creative_types:
        fig = px.pie(
            values=list(creative_types.values()),
            names=list(creative_types.keys()),
            title="Creative Type Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Status distribution
    st.subheader("Creative Status Distribution")
    
    statuses = {}
    for creative in creatives:
        status = creative["status"]
        statuses[status] = statuses.get(status, 0) + 1
    
    if statuses:
        fig = px.bar(
            x=list(statuses.keys()),
            y=list(statuses.values()),
            labels={"x": "Status", "y": "Count"},
            title="Creative Status Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Timeline
    st.subheader("Creative Creation Timeline")
    
    df = pd.DataFrame(creatives)
    df["created_date"] = pd.to_datetime(df["created_at"]).dt.date
    
    timeline = df.groupby("created_date").size().reset_index(name="count")
    
    if not timeline.empty:
        fig = px.line(
            timeline,
            x="created_date",
            y="count",
            markers=True,
            title="Creative Creation Timeline"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance metrics
    st.subheader("Performance Metrics")
    
    all_performance = supabase.table("performance").select("*").execute()
    
    if all_performance.data:
        perf_df = pd.DataFrame(all_performance.data)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Impressions", f"{perf_df['impressions'].sum():,}")
        
        with col2:
            st.metric("Total Clicks", f"{perf_df['clicks'].sum():,}")
        
        with col3:
            st.metric("Total Conversions", f"{perf_df['conversions'].sum():,}")
        
        with col4:
            st.metric("Total Spend", f"${perf_df['spend'].sum():,.2f}")
        
        st.markdown("---")
        
        # CTR over time
        st.subheader("CTR Trend")
        
        perf_df["recorded_date"] = pd.to_datetime(perf_df["recorded_date"])
        perf_df = perf_df.sort_values("recorded_date")
        
        fig = px.line(
            perf_df,
            x="recorded_date",
            y="ctr",
            title="CTR Trend"
        )
        st.plotly_chart(fig, use_container_width=True)

def page_performance():
    """Performance tracking page"""
    st.title("📊 Performance Tracking")
    st.markdown("---")
    
    creatives = get_creatives()
    
    if not creatives:
        st.info("No creatives available")
        return
    
    creative_options = {c["name"]: c["id"] for c in creatives}
    
    selected_creative_name = st.selectbox("Select Creative", list(creative_options.keys()))
    selected_creative_id = creative_options[selected_creative_name]
    
    st.markdown("---")
    st.subheader("Add Performance Data")
    
    with st.form("performance_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            impressions = st.number_input("Impressions", min_value=0, value=0)
            clicks = st.number_input("Clicks", min_value=0, value=0)
        
        with col2:
            conversions = st.number_input("Conversions", min_value=0, value=0)
            spend = st.number_input("Spend ($)", min_value=0.0, value=0.0, step=0.01)
        
        submit = st.form_submit_button("💾 Save Performance Data", use_container_width=True)
        
        if submit:
            success, msg = save_performance_data(
                selected_creative_id,
                impressions,
                clicks,
                conversions,
                spend
            )
            
            if success:
                st.success("✅ Performance data saved")
            else:
                st.error(f"❌ Save failed: {msg}")
    
    st.markdown("---")
    st.subheader("Performance History")
    
    performance_data = get_performance_for_creative(selected_creative_id)
    
    if performance_data:
        perf_df = pd.DataFrame(performance_data)
        perf_df["recorded_date"] = pd.to_datetime(perf_df["recorded_date"]).dt.strftime("%Y-%m-%d")
        
        display_df = perf_df[["recorded_date", "impressions", "clicks", "conversions", "spend", "ctr", "conversion_rate", "roi"]]
        st.dataframe(display_df, use_container_width=True)
    else:
        st.info("No performance data yet")

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main app"""
    
    # Sidebar navigation
    st.sidebar.title("🎨 Creative Manager")
    st.sidebar.markdown("---")
    
    page = st.sidebar.radio(
        "Navigation",
        ["📊 Dashboard", "✏️ Create Creative", "🎨 Library", "📈 Analytics", "📊 Performance"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info(
        "**Facebook Ads Creative Manager**\n\n"
        "A complete creative management platform to:\n"
        "- 📝 Record all creative ideas\n"
        "- 📤 Upload and manage materials\n"
        "- 📊 Track ad performance\n"
        "- 📈 Analyze data trends"
    )
    
    # Route pages
    if page == "📊 Dashboard":
        page_dashboard()
    elif page == "✏️ Create Creative":
        page_create_creative()
    elif page == "🎨 Library":
        page_creative_library()
    elif page == "📈 Analytics":
        page_analytics()
    elif page == "📊 Performance":
        page_performance()

if __name__ == "__main__":
    main()
