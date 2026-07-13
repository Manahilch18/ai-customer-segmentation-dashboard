import streamlit as st
import pandas as pd
import os

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD CUSTOM CSS
# ==========================================
def load_css(css_file):
    """
    Loads custom CSS from a file into the Streamlit app.
    Args:
        css_file (str): Path to the CSS file.
    """
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found: {css_file}")

# Load the custom CSS for professional UI polishing
load_css("assets/style.css")

# ==========================================
# CACHING DATA LOAD
# ==========================================
@st.cache_data
def load_data(filepath):
    """
    Loads dataset from a CSV file. Uses Streamlit caching for performance.
    Args:
        filepath (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    try:
        if not os.path.exists(filepath):
            st.error(f"File not found: {filepath}")
            return None
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None

# ==========================================
# MAIN APP COMPONENT
# ==========================================
def main():
    """
    Main function to render the Welcome Page of the Dashboard.
    """
    # Sidebar Setup
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3121/3121693.png", width=100)
    st.sidebar.title("Navigation")
    st.sidebar.info(
        "Welcome to the AI-Powered Customer Segmentation Dashboard. "
        "Use the sidebar to navigate through datasets, segments, PCA visualization, and insights."
    )

    # Page Header
    st.title("📊 AI-Powered Customer Segmentation Dashboard")
    st.markdown("""
        **Welcome to the Customer Analytics Hub.** 
        This dashboard uses Unsupervised Machine Learning (K-Means Clustering) and RFM 
        (Recency, Frequency, Monetary) analysis to group customers into meaningful segments.
    """)
    st.markdown("---")

    # Load Dataset for KPIs
    DATA_PATH = "Data/processed/clustered_data.csv"
    
    with st.spinner("Loading data for KPI calculations..."):
        df = load_data(DATA_PATH)

    if df is not None and not df.empty:
        # Calculate Basic KPIs
        total_customers = len(df)
        
        # If 'Monetary' or 'TotalSpend' column exists, calculate total revenue
        monetary_col = 'Monetary' if 'Monetary' in df.columns else None
        if not monetary_col and 'Total_Spend' in df.columns:
            monetary_col = 'Total_Spend'
            
        total_revenue = df[monetary_col].sum() if monetary_col else 0
        total_segments = df['Cluster'].nunique() if 'Cluster' in df.columns else 3
        
        # Display KPI Cards
        st.subheader("Key Performance Indicators (KPIs)")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-title">Total Customers</div>
                    <div class="kpi-value">{total_customers:,}</div>
                </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-title">Total Revenue</div>
                    <div class="kpi-value">${total_revenue:,.2f}</div>
                </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-title">Customer Segments</div>
                    <div class="kpi-value">{total_segments}</div>
                </div>
            """, unsafe_allow_html=True)
            
        # Dataset Summary Expander
        with st.expander("Show Dataset Summary"):
            st.write("Preview of the underlying clustered dataset:")
            st.dataframe(df.head(10), use_container_width=True)
            st.write(f"**Shape:** {df.shape[0]} rows, {df.shape[1]} columns")
    else:
        st.warning("Empty dataset or file not found. KPI Cards could not be rendered.")

    # ==========================================
    # FOOTER
    # ==========================================
    st.markdown(
        """
        <div class="footer">
        AI Customer Segmentation v1.0
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
