# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:53:43 2022

@author: Ariel
"""
import requests
from bs4 import BeautifulSoup
base_url = r"https://realpython.github.io/fake-jobs/"
page = requests.get(base_url)

#print(page)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id = "ResultsContainer")

job_info = results.find_all("div", class_="card-content")

for idx, info in enumerate(job_info):
    
    title = info.find("h2", class_ = "title")
    company = info.find("h3", class_ = "company")
    location = info.find('p', class_ = "location")
    
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip(), end = "\n"*3)
    
python_jobs = results.find_all("h2", 
                               string=lambda text : "python" in text.lower())

elements_of_python = [h2_element.parent.parent.parent for h2_element in python_jobs]

for element in elements_of_python:
    title = element.find("h2", class_ = "title")
    print(title.text.strip())
    
    links = element.find_all("a")
    
    for link in links:
        link_url = link["href"]
        print(link_url, end = "\n"*2)
    


