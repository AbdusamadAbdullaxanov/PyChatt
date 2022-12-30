from pytesseract import pytesseract
from googletrans import Translator
from PIL import Image
import os


# print(os.listdir("D:/test-images/"))
def image_to_text(image_name: str) -> str:
    pytesseract.tesseract_cmd = r'D:\windows_apps\pytesseract\tesseract.exe'
    img = Image.open(f"D:/test-images/{image_name}")
    text = pytesseract.image_to_string(img)
    translator = Translator().translate(text=text, dest="uz").text
    return str(translator)


path = os.listdir("D:/test-images/")
for i in path:
    with open(f"D:/result/file{str(path.index(i) + 1)}.txt", mode="wb") as file:
        file.write(image_to_text(i).encode("utf-8"))
        print(f"file {os.listdir('D:/test-images/').index(i)} accomplished")

