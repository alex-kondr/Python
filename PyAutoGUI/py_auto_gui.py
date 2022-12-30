from pathlib import Path
import pyautogui
from PyPDF2 import PdfFileReader
import win32clipboard


TYPES_DOC_FOR_USER = {
    "1": "Заява",
    "2": "Клопотання",
    "3": "Матеріали адмінправопорушення"
}

TYPES_DOC = {
    "1": "Pfzdf",
    "2": "Rkjgjnfyyz",
    "3": "Vfnthsfkb flvsyghfdjgjheityyz"
}


class Doc:

    def __init__(self, type_doc: str) -> None:
        self.type_doc = type_doc
        self.number_of_pages = 0

    def open_d3(self):
        pyautogui.PAUSE = 1.5
        pyautogui.leftClick(1054, 1057)     # Відкрити Д-3

    def open_menu_attach_file(self):
        pyautogui.PAUSE = 0.5
        pyautogui.rightClick(880, 695)      # Відкрити меню
        pyautogui.moveRel(50, -100)         # Додаткові дії
        pyautogui.moveRel(200, 20)          # Прикріпити файли
        pyautogui.click(button="left")
        pyautogui.press("Enter")            # Ок

    def open_folder(self):
        pyautogui.leftClick(1063, 225)      # Ввести адрес
        pyautogui.typewrite(
            "C:\\Users\\TrueConf\\Documents\\My OneTouch Archive\\PDF Documents")
        pyautogui.press("Enter")

    def find_out_the_number_of_pages(self):
        pyautogui.leftClick(743, 332)
        pyautogui.hotkey("ctrl", "c")
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
        win32clipboard.CloseClipboard()
        file = Path(data[0])                 # Шлях до файлу

        with open(file, "rb") as fh:
            reader = PdfFileReader(fh)
            self.number_of_pages = reader.getNumPages()  # Кількість сторінок

    def select_file(self):
        pyautogui.hotkey("shift", "alt")    # Перемкнути мову
        pyautogui.doubleClick(743, 332)     # Відкрити файл

    def enter_data(self):
        pyautogui.typewrite(self.type_doc)   # Внести тип документа
        pyautogui.press("Right")             # Перейти в праву комірку
        pyautogui.typewrite(self.type_doc)   # Внести тип документа
        pyautogui.press("Right")             # Перейти в праву комірку
        pyautogui.press("Right")             # Перейти в праву комірку
        pyautogui.typewrite(str(self.number_of_pages))  # Внести кількість сторінок


def main():

    for i, value in TYPES_DOC_FOR_USER.items():
        print(f"{i}: {value}")

    number_type_doc = input("Виберіть тип документу: ")

    doc = Doc(TYPES_DOC[number_type_doc])

    doc.open_d3()
    doc.open_menu_attach_file()
    doc.open_folder()
    doc.find_out_the_number_of_pages()
    doc.select_file()
    doc.enter_data()


if __name__ == "__main__":
    main()