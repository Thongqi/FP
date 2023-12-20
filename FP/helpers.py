import pytesseract
from pytesseract import Output

import cv2



def largestWord(filename):
    image = cv2.imread(filename)

    img = cv2.resize(image, (600, 360))

    return pytesseract.image_to_boxes(img)


    for word in text.split():
        if word.size >= 12:
            a = word # Replace as needed
            return a
        else:
            return error

    