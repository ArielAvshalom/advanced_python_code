from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/Omega-categorical_theory"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")