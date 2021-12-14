import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QBoxLayout, QVBoxLayout, QListWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import *
from PyQt6 import uic
import pandas as pd
from DetailView import DetailView 


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainPage.ui', self)
        self.setWindowTitle('IMDB Database')
        self.setIconSize(QSize(800, 800))


        df = pd.read_csv('./CSVData/ActorsBio.csv')
        print(df)
        for i, row in df.iterrows():
            #Put the item into the widget
            actor = QListWidgetItem()
            actor.setIcon(QIcon('./ImagesActors/' + row['NameID']))
            actor.setText(row['Name'])
            self.listWidget.addItem(actor)
            
        self.listWidget.itemClicked.connect(self.actorClicked)
        
    def actorClicked(self, item):
        #self.showMinimized()
        self.detailView = DetailView()
        uic.loadUi('DetailView.ui', self.detailView)

        actorsBio = pd.read_csv('./CSVData/ActorsBio.csv')
        index = self.listWidget.row(item)
        actorInfo = actorsBio.iloc[index]
        actorID = actorInfo['NameID']
        imagePath = "ImagesActors/" + actorID + ".jpg"
        actorName = actorInfo['Name']
        actorBio = actorInfo['Bios']
        self.detailView.initContent(imagePath, actorID, actorName, actorBio)
        self.detailView.getGenreActor(actorID)
        self.detailView.getFilmography(actorID)
        self.detailView.show()
        


if __name__ == '__main__':

    app = QApplication(sys.argv)

    myApp = MainPage()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
