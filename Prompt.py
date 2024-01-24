#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import openai

# Function to read the text file
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to interact with ChatGPT and ask questions
def ask_question(prompt):
    response = openai.ChatCompletion.create(
        model = 'gpt-4',  # Use the appropriate GPT-4 model
        messages = [{'role': 'user', 'content': prompt}],
        temperature=0.5,
        top_p=1
    )
    response_text = response['choices'][0]['message']['content']
    return response_text

def process_sets():
    for set_num in range(1, 6):
        prompt_file_path = f'/Users/adrita/Downloads/Personality_tests/PROMPTS/ASI_PROMPT.txt' #put your own file path
        response_file_path = f'/Users/adrita/Downloads/Personality_tests/RESPONSES/ASI_0.5/response_ASI_0.5_{set_num}.txt' #put your own file path

        # Read the contents of the prompt
        text = read_text_file(prompt_file_path)

        # Construct the prompt question
        prompt = text

        # Ask the question to the ChatGPT model
        answer = ask_question(prompt)

        # Store the response in a separate file
        with open(response_file_path, 'w') as response_file:
            response_file.write(answer)

        print(f"Response for Set{set_num} saved to {response_file_path}")

# Call the function to process all sets
process_sets()

