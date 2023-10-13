import sys
from PyQt5 import QtWidgets
from string_formatter import StringFormatter
from mydesign import Ui_MainWindow


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.format_btn.clicked.connect(self.handle_click)
        self.ui.sort_check.toggled.connect(self.on_sort_check_toggled)
        self.on_sort_check_toggled(self.ui.sort_check.isChecked())
        self.ui.word_len_check.toggled.connect(self.on_word_len_check_toggled)
        self.on_word_len_check_toggled(self.ui.word_len_check.isChecked())

    def on_word_len_check_toggled(self, checked):
        self.ui.word_len_box.setEnabled(checked)

    def on_sort_check_toggled(self, checked):
        self.ui.sort_for_lexic_btn.setEnabled(checked)
        self.ui.sort_for_len_btn.setEnabled(checked)

    def handle_click(self):
        input_str = self.ui.input_str.toPlainText()
        formatted_str = self.format(input_str=input_str)

        # self.ui.input_str.setText("")
        self.ui.result_str.setText(formatted_str)

    def format(self, input_str):
        formatter = StringFormatter()

        if self.ui.word_len_check.isChecked():
            word_len = self.ui.word_len_box.value()
            input_str = formatter.delete_words(input_str, word_len)

        if self.ui.replace_num_check.isChecked():
            input_str = formatter.swap_digits(input_str)

        if self.ui.space_between_check.isChecked():
            input_str = formatter.split_for_every_symbol(input_str)

        if self.ui.sort_check.isChecked():
            if self.ui.sort_for_lexic_btn.isChecked():
                return formatter.sort_for_lexicographic(input_str)
            else:
                return formatter.sort_for_word_len(input_str)

        return input_str


def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
