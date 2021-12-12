import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QBoxLayout, QVBoxLayout, QListWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import *
from PyQt6 import uic
import pandas as pd


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.setWindowTitle('IMDB Database')
        self.setIconSize(QSize(800, 800))


        df = pd.read_csv('./CSVData/ActorsBio.csv')
        print(df)
        rows = []
        for i, row in df.iterrows():
            #Put the item into the widget
            item = QListWidgetItem()
            item.setIcon(QIcon('./ImagesActors/' + row['NameID']))
            item.setText(row['Name'])
            self.listWidget.addItem(item)


            

        


if __name__ == '__main__':

    app = QApplication(sys.argv)

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
