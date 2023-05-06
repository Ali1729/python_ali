
import requests
import pandas as pd

from bs4 import BeautifulSoup

topic_url = "https://github.com/topics/3d"

response = requests.get(topic_url)

soup = BeautifulSoup(response.text, 'html.parser')

project_class = 'f3 color-fg-muted text-normal lh-condensed'
project_tags = soup.find_all('h3', project_class)

authors =[]
for project_tag in project_tags:
    authors.append(project_tag.text.strip().split('\n')[0])
    
    
project_url_class = 'text-bold wb-break-word'
project_url_tags = soup.find_all('a', project_url_class)
project_urls =[]


for project_url in project_url_tags:
    project_urls.append(str(topic_url) + str(project_url.get('href')))
    
projects_dict = {'Authors':authors,'project_urls':project_urls}
df = pd.DataFrame(projects_dict)
df.to_csv('3d_topics1.csv',index=False)