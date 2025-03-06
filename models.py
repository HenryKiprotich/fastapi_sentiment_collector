from pydantic import BaseModel

class SentimentData(BaseModel):
    username: str  # Changed from user_name
    text: str  # Changed from comment
    sentiment: str  # "Positive" or "Negative"
    purchase_intent: str  # "Yes" or "No"
 
