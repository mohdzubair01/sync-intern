import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def _generate_shortened_url(self, url):
        hash_object = hashlib.md5(url.encode())
        hash_hex = hash_object.hexdigest()

        shortened_url = hash_hex[:8]
        return shortened_url

    def shorten_url(self, original_url):
        shortened_url = self._generate_shortened_url(original_url)
        self.url_map[shortened_url] = original_url
        return shortened_url

    def expand_url(self, shortened_url):
        original_url = self.url_map.get(shortened_url)
        return original_url


if __name__ == "__main__":
    url_shortener = URLShortener()
    original_url = "https://drive.google.com/file/d/1z_qnkMuiNjXUVDRkj6_NJtVJShKaXbxt/view"
    shortened = url_shortener.shorten_url(original_url)
    print(f"Shortened URL: {shortened}")
    user_input = input("Enter the shortened URL to expand: ")
    expanded = url_shortener.expand_url(user_input)
    if expanded:
        print(f"Expanded URL: {expanded}")
    else:
        print("URL not found.")
