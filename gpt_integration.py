# https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/

import openai 

openai.api_key = "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"
messages = [ {"role": "system", "content": "You are a intelligent assistant who is care focused. Keep your responses under 1900 characters."} ]

def accost_gpt(message) -> str:
	if message: 
		messages.append( {"role": "user", "content": message},) 
		chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages ) 

	reply = chat.choices[0].message.content 
	print(f"ChatGPT: {reply}") 
	messages.append({"role": "assistant", "content": reply})
	return reply