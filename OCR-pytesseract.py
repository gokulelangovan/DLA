import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread('7.jpg')
img = cv2.resize(img, None, fx=3.5, fy=3.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
config = "--psm 3"
text = pytesseract.image_to_string(adaptive_threshold, config=config, lang='tam')
print(text)
cv2.imshow('Result',gray)
cv2.imshow("adaptive", adaptive_threshold)
cv2.waitKey(0)


