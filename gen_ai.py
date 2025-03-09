from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_path = "finetuned_model_backup"

# Move the model to the appropriate device (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# Set the model to evaluation mode
label_dict = {
    "bank_service": 0,
    "credit_card": 1,
    "credit_reporting": 2,
    "debt_collection": 3,
    "loan": 4,
    "money_transfers": 5,
    "mortgage": 6
}



class traditional_model:
    def __init__(self, query):
        self.model =  AutoModelForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

    def predict(self):
        self.model.to(device)
        self.model.eval()  
        inputs = self.tokenizer(self.query, return_tensors="pt", truncation=True, padding=True).to(device)  # Move input to device
        with torch.no_grad():
            outputs = self.model(**inputs)
        predicted_class = torch.argmax(outputs.logits, dim=1).item()
        prediction = list(label_dict.keys())[predicted_class]
        return prediction
class ResultB:
    def __init__(self, query):
        self.response = f"Result from Function B for query: {query}"

class ResultC:
    def __init__(self, query):
        self.response = f"Result from Function C for query: {query}"
