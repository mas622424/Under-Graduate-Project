'''import transformers
from transformers import pipeline
import json

# Load the small language model (QA pipeline)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased")

# Load saree data
with open("sarees.json", "r") as f:
    saree_data = json.load(f)

def answer_query(question):
    # Identify which saree is mentioned in the question
    for saree, context in saree_data.items():
        if saree.lower() in question.lower():
            result = qa_pipeline(question=question, context=context)
            return result["answer"]
    
    return "I don't have information on that."

if __name__ == "__main__":
    print(answer_query("What is special about Banarasi sarees?"))i'''
    
    
import transformers
from transformers import pipeline
import json

# Load the small language model (QA pipeline)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased")

# Load saree data
with open("sarees.json", "r") as f:
    saree_data = json.load(f)

def answer_query(question):
    """
    Answers a query based on the saree data.
    :param question: The user's question as a string.
    :return: The answer as a string.
    """
    # Identify which saree is mentioned in the question
    for saree, context in saree_data.items():
        if saree.lower() in question.lower():
            result = qa_pipeline(question=question, context=context)
            return result["answer"]
    
    # If no relevant saree is found
    return "I'm sorry, I don't have information on that. Please try asking about another saree."

if __name__ == "__main__":
    # Example usage
    print(answer_query("What is special about Banarasi sarees?"))
