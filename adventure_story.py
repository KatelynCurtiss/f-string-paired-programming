# Katelyn Curtiss
# Current date
# f-String Adventure Story

'''
Directions:

1. Update the comment block at the top of this script.

2. Use the Python `input( )` function to prompt (ask) the user for three pieces of information:

     - the hero's first name
     - the setting of the story (e.g., forest, desert, cave system)
     - the object the hero finds while on his/her adventure

3. Assign each piece of information collected to a variable with a short, specific name.

4. Declare (create) a variable named `story` and assign to it the `f-string` that is your adventure story

5. Use the `print( )` function to display your adventure story on the screen.

6. Execute (run) your script in Visual Studio Code and correct any errors.
'''
first_name = input('Please enter your first name:\n')
setting = input('Where does your story take place? (Example: desert)\n')
item = input('Enter the magic item you found while on your adventure:\n')

print(f'{first_name} was running in the {setting} and found, quite unexpectedly, a magic {item}.')


