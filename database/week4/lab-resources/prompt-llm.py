from openai import OpenAI
import sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-prompt", "--promptfile", help = "Enter prompt file path")
parser.add_argument("-key", "--keyfile", help = "Enter OpenAI key file path")

args = parser.parse_args()

apiKey = ""
prompt = ""
prompt_file = args.promptfile  #read from the command line
api_file = args.keyfile

#Read OpenAI key
with open(api_file) as f:
    apiKey = f.read()

#Read the promt
with open(prompt_file) as p_file:
    prompt = p_file.readline()

#define OpenAI client
client = OpenAI(api_key=apiKey)
model_name = "gpt-4" #Assign value "gpt-5" to query GPT-5 model

def prompt_GPT(user_input):
    new_elem = {}
    input_text = prompt + "\n"+ user_input
    message = []
    message.append({"role": "user", "content": input_text})
    print("PROMPT:\n"+input_text+"\n")
    answer = None
    while True:
        error = False
        try:
	
            answer = client.chat.completions.create(
                                model=model_name,
                                messages=message,
                                temperature=0)
            #print("Prompted!")
        except Exception as e:
            error = True
            print("An exception occurred:", e)
        
        if not error:
            break

    extr = True
    
    try:
        response = answer.choices[0].message.content         
    except Exception as e:
        print("An exception occurred:", e)
        extr = False
    if extr:
        return response
    
if __name__=="__main__":

    # Set the input query here
    query = "Write a SQL query to get the list of people who contributed at least 50 to every gift."

    if len(query) == 0:
        raise Exception("Your prompt is incomplete! Assign non-empty value to variable query ")

    response = prompt_GPT(query)
    print("RESPONSE:")
    print(response)
