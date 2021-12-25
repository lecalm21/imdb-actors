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
        self.nameLabel.setText("Name: " + name)
        self.bioText.setText(bio)
        

    def getGenreActor(self, id):
        filmography = pd.read_csv('./CSVData/FilmographyAnalysis.csv')
        rows = []
        genreActorText = ""
        for i, row in filmography.iterrows():
            if row['NameID'] == id:
                genre = row['Genre']
                rows.append(genre)
        
        uniqueGenres = pd.unique(rows).tolist()

        for genre in uniqueGenres:
            genreActorText = genreActorText + genre + " "
        
        self.genreLabel.setText("Genres: " + genreActorText)

    def getFilmography(self, id):
        filmography = pd.read_csv('./CSVData/FilmographyAnalysis.csv')
        filmography = filmography.drop_duplicates(subset='TitleID', keep='last')
        
        #self.filmTable.setColumnCount(5)
        #self.filmTable.setHorizontalHeaderLabels(['ID', 'TitleName', 'Genre', 'Year', 'Rating'])
        #self.filmTable.verticalHeader().setVisible(False)

        rows = []
        #for i, row in filmography.iterrows():
        #    if row['NameID'] == id:
                #self.filmTable.insertRow(i)
                #self.filmTable.setItem(i, 1, QTableWidgetItem(str(i+1)))
                #self.filmTable.setItem(i, 1, QTableWidgetItem(str(row['TitleName'])))
                #self.filmTable.setItem(i, 2, QTableWidgetItem(str(row['Genre'])))
                #self.filmTable.setItem(i, 3, QTableWidgetItem(str(row['Year'])))
                #self.filmTable.setItem(i, 4, QTableWidgetItem(str(row['Rating'])))
        
        #self.filmTable.resizeColumnsToContents()        
        
        for i, row in filmography.iterrows():
            if row['NameID'] == id:
                rows.append([row['TitleName'], row['Genre'], row['Year'], row['Rating']])
                actor = QListWidgetItem()
                actor.setText('Title: ' + row['TitleName'] + "  " + 'Genre: ' + row['Genre'] + "  " 
                    + 'Year: ' + str(row['Year']) + "  " + 'Rating: ' + str(row['Rating']))
                self.movieList.addItem(actor)


        ratingFrame = pd.DataFrame(rows)
        ratingFrame.columns = ['TitleName', 'Genre', 'Year', 'Rating']
        averageRating = ratingFrame['Rating'].mean()
        self.avgLabel.setText('Average Rating: ' + str(round(averageRating, 3)))

        top5Movies = ratingFrame.sort_values(by=["Rating"], ascending=False).head(5)

        for i, row in top5Movies.iterrows():
            actor = QListWidgetItem()
            actor.setText('Title: ' + row['TitleName'] + "  " + 'Genre: ' + row['Genre'] + "  " 
                + 'Year: ' + str(row['Year']) + "  " + 'Rating: ' + str(row['Rating']))
            self.topList.addItem(actor)


        #self.topTable.setColumnCount(5)
        #self.topTable.setHorizontalHeaderLabels(['ID', 'TitleName', 'Genre', 'Year', 'Rating'])
        #self.topTable.verticalHeader().setVisible(False)
        #for i, row in top5Movies.iterrows():
        #    self.topTable.insertRow(i)
        #    self.topTable.setItem(i, 0, QTableWidgetItem(str(i+1)))
        #    self.topTable.setItem(i, 1, QTableWidgetItem(str(row['TitleName'])))
        #    self.topTable.setItem(i, 2, QTableWidgetItem(str(row['Genre'])))
        #    self.topTable.setItem(i, 3, QTableWidgetItem(str(row['Year'])))
        #    self.topTable.setItem(i, 4, QTableWidgetItem(str(row['Rating'])))

        #self.topTable.resizeColumnsToContents()    



    
    def getAwards(self, id):
        awards = pd.read_csv('./CSVData/ActorsAwards.csv')
        awards = awards.drop_duplicates(subset='AwardName', keep='last')
        
        #self.awardsTable.setColumnCount(3)
        #self.awardsTable.setHorizontalHeaderLabels(['ID', 'AwardName', "Year"])
        #self.awardsTable.verticalHeader().setVisible(False)

        #for i, row in awards.iterrows():
        #    if row['NameID'] == id:
        #        self.awardsTable.insertRow(i)
        #        self.awardsTable.setItem(i, 0, QTableWidgetItem(str(i+1)))
        #        self.awardsTable.setItem(i, 1, QTableWidgetItem(row['AwardName']))
        #        self.awardsTable.setItem(i, 2, QTableWidgetItem(str(row['Year'])))

        for i, row in awards.iterrows():
            actor = QListWidgetItem()
            actor.setText('Award: ' + row['AwardName'] + "  " + 'Year: ' + str(row['Year']))
            self.awardList.addItem(actor)

