import pickle

class Result(object):
    
    def __init__(self, article_obj, emotion_result, face_result):
        self.article_obj = article_obj
        self.emotion_result = emotion_result
        self.face_result = face_result


def save_to_pickle(result_list):
    with open('result_pickle.pkl', 'wb') as fp:
        pickle.dump(result_list, fp)

    print('Saved to pickle')

