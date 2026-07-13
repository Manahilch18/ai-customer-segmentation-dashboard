import streamlit as st
import os

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

def load_css(css_file):
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("assets/style.css")

# ==========================================
# MAIN PAGE CONTENT
# ==========================================
def main():
    st.title("💡 Business Insights & Recommendations")
    st.markdown("Actionable marketing strategies based on the identified customer segments.")
    st.markdown("---")

    # Executive Summary
    st.header("Executive Summary")
    st.write("""
    Based on the RFM (Recency, Frequency, Monetary) analysis and K-Means clustering, 
    we have identified three distinct customer segments. By tailoring our marketing 
    strategies to these specific groups, we can optimize resource allocation, 
    increase customer retention, and maximize revenue.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Segment 1: VIP Customers
    st.subheader("🌟 VIP Customers (Cluster 2)")
    with st.expander("View Details & Strategies for VIPs", expanded=True):
        st.write("""
        **Profile:** High frequency, high monetary value, and recent purchases. These are your most loyal and profitable customers.
        
        **Business Recommendations:**
        * **Exclusive Rewards:** Offer them premium loyalty programs or early access to new products.
        * **Personalized Outreach:** Assign dedicated account managers or send highly personalized thank-you notes.
        * **Upselling/Cross-selling:** Recommend high-margin, premium items as they are less price-sensitive.
        * **Feedback Loop:** Engage them for feedback on new features; they are highly invested in your brand.
        """)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # Segment 2: Regular Customers
    st.subheader("🤝 Regular Customers (Cluster 0)")
    with st.expander("View Details & Strategies for Regular Customers", expanded=True):
        st.write("""
        **Profile:** Average frequency and spend. They purchase somewhat regularly but aren't your top spenders.
        
        **Business Recommendations:**
        * **Incentivize Frequency:** Offer volume discounts or "buy one get one" (BOGO) deals to increase order size.
        * **Engagement Campaigns:** Send targeted newsletters featuring popular products.
        * **Loyalty Points:** Create a point-based system to encourage them to reach the "VIP" tier.
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    # Segment 3: At-Risk Customers
    st.subheader("⚠️ At-Risk Customers (Cluster 1)")
    with st.expander("View Details & Strategies for At-Risk Customers", expanded=True):
        st.write("""
        **Profile:** High recency (haven't bought in a long time), low frequency, and low spend. They are close to churning or have already churned.
        
        **Business Recommendations:**
        * **Re-engagement Campaigns:** Send "We Miss You" emails with aggressive discount codes (e.g., 20-30% off).
        * **Survey:** Send a brief survey to understand why they stopped purchasing and address any pain points.
        * **Retargeting Ads:** Use social media retargeting to remind them of items they previously viewed.
        * **Low Investment:** Limit high-cost marketing efforts; focus on automated email pipelines instead.
        """)

    st.markdown("---")
    st.info("💡 **Note:** These recommendations should be tested using A/B testing frameworks to validate their effectiveness before full-scale deployment.")

if __name__ == "__main__":
    main()
