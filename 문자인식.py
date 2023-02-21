import pytesseract
from PIL import Image

# 이미지 불러오기
image = Image.open('cap.png')
# 이미지에서 문자 추출

text = pytesseract.image_to_string(image, lang='eng')

# 추출된 문자 출력
print('Car number:', text)