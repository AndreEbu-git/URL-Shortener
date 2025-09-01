import json
import os
import random
import string
import validators

url_mappings = {}
filename = "url_mappings.json"

url_mappings = (
    json.load(open(filename, "r")) if os.path.exists(filename) else {}
)

def get_long_url(short_id):
    if short_id in url_mappings:
        return url_mappings[short_id]
    else:
        return "Short URL not found."

url_count = len(url_mappings)

def shorten_url(long_url):
    global url_count

    if not validators.url(long_url):  
        return "Error! Invalid URL"

    while True:
        short_id_length = random.randint(6, 11) 
        short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=short_id_length))
        if short_id not in url_mappings:
            break

    url_mappings[short_id] = long_url
    url_count += 1

    with open(filename, "w") as f:
        json.dump(url_mappings, f)

    return short_id

def display_url_count():
    return url_count

def display_options():
    """Displays the menu options to the user."""
    print("\nURL Shortener Menu:")
    print("1. Shorten URL")
    print("2. Retrieve original URL")
    print("3. Display number of shortened URLs")
    print("4. Exit")

def run_interface():
    while True:
        display_options()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            long_url = input("Enter the long URL: ")
            short_id = shorten_url(long_url)
            print(f"Shortened URL ID: {short_id}")
        elif choice == '2':
            short_id = input("Enter the short ID: ")
            long_url = get_long_url(short_id)
            print(f"Original URL: {long_url}")
        elif choice == '3':
            count = display_url_count()
            print(f"Number of shortened URLs: {url_count}")
        elif choice == '4':
            print("Exiting URL Shortener. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

run_interface()
