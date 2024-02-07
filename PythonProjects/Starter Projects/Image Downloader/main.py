# Image downloader with the ability to download either a single image or multiple images.
# If you choose to download multiple images,
# you can provide a list of URLs and corresponding names separated by commas. Have fun!

import os
import requests

# Function to get the extension of the image from its URL
def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', '.svg']
    for ext in extensions:
        if ext in image_url:
            return ext

# Function to download a single image from a URL
def download_image(image_url: str, name: str, folder: str = None):
    # Determine the extension of the image
    if ext:=get_extension(image_url):
        # Create the full path for the image
        if folder:
            image_name: str = os.path.join(folder, f'{name}{ext}')
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extension could not be located...')

    # Check if the file already exists
    if os.path.isfile(image_name):
        raise Exception('File name already exists...')

    # Download the image
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully!')
    except Exception as e:
        print(f'Error: {e}')

# Function to download multiple images from a list of URLs
def download_images(urls: list[str], names: list[str], folder: str = None):
    # Check if the number of URLs matches the number of names
    if len(urls) != len(names):
        raise ValueError('The number of URLs should match the number of names.')

    # Iterate over each URL and name, and download the corresponding image
    for url, name in zip(urls, names):
        download_image(url, name, folder)

if __name__ == '__main__':
    choice = input('Do you want to download a single image (1) or multiple images (2)? ')

    if choice == '1':
        input_url: str = input('Enter a url: ')
        input_name: str = input('What would you like to name it?: ')

        print('Downloading...')
        download_image(input_url, name=input_name, folder='image')
    elif choice == '2':
        urls_input = input('Enter image URLs separated by comma: ').split(',')
        names_input = input('Enter names separated by comma: ').split(',')

        print('Downloading...')
        download_images(urls_input, names_input, folder='image')
    else:
        print('Invalid choice.')


