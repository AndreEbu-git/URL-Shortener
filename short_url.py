import json, os, string, random
from urllib.parse import urlparse

DATA_FILE = "data.json"
BASE_DOMAIN = "https://myapp.com/"
ALPHABET = string.ascii_letters + string.digits  # base62

def load_db():
    if not os.path.exists(DATA_FILE):
        return {"long_to_short": {}, "short_to_long": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_db(db):
    with open(DATA_FILE, "w") as f:
        json.dump(db, f, indent=2)

def is_valid_url(url: str) -> bool:
    p = urlparse(url)  # no try/except
    if p.scheme in ("http", "https") and p.netloc:
        return True
    else:
        return False

def make_id(db, length=7):
    # simple, collisions handled by re-rolling
    while True:
        sid = "".join(random.choice(ALPHABET) for _ in range(length))
        if sid not in db["short_to_long"]:
            return sid

def shorten_url(db, long_url: str) -> str | None:
    if not is_valid_url(long_url):
        return None  # no exceptions; let caller handle
    # Deduplicate
    if long_url in db["long_to_short"]:
        sid = db["long_to_short"][long_url]
    else:
        sid = make_id(db)
        db["long_to_short"][long_url] = sid
        db["short_to_long"][sid] = long_url
        save_db(db)
    return BASE_DOMAIN + sid

def expand_url(db, short_url_or_id: str) -> str | None:
    sid = short_url_or_id
    if short_url_or_id.startswith("http://") or short_url_or_id.startswith("https://"):
        parsed = urlparse(short_url_or_id)
        sid = parsed.path.strip("/")
    long_url = db["short_to_long"].get(sid)
    if long_url:
        return long_url
    else:
        return None

def count_urls(db) -> int:
    return len(db["short_to_long"])

if __name__ == "__main__":
    db = load_db()
    while True:
        print("\n1. Shorten URL\n2. Expand URL\n3. Count URLs\n4. Exit")
        choice = input("Choose option: ").strip()

        if choice == "1":
            long_url = input("Enter long URL: ").strip()
            short_url = shorten_url(db, long_url)
            if short_url:
                print("Shortened URL:", short_url)
            else:
                print("Invalid URL!")

        elif choice == "2":
            short_url = input("Enter short URL or ID: ").strip()
            original = expand_url(db, short_url)
            if original:
                print("Original URL:", original)
            else:
                print("Short URL not found!")

        elif choice == "3":
            print("Total URLs shortened:", count_urls(db))

        elif choice == "4":
            break

        else:
            print("Invalid choice.")
