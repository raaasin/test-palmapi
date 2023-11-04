from creds import palmpi
import google.generativeai as palm
palm.configure(api_key=palmpi)

model = 'models/text-bison-001'



prompt = """
You are a question answering bot that answers questions, first read the context that is written after this and then answer the question as if you are the person who wrote the context.
----------------------------------------------------------
"""
with open('context.txt', 'r') as file:
    context = file.read()

prompt += context
prompt += "-----------------------------------------------------------------------------------"
prompt = prompt + "question is:"


def task(message,prompt=prompt):
    prompt= prompt + message
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
    )   
    return completion.result  

print(task("explain why you'd be a good fit for the AI job?"))