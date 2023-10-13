import sys
from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from datetime import datetime
import re
import os


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionLogOpen.triggered.connect(self.handle_open_file)
        self.ui.actionLogAdd.triggered.connect(self.add_to_log)
        self.ui.actionLogWatch.triggered.connect(self.watch_log)
        self.ui.actionLogExport.triggered.connect(self.export_data)
        self.show_log_not_find()
        self.ui.label = QtWidgets.QLabel()
        self.ui.label.setText("dmd")
        self.ui.statusBar.addWidget(self.ui.label)

    def handle_open_file(self):
        current_datetime = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        file_path = QFileDialog.getOpenFileName()[0]
        if file_path:
            filesize = f'{os.path.getsize(file_path): }'
            self.ui.label.setText(
                f"Открыт файл {file_path}  | {filesize} байт")
            file = open(file_path, 'r')
            self.ui.listWidget.addItem(
                f'Файл {file_path} был открыт {current_datetime}')
            self.ui.listWidget.addItem(" ")
            self.find_pattern_in_file(file)
            file.close()
            self.ui.listWidget.addItem(" ")

    def find_pattern_in_file(self, file):
        pattern = '[0-9]{2}-[0-9]{2}-[0-9]{4}'
        for i, line in enumerate(file):
            match = re.search(pattern, line)
            self.ui.listWidget.addItem(
                f'строка:{i + 1}, позиция {match.span()[0]} : найдено "{match.group()}" ')

    def add_to_log(self):
        if self.ui.listWidget.count() > 0:
            with open("script18.log", "a") as f:
                for i in range(self.ui.listWidget.count()):
                    f.write(self.ui.listWidget.item(i).text())
                    f.write('\n')

    def show_log_not_find(self):
        if not os.path.isfile("script18.log"):
            QtWidgets.QMessageBox.about(
                self, "Создание файла лога", "Файл лога не найден. Файл будет создан автоматически.")
            new_file = open("script18.log", "a")
            new_file.close()

    def watch_log(self):
        qm = QtWidgets.QMessageBox
        ret = QtWidgets.QMessageBox.question(
            self, 'Просмотр лога', "Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!", qm.Yes | qm.No)
        if ret == qm.Yes:
            self.ui.listWidget.clear()
            with open("script18.log", "r") as f:
                for i, line in enumerate(f):
                    self.ui.listWidget.addItem(line)
                filesize = f'{os.path.getsize("script18.log"): }'
                self.ui.label.setText(
                    f"Открыт Лог  | {filesize} байт")

    def export_data(self):
        file_path = QFileDialog.getSaveFileName(
            self, 'Save file', '/savefile', "Text file (*.txt)")[0]
        if file_path:
            with open(file_path, "w") as f:
                for i in range(self.ui.listWidget.count()):
                    f.write(self.ui.listWidget.item(i).text())
                    f.write('\n')


def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
