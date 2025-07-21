# 📊 Data Pipeline Development Project

This project focuses on building an automated data pipeline using Python, Pandas, and Scikit-Learn. The pipeline performs ETL (Extract, Transform, Load) operations on the Telco Customer Churn dataset to prepare it for machine learning or analytics tasks.

## 📁 Project Structure

data_pipeline_project/
│
├── data/ # Raw dataset
│ └── projectdata.csv
│
├── processed_data/ # Cleaned/Transformed dataset
│ └── processed_data.csv
│
├── notebooks/
│ └── data_pipeline_etl.ipynb
│
├── scripts/
│ └── etl_pipeline.py
│
├── README.md
└── .gitignore


---

###  **Dataset**
```md
## 🧾 Dataset

- **Name:** Telco Customer Churn dataset  
- **Location:** `data/projectdata.csv`  

## 🛠 Tools & Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook / VS Code

## ⚙️ ETL Pipeline Steps

1. **Extract:** Load CSV data using Pandas  
2. **Transform:** 
   - Handle missing values  
   - Encode categorical variables  
   - Normalize / scale numerical data  
3. **Load:** Save the processed data into `processed_data/processed_data.csv`

## 📈 Sample Visualizations

- Distribution of Churned vs Non-Churned customers  
- Correlation heatmap  
- Feature distributions  
- Countplots for categorical features  


## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/data-pipeline-project.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the script:
python scripts/etl_pipeline.py


---

###  **Author**
```md
## 👤 Author

- **Ankit Garg**  
- GitHub: [dvs-pixel](https://github.com/dvs-pixel)

