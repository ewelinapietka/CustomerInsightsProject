from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

def train_model(X_train, y_train, model_type='logistic'):
    """
    Train a classification model on the training data.
    
    Args:
        X_train (pd.DataFrame): Features for training.
        y_train (pd.Series): Target variable for training.
        model_type (str): Type of model to train ('logistic' or 'random_forest').
        
    Returns:
        model: Trained model.
    """
    if model_type == 'logistic':
        model = LogisticRegression()
    elif model_type == 'random_forest':
        model = RandomForestClassifier()
    else:
        raise ValueError("Unsupported model type. Choose 'logistic' or 'random_forest'.")
    
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test, report_path=None):
    """
    Evaluate the trained model on the test data and print the classification report.
    
    Args:
        model: Trained model.
        X_test (pd.DataFrame): Features for testing.
        y_test (pd.Series): Target variable for testing.
        report_path (str): Path to save the classification report.
        
    Returns:
        None
    """
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)

    if report_path:
        with open(report_path, 'w') as f:
            f.write("Confusion Matrix:\n")
            f.write(str(cm) + "\n\n")
            f.write("Classification Report:\n")
            f.write(cr)

    return cm, cr