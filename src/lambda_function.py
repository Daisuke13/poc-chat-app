import openai
import os
# import json
from logger import init_logger

openai.api_key = os.environ['OPENAI_SECRET_KEY']

def lambda_hundler(event, context):
    logger = init_logger(__name__)
    logger.info('Event: %s, Context: %s' ,event, context)
    answer = ask(event['question'])
    logger.info('Answer: %s', answer)
    return answer

def ask(question):
    prompt = f"{question}"
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