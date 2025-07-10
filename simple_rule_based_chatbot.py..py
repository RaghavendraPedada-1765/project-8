import re

# Optional: Basic text preprocessing using NLTK
# Uncomment below to use NLTK (requires pip install nltk)
# import nltk
# from nltk.tokenize import word_tokenize
# nltk.download('punkt')

# Rule-based patterns and responses
patterns = {
    r"\b(hi|hello|hey)\b": "Hello! How can I help you today?",
    r"\bhow (are|r) (you|u)\b": "I'm just a bot, but I'm doing great! How can I assist you?",
    r"\b(course|courses)\b": "Tamizhan Skills offers a variety of courses in programming, AI, and more. What course are you interested in?",
    r"\bpython\b": "We have Python courses for beginners and advanced learners! Would you like information on course duration, fees, or syllabus?",
    r"\b(ai|artificial intelligence)\b": "Our AI courses cover basics to advanced topics. Would you like to know about prerequisites or course structure?",
    r"\b(fees|price|cost)\b": "Course fees vary. Please specify the course you're interested in.",
    r"\b(duration|length|time)\b": "Courses typically last from 4 to 12 weeks, depending on the topic.",
    r"\b(syllabus|content)\b": "You can find detailed syllabuses for each course on our website or by specifying the course name.",
    r"\b(contact|support)\b": "You can contact Tamizhan Skills support at support@tamizhanskills.com.",
    r"\b(thank|thanks)\b": "You're welcome! Let me know if you have more questions.",
    r"\bbye\b": "Goodbye! Have a great day and happy learning!",
}

def preprocess(text):
    # Optional NLTK preprocessing
    # tokens = word_tokenize(text.lower())
    # return ' '.join(tokens)
    return text.lower()

def chatbot_response(msg):
    user_msg = preprocess(msg)
    for pattern, response in patterns.items():
        if re.search(pattern, user_msg):
            return response
    return "Sorry, I don't understand. Can you please rephrase your question or ask about Tamizhan Skills courses?"

def run_chatbot():
    print("Tamizhan Skills Chatbot (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if re.search(r"\bbye\b", user_input.lower()):
            break

if __name__ == "__main__":
    run_chatbot()
