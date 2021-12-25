import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
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
        for i, row in df.iterrows():
            #Put the item into the widget
            actor = QListWidgetItem()
            #set the icon with the image of the actor
            actor.setIcon(QIcon('./ImagesActors/' + row['NameID']))
            #set the name for the actor 
            actor.setText(row['Name'])
            self.listWidget.addItem(actor)
            
        self.listWidget.itemClicked.connect(self.actorClicked)
        
    def actorClicked(self, item):
        self.detailView = DetailView()
        # load the detail view
        uic.loadUi('DetailView.ui', self.detailView)

        actorsBio = pd.read_csv('./CSVData/ActorsBio.csv')
        index = self.listWidget.row(item)
        #get the clicked actor and from there get all the informations for the actor
        actorInfo = actorsBio.iloc[index]
        actorID = actorInfo['NameID']
        imagePath = "ImagesActors/" + actorID + ".jpg"
        actorName = actorInfo['Name']
        actorBio = actorInfo['Bios']

        #here is the execution of the different methods for the ifnormations in
        self.detailView.initContent(imagePath, actorID, actorName, actorBio)
        self.detailView.getGenreActor(actorID)
        self.detailView.getFilmography(actorID)
        self.detailView.getAwards(actorID)
        self.detailView.show()
        


if __name__ == '__main__':

    app = QApplication(sys.argv)

    myApp = MainPage()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
