""" Headline Scraper: This code fetches headlines from the BBC Wales news webpage and
    allows the user to search for specific terms within those headlines.
    Then it prints the matching headlines along with their occurrence count.
"""

import re
from bs4 import BeautifulSoup
import requests

def get_soup() -> BeautifulSoup:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    try:
        request = requests.get('https://www.bbc.co.uk/news/wales', headers=headers)
        request.raise_for_status()  # Raise an exception for bad status codes
        html = request.content
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except requests.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines = set()

    for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
        headline = h.text.lower()
        headlines.add(headline)

    return sorted(headlines)

def check_headlines(headlines: list[str], term: str):
    term_list = []
    terms_found = 0

    # Compile a regular expression pattern to match the whole word
    pattern = re.compile(r'\b{}\b'.format(re.escape(term)), re.IGNORECASE)

    for i, headline in enumerate(headlines, start=1):
        if re.search(pattern, headline):
            terms_found += 1
            term_list.append(headline)
            print(f'{i}: {headline.capitalize()}<------------------"{term}"')
        else:
            print(f'{i}: {headline.capitalize()}')

    print('---------------------------------')
    if terms_found:
        print(f'"{term}" was mentioned {terms_found} times')
        print('---------------------------------')

        for i, headline in enumerate(term_list, start=1):
            print(f'{i}: {headline.capitalize()}')

    else:
        print(f'No matches found for: "{term}"')


def main():
    soup = get_soup()
    if soup:
        headlines = get_headlines(soup)
        user_input = input("Enter a term to search: ").strip()
        check_headlines(headlines, user_input)


if __name__ == '__main__':
    main()
