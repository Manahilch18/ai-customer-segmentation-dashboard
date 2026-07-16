<h1 align="center">📊 AI-Powered Customer Segmentation Dashboard</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge"/>
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn Badge"/>
  <img src="https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="License Badge"/>
</p>

<p align="center">
  <strong>An end-to-end Data Science project applying Unsupervised Machine Learning and RFM Analysis to segment retail customers based on purchasing behavior.</strong>
</p>


## 📖 Project Overview

This project applies **Unsupervised Machine Learning** to segment retail customers based on their purchasing behavior using **RFM (Recency, Frequency, Monetary)** analysis and the **K-Means Clustering** algorithm. 

The project encompasses a complete data science workflow, starting from raw data preprocessing and exploratory data analysis (EDA), through to feature engineering, K-Means clustering, and culminates in a production-ready, interactive **Streamlit Dashboard** for business stakeholders.


## 💾 Dataset Information

The project utilizes the **Online Retail Dataset**, a transnational data set containing all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.

| Attribute | Details |
| :--- | :--- |
| **Dataset Name** | Online Retail Dataset |
| **Original Records** | 541,909 |
| **Features** | `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country` |


## 🛠️ Technologies Used

- **Programming:** Python
- **Data Manipulation:** Pandas, NumPy, OpenPyXL
- **Data Visualization:** Matplotlib, Seaborn, Plotly
- **Machine Learning:** Scikit-learn, Joblib
- **Web Application / UI:** Streamlit
- **Version Control:** Git, GitHub

## 🔄 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis (EDA)
     ↓
RFM Feature Engineering
     ↓
Feature Scaling
     ↓
K-Means Clustering
     ↓
Model Evaluation
     ↓
Customer Segmentation
     ↓
Interactive Dashboard
```


## 📂 Project Structure

```text
AI_Customer_Segmentation/
│
├── app.py                      # Main Streamlit application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── assets/                     
│   └── style.css               # Custom CSS for the Streamlit dashboard
│
├── Data/                       
│   ├── Raw/                    # Raw, unprocessed data files
│   └── processed/              # Cleaned, RFM, and clustered CSV datasets
│
├── models/                     
│   ├── kmeans.pkl              # Pickled K-Means model
│   ├── pca.pkl                 # Pickled PCA model
│   └── scaler.pkl              # Pickled StandardScaler model
│
├── notebooks/                  
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_EDA.ipynb
│   ├── 04_RFM_Feature_Engineering.ipynb
│   ├── 05_KMeans_Model.ipynb
│   └── 06_Model_Evaluation.ipynb
│
└── pages/                      # Streamlit multipage application files
    ├── 1_Dataset.py
    ├── 2_Segments.py
    ├── 3_PCA.py
    └── 4_Insights.py
