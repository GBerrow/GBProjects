from difflib import get_close_matches
import json
import random
import discord

def get_best_match(user_question: str, questions: dict) -> str | None:
    """Compares the user message similarity to the ones in the dictionary"""

    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    # Return the first best match, else return None
    if matches:
        return matches[0]


def get_response(message: str, knowledge: dict) -> discord.Embed:
    # Finds the best match, otherwise returns none.
    best_match: str | None = get_best_match(message, knowledge)

    # Gets the base match from the knowledge base
    if best_match:
        answer = knowledge.get(best_match)
        if answer:
            embed = discord.Embed(title="Bot Response", description=answer, color=0x00ff00)
            return embed

    # If no suitable response is found, provide a generic response
    responses = [
        "I'm sorry, I didn't quite understand that. Could you please rephrase your question?",
        "Hmm, I'm not sure I follow. Can you try asking again in a different way?",
        "It seems I'm having trouble understanding your question. Maybe try wording it differently?",
        "I'm still learning! Your question might be a bit too complex for me. Can you simplify it?",
        "I'm not programmed to understand everything! Feel free to ask me something else.",
    ]
    response = random.choice(responses)
    embed = discord.Embed(title="Bot Response", description=response, color=0xff0000)
    return embed


def load_knowledge(file: str) -> dict:
    with open(file, 'r') as f:
        return json.load(f)

    # if __name__ == "__main__":
    #     test_knowledge: dict = load_knowledge('knowledge.json')
    #     test_response: str = get_response('hello', knowledge=test_knowledge)
    #     print(test_response)
