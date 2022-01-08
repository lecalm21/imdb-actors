from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6.QtGui import *
import pandas as pd


class DetailView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('IMDB Database')
    
    # get the name the 'about' and the image of the actor and show it
    def initContent(self, image, id, name, bio):
        pixmap = QPixmap(image)
        pixmap = pixmap.scaledToWidth(160)
        self.imageLabel.setPixmap(pixmap)
        self.nameLabel.setText("Name: " + name)
        self.bioText.setText(bio)
        

    # list the genres of the actor in thze detail view
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

    # get the filmography
    def getFilmography(self, id):
        filmography = pd.read_csv('./CSVData/FilmographyAnalysis.csv')
        filmography = filmography.drop_duplicates(subset='TitleID', keep='last')
        

        rows = []

        # iterate through the filmography and list the movies       
        for i, row in filmography.iterrows():
            if row['NameID'] == id:
                rows.append([row['TitleName'], row['Genre'], row['Year'], row['Rating']])
                actor = QListWidgetItem()
                actor.setText('Title: ' + row['TitleName'] + "  " + 'Genre: ' + row['Genre'] + "  " 
                    + 'Year: ' + str(row['Year']) + "  " + 'Rating: ' + str(row['Rating']))
                self.movieList.addItem(actor)


        # get the top 5 movies by  rating
        ratingFrame = pd.DataFrame(rows)
        ratingFrame.columns = ['TitleName', 'Genre', 'Year', 'Rating']
        averageRating = ratingFrame['Rating'].mean()
        self.avgLabel.setText('Average Rating: ' + str(round(averageRating, 3)))

        top5Movies = ratingFrame.sort_values(by=["Rating"], ascending=False).head(5)

        # iterate through the top 5 movies to show them
        for i, row in top5Movies.iterrows():
            actor = QListWidgetItem()
            actor.setText('Title: ' + row['TitleName'] + "  " + 'Genre: ' + row['Genre'] + "  " 
                + 'Year: ' + str(row['Year']) + "  " + 'Rating: ' + str(row['Rating']))
            self.topList.addItem(actor)


    # get the awards and show them
    def getAwards(self, id):
        awards = pd.read_csv('./CSVData/ActorsAwards.csv')
        awards = awards.drop_duplicates(subset='AwardName', keep='last')

        for i, row in awards.iterrows():
            actor = QListWidgetItem()
            actor.setText('Award: ' + row['AwardName'] + "  " + 'Year: ' + str(row['Year']))
            self.awardList.addItem(actor)

