from flask import Flask, render_template, request, jsonify
import pandas as pd
import difflib
import os
import random
app = Flask(__name__)
# Simple responses for when no FAQ match is found
fallback_responses = [
    "I'm sorry, I don't have specific information about that. Please contact the college office for assistance.",
    "That's a great question! I don't have that information in my database. Please visit the college office for help.",
    "I'm not sure about that. Could you please contact the relevant department for more details?",
    "I don't have information on that topic. Please reach out to the college administration for assistance.",
    "That's outside my current knowledge base. Please contact the college office for accurate information."
]
def get_simple_response(user_input):
    """Generate a simple contextual response"""
    user_lower = user_input.lower()
    # Simple keyword-based responses
    if any(word in user_lower for word in ['thank', 'thanks']):
        return "You're welcome! Is there anything else I can help you with?"
    elif any(word in user_lower for word in ['bye', 'goodbye', 'see you']):
        return "Goodbye! Have a great day!"
    elif any(word in user_lower for word in ['hello', 'hi', 'hey']):
        return "Hello! I'm here to help with college-related questions."
    elif any(word in user_lower for word in ['help', 'assistance']):
        return "I can help you with information about admissions, courses, facilities, and general college queries."
    else:
        return random.choice(fallback_responses)
# Load college data
def load_data():
    """Load the CSV data with questions and answers"""
    try:
        data_path = "data/chat_inputs.csv"
        if os.path.exists(data_path):
            return pd.read_csv(data_path)
        else:
            print(f"Warning: {data_path} not found. Creating sample data.")
            return pd.DataFrame({
                'question': ['Hello', 'Hi'],
                'answer': ['Hi there! How can I help you?', 'Hello! What would you like to know?']
            })
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame({
            'question': ['Hello', 'Hi'],
            'answer': ['Hi there! How can I help you?', 'Hello! What would you like to know?']
        })
# Load data
data = load_data()
@app.route("/")
def index():
    return render_template("chat.html")
@app.route("/get", methods=["POST"])
def get_response():
    try:
        user_input = request.form.get("msg", "").strip()
        if not user_input:
            return "Please enter a message."
        # First, try to find a matching question in the dataset
        best_score = 0
        best_answer = None
        for idx, row in data.iterrows():
            similarity = difflib.SequenceMatcher(None, user_input.lower(), row["question"].lower()).ratio()
            score = similarity * 100  # Convert to percentage 
            if score > best_score:
                best_score = score
                best_answer = row["answer"]
        # If we found a good match (threshold: 60%), return it
        if best_score > 60:
            return best_answer
        # If no good match found, use simple contextual response
        else:
            return get_simple_response(user_input)
    except Exception as e:
        print(f"Error in get_response: {e}")
        return "Sorry, there was an error processing your request. Please try again."
if __name__ == "__main__":
    print("Starting College Assistant Chatbot...")
    print("Using FAQ matching with intelligent fallback responses...")
    print("Starting Flask application...")
    app.run(debug=True, host='0.0.0.0', port=5000)
