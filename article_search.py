import requests
import pprint

NY_TIMES_ARTICLE_API = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
NY_TIMES_API_KEY = '8c6b810edc3a42de829129b0e38eaf99'
NY_TIMES_ARCHIVE_API = 'https://api.nytimes.com/svc/archive/v1/'


class ArticleData(object):

    def __init__(self, json_data):
        self.raw_json = json_data

        # Get the biggest image from list
        height = 0
        self.biggest_image_url = ''
        for img in self.raw_json['multimedia']:
            if img['height'] > height:
                height = img['height']
                self.biggest_image_url = img['url']

        if self.biggest_image_url == '':
            raise Exception('Image not found')

        self.biggest_image_url = 'https://www.nytimes.com/' + self.biggest_image_url


class ArticleResponseList(object):

    def __init__(self, json_response):
        self.raw_json = json_response
        self.list_articles = []
        for n in self.raw_json['response']['docs']:
            try:
                self.list_articles.append(ArticleData(n))
            except Exception:
                pass

    def __getitem__(self, index):
        return self.list_articles[index]



def get_articles(json_data): # only returns 10 articles
    json_data['api-key'] = NY_TIMES_API_KEY
    r = requests.get(NY_TIMES_ARTICLE_API, params=json_data)
    #return r.json()
    return ArticleResponseList(r.json())


def get_archive(json_data, search_range):
    json_data['api-key'] = NY_TIMES_API_KEY
    url = NY_TIMES_ARCHIVE_API + search_range + '.json'
    r = requests.get(url, params=json_data)
    return r.json()


if __name__ == '__main__':
    payload = {
    'fq': "section_name:(\"Technology\")",
    'begin_date': "20160101",
    'end_date': "20160131"
            }

    t = get_articles(payload)
    print(t[0].biggest_image_url)
    print(t[1].biggest_image_url)
    print(t[2].biggest_image_url)
    print(t[3].biggest_image_url)
    print(t[4].biggest_image_url)

    search_range = '2016/1'
    t = get_archive(payload, search_range)
    response = t['response']
    docs = response['docs']
    print len(docs)

