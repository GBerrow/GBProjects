# In creating this Madlibs story, I have decided to add a random element effect,
# by incorporating a list of options for each word type and randomly selecting one from the list.
# users can enter a specific word or type "random",
# to get a randomly selected word from the predefined options for each word type.
# This adds an element of surprise and variety to your MadLibs story.

import random

def get_input(word_type: str, options: list[str]):
    user_input = input(f"Enter a {word_type} ({', '.join(options)}): ")
    if user_input.lower() == 'random':
        return random.choice(options)
    return user_input

noun_options = ["cat", "dog", "tree", "mountain", "book"]
adjective_options = ["happy", "sad", "exciting", "calm", "mysterious"]
verb_options = ["run", "jump", "sing", "dance", "read"]

noun1 = get_input("noun", noun_options)
adjective1 = get_input("adjective", adjective_options)
verb1 = get_input("verb", verb_options)
noun2 = get_input("noun", noun_options)
verb2 = get_input("verb", verb_options)

story = f"""
Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} all day.

One day, {noun2} walked into the room and caught the {noun1} in the act. 

{noun2}: "What are you doing?"
{noun1}: "I'm just {verb1}ing, what's the big deal?"
{noun2}: "Well, it's not every day that you see a {noun1} {verb1}ing in the middle of the day."
{noun1}: "I guess you're right. Maybe I should take a break."
{noun2}: "That's probably a good idea. Why don't we go {verb2} instead?"
{noun1}: "Sure, that sounds like fun!"

And so, {noun2} and the {noun1} went off to {verb2} and had a great time. 
The end.
"""

print(story)
