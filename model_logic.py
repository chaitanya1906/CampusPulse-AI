import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_occupancy_model():
    # Load the data
    df = pd.read_csv('data.csv')
    
    # Feature Selection (CO4: Estimators and Hyper-parameters)
    X = df[['hour', 'is_exam_week']] 
    y = df['occupancy_percent']
    
    # Split into Training and Validation Sets (CO4)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Linear Regression Model (CO4)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Validation (CO4: Bias and Variance check)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    print(f"--- Model Trained ---")
    print(f"Validation Mean Squared Error: {mse:.2f}")
    return model

def predict_busy_hours(model, hour, is_exam):
    prediction = model.predict([[hour, is_exam]])
    return np.clip(prediction[0], 0, 100)