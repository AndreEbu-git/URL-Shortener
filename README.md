# URL-Shortener
A simple and efficient URL shortener application with both command-line and graphical user interfaces. This tool allows you to shorten long URLs into compact, shareable links and retrieve the original URLs when needed.

## Features

- **URL Shortening:** Convert long URLs into short, random alphanumeric IDs

- **URL Retrieval:** Get the original URL from a shortened ID

- **Persistence:** All shortened URLs are saved to a JSON file and persist between sessions

- **URL Validation:** Automatically validates URLs before shortening

- **Statistics:** Track the total number of shortened URLs

- **Dual Interface:** Available as both a command-line tool and a graphical application

## Installation
1. Clone or download this project to your local machine
2. Ensure you have Python 3.7 or higher installed
3. Install the required dependencies:
   `pip install flet validators`

## **Usage**

## Graphical Interface (Recommended)
Run the graphical interface with:
`python main.py`
This will launch a user-friendly window where you can:
- Enter a long URL and click "Shorten URL" to generate a short ID
- Enter a short ID and click "Retrieve Original URL" to get the original URL
- View the total count of shortened URLs
## Command-Line Interface

Run the command-line interface with:
`python short_url.py`
This will present a text menu with the following options:
1. Shorten URL - Enter a long URL to get a short ID
2. Retrieve original URL - Enter a short ID to get the original URL
3. Display number of shortened URLs - View the total count
4. Exit - Close the application

## How It Works

- When you shorten a URL, the application generates a random alphanumeric string (6-11 characters long)
- The mapping between the short ID and the original URL is stored in a JSON file (`url_mappings.json`)
- The application validates URLs before shortening them
- All data is persisted between sessions using the JSON file

## File Structure
`url-shortener/
├── main.py          # Graphical interface using Flet
├── short_url.py     # Core functionality and CLI
└── url_mappings.json # Data storage (created automatically)`

## Dependencies
- flet: For the graphical user interface
- validators: For URL validation

## Notes
- The application creates a `url_mappings.json` file in the same directory to store all URL mappings
- Short IDs are randomly generated and are not quaranteed to be the same for the same URL across different sessions
- The application does not currently provide a way to create custom short IDs

## License
This project is open source and available under the MIT License.
