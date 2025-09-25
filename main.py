# main.py
from database import create_database, add_recipe

def parse_directions(transcript):
    """Simple sentence parsing for directions"""
    sentences = transcript.replace('\n', ' ').split('.')
    directions = []
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 15:
            directions.append(sentence)
    return directions

def load_transcript(filename):
    """Load transcript from file"""
    with open(f'transcripts/{filename}', 'r') as file:
        return file.read()

""" def view_recipes():
    Display all recipes from database
    import sqlite3
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    print("\n=== ALL RECIPES ===")
    for recipe in recipes:
        print(f"ID: {recipe[0]}")
        print(f"Name: {recipe[1]}")
        print(f"Ingredients: {recipe[2]}")
     
      # Debug: Show what directions actually look like
        print(f"Directions type: {type(recipe[3])}")
        print(f"Directions length: {len(recipe[3]) if recipe[3] else 0}")
        print(f"First 100 chars of directions: {str(recipe[3])[:100]}...")
        

        print(f"Source: {recipe[4]}")
        print("-" * 50)
    conn.close() """ 


def view_recipes():
    import sqlite3
    import json
    
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, directions FROM recipes")
    
    for name, directions in cursor.fetchall():
        print(f"\n=== {name} - COOKING STEPS ===")
        steps = json.loads(directions)
        
        for i, step in enumerate(steps[:10], 1):  # First 10 steps
            print(f"{i}. {step}")
        
        print(f"\n(Showing 10 of {len(steps)} total steps)")
        print("-" * 50)
    
    conn.close()


def main():
    # Step 1: Create database
    print("Setting up database...")
    create_database()
    
    # Step 2: Process Ethiopian Stew
    print("Processing Ethiopian Doro Wat...")
    ethiopian_transcript = load_transcript('ethiopian_dorowat.txt')
    ethiopian_ingredients = [
     '4 medium-sized red onions',
     '4 pounds chicken I used skinless legs',
     '3/4 to 1 cup Vegetable oil or any good cooking oil of your choice',
     '2 tablespoon kibbeh Ethiopian spiced butter',
     '2 tablespoons tomato paste optional',
     '6 eggs hard-boiled',
     '2 tbsp minced garlic',
     '2 tbsp grated ginger',
     '1/4 cup water',
     'salt to taste',
     '1/2 cup of berbere spice',
     '1 cup vinegar',
     '2 cups water to clean chicken']
    ethiopian_directions = parse_directions(ethiopian_transcript)
    add_recipe('Ethiopian Doro Wat', ethiopian_ingredients, ethiopian_directions, "Lola's Kitchen")
    
    # Step 3: Process Somali Rice
    print("Processing Somali Rice...")
    somali_transcript = load_transcript('somali_rice.txt')
    somali_ingredients = [
    '1 cup rice (I like to use sella rice), parboiled (Cook until it is half cooked, so half the rice is clear and some is still white, for me it takes about 8 mins. This can differ)'
    '1/2 onion, sliced (you can choose to use a whole one)'
    '1/2 cup vegetable oil (about 8tbsp)'
    '1 onion, diced'
    '1 medium tomato, diced'
    'Handful coriander, crushed'
    '3-4 garlic cloves, crushed'
    '1 chicken stock cube (I used Maggi brand, you can use 1 tbsp of the powdered version, you can substitute this for vegetable stock)'
    '4-5 cardamom pods, (you can also use 1/4 teaspoon powdered cardamom)'
    '1 cinnamon stick'
    '1 tbsp ground cumin'
    '1/4 tsp food colouring of your choice (turning it into a liquid or using the liquid versions work too)'
    '1/4 cup raisins/sultanas, rinse in boiling water to soften'
]
    somali_directions = parse_directions(somali_transcript)
    add_recipe('Somali Rice', somali_ingredients, somali_directions, 'Ilhan A.')
    
    # Step 4: Show results
    print("\nRecipes added successfully!")
    view_recipes()

if __name__ == "__main__":
    main()
