from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QBoxLayout, QVBoxLayout, QTableWidgetItem, QListWidgetItem, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import *
from PyQt6 import uic
import pandas as pd


class DetailView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('IMDB Database')
    
    def initContent(self, image, id, name, bio):
        pixmap = QPixmap(image)
        pixmap = pixmap.scaledToWidth(160)
        self.imageLabel.setPixmap(pixmap)
        self.nameLabel.setText(name)
        self.bioText.setText(bio)
        

    def getGenreActor(self, id):
        filmography = pd.read_csv('./CSVData/FilmographyAnalysis.csv')
        rows = []
        genreActorText = ""
        print(filmography)
        for i, row in filmography.iterrows():
            if row['NameID'] == id:
                genre = row['Genre']
                rows.append(genre)
        
        uniqueGenres = pd.unique(rows).tolist()

        for genre in uniqueGenres:
            genreActorText = genreActorText + genre + " "
        
        self.genreLabel.setText(genreActorText)

    def getFilmography(self, id):
        filmography = pd.read_csv('./CSVData/FilmographyAnalysis.csv')
        
        for i, row in filmography.iterrows():
            if row['NameID'] == id:
                print(row['TitleName'])
                filmItem = [row['TitleName'], row['Genre'], row['Year'], row['Rating']]
                tableItem = QTableWidgetItem(filmItem)
                self.filmography.setItem(tableItem)


