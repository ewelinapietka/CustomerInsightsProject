import pandas as pd

def create_total_price(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column 'total_price' in the DataFrame by multiplying 'price' and 'quantity' columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame containing 'price' and 'quantity' columns.
        
    Returns:
        pd.DataFrame: DataFrame with the new 'total_price' column.
    """
    df['TotalPrice'] = df['UnitPrice'] * df['Quantity']
    return df

def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add time-related features to the DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame containing 'date' column.
        
    Returns:
        pd.DataFrame: DataFrame with additional time-related features.
    """
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['year'] = df['InvoiceDate'].dt.year
    df['month'] = df['InvoiceDate'].dt.month
    df['day'] = df['InvoiceDate'].dt.day
    df['day_of_week'] = df['InvoiceDate'].dt.dayofweek
    return df

def create_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create RFM (Recency, Frequency, Monetary) features from the DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame containing 'customer_id', 'date', and 'total_price' columns.
        
    Returns:
        pd.DataFrame: DataFrame with RFM features.
    """
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (df['InvoiceDate'].max() - x.max()).days,
        'CustomerID': 'count',
        'TotalPrice': 'sum'
    }).rename(columns={'InvoiceDate': 'Recency', 'CustomerID': 'Frequency', 'TotalPrice': 'Monetary'})
    
    return rfm.reset_index()