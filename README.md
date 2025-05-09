# Customer Insights Project
📊 Customer Insights Project
Welcome to the Customer Insights Project!
This project analyzes customer purchase behavior, segments customers, and predicts future purchases using real-world transactional data.

📁 Project Structure
```plaintext
customer_insights_project/
├── setup_project.py
├── data/
│   ├── online_retail.xls         # Raw dataset
│   └── online_retail_cleaned.csv # Cleaned dataset
├── notebooks/
│   ├── 0_eda_online_retail.ipynb     # Exploratory Data Analysis (EDA)
│   ├── 1_data_cleaning.ipynb         # Data cleaning and preprocessing
│   ├── 2_customer_segmentation.ipynb # Customer segmentation (clustering)
│   └── 3_purchase_prediction.ipynb   # Purchase prediction (classification)
├── src/
│   ├── features.py    # Feature engineering functions
│   ├── clustering.py  # Clustering utilities
│   └── classifier.py  # Classification model utilities
├── visuals/
│   ├── total_price_distribution.png # Total price distribution plot
│   ├── daily_sales.png              # Daily sales over time plot
│   └── top_products.png             # Top 10 products purchased
├── results/
│   ├── customer_segments.csv # Clustered customer profiles
│   └── prediction_report.txt # Classifier performance report
├── full_setup_project.py
├── README.md
└── requirements.txt

🛠️ Project Setup
Option 1: Manual Setup
If you already have the folders and dataset ready, you can proceed directly to running the notebooks.

Option 2: Automatic Setup (Recommended)
You can automatically create the project structure and download the dataset by running:

python setup_project.py

Available options:

--force : Force re-download and overwrite the existing dataset.

Example usage:


python setup_project.py --force
This will:

Create the project directory structure

Download the Online Retail dataset

Extract and convert it if needed

Save the cleaned .csv file in the /data directory

📈 Project Workflow

Step	Description
EDA	Explore the dataset, visualize distributions, check missing values.
Data Cleaning	Remove cancellations, handle missing values, create new features.
Customer Segmentation	Create RFM features, apply KMeans clustering to group customers.
Purchase Prediction	Build a supervised machine learning model to predict future customer purchases.

📊 Key Techniques Used

Pandas for data manipulation

Matplotlib and Seaborn for visualization

KMeans Clustering for unsupervised learning

Random Forest Classifier for supervised learning

Scikit-learn for model building and evaluation


💻 How to Run the Project

Install required Python packages:

pip install -r requirements.txt

(Optional) Automatically set up the project structure:

python setup_project.py
Start exploring by running the notebooks in this order:

0_eda_online_retail.ipynb

1_data_cleaning.ipynb

2_customer_segmentation.ipynb

3_purchase_prediction.ipynb




📂 Outputs
Customer segments saved in results/customer_segments.csv

Model evaluation report saved in results/prediction_report.txt

Visualizations saved in visuals/ folder

⚡ Author
Built by Ewelina Pietka


