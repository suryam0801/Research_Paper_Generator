from openai import OpenAI
import json
import re

# Initialize the OpenAI client
client = OpenAI(
    api_key='')

model_name = "ft:gpt-4o-mini-2024-07-18:prosp::9sbFtT1B"


# Function to extract JSON data from the output string
def extract_json_from_output(output_string):
    # Use regex to find the JSON part of the string
    json_match = re.search(r'\[.*\]', output_string, re.DOTALL)

    if json_match:
        json_str = json_match.group(0)
        try:
            parsed_json = json.loads(json_str)
            return parsed_json
        except json.JSONDecodeError as e:
            print("Failed to parse JSON:", e)
            return None
    else:
        print("No JSON found in the output.")
        return None


# Function to generate text based on the input prompt
def generate_text(prompt):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": """You are an AI research paper assistant that writes full sections of research papers based on a single prompt. Your responses must sound human to bypass AI detectors. If the user provides specific data, use that in your response to enhance credibility and depth.
                    
            Ensure your writing includes natural language patterns, varied sentence structures, and a coherent flow. Use idiomatic expressions, appropriate tone, and contextually relevant vocabulary. Integrate transitions between paragraphs and ideas smoothly. Pay attention to grammar, punctuation, and spelling. Incorporate critical thinking and logical reasoning to support arguments."""
            },
            {
                "role": "user",
                "content": f"""{prompt} Data: No data provided by this user"""
            }
        ]
    )

    humanized_text = response.choices[0].message.content.strip()
    return humanized_text


# Sample Prompts:

# Generate content for the "Discussion" section of a research paper titled "The Impact and Future of Cryptocurrency." The content should be divided into three subsections: Economic Implications, Future Prospects, and Challenges. Each subsection should be well-detailed and cover the following points:

# 1. Economic Implications:
#    - Discuss the potential of cryptocurrencies to disrupt traditional banking and finance sectors.
#    - Examine the impact of cryptocurrencies on global economic stability and the regulatory challenges associated with their adoption.

# 2. Future Prospects:
#    - Provide predictions for the growth and evolution of cryptocurrency, including trends in adoption and technological advancements.
#    - Explore potential new applications for blockchain technology in various industries, such as supply chain management, healthcare, and real estate.

# 3. Challenges:
#    - Identify security risks, including hacking, fraud, and the protection of digital assets.
#    - Discuss regulatory hurdles and the need for global cooperation to establish standardized legal frameworks for cryptocurrency.
#    - Analyze market volatility and investor risk due to fluctuating cryptocurrency prices and the speculative nature of the market.

# Do not include an introduction, table of contents, or conclusion. Focus solely on the Discussion section as outlined above.


#------------------------------------------------------------

# Generate content for the "Discussion" section of a research paper. The content should cover Economic Implications, Future Prospects, and Challenges without including an introduction, table of contents, or conclusion.

# "The development of renewable energy technologies has drastically transformed the global energy landscape. Despite these advancements, numerous challenges related to the integration and efficiency of renewable energy sources remain. The development of renewable energy technologies has drastically transformed the global energy landscape. Despite these advancements, numerous challenges related to the integration and efficiency of renewable energy sources remain."

# Data: No data provided by this user