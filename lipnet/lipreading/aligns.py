import numpy as np

class Align(object):
    def __init__(self, absolute_max_string_len=32, label_func=None):
        self.label_func = label_func
        self.absolute_max_string_len = absolute_max_string_len

    def from_file(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()
        if not lines[0].strip().split(" ")[0].isdigit():
            print('NOT HERE')
            align = [(0,0,y.strip()) for y in lines]
            self.build(align)
            return self
        print('HERE')
        align = [(int(y[0])/1000, int(y[1])/1000, y[2]) for y in [x.strip().split(" ") for x in lines]]
        self.build(align)
        return self

    def from_array(self, align):
        self.build(align)
        return self

    def build(self, align):
        self.align = self.strip(align, ['sp','sil'])
        self.sentence = self.get_sentence(align)
        print(self.align)
        print(self.sentence)
        #passes in actual sentence into label function to get actual label
        self.padded_label = self.get_padded_label(self.sentence)
        print(self.padded_label)

    def strip(self, align, items):
        return [sub for sub in align if sub[2] not in items]

    def get_sentence(self, align):
        return " ".join([y[-1] for y in align if y[-1] not in ['sp', 'sil']])

    def get_padded_label(self, sentence):
        if sentence == "what is the weather":
            return np.array([1,0,0]).astype(int)
        elif sentence == "what time is it":
            return np.array([0,1,0]).astype(int)
        else:
            return np.array([0,0,1]).astype(int)

    @property
    def word_length(self):
        return len(self.sentence.split(" "))

    @property
    def sentence_length(self):
        return len(self.sentence)
