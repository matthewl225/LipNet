from keras import backend as K

# Actual loss calculation
def ctc_lambda_func(args):
    y_pred, labels = args
    # from keras example image_ocr.py:
    # the 2 is critical here since the first couple outputs of the RNN
    # tend to be garbage:
    # y_pred = y_pred[:, 2:, :]
    #y_pred = y_pred[:, :, :]
    return K.categorical_crossentropy(labels, y_pred)