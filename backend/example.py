my_key = "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"

import openai
from location import *
from openai import OpenAI

openai.api_key = my_key

def prepare_user_data(ip_address):
    
    location_data = get_user_location(ip_address)
    
    user_preferences = {
        "categories": ["museum", "park", "zoo", "swimming_pool"]
    }

    data = {
        "location": location_data,
        "preferences": user_preferences
    }
    
    return data

def format_prompt(data):
    location = data['location']
    categories = data['preferences']['categories']
    
    prompt = (
        f"Recommend the top 1-2 most popular places for each of the following categories "
        f"for a new visitor to {location['city']}, {location['country']} "
        f"({location['latitude']}, {location['longitude']}).\n"
        f"Categories: {', '.join(categories)}.\n"
        f"Provide the response in JSON format with the following structure:\n"
        "{\n"
        "  \"recommendations\": [\n"
        "    {\n"
        "      \"category\": \"Category Name\",\n"
        "      \"places\": [\n"
        "        {\n"
        "          \"name\": \"Place Name\",\n"
        "          \"description\": \"Short description of the place.\",\n"
        "          \"link\": \"Google Maps link to the place.\"\n"
        "        }\n"
        "      ]\n"
        "    }\n"
        "  ]\n"
        "}\n"
        "Make sure the response is formatted as valid JSON, with appropriate fields for each recommendation."
    )

    
    return prompt


system_content = (
    "You are a recommendation assistant specialized in suggesting popular and interesting activities for visitors based on their location, preferences, and interests. "
    "Always provide a balanced selection of different types of activities, such as cultural places, natural parks, and entertainment options. "
    "For each recommendation, include a short description and a Google Maps link if possible. "
    "Assume the user is a new visitor and may not be familiar with the region."
)

def get_recommendations(prompt):
    client = OpenAI()
    client.api_key = my_key
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_content
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion


def convert_into_readable_format(response):
    for category_info in recommendations:
        category = category_info.get("category")
        places = category_info.get("places", [])
        
        print(f"Category: {category}")
        for place in places:
            print(f"  Name: {place.get('name')}")
            print(f"  Description: {place.get('description')}")
            print(f"  Link: {place.get('link')}\n")

ip_add = "104.223.103.78" 


def get_content(ip_add):
    
    user_data = prepare_user_data(ip_add)
    
    formatted_prompt = format_prompt(user_data)
    
    recommendations = get_recommendations(formatted_prompt)
    
    contents = recommendations.choices[0].message.content

    return contents

if __name__ == "__main__":
    print(get_content(ip_add))