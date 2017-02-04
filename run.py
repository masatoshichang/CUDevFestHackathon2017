import time

from article_search import *
from microsoft.microsoft_api import *
from results import *



if __name__ == '__main__':
    payload = {}

    for m in range(2, 13):
        search_range = '2016/{}'.format(m)
        archive_list = get_archive(payload, search_range)

        result_list = []

        num_articles = len(archive_list)
        
        i = 0
        for an_article in archive_list:
            i += 1
            print('{}/{}'.format(i, num_articles))
            image_url = an_article.image_url
            emotion_json = get_emotion(image_url)

            face_json = get_face(image_url)

            result = Result(an_article, emotion_json, face_json)
            result_list.append(result)


            time.sleep(1)


        
    save_to_pickle(result_list)
