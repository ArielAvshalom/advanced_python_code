from urllib.request import urlopen
import re

url = "https://en.wikipedia.org/wiki/Omega-categorical_theory"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

title_index = html.find("<title>")

start_index = title_index + len("<title>")
end_index = html.find("</title>")

title = html[start_index:end_index]




