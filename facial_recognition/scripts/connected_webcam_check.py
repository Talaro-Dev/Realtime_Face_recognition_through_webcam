#script to check which webcams are connected to my pc
import cv2

def list_webcams():
    index = 0
    array = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            array.append(f"Webcam {index}")
        cap.release()
        index += 1
    return array

webcams = list_webcams()
print(webcams)
