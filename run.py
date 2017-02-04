import time

from article_search import *
from microsoft.microsoft_api import *
from results import *



if __name__ == '__main__':
    payload = {}


    result_list = []
    result_list = read_from_pickle('result_pickle2.pkl')

    for m in range(3, 13):
        search_range = '2016/{}'.format(m)
        print('-' * 50)
        print('Search range')
        print(search_range)
        archive_list = get_archive(payload, search_range)
        print(archive_list)


        num_articles = len(archive_list)
        
        i = 0
        for an_article in archive_list:
            i += 1
            print('{}/{}'.format(i, num_articles))
            image_url = an_article.image_url
            emotion_json = get_emotion(image_url)

            # face_json = get_face(image_url)

            result = Result(an_article, emotion_json)
            result_list.append(result)

            if i % 50 == 0:
                save_to_pickle(result_list)

        save_to_pickle(result_list)

        
    save_to_pickle(result_list)
