from model_logic import train_occupancy_model, predict_busy_hours
from textblob import TextBlob # Ensure you run: pip install textblob

def analyze_campus_sentiment(feedback_text):
    """
    Uses Transfer Learning principles via TextBlob's pre-trained 
    NLP models to perform Sentiment Analysis (CO5).
    """
    blob = TextBlob(feedback_text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        return "Positive (Student Happy)"
    elif polarity < -0.1:
        return "Negative (Intervention Needed)"
    else:
        return "Neutral"

if __name__ == "__main__":
    # 1. Train the ML Model
    campus_model = train_occupancy_model()
    
    # 2. Test Prediction
    test_hour = 12
    exam_status = 0
    crowd = predict_busy_hours(campus_model, test_hour, exam_status)
    print(f"\nPrediction for {test_hour}:00: {crowd:.1f}% Occupancy")
    
    # 3. Test NLP Sentiment
    sample_review = "The library is way too hot and the Wi-Fi is failing."
    sentiment = analyze_campus_sentiment(sample_review)
    print(f"Feedback Analysis: {sentiment}")