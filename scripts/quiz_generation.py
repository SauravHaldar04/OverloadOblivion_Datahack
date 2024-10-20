# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain.schema.runnable import RunnablePassthrough

# # Set up Google API key (replace with your actual key)
# os.environ['GOOGLE_API_KEY'] = 'AIzaSyDc1cp9pzO2OcwYTj2Y5XHpO0lVx-7oQow'

# # Initialize Gemini model
# gemini = ChatGoogleGenerativeAI(model="gemini-pro")

# def generate_question(grade, subject, topic, difficulty):
#     prompt_template = f"""Generate a multiple-choice question for a student in grade {grade} about {subject} and {topic}. 
#     The difficulty level of the question should be {difficulty}.
#     Provide the question, four answer options (A, B, C, D), and indicate the correct answer.
#     Format:
#     Question: [Question text]
#     A. [Option A]
#     B. [Option B]
#     C. [Option C]
#     D. [Option D]
#     Correct Answer: [A, B, C, or D]
#     """
#     prompt = PromptTemplate(template=prompt_template, input_variables=["grade", "subject", "topic", "difficulty"])
#     chain = prompt | gemini
    
#     result = chain.invoke({"grade": grade, "subject": subject, "topic": topic, "difficulty": difficulty}).content.strip()
    
#     return result

# def generate_multiple_questions(grade, subject, topic, difficulty, count):
#     questions = []
#     for _ in range(count):
#         question = generate_question(grade, subject, topic, difficulty)
#         questions.append(question)
#     return questions

# def generate_question_dictionary(grade, subject, topic, counts):
#     question_dict = {}
    
#     for difficulty, count in counts.items():
#         questions = generate_multiple_questions(grade, subject, topic, difficulty, count)
#         question_dict[difficulty] = questions
    
#     return question_dict

# # Generate questions
# grade = 8
# subject = "Science"
# topic = "Solar System"
# counts = {
#     "easy": 10,
#     "medium": 10,
#     "hard": 10
# }

# question_dictionary = generate_question_dictionary(grade, subject, topic, counts)

# # Print the dictionary (for verification)
# for difficulty, questions in question_dictionary.items():
#     print(f"\n{difficulty.capitalize()} Questions:")
#     for i, q in enumerate(questions, 1):
#         print(f"{i}. {q}\n")

# # Return the dictionary
# print("\nReturning the question dictionary:")
# print(question_dictionary)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough

def initialize_gemini(api_key):
    return ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

def generate_question(gemini, grade, subject, topic, difficulty):
    prompt_template = f"""Generate a multiple-choice question for a student in grade {grade} about {subject} and {topic}. 
    The difficulty level of the question should be {difficulty}.
    Provide the question, four answer options (A, B, C, D), and indicate the correct answer.
    Format:
    Question: [Question text]
    A. [Option A]
    B. [Option B]
    C. [Option C]
    D. [Option D]
    Correct Answer: [A, B, C, or D]
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["grade", "subject", "topic", "difficulty"])
    chain = prompt | gemini
    
    result = chain.invoke({"grade": grade, "subject": subject, "topic": topic, "difficulty": difficulty}).content.strip()
    
    return result

def generate_multiple_questions(gemini, grade, subject, topic, difficulty, count):
    questions = []
    for _ in range(count):
        question = generate_question(gemini, grade, subject, topic, difficulty)
        questions.append(question)
    return questions

def generate_question_dictionary(grade, subject, topic, counts,api_key='AIzaSyDc1cp9pzO2OcwYTj2Y5XHpO0lVx-7oQow'):
    gemini = initialize_gemini(api_key)
    question_dict = {}
    
    for difficulty, count in counts.items():
        questions = generate_multiple_questions(gemini, grade, subject, topic, difficulty, count)
        question_dict[difficulty] = questions
    
    return question_dict

# Example usage:
# api_key = 'YOUR_API_KEY_HERE'
# result = generate_question_dictionary(api_key, grade=8, subject="Science", topic="Solar System", counts={"easy": 2, "medium": 2, "hard": 1})
# print(result)