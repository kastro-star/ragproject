from openai import OpenAI

cli = OpenAI(
    base_url="enter your url",
    api_key="enter you api key",
)

def chat_completion(messages, model):
    response = cli.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a cooking expert. The user will provide the ingredients they have, and you will suggest a recipe using those ingredients."
            },
            {
                "role": "user",
                "content": messages  
            }
        ]
    )
    
   
    

    message_content = response.choices[0].message.content
    
    return message_content