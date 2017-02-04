import requests

NY_TIMES_ARTICLE_API = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
NY_TIMES_API_KEY = '8c6b810edc3a42de829129b0e38eaf99'
NY_TIMES_ARCHIVE_API = 'https://api.nytimes.com/svc/archive/v1/'

def get_articles(json_data): # only returns 10 articles
    r = requests.get(NY_TIMES_ARTICLE_API, params=json_data)
    return r.json()


def get_archive(json_data, search_range):
    url = NY_TIMES_ARCHIVE_API + search_range + '.json'
    r = requests.get(url, params=json_data)
    return r.json()


if __name__ == '__main__':
    payload = {
    'api-key': "8c6b810edc3a42de829129b0e38eaf99",
    'fq': "section_name:(\"Technology\")",
    'begin_date': "20160101",
    'end_date': "20160131"
            }

    t = get_articles(payload)
    response = t['response']
    docs = response['docs']
    print len(docs)

    search_range = '2016/1'
    t = get_archive(payload, search_range)
    response = t['response']
    docs = response['docs']
    print len(docs)

