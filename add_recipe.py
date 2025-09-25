import sqlite3

def add_recipe(recipe_name, list_ingredients, steps, original_source): 
    #connect to db or create it if it doesn't exist  
    connection_obj  = sqlite3.connect('recipes.db')
    # Create a cursor object to interact with the database
    cursor_obj = connection_obj.cursor() 
    #drop table if it already exists 

    table_insert = '''INSERT INTO recipes (name, ingredients, directions, source)
    VALUES(recipe_name, list_ingredients, steps, original_source);
    '''
    #execute the statement
    cursor_obj.execute(table_insert) 
    #commit changes
    connection_obj.commit()
    #confirm changes 
    print(f'Recipe Name: {name}.')
    #close the connection
    connection_obj.close()

    