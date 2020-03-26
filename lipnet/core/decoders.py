from keras import backend as K
import numpy as np

class Decoder(object):
    def __init__(self):
        pass

    def decode(self, y_pred):
        decoded = np.argmax(y_pred, axis=1)
        sentences = []
        for decoding in decoded:
            if decoding == 0:
                sentences.append("what is the weather")
            elif decoding == 1:
                sentences.append("what time is it")
            else:
                sentences.append("directions to home")
        return sentences