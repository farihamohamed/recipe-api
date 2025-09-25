def parse_directions(transcript):
    """Parse cooking directions from continuous speech transcript"""
    import re
    
    text = transcript.replace('\n', ' ').lower()
    
    # More precise split patterns
    split_patterns = [
        r'\bnow let\'s\b',
        r'\bso now\b', 
        r'\bthe next step\b',
        r'\bthe next thing\b',
        r'\bonce you\'ve\b',
        r'\bafter that\b',
        r'\bthen you want to\b',
        r'\bstart washing\b',
        r'\bstart by\b',
        r'\bstart adding\b',
        r'\bi\'m going to add\b',
        r'\bwe\'re going to add\b',
        r'\bnow add\b',
        r'\bgive it a\b'
    ]
    
    combined_pattern = '|'.join(split_patterns)
    segments = re.split(combined_pattern, text)
    
    directions = []
    for segment in segments:
        segment = segment.strip()
        
        if len(segment) < 20:
            continue
            
        # Clean up
        segment = re.sub(r'\b(?:you know|um|uh|like|really|just|actually|so)\b\s*', '', segment)
        segment = re.sub(r'\s+', ' ', segment)
        
        if segment:
            segment = segment[0].upper() + segment[1:]
        
        cooking_words = ['add', 'cook', 'mix', 'heat', 'place', 'put', 'cut', 'boil', 
                        'stir', 'cover', 'remove', 'drain', 'rinse', 'wash', 'chop']
        
        if any(word in segment.lower() for word in cooking_words):
            directions.append(segment.strip())
    
    return directions

# Test function
def test_parser():
    # Load one of your transcripts
    with open('transcripts/somali_rice.txt', 'r') as f:
        transcript = f.read()
    
    result = parse_directions(transcript)
    
    print("=== PARSED COOKING STEPS ===")
    for i, step in enumerate(result, 1):
        print(f"{i}. {step}")
        print()

if __name__ == "__main__":
    test_parser()