from article_search import *
from results import *
from collections import defaultdict



if __name__ == '__main__':
    results_list = read_from_pickle()
    
    num = 0
    num_faces = 0

    emotions_list = ['sadness', 'neutral', 'contempt', 'disgust', 'anger', 'surprise', 'fear', 'happiness']
    averages = {}
    for e in emotions_list:
        averages[e] = defaultdict(int)

    section_count = defaultdict(int)

    for a_result in results_list:
        if len(a_result.emotion_result) == 0:
            # No faces?
            continue

        article_json = a_result.article_obj.raw_json
        a_id = article_json['_id']

        title = article_json['headline']['main']
        date = article_json['pub_date']
        section = article_json['section_name']
        subsection = article_json['subsection_name']
        news_desk = article_json['news_desk']

        img_url = a_result.article_obj.image_url

        for i in range(len(a_result.emotion_result)):
            try:
                face_rectangle = a_result.emotion_result[i]['faceRectangle']
            except Exception:
                # Rate limit exceeded
                continue

            emotion = a_result.emotion_result[i]['scores']
            
            sadness = emotion['sadness']
            neutral = emotion['neutral']
            contempt = emotion['contempt']
            disgust = emotion['disgust']
            anger = emotion['anger']
            surprise = emotion['surprise']
            fear = emotion['fear']
            happiness = emotion['happiness']

            for e in emotions_list:
                averages[e][section] += emotion[e]

            """
            title, date, section, subsection, news_desk, img_url, face_rectangle, sadness, neutral, contempt, disgust, anger, surprise, fear, happiness
            """

            #input_values = [title, date, section, subsection, news_desk, img_url, face_rectangle, sadness, neutral, contempt, disgust, anger, surprise, fear, happiness]
            #input_values = [title, date, section, subsection, news_desk, emotion]
            #print(input_values)
            num_faces += 1
            section_count[section] += 1

            #insert_sql_database(input_values)
        num += 1
        print(num)

    for sec in section_count.keys():
        print(sec)
        print(section_count[sec])
        for e in emotions_list:
            averages[e][sec] = averages[e][sec]/section_count[sec]
            print(e + ': ' + str(averages[e][sec]))
        print('\n')
    

    print('num: {}'.format(num)) 
    print('num_faces: {}'.format(num_faces))

        
