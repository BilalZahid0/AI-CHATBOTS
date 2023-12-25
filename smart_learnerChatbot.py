import json
from difflib import get_close_matches

# Function to load the definition of words from json file
def load_smartLearning_bot(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
        return data
    
# Function to save the definition of words back in json file  
def save_smartLearning_bot(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Function to find the best match of word from the dictionary
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)   
    # n means the number of matches to be returned, cutoff means the minimum accuracy in matching the words.
    return matches[0] if matches else None
    
# Function to get the answer to each question
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

# Function for the main chatbot 
def chatbot():
    knowledge_base: dict = load_smartLearning_bot('smart_learnerChatbot.json') 

    user_input: str = input('Type your question: ')
    best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

    if best_match:
        response: str | None = get_answer_for_question(best_match, knowledge_base)
        print(f'bot: {response}')
    else:
        new_answer: str = input('I don\'t know the answer. Type the answer or "skip" to skip: ')
                                        
        if new_answer.lower() != 'skip':
            knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
            save_smartLearning_bot('smart_learnerChatbot.json', knowledge_base)
            print('bot: Thank You, I learned a new response.')

if __name__ == '__main__':
    chatbot()
