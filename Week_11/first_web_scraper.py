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


#quick intro on regular ex[press]ions

re.findall('ab*c', 'ac')
#ac abc abbc abbbc

re.findall('ab*.*c', 'scscsfasfqwwfasAbbbBbbdCcccdasdAc', re.IGNORECASE)


match_results = re.search('ab*c', "ABC", re.IGNORECASE)

string = "everything is <awesome> everything is cool when you work as a <team>."

string1 = re.sub("<.*?>", "supercalifragilisticespionodocious", string)

mytesttext = """
html htmhl hml lalal alalla
<TITLE > PROFILE : ARIEL IS AWESOME</title  / >
lal ala land cake walk bored shorts
"""

pattern = "<title.*?>.*?</title.*?>"

match_results2 = re.search(pattern, mytesttext, re.IGNORECASE)

title = match_results2.group()
title_without_tags = re.sub("<.*?>", "", title)







