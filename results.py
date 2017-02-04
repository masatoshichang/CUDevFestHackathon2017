import pickle

class Result(object):
    
    def __init__(self, article_obj, emotion_result):
        self.article_obj = article_obj
        self.emotion_result = emotion_result


def save_to_pickle(result_list):
    with open('result_pickle2.pkl', 'wb') as fp:
        pickle.dump(result_list, fp)

    print('Saved to pickle')


def read_from_pickle(file_name='result_pickle.pkl'):
    with open(file_name, 'rb') as fp:
        result_list = pickle.load(fp)

    return result_list

