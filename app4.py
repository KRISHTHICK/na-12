import openai

def generate_caption(image_description):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Generate a catchy caption for: {image_description}"}
        ]
    )
    return response['choices'][0]['message']['content']