```


## 📓 Notebooks

The data science lifecycle is broken down into structured Jupyter Notebooks:

1. **`01_Data_Understanding.ipynb`**: Initial inspection of the raw dataset, assessing feature distributions, and understanding the core attributes.
2. **`02_Data_Cleaning.ipynb`**: Handling missing values (e.g., missing CustomerIDs), removing duplicates, and filtering out negative quantities/prices.
3. **`03_EDA.ipynb`**: Deep dive into sales trends, top-selling products, and geographical distribution of orders.
4. **`04_RFM_Feature_Engineering.ipynb`**: Transforming transactional data into customer-level RFM metrics (Recency, Frequency, Monetary).
5. **`05_KMeans_Model.ipynb`**: Scaling the RFM features, finding the optimal number of clusters using the Elbow Method, and training the final K-Means model.
6. **`06_Model_Evaluation.ipynb`**: Evaluating cluster quality using Silhouette Scores and profiling the final customer segments.


## 🧠 Machine Learning Details

| Metric / Parameter | Value |
| :--- | :--- |
| **Algorithm** | K-Means Clustering |
| **Learning Type** | Unsupervised Learning |
| **Feature Engineering** | RFM (Recency, Frequency, Monetary) |
| **Evaluation Metrics** | Elbow Method, Silhouette Score |
| **Best K (Clusters)** | 3 |
| **Silhouette Score** | 0.5097 |


## 🎯 Customer Segments

The model successfully grouped the customer base into 3 distinct segments:

| Cluster | Segment Name | Business Meaning |
| :---: | :--- | :--- |
| **2** | 🌟 **VIP Customers** | High spend, frequent purchases, and recent activity. These are the most loyal and profitable customers. |
| **0** | 🤝 **Regular Customers** | Average spend and frequency. They purchase somewhat regularly but are not the top spenders. |
| **1** | ⚠️ **At-Risk Customers** | High recency (long time since last purchase), low frequency, and low spend. Likely to churn or have already churned. |



## 📈 Dashboard Features

The accompanying Streamlit dashboard transforms the machine learning outputs into a business intelligence tool:

- **Home Dashboard:** Welcome page summarizing the project with dynamic KPI Cards.
- **Dataset Explorer:** Search by CustomerID, filter by segment, view dataset statistics, and download custom CSVs.
- **Segment Analysis:** Interactive Plotly pie and bar charts detailing customer count, revenue distribution, and average RFM metrics by segment.
- **PCA Visualization:** Stunning 3D and 2D Principal Component Analysis (PCA) scatter plots to visualize the mathematical separation of the clusters.
- **Business Insights:** Actionable marketing and retention strategies tailored to VIP, Regular, and At-Risk customers.



## 🚀 Results

- ✅ **Successful Segmentation:** Effectively divided the customer base into 3 highly distinct, actionable clusters.
- ✅ **Customer-Level RFM Analysis:** Mapped complex transactional data into highly interpretable Recency, Frequency, and Monetary scores.
- ✅ **Interactive Dashboard:** Built a professional, ATS-friendly web application serving as a bridge between data science and business strategy.
- ✅ **Business Insights Generated:** Created concrete, data-backed marketing strategies to increase revenue and prevent customer churn.


## Key Learnings
✔ Learned the complete Unsupervised Learning workflow.
✔ Understood RFM Feature Engineering.
✔ Learned Feature Scaling before K-Means.
✔ Used the Elbow Method to determine the optimal number of clusters.
✔ Evaluated clusters using the Silhouette Score.
✔ Visualized clusters using PCA.
✔ Built an interactive Streamlit Dashboard.
✔ Connected machine learning outputs with real business decisions.

## ⚙️ Installation & Usage

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/Manahilch18/ai-customer-segmentation-dashboard.git>
   cd AI_Customer_Segmentation
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Dashboard:**
   ```bash
   streamlit run app.py
   ```


## 📸 Screenshots

- **Dashboard Home**  
 <img width="1914" height="953" alt="image" src="https://github.com/user-attachments/assets/e6a7d548-6420-4894-aa92-be57cbf84423" />

- **Dataset Explorer**  
   <img width="1907" height="936" alt="image" src="https://github.com/user-attachments/assets/87498c2c-feba-482e-ba4b-03e75302de68" />

- **Segment Analysis**  
  <img width="1807" height="939" alt="image" src="https://github.com/user-attachments/assets/af2bf8e0-3aca-4cc7-8dfd-30679467ecb9" />

- **3D PCA Visualization**  
   <img width="1900" height="960" alt="image" src="https://github.com/user-attachments/assets/da8377ba-ec6d-453d-bb1f-9ca16e95374f" />

- **Business Insights**  
  <img width="1898" height="941" alt="image" src="https://github.com/user-attachments/assets/e54c39a1-f11c-4728-91e9-890572fb223a" />



## 🔮 Future Improvements

- [ ] Deploy the application publicly on **Streamlit Community Cloud**.
- [ ] Implement **Real-time customer  Segmentation** by allowing users to input new RFM values to predict their cluster on the fly.
- [ ] Develop a **Customer Recommendation Engine** based on cluster purchase history.
- [ ] Add **Automated Reporting** features (e.g., exporting charts as PDF reports).
- [ ] Integrate a **Cloud Database** (e.g., AWS RDS, PostgreSQL) to replace static CSV files.
- [ ] Add **Authentication** for secure business access.


## 👨‍💻 Author

**Manahil**
- **GitHub:** https://github.com/Manahilch18
- **LinkedIn:** www.linkedin.com/in/manahil-ishfaq-673439322


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
