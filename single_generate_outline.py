import logging
from openai import OpenAI

# Set up your OpenAI API client
client = OpenAI(
    api_key='')

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def openai_function(prompt):
    # Log the beginning of the prompt
    logging.info(f"Sending prompt to OpenAI: {prompt[:50]}...")
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                "role": "system",
                "content": "You are a highly intelligent research assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return_text = response.choices[0].message.content.strip()
    # Log the beginning of the response
    logging.info(f"Received response from OpenAI: {return_text[:50]}...")
    return return_text


def generate_detailed_outline(topic, context):
    prompt = f"""
    Generate a professional and detailed outline for a college-level research paper on the topic "{topic}". The paper should focus on new and advanced information, assuming the readers are already familiar with the basics of {topic}. The outline should include sections appropriate for a 5000-7000 word paper, with each section being a major part of the research paper and including appropriate subsections and details for a comprehensive and professional discussion. 

    CONTEXT: {context}

    The outline should be highly structured, with clear section titles and subsections similar to the following examples:
    
    Example 1:
    1. Introduction
    2. Related Work
        2.1 Foundation models, multimodality, and generalists
        2.2 Multimodal foundation models in biomedicine
        2.3 Multimodal medical AI benchmarks
    3. MultiMedBench: A Benchmark for Generalist Biomedical AI
    4. Med-PaLM M: A Proof of Concept for Generalist Biomedical AI
        4.1 Model preliminaries
        4.2 Putting it all together: Med-PaLM M
    5. Evaluation
        5.1 Evaluation on MultiMedBench
        5.2 Evaluation of language enabled zero-shot generalization
        5.3 Clinician evaluation of radiology report generation
    6. Results
        6.1 Med-PaLM M performs near or exceeding SOTA on all MultiMedBench tasks
        6.2 Med-PaLM M demonstrates zero-shot generalization to novel medical tasks and concepts
            6.2.1 Evidence of generalization to novel medical concepts
            6.2.2 Evidence of emergent zero-shot multimodal medical reasoning
            6.2.3 Evidence of generalization to novel tasks
            6.2.4 Evidence of positive task transfer
        6.3 Med-PaLM M performs encouragingly on radiology report generation across model scales
            6.3.1 Side-by-side evaluation
            6.3.2 Independent evaluation
    7. Discussion
    8. Perspective on Generalist Biomedical AI

    Example 2:
    1. Introduction
    2. Structure and Property of Ferritin
        2.1 General Aspects of Ferritin Structure
        2.2 Animal Ferritin
        2.3 Phytoferritin
        2.4 Bacterial Ferritin
        2.5 Non-Native Ferritin
    3. Preparation of Ferritin-Hybrid Nanoparticles
        3.1 Reversible Self-Assembly Property of Ferritin
        3.2 Self-Assembly of Ferritin Controlled by Different Chemicals
        3.3 Regulation of Ferritin Self-Assembly by Physical Methods
        3.4 Genetic Modification for Controlling Ferritin Self-Assembly
        3.5 Expansion of Ferritin Channels by Different Methods for Encapsulation
        3.6 Biomineralization for Preparing Ferritin-Hybrid Nanoparticles
    4. Applications of Ferritin-Directed Nanoparticles
        4.1 Applications in Food Science and Nutrition
        4.2 Applications in Medicine and Diagnostics
    5. Challenges of Ferritin as a Nanocarrier
    6. Conclusions and Perspectives
    """
    detailed_outline = openai_function(prompt)
    return detailed_outline