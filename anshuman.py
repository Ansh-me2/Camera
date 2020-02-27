import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8) 
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray,4,255,cv2.THRESH_BINARY)
    blur = cv2.GaussianBlur(thresh1,(3,3),0)
    #kernel = np.ones((3,3), np.uint8)
    img_erosion = cv2.erode(blur, None, iterations=3) 
    img_dilation = cv2.dilate(img_erosion, None, iterations=3)
    return img_dilation

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_textnon23.png', output)
