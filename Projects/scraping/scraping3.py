import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = "https://github.com/topics/"
response = requests.get(base_url)


soup = BeautifulSoup(response.text, 'html.parser')

selection_class ='f3 lh-condensed mb-0 mt-1 Link--primary'
topic_tags = soup.find_all('p', selection_class)

url_class ='no-underline flex-1 d-flex flex-column'
url_tags = soup.find_all('a', url_class)

git_base_url = 'https://github.com'
for url_tag in url_tags:
    print(git_base_url + url_tag.get('href'))
    
real_topics=[]
for topic_tag in topic_tags:
    real_topics.append(topic_tag.text)
    
real_urls =[]
for url_tag in url_tags:
    real_urls.append(git_base_url + url_tag.get('href'))
    
topics_dict = {'topics':real_topics,'urls':real_urls}
topics_dict



df = pd.DataFrame(topics_dict)

df.to_csv('topics2.csv',index=False)