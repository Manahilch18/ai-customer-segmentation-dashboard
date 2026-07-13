import streamlit as st
import pandas as pd
import os

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Dataset & Features",
    page_icon="📁",
    layout="wide"
)

# Load CSS if available to maintain consistency
def load_css(css_file):
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("assets/style.css")

# ==========================================
# CACHING DATA LOAD
# ==========================================
@st.cache_data
def load_data():
    """
    Load the pre-processed and clustered customer dataset.
    """
    filepath = "Data/processed/clustered_data.csv"
    if not os.path.exists(filepath):
        st.error(f"Dataset not found at {filepath}")
        return pd.DataFrame()
    return pd.read_csv(filepath)

# ==========================================
# MAIN PAGE CONTENT
# ==========================================
def main():
    st.title("📁 Customer Dataset Overview")
    st.markdown("Explore the raw data, applied filters, and basic dataset statistics used in our segmentation model.")
    st.markdown("---")
    
    # Load Data
    with st.spinner("Loading dataset..."):
        df = load_data()
        
    if df.empty:
        st.warning("No data available to display.")
        return

    # Dataset Statistics section
    st.subheader("Dataset Statistics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Records", f"{df.shape[0]:,}")
    with col2:
        st.metric("Total Features", df.shape[1])
    with col3:
        num_clusters = df['Cluster'].nunique() if 'Cluster' in df.columns else 0
        st.metric("Unique Segments", num_clusters)
    with col4:
        missing_vals = df.isnull().sum().sum()
        st.metric("Missing Values", missing_vals)

    st.markdown("---")
    
    # Filters and Search
    st.subheader("Filter and Search")
    search_col, filter_col = st.columns([2, 1])
    
    with search_col:
        # Search for a customer ID if available
        customer_id_col = 'CustomerID' if 'CustomerID' in df.columns else (
            'Customer ID' if 'Customer ID' in df.columns else None)
            
        search_term = ""
        if customer_id_col:
            search_term = st.text_input("Search by Customer ID:")
            
    with filter_col:
        if 'Cluster' in df.columns:
            selected_cluster = st.selectbox("Filter by Segment:", ["All"] + sorted(df['Cluster'].unique().tolist()))
        else:
            selected_cluster = "All"
            
    # Apply filters
    filtered_df = df.copy()
    
    if search_term and customer_id_col:
        # Assuming CustomerID might be numeric, convert to string for search
        filtered_df = filtered_df[filtered_df[customer_id_col].astype(str).str.contains(search_term)]
        
    if selected_cluster != "All":
        filtered_df = filtered_df[filtered_df['Cluster'] == selected_cluster]

    # Dataset Preview
    st.subheader("Dataset Preview")
    st.dataframe(filtered_df, use_container_width=True)

    # Download Section
    st.markdown("---")
    st.subheader("Export Data")
    
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered CSV 📥",
        data=csv_data,
        file_name='filtered_customer_data.csv',
        mime='text/csv',
    )
    
if __name__ == "__main__":
    main()
