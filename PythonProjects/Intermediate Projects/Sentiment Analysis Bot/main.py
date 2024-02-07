""" I have improved the function that takes the bot's mood as an argument. Depending on the bot's mood, it selects an appropriate reaction from a predefined set of reactions. 
If the bot's mood is happy, the user responds with a happy emoji. 
If the bot's mood is angry, the user responds with a thumbs down emoji. Otherwise, it randomly selects a reaction from the list of reactions. """


import logging
import random
from textblob import TextBlob
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    try:
        polarity: float = TextBlob(input_text).sentiment.polarity
        friendly_threshold: float = sensitivity
        hostile_threshold: float = -sensitivity

        if polarity >= friendly_threshold:
            return Mood('😀', polarity)
        elif polarity <= hostile_threshold:
            return Mood('😡', polarity)
        else:
            return Mood('😑', polarity)
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        return Mood('❌', 0)


def get_user_reaction(bot_mood: Mood):
    if bot_mood.emoji == '😀':
        return '😄'
    elif bot_mood.emoji == '😡':
        return '👎'
    else:
        return random.choice(['👍', '😕'])


def run_bot():
    print('Enter some text to get a sentiment analysis back (type "exit" to quit):')
    while True:
        user_input: str = input('You: ')
        if user_input.lower() in ['exit', 'quit']:
            logging.info("Exiting bot.")
            break

        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f'Bot: {mood.emoji} ({mood.sentiment})')

        reaction = get_user_reaction(mood)
        print(f'You: {reaction} (Your reaction to the bot\'s response)')

        if mood.sentiment >= 0.5:
            print("Bot: Looks like you're feeling great! Anything exciting happening?")
        elif mood.sentiment <= -0.5:
            print("Bot: I'm sorry to hear that. Would you like to talk about it?")
        else:
            print("Bot: Seems like a neutral response. How can I assist you further?")


if __name__ == '__main__':
    run_bot()
