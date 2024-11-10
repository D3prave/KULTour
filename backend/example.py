keyy = "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"


import openai
from openai.error import OpenAIError, RateLimitError

# Set the API key directly
openai.api_key = keyy

# Define a function to make a request to the API
def get_ai_recommendations(user_preferences):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Recommend activities based on the following preferences: {user_preferences}.",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except RateLimitError:
        print("Rate limit reached. Please wait before making more requests.")
    except OpenAIError as e:
        print(f"An OpenAIError occurred: {str(e)}")

user_preferences = "User likes history, nature, and relaxing experiences."
ai_recommendations = get_ai_recommendations(user_preferences)
if ai_recommendations:
    print(ai_recommendations)