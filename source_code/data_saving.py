import pickle
import os


def load_data():
    if 'user_data' not in os.listdir():
        db = {}
        with open('user_data','wb') as f:
            pickle.dump(db,f)

    try:
        user_data = open('user_data', 'rb')
        db = pickle.load(user_data)
        user_data.close()
        with open('user_data','wb') as f:
            pickle.dump(db,f)
    except EOFError:
        db = {}
    return db

load_data()
