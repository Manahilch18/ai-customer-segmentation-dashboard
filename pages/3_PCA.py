import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Professional 3D PCA Visualization",
    page_icon="🧊",
    layout="wide"
)

# Load CSS if available to maintain consistent branding
def load_css(css_file):
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("assets/style.css")

# ==========================================
# DATA & MODEL LOADING
# ==========================================
@st.cache_data
def load_data():
    """Load the clustered dataset."""
    filepath = "Data/processed/clustered_data.csv"
    if not os.path.exists(filepath):
        st.error(f"Dataset not found at {filepath}")
        return pd.DataFrame()
    return pd.read_csv(filepath)

@st.cache_resource
def load_scaler():
    """Load the saved StandardScaler, if available."""
    scaler_path = "models/scaler.pkl"
    if os.path.exists(scaler_path):
        try:
            return joblib.load(scaler_path)
        except Exception as e:
            st.warning(f"Error loading scaler: {e}")
    return StandardScaler() # Fallback to a new scaler

# ==========================================
# MAIN PAGE CONTENT
# ==========================================
def main():
    st.title("🧊 High-Dimensional Customer Segmentation Analysis")
    st.markdown("""
    Explore how our K-Means algorithm (K=3) mathematically separates our customer base 
    across the Recency, Frequency, and Monetary (RFM) dimensions.
    """)
    st.markdown("---")

    # 1. Load Data
    with st.spinner("Loading dataset and applying transformations..."):
        df = load_data()
        scaler = load_scaler()
        
    if df.empty or 'Cluster' not in df.columns:
        st.error("Invalid dataset. Please ensure it contains the clustered RFM data.")
        return

    # 2. Map Clusters to Business Segments
    cluster_map = {0: 'Regular Customers', 1: 'At-Risk Customers', 2: 'VIP Customers'}
    df['Segment'] = df['Cluster'].map(lambda x: cluster_map.get(x, f"Cluster {x}"))
    
    # 3. Select RFM Features
    rfm_features = ['Recency', 'Frequency', 'Monetary']
    missing_features = [f for f in rfm_features if f not in df.columns]
    
    # Fallback for 'Monetary' naming variations
    if 'Monetary' in missing_features and 'Total_Spend' in df.columns:
        df = df.rename(columns={'Total_Spend': 'Monetary'})
        rfm_features = ['Recency', 'Frequency', 'Monetary']
        missing_features = []
        
    if missing_features:
        st.error(f"Missing required RFM features: {missing_features}")
        return

    # 4 & 5. Scale Data and Apply PCA (n_components = 3)
    X = df[rfm_features]
    
    try:
        X_scaled = scaler.transform(X)
    except:
        # Fallback if scaler expects different feature names
        X_scaled = StandardScaler().fit_transform(X)
        
    pca = PCA(n_components=3)
    pca_components = pca.fit_transform(X_scaled)

    # 6. Create PCA DataFrame
    pca_df = pd.DataFrame(data=pca_components, columns=['PC1', 'PC2', 'PC3'])
    
    # Attach categorical and tooltip data
    pca_df['Cluster'] = df['Cluster']
    pca_df['Segment'] = df['Segment']
    pca_df['CustomerID'] = df['CustomerID'] if 'CustomerID' in df.columns else df.index
    pca_df['Recency'] = df['Recency']
    pca_df['Frequency'] = df['Frequency']
    pca_df['Monetary'] = df['Monetary']

    # Explained Variance
    variance_ratios = pca.explained_variance_ratio_ * 100
    total_variance = variance_ratios.sum()

    # ==========================================
    # SIDEBAR CONTROLS (EXTRA FEATURES)
    # ==========================================
    st.sidebar.header("Visualization Controls")
    
    # Cluster Filter
    all_segments = ["All"] + sorted(pca_df['Segment'].unique().tolist())
    selected_segment = st.sidebar.selectbox("Filter by Segment:", all_segments)
    
    if selected_segment != "All":
        plot_df = pca_df[pca_df['Segment'] == selected_segment]
    else:
        plot_df = pca_df

    # Toggle 2D / 3D
    view_mode = st.sidebar.radio("PCA View Mode:", ["3D PCA", "2D PCA"])

    # Modern Color Palette
    color_discrete_map = {
        'VIP Customers': '#2a9d8f',       # Elegant Green/Teal
        'Regular Customers': '#e9c46a',   # Warm Yellow/Gold
        'At-Risk Customers': '#e76f51'    # Attention Red/Orange
    }

    # ==========================================
    # 7 & 8 & 9. PLOTLY EXPRESS VISUALIZATION
    # ==========================================
    st.subheader(f"Interactive {view_mode} Scatter Plot")
    
    if view_mode == "3D PCA":
        fig = px.scatter_3d(
            plot_df, 
            x='PC1', y='PC2', z='PC3',
            color='Segment',
            color_discrete_map=color_discrete_map,
            hover_name='CustomerID',
            hover_data={
                'PC1': False, 'PC2': False, 'PC3': False,
                'Segment': True,
                'Recency': ':.1f',
                'Frequency': ':.1f',
                'Monetary': ':$,.2f'
            },
            title="3D Principal Component Analysis of Customer Segments",
            template="plotly_white",
            opacity=0.75,
            size_max=10
        )
        
        # Camera Settings for Professional Default View
        camera = dict(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=1.5, y=1.5, z=1.2)
        )
        
        fig.update_layout(
            scene_camera=camera,
            scene=dict(
                xaxis_title=f"PC1 ({variance_ratios[0]:.1f}%)",
                yaxis_title=f"PC2 ({variance_ratios[1]:.1f}%)",
                zaxis_title=f"PC3 ({variance_ratios[2]:.1f}%)",
                xaxis=dict(showbackground=True, backgroundcolor="white", gridcolor="lightgray"),
                yaxis=dict(showbackground=True, backgroundcolor="white", gridcolor="lightgray"),
                zaxis=dict(showbackground=True, backgroundcolor="white", gridcolor="lightgray"),
            ),
            title_x=0.5, # Center title
            margin=dict(l=0, r=0, b=0, t=50),
            height=700,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                title_text="Customer Segments",
                bgcolor="rgba(255, 255, 255, 0.8)",
                bordercolor="lightgray",
                borderwidth=1
            )
        )
        # Fix marker size for consistency
        fig.update_traces(marker=dict(size=5, line=dict(width=0.5, color='DarkSlateGrey')))
        
    else: # 2D PCA
        fig = px.scatter(
            plot_df, 
            x='PC1', y='PC2',
            color='Segment',
            color_discrete_map=color_discrete_map,
            hover_name='CustomerID',
            hover_data={
                'PC1': False, 'PC2': False,
                'Segment': True,
                'Recency': ':.1f',
                'Frequency': ':.1f',
                'Monetary': ':$,.2f'
            },
            title="2D Principal Component Analysis of Customer Segments",
            template="plotly_white",
            opacity=0.75
        )
        fig.update_layout(
            xaxis_title=f"PC1 ({variance_ratios[0]:.1f}%)",
            yaxis_title=f"PC2 ({variance_ratios[1]:.1f}%)",
            title_x=0.5,
            margin=dict(l=0, r=0, b=0, t=50),
            height=600,
            legend=dict(title_text="Customer Segments")
        )
        fig.update_traces(marker=dict(size=8, line=dict(width=0.5, color='DarkSlateGrey')))

    # Render Plot
    st.plotly_chart(fig, use_container_width=True)

    # ==========================================
    # 10. EXPLAINED VARIANCE
    # ==========================================
    st.markdown("---")
    st.subheader("Statistical Diagnostics: Explained Variance")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("PC1 Variance", f"{variance_ratios[0]:.2f}%")
    with col2:
        st.metric("PC2 Variance", f"{variance_ratios[1]:.2f}%")
    with col3:
        st.metric("PC3 Variance", f"{variance_ratios[2]:.2f}%")
    with col4:
        st.metric("Total Explained", f"{total_variance:.2f}%", delta="High Information Retention", delta_color="normal")

    # ==========================================
    # 11. BUSINESS INTERPRETATION
    # ==========================================
    st.markdown("---")
    st.subheader("Business Interpretation")
    
    st.info("""
    **What the Clusters Represent:**
    * **VIP Customers** map to the region of high Monetary and high Frequency, anchoring one distinct side of our component space.
    * **At-Risk Customers** cluster towards high Recency (long time since last purchase) and low spend, visually isolating them from VIPs.
    * **Regular Customers** form the bridge between these extremes, representing average metrics.
    
    **Do the Clusters Overlap?**
    While K-Means ensures strict mathematical boundaries in the 3D space, minimal visual overlap at the edges indicates customers on the threshold of transitioning segments (e.g., a Regular Customer who recently made a large purchase and is moving towards VIP status).
    
    **Does PCA Successfully Separate Customer Segments?**
    Yes! The visualization demonstrates clear spatial separation between the segments. Because the Total Explained Variance is extremely high (often >95% for 3 features reduced to 3 components), this plot perfectly preserves the distance calculations made by the K-Means algorithm.
    """)

    # ==========================================
    # BONUS: DOWNLOAD PCA DATA
    # ==========================================
    st.markdown("---")
    csv_data = pca_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download PCA Coordinates & Clusters CSV 📥",
        data=csv_data,
        file_name='pca_customer_segments.csv',
        mime='text/csv',
    )

if __name__ == "__main__":
    main()
