import sqlite3 
import json

def create_database(): 
    #connect to db or create it if it doesn't exist  
    connection_obj  = sqlite3.connect('recipes.db')
    # Create a cursor object to interact with the database
    cursor_obj = connection_obj.cursor() 
    #drop table if it already exists 
    cursor_obj.execute("DROP TABLE IF EXISTS recipes")
    #SQL command to create a table in the database 
    table_creation_query = '''CREATE TABLE recipes
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL,
                         ingredients JSON,
                         directions JSON,
                         source TEXT
                        );'''
    #execute the statement
    cursor_obj.execute(table_creation_query) 
    #commit changes
    connection_obj.commit()
    #confirm changes 
    print("Table created successfully.") 
    #close the connection
    connection_obj.close()


def add_recipe(recipe_name, list_ingredients, steps, original_source): 
    #connect to db or create it if it doesn't exist  
    connection_obj  = sqlite3.connect('recipes.db')
    # Create a cursor object to interact with the database
    cursor_obj = connection_obj.cursor() 
    #drop table if it already exists 

    table_insert = '''INSERT INTO recipes (name, ingredients, directions, source)
    VALUES(?, ?, ?, ?);'''
    #execute the statement
    #cursor_obj.execute(table_insert, (recipe_name, str(list_ingredients), str(steps), original_source)) # - we're gonna try json dumps
    cursor_obj.execute(table_insert, (
        recipe_name, 
        json.dumps(list_ingredients),  # Use json.dumps instead of str()
        json.dumps(steps),             # Use json.dumps instead of str()
        original_source
    ))
     
    #commit changes
    connection_obj.commit()
    #confirm changes 
    print(f'Recipe added: {recipe_name}')
    #close the connection
    connection_obj.close() 

def view_recipes():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    for recipe in recipes:
        print(recipe)
    conn.close()

 


create_database()
view_recipes()  