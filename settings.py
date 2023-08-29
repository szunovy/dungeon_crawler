import csv
from os import path
# game setup
WIDTH = 1280  # width of the screen
HEIGTH = 736  # heigth of the screen
FPS = 60  # frame rate, defines clock tick rate
TILESIZE = 32  # size of single tile of the map

font_path = path.join('assets', 'font', 'Pixeltype.ttf')  # path to the font in assets
text_size = 100  # size of big text

file = open('map.csv','r')
MAP = list(csv.reader(file,delimiter=",")) # list map loaded from file
file.close()

enemies_stats = {  # dictionary of stats for each enemy type
        'skeleton' : {
                'hp' : 100,
                'exp' : 10,
                'damage' : 5,
                'aggro_radius' : 200,
                'speed' : 1.5,
        },
        'orc': {
                'hp': 120,
                'exp': 20,
                'damage': 10,
                'aggro_radius': 200,
                'speed': 1,
        },
        'chort': {
                'hp': 200,
                'exp': 50,
                'damage': 10,
                'aggro_radius': 100,
                'speed': 1.5,
        },
        'big_demon': {
                'hp': 200,
                'exp': 100,
                'damage': 20,
                'aggro_radius': 100,
                'speed': 1,
        },
        'wizzard': {
                'hp': 100,
                'exp': 80,
                'damage': 15,
                'aggro_radius': 100,
                'speed': 1,
        },
}

player_stats = {  # dictionary of players character stats
        'hp': 100,
        'damage': 25,
        'speed': 2,
        'weapon': 'sword',
        'exp': 0,
}

