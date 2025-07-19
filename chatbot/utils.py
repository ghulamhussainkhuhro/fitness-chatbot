# chatbot/utils.py

def is_safe_query(text):
    unsafe_keywords = [
        "supplement", "prescribe", "diagnose", "dosage", "dose",
        "treat", "medicine", "can I take", "should I take",
        "protein", "creatine", "vitamin"
    ]
    return not any(word in text.lower() for word in unsafe_keywords)
