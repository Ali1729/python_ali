import requests
import pandas as pd
from bs4 import BeautifulSoup
from scraping5 import get_topics

from multiprocessing import Pool

import time


def get_projects_url(topic_url,topic_name):
    
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
    df.to_csv(topic_name+'.csv')
    # print(df.head(5))
    


start_time = time.time()
topic_urls_dict= get_topics()
# for topic_url,topic_name in zip(topic_urls_dict['urls'], topic_urls_dict ['topics']):
#     get_projects_url(topic_url=topic_url,topic_name = topic_name)

# print(list(zip(topic_urls_dict['urls'], topic_urls_dict ['topics'])))
# print(type(list(zip(topic_urls_dict['urls'], topic_urls_dict ['topics']))))

with Pool(4) as p:
    p.map(get_projects_url,zip(topic_urls_dict['urls'], topic_urls_dict ['topics']))

end_time= time.time()

print("total_time_took"+str(end_time-start_time))