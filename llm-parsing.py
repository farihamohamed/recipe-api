import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

def parse_transcript(transcript):
    print("Starting...")
    
    # Read file
    if transcript.endswith('.txt'):
        try:
            with open(f'transcripts/{transcript}', 'r', encoding='utf-8') as file:
                transcript_text = file.read()
            print(f"File read successfully. Length: {len(transcript_text)} characters")
        except FileNotFoundError:
            print(f"File {transcript} not found!")
            return
    else:
        transcript_text = transcript
    
    print("Creating pipeline...")
    try:
        client = pipeline('text2text-generation', 
                         model='google/flan-t5-base')
        print("Pipeline created successfully")
    except Exception as e:
        print(f"Pipeline error: {e}")
        return
    
    # More specific extraction prompt
    prompt = f"""What are the main cooking actions in this Ethiopian doro wat recipe? Ignore the introduction and explanations, just list the cooking steps:

    {transcript_text[:1500]}

    Example: Cut onions, heat oil, add spices, etc."""
    
    print(f"Prompt length: {len(prompt)} characters")
    
    try:
        print("Calling model...")
        response = client(prompt, 
                         max_new_tokens=300,
                         do_sample=True,
                         temperature=0.3,
                         repetition_penalty=1.1)
        print("Model responded:")
        print(response[0]['generated_text'])
    except Exception as e:
        print(f"Model error: {e}")

if __name__ == "__main__":
   parse_transcript('ethiopian_dorowat.txt') 