# Website Checker: This code uses the logging module for outputting messages,
# and it catches more specific exceptions for handling HTTP requests. Additionally,
# logging messages are printed with different severity levels, allowing for easier debugging and error tracking.



import csv
import requests
import logging
from fake_useragent import UserAgent
from http import HTTPStatus

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO

def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
    return websites

def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome

def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value.value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description
    return '(???) Unknown status code'

def check_website(website: str, user_agent):
    try:
        response = requests.get(website, headers={'User-Agent': user_agent})
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        logging.info('%s %s', website, get_status_description(response.status_code))
    except requests.exceptions.RequestException as e:
        logging.error('Could not get information for website: "%s" due to error: %s', website, e)

def main():
    sites: list[str] = get_websites('websites.csv')
    user_agent: str = get_user_agent()

    for site in sites:
        check_website(site, user_agent)

if __name__ == '__main__':
    main()



