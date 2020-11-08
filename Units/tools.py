import numpy as np

def get_setting(setting):
    read_dictionary = np.load('settings.npy',allow_pickle='TRUE').item()
    got_setting = read_dictionary[setting]
    return got_setting