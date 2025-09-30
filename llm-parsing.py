import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

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
    
    # Use the prompt that worked well in ChatGPT
    prompt = f"""Please analyze this recipe transcript and extract:

INGREDIENTS (with quantities if mentioned):
- [list format]

STEPS (in order):
1. [numbered list]

Transcript: {transcript_text}"""
    
    print("Calling OpenAI API...")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )
        
        print("\n=== PARSED RECIPE ===")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parse_transcript('ethiopian_dorowat.txt')