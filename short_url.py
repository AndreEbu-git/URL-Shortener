import json
import string, random
from urllib.parse import urlparse

def shorten_url(L_url):
    if valid_url(L_url):
        

def expand_url():
def valid_url():
def count_urls():


if __name__ == "__main__":
    while True:
        print("\n1. Shorten URL\n2. Expand URL\n3. Count URLs\n4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            long_url = input("Enter long URL: ")
            short_url = shorten_url(long_url)
            if short_url:
                print("Shortened URL:", short_url)
            else:
                print("Invalid URL!")

        elif choice == "2":
            short_url = input("Enter short URL: ")
            original = expand_url(short_url)
            if original:
                print("Original URL:", original)
            else:
                print("Short URL not found!")

        elif choice == "3":
            print("Total URLs shortened:", count_urls())

        elif choice == "4":
            break