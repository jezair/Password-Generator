from PyQt5.QtWidgets import QApplication 
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random 

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.generator)

    def generator(self):
        signs = ""
        if self.ui.checkBox.isChecked():
            signs += "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        if self.ui.checkBox_2.isChecked():
            signs += "1234567890"
        
        result = ""
        number = random.randint(8, 20)
        for i in range(number):
            result += random.choice(signs)

        self.ui.label_2.setText(result)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()