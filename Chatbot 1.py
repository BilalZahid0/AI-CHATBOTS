#chatbot
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download('stopwords')
#nltk.download('punkt')

stop_words = set(stopwords.words('english'))

response = {}

with open('Botscript.txt', 'r') as file:
    for line in file:
        question, answer = map(str.strip, line.split('~'))
        question_tokens = [word.lower() for word in word_tokenize(question) if word.isalnum() and word.lower() not in stop_words]
        response[tuple(question_tokens)] = answer

print("Ask a question or type 'exit' to leave.")

while True:
    input_text = input("User: ").lower()

    if input_text == 'exit':
        print("ChatBot: Goodbye!")
        break

    input_tokens = [word.lower() for word in word_tokenize(input_text) if word.isalnum() and word.lower() not in stop_words]
    matched_response = "I'm sorry, I don't understand that question."

    for question_tokens, answer in response.items():
        if set(input_tokens) == set(question_tokens):
            matched_response = answer
            break

    print("ChatBot:", matched_response)