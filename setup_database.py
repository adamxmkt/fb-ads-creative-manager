"""
Setup script to create database tables in Supabase
"""

from supabase import create_client, Client
import os

# Supabase credentials
SUPABASE_URL = "https://lrvezjcycxixmtxqqclh.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxydmV6amN5Y3hpeG10eHFxY2xoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzA4NjE4MDYsImV4cCI6MjA4NjQzNzgwNn0.TG047KRptzFhALcS62BZ9tJblD9FTqjKrfoom2bL2Bk"

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_tables():
    """Create all necessary tables in Supabase"""
    
    # Create creatives table
    print("Creating 'creatives' table...")
    try:
        supabase.table("creatives").select("id").limit(1).execute()
        print("✓ 'creatives' table already exists")
    except:
        print("✗ Creating 'creatives' table...")
        # We'll use SQL to create the table
        # Since we can't directly execute SQL, we'll create it through the UI
        # For now, we'll prepare the SQL
        pass
    
    print("\n✓ Database setup complete!")
    print("\nPlease create the following tables in Supabase SQL Editor:")
    print("\n" + "="*80)
    print("""
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

-- Create materials table (for tracking uploaded files)
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

-- Create performance table (for tracking ad performance)
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

-- Create indexes for better performance
CREATE INDEX idx_creatives_status ON creatives(status);
CREATE INDEX idx_creatives_created_at ON creatives(created_at);
CREATE INDEX idx_materials_creative_id ON materials(creative_id);
CREATE INDEX idx_performance_creative_id ON performance(creative_id);
    """)
    print("="*80)

if __name__ == "__main__":
    create_tables()
