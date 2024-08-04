from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key='')

# # Upload the training file
# response = client.files.create(
#     file=open("./data/instructions_training_data_set.jsonl", "rb"),
#     purpose="fine-tune"
# )

# # Access the file ID from the response
# training_file_id = response.id
# print(f"Training file uploaded with ID: {training_file_id}")

# # Create a fine-tuning job
# response = client.fine_tuning.jobs.create(
#     training_file=training_file_id,
#     model="gpt-4o-mini-2024-07-18"
# )

# # Access the fine-tuning job ID from the response
# fine_tuning_job_id = "ftjob-Zm71MeIbmqPpF4bToEYnHKyb"  # response.id
# print(f"Fine-tuning job created with ID: {fine_tuning_job_id}")

# # List 10 fine-tuning jobs
# response = client.fine_tuning.jobs.list(limit=10)
# print("List of fine-tuning jobs:")
# for job in response.data:
#     print(job)

# # Retrieve the state of a specific fine-tuning job
# job_id = fine_tuning_job_id  # Replace with your fine-tuning job ID
# response = client.fine_tuning.jobs.retrieve(job_id)
# print(f"Status of job {job_id}: {response.status}")

# # Retrieve fine-tuned model name
# fine_tuned_model_name = response.fine_tuned_model
# print(f'The fine-tuned model name is: {fine_tuned_model_name}')

# # Cancel a fine-tuning job
# response = client.fine_tuning.jobs.cancel(job_id)
# print(f"Cancelled job {job_id}")

# # List up to 10 events from a fine-tuning job
# response = client.fine_tuning.jobs.list_events(
#     fine_tuning_job_id=job_id, limit=10)
# print(f"Events for job {job_id}:")
# for event in response.data:
#     print(event)

# # Delete a fine-tuned model (must be an owner of the org the model was created in)
# model_id = "ft:gpt-3.5-turbo:acemeco:suffix:abc123"  # Replace with your model ID
# response = client.models.delete(model_id)
# print(f"Deleted model {model_id}")

# Use the fine-tuned model
# Replace with your fine-tuned model name
fine_tuned_model_name = "ft:gpt-4o-mini-2024-07-18:prosp::9sbFtT1B"
response = client.chat.completions.create(
    model=fine_tuned_model_name,
    messages=[
        {
            "role": "system",
            "content": """You are an AI research paper assistant that writes full sections of research papers based on a single prompt. Your responses must sound human to bypass AI detectors. If the user provides specific data, use that in your response to enhance credibility and depth.
                    
            Ensure your writing includes natural language patterns, varied sentence structures, and a coherent flow. Use idiomatic expressions, appropriate tone, and contextually relevant vocabulary. Integrate transitions between paragraphs and ideas smoothly. Pay attention to grammar, punctuation, and spelling. Incorporate critical thinking and logical reasoning to support arguments."""
        },
        {
            "role": "user",
            "content": """Generate content for the "Discussion" section of a research paper titled "The Impact and Future of Cryptocurrency." The content should be divided into three subsections: Economic Implications, Future Prospects, and Challenges. Each subsection should be well-detailed and cover the following points:

1. Economic Implications:
   - Discuss the potential of cryptocurrencies to disrupt traditional banking and finance sectors.
   - Examine the impact of cryptocurrencies on global economic stability and the regulatory challenges associated with their adoption.

2. Future Prospects:
   - Provide predictions for the growth and evolution of cryptocurrency, including trends in adoption and technological advancements.
   - Explore potential new applications for blockchain technology in various industries, such as supply chain management, healthcare, and real estate.

3. Challenges:
   - Identify security risks, including hacking, fraud, and the protection of digital assets.
   - Discuss regulatory hurdles and the need for global cooperation to establish standardized legal frameworks for cryptocurrency.
   - Analyze market volatility and investor risk due to fluctuating cryptocurrency prices and the speculative nature of the market.

Do not include an introduction, table of contents, or conclusion. Focus solely on the Discussion section as outlined above.

Data: No data provided by this user
"""
        }
    ]
)
print("Response from the fine-tuned model:")
print(response.choices[0].message.content.strip())
