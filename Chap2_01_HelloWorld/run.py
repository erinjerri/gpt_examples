from dotenv import load_dotenv

load_dotenv()
import os
import openai

openai.api_key = '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'

# Call the openai ChatCompletion endpoint, with th ChatGPT model
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "user", 
       "content": "Hello World!"},
    ],
temperature=0.7,
max_tokens=3,
top_p=1,
frequency_penalty=0,
presence_penalty=0,  
)
# Extract the response
print(response['choices'][0]['message']['content'])
