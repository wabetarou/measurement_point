# pip install -r requirements.txt

from detect_contour import detect_contour
from extract_coordinate import extract_coordinate

if __name__ == '__main__':
  # detect_contour('vibration.png')
  extract_coordinate('vibration.png')