# ocr_check.py
import sys
import pytesseract
from PIL import ImageGrab

def ocr_check(x1, y1, x2, y2):
    # Capture the screen region
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    # Perform OCR
    text = pytesseract.image_to_string(img)
    return text.strip()

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, sys.argv[1:])
    print(ocr_check(x1, y1, x2, y2))
