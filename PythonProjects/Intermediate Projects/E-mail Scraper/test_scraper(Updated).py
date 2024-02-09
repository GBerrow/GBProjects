"""The original code required you to manually download the ChromeDriver
executable file and specify its path in the driver variable.
This updated code I have amended uses webdriver_manager to dynamically manage the WebDriver binaries.
It automatically downloads the appropriate version of ChromeDriver based on the installed Chrome browser version,
eliminating the need for manual management of the WebDriver executable. Thus, should be working correctly"""


from typing import Set
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


class Browser:
    """Create a browser that scrapes any url for e-mail addresses."""

    def __init__(self):
        """Initialize the browser."""
        print('Starting up browser...')
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--headless")  # Prevents the browser from showing
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")

        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def __enter__(self):
        """Enter context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager."""
        if self.browser:
            print('Closing browser...')
            self.browser.quit()

    def scrape_emails(self, url: str) -> Set[str]:
        """Scrape emails from the specified URL."""
        print(f'Scraping "{url}" for emails')
        self.browser.get(url)
        page_source = self.browser.page_source

        # Create a set to avoid duplicates
        list_of_emails = set()
        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(re_match.group())

        return list_of_emails


def main():
    with Browser() as browser:
        # Scrape the e-mails
        emails = browser.scrape_emails('https://www.randomlists.com/email-addresses?qty=50')

        # Display the e-mails
        for i, email in enumerate(emails, start=1):
            print(i, email, sep='\n')


if __name__ == '__main__':
    main()
