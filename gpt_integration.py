# https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/
#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
import openai 

openai.api_key = "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"
messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
one = 1
while one == 1: 
	message = input("User : ") 
	if message: 
		messages.append( {"role": "user", "content": message},) 
		chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages ) 
	
	reply = chat.choices[0].message.content 
	print(f"ChatGPT: {reply}") 
	messages.append({"role": "assistant", "content": reply})