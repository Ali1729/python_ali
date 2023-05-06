for url_tag in url_tags:
    with open('tag.csv',w) as fp:
        fp.writelines(git_base_url + url_tag.get('href'))


for topic_tag in topic_tags:
        with open('tag.csv',w) as fp:
        fp.writelines(git_base_url + url_tag.get('href'))


