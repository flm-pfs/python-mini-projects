import hashlib
import base64


class URLShortener:
    def __init__(self):
        self.url_map = {}  # Dictionary to store the mapping of short URLs to long URLs

    def shorten_url(self, long_url):
        # Generate a unique hash for the long URL
        hash_object = hashlib.sha256(long_url.encode())
        hash_hex = hash_object.hexdigest()
        short_url = base64.urlsafe_b64encode(
            hash_hex[:8].encode()).decode()[:6]

        # Store the mapping
        self.url_map[short_url] = long_url
        return short_url

    def expand_url(self, short_url):
        return self.url_map.get(short_url, "URL not found")

    def menu(self):
        while True:
            print("\nURL Shortener Menu:")
            print("1. Shorten URL")
            print("2. Expand URL")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                long_url = input("Enter the long URL: ")
                short_url = self.shorten_url(long_url)
                print(f"Shortened URL: {short_url}")
            elif choice == '2':
                short_url = input("Enter the short URL: ")
                long_url = self.expand_url(short_url)
                print(f"Expanded URL: {long_url}")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    url_shortener = URLShortener()
    url_shortener.menu()
