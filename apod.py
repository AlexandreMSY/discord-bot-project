import requests
import urllib

class apod:
    def __init__(self, year, month, day): #sets the date

        self.year = year
        self.month = month
        self.day = day
        
        self.date = f'{self.year}-{self.month}-{self.day}'
    
    def getApod(self):

        parameters = {
            'date' : self.date
        }

        api = requests.get('https://api.nasa.gov/planetary/apod?api_key=1px7yIQ6EHwE37otI91bCo8NI2qHwUChM2Z9JTam', params= parameters)
        nasa = api.json()
        
        text = 'Title = ' + nasa['title'] + "\n" + 'Date = ' + nasa['date']  + '\n' + '\n' + 'Explanation = ' + nasa['explanation'] + "\n" + nasa['hdurl']
        
        return text
    
    #experimental
    def apodIMG(self):

        parameters = {
            'date' : self.date
        }

        api = requests.get('https://api.nasa.gov/planetary/apod?api_key=1px7yIQ6EHwE37otI91bCo8NI2qHwUChM2Z9JTam', params= parameters)
        nasa = api.json()

        try:
            urllib.request.urlretrieve(nasa['hdurl'], 'apodIMG.jpg') #downloads the image from the URL
        
        except KeyError:
            urllib.request.urlretrieve(nasa['url'], 'apodIMG.jpg')

    