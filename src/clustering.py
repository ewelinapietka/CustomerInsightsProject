from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd

def scale_rfm(rfm: pd.DataFrame) -> pd.DataFrame:
    """
    Scale the RFM features using StandardScaler.
    
    Args:
        rfm (pd.DataFrame): Input DataFrame containing RFM features.
        
    Returns:
        pd.DataFrame: Scaled RFM features.
    """
    scaler = StandardScaler()
    scaled_rfm = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])
    return scaled_rfm

def run_kmeans(data, n_clusters=4, random_state=42):
    """
    Run KMeans clustering on the scaled data.
    
    Args:
        data (pd.DataFrame): Input DataFrame containing scaled RFM features.
        n_clusters (int): Number of clusters for KMeans.
        random_state (int): Random state for reproducibility.
        
    Returns:
        pd.DataFrame: DataFrame with cluster labels.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    labels = kmeans.fit_predict(data)
    return labels, kmeans.inertia_

def get_elbow_sse(data, max_k=10):
    """
    Get the inertia values for different numbers of clusters to find the elbow point.
    
    Args:
        data (pd.DataFrame): Input DataFrame containing scaled RFM features.
        max_clusters (int): Maximum number of clusters to test.
        
    Returns:
        list: List of inertia values for each number of clusters.
    """
    sse = []
    for k in range(1, max_k):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)
    return sse