import openai
import os
import json

openai.api_key = os.environ['OPENAI_SECRET_KEY']

def lambda_hundler(event, context):
    answer = ask(event['question'])
    return answer

def ask(question):
    prompt = f"I am a large language model trained by OpenAI. Ask me anything!\nQ: {question}\nA:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer