import requests
import pprint
import pypyodbc

NY_TIMES_ARTICLE_API = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
NY_TIMES_API_KEY = '8c6b810edc3a42de829129b0e38eaf99'
NY_TIMES_ARCHIVE_API = 'https://api.nytimes.com/svc/archive/v1/'


class ArticleData(object):
    """
    Represents each individual article
    """

    def __init__(self, json_data):
        self.raw_json = json_data

        # Get the biggest image from list
        height = 0
        self.image_url = ''
        for img in self.raw_json['multimedia']:
            if img['height'] > height:
                height = img['height']
                self.image_url = img['url']

        if self.image_url == '':
            raise Exception('Image not found')

        self.image_url = 'https://www.nytimes.com/' + self.image_url


class ArticleResponseList(object):
    """
    Holds list of ArticleData
    Input is the json data from HTTP requests
    """

    def __init__(self, json_response):
        self.current = 0

        self.raw_json = json_response
        self.list_articles = []
        for n in self.raw_json['response']['docs']:
            try:
                self.list_articles.append(ArticleData(n))
            except Exception:
                pass

    def __getitem__(self, index):
        return self.list_articles[index]

    def __iter__(self):
        return self

    def next(self):
        if self.current >= len(self.list_articles):
            raise StopIteration
        else:
            self.current += 1
            return self.list_articles[self.current - 1]

    def __len__(self):
        return len(self.list_articles)



def get_articles(json_data): # only returns 10 articles
    json_data['api-key'] = NY_TIMES_API_KEY
    r = requests.get(NY_TIMES_ARTICLE_API, params=json_data)
    return ArticleResponseList(r.json())


def get_archive(json_data, search_range):
    json_data['api-key'] = NY_TIMES_API_KEY
    url = NY_TIMES_ARCHIVE_API + search_range + '.json'
    r = requests.get(url, params=json_data)
    # return r.json()
    return ArticleResponseList(r.json())


def insert_sql_database(input_values):
    connection = pypyodbc.connect('Driver={ODBC Driver 13 for SQL Server};'
                                  'Server=tcp:cudevfest2017.database.windows.net,1433;'
                                  'Database=cudevfest2017;'
                                  'Uid=devfest@cudevfest2017;'
                                  'Pwd=!23QweAsdZxc;'
                                  'Encrypt=yes;'
                                  'TrustServerCertificate=no;'
                                  'Connection Timeout=30;')

    cursor = connection.cursor()
    SQLCommand = ("INSERT INTO dbo.EmotionSection "
                  "(id, title, section, subsection, news_desk, img_url, face_rectangle, sadness, neutral, contempt, disgust, anger, surprise, fear, happiness)"
                  "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

    Values = [1, "test", "test", "test", "test", "test", "test", 0, 0, 0, 0, 0, 0, 0, 0]
    cursor.execute(SQLCommand, input_values)

    #Commit the change
    connection.commit()
    #Close the sql server connection
    connection.close()


if __name__ == '__main__':
    payload = {
    'fq': "section_name:(\"Technology\")",
    'begin_date': "20160101",
    'end_date': "20160131"
            }

    t = get_articles(payload)

    for i in t:
        print(i.image_url)

    search_range = '2016/1'
    t = get_archive(payload, search_range)

    for i in t:
        print(i.image_url)


