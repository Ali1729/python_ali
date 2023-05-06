import requests
from bs4 import BeautifulSoup
import pandas as pd


BASE_URL = "https://github.com/topics/"
GIT_BASE_URL = 'https://github.com'


def get_topics(): 
    """_summary_

    Returns:
        dictionary: dictionary 
                    first element is topic name
                    second element is url
    """
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    selection_class ='f3 lh-condensed mb-0 mt-1 Link--primary'
    topic_tags = soup.find_all('p', selection_class)
    url_class ='no-underline flex-1 d-flex flex-column'
    url_tags = soup.find_all('a', url_class)

    # for url_tag in url_tags:
    #     print(GIT_BASE_URL + url_tag.get('href'))
        
    real_topics=[]
    for topic_tag in topic_tags:
        real_topics.append(topic_tag.text)
        
    real_urls =[]
    for url_tag in url_tags:
        real_urls.append(GIT_BASE_URL + url_tag.get('href'))
        
    topics_dict = {'topics':real_topics,'urls':real_urls}
    topics_dict

    df = pd.DataFrame(topics_dict)

    df.to_csv('topics2.csv',index=False)
    # print(df.head(10))
    return topics_dict

if __name__ == '__main__':
    get_topics()