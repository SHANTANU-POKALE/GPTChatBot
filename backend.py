import openai

class Chatbot:
    def __init__(self):
        openai.api_key = os.read("API_KEY")

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="gpt-4o-mini",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    text_1 = "Write a jock about cats."
    response = chatbot.get_response(text_1)
    print(response)
