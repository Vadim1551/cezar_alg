import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI.ui', self)
        self.alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.encryption_radioButton.setChecked(True)
        self.RU_radioButton.setChecked(True)
        self.label_6.setPixmap(QPixmap('cezar.png'))
        self.pushButton.clicked.connect(self.func)

    def change_color(self):
        self.pushButton.setStyleSheet("""
            background-color: rgb(74, 74, 74);
            border-color: green;
            border-width: 2px;
            border-style: solid;
            border-radius: 10px;
            color: rgb(235, 235, 235);
        """)
        QTimer.singleShot(300, lambda: self.pushButton.setStyleSheet("""
            background-color: rgb(74, 74, 74);
            border-color: rgb(225, 225, 225);
            border-width: 2px;
            border-style: solid;
            border-radius: 10px;
            color: rgb(235, 235, 235);
        """))

        self.label_3.setStyleSheet("""
            color: green;
            border-width: 2px;
            border-style: solid;
            border-color: green;
            background-color: rgb(74, 74, 74);
        """)
        QTimer.singleShot(300, lambda: self.label_3.setStyleSheet("""
            color:rgb(247, 247, 247);
            border-width: 2px;
            border-style: solid;
            border-color: rgb(243, 243, 243);
            background-color: rgb(74, 74, 74);
        """))

    def func(self):
        self.change_color()
        key = self.kayBox.value()
        lang = 'RU' if self.RU_radioButton.isChecked() else 'EU'
        data = self.input_textEdit.toPlainText().upper()
        if self.encryption_radioButton.isChecked():
            self.encryption(key, lang, data)
        else:
            self.decryption(key, lang, data)

    def encryption(self, key, lang, data):   #Функция для шифрования сообщения
        itog = ''
        if lang == 'RU':    #Если язык сообщения русский...
            for i in data:    #Перебираем каждый символ из сообщения
                index = self.alfavit_RU.find(i)  # Находим индекс этого символа в русском алфавите
                new_index = index + (key % 33)   # Находим новый индекс со сдвигом key, путем прибавления шага к индексу
                if i in self.alfavit_RU:   #Если символ существует в алфавите...
                    itog += self.alfavit_RU[new_index]   #К выводу добавляем зашифрованный символ
                else:    #Если символа нет в алфавите...
                    itog += i   #Добавляем незашифрованный символ к выводу
        else:   #Если язык сообщения английский...
            for i in data:   #Перебираем каждый символ из сообщения
                index = self.alfavit_EU.find(i)  # Находим индекс этого символа в английском алфавите
                new_index = index + (key % 26)   # Находим новый индекс со сдвигом key, путем прибавления шага к индексу
                if i in self.alfavit_EU:   #Если символ существует в алфавите..
                    itog += self.alfavit_EU[new_index]   #К выводу добавляем зашифрованный символ
                else:   #Если символа нет в алфавите...
                    itog += i   #Добавляем незашифрованный символ к выводу
        self.output_textEdit.setPlainText(itog)


    def decryption(self, key, lang, data):  #Функция для расшифрования сообщения точно такая же как и для шифрования,
                                            # кроме поиска нужного индекса, тут вычитание, а не сложение
        itog = ''
        if lang == 'RU':
            for i in data:
                index = self.alfavit_RU.find(i)
                new_index = index - (key % 33)
                if i in self.alfavit_RU:
                    itog += self.alfavit_RU[new_index]
                else:
                    itog += i
        else:
            for i in data:
                index = self.alfavit_EU.find(i)
                new_index = index - (key % 26)
                if i in self.alfavit_EU:
                    itog += self.alfavit_EU[new_index]
                else:
                    itog += i
        self.output_textEdit.setPlainText(itog)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
