## Python URL Shortener by Nilesh using MD5 Hash Algorithm

import hashlib

class UrlShortener:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "http://short.url/"

    def shorten_url(self, original_url):
        hash_value = hashlib.md5(original_url.encode()).hexdigest()[:6]
        short_url = self.base_url + hash_value
        self.url_mapping[short_url] = original_url
        return short_url

    def expand_url(self, short_url):
        original_url = self.url_mapping.get(short_url)
        return original_url

# Calling the function and assigning it to a variable
url_shortener = UrlShortener()

original_url = input("\nEnter url here: ")
short_url = url_shortener.shorten_url(original_url)

print(f"\nOriginal URL: {original_url}")
print(f"\nShort URL: {short_url}")

expanded_url = url_shortener.expand_url(short_url)
print(f"\nExpanded URL: {expanded_url}")