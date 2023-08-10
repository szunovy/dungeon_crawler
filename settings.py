# game setup
WIDTH = 1280
HEIGTH = 736
FPS = 60
TILESIZE = 32

MAP = [
        ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        ['w', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', 'w', ' ', 'w', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', 'w', ' ', 'w', ' ', ' ', ' ', 'w'],
        ['w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'w', 'w', 'w', 'w', 'w', ' ', 'w', ' ', 'w', 'w', 'w', 'w', 'w', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w'],
        ['w', ' ', ' ', ' ', 'w', 'w', 'w', ' ', 'w', 'w', 'w', 'w', 'w', 'w', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', 'w', ' ', ' ', 'w', ' ', ' ', 'w', ' ', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', ' ', 'w'],
        ['w', 'w', 'w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', 'w', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', 'w', ' ', ' ', ' ', ' ', 'w', 'w', 'w', 'w', 'w'],
        ['w', ' ', 'w', ' ', ' ', ' ', 'w', 'w', 'w', ' ', ' ', 'w', ' ', ' ', 'w', ' ', 'w', 'w', 'w', 'w', ' ', 'w', 'w', 'w', 'w', ' ', 'w', 'w', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', 'w', ' ', 'w'],
        ['w', ' ', ' ', ' ', ' ', 'w', 'w', ' ', 'w', 'w', ' ', 'w', 'w', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', 'w', 'w', 'w', 'w', ' ', 'w', ' ', 'w'],
        ['w', ' ', 'w', 'w', 'w', 'w', ' ', ' ', 'w', ' ', ' ', 'w', ' ', ' ', 'w', ' ', 'w', 'w', ' ', 'w', ' ', 'w', ' ', 'w', 'w', ' ', 'w', ' ', 'w', 'w', 'w', 'w', 'w', ' ', 'w', ' ', ' ', ' ', ' ', 'w'],
        ['w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', 'w', 'w', 'w', ' ', ' ', 'w', ' ', 'w', ' ', ' ', 'w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'w', 'w', ' ', 'w'],
        ['w', ' ', 'w', 'w', ' ', 'w', 'w', ' ', 'w', 'w', ' ', ' ', ' ', 'w', 'w', ' ', ' ', ' ', 'w', 'w', ' ', 'w', 'w', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'w', 'w', 'w', 'w', 'w', ' ', 'w', ' ', ' ', 'w'],
        ['w', ' ', 'w', ' ', ' ', 'w', ' ', ' ', ' ', 'w', 'w', 'w', ' ', ' ', 'w', ' ', 'w', 'w', 'w', ' ', ' ', ' ', 'w', 'w', 'w', ' ', 'w', 'w', 'w', 'w', 'w', ' ', ' ', ' ', 'w', 'w', 'w', 'w', 'w', 'w'],
        ['w', ' ', ' ', ' ', 'w', 'w', ' ', ' ', ' ', 'w', ' ', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'w', 'w'],
        ['w', 'w', 'w', ' ', ' ', 'w', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', 'w', ' ', 'w', 'w', 'w', ' ', ' ', ' ', 'w', 'w', 'w', ' ', 'w', 'w', 'w', ' ', 'w', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', 'w'],
        ['w', ' ', 'w', 'w', ' ', 'w', 'w', 'w', 'w', 'w', ' ', 'w', 'w', ' ', 'w', ' ', ' ', ' ', 'w', 'w', ' ', 'w', 'w', ' ', ' ', ' ', 'w', ' ', 'w', ' ', 'w', 'w', ' ', 'w', 'w', ' ', 'w', 'w', ' ', 'w'],
        ['w', ' ', 'w', ' ', ' ', 'w', ' ', ' ', ' ', 'w', ' ', ' ', 'w', ' ', 'w', 'w', 'w', ' ', ' ', 'w', ' ', 'w', ' ', ' ', 'w', 'w', 'w', ' ', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', 'w', ' ', ' ', 'w'],
        ['w', ' ', 'w', ' ', 'w', 'w', 'w', 'w', ' ', ' ', ' ', ' ', 'w', ' ', 'w', ' ', 'w', 'w', ' ', 'w', ' ', 'w', ' ', 'w', 'w', ' ', ' ', ' ', 'w', 'w', 'w', 'w', ' ', 'w', ' ', ' ', 'w', ' ', ' ', 'w'],
        ['w', ' ', 'w', ' ', ' ', 'w', ' ', 'w', ' ', 'w', 'w', ' ', 'w', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w', 'w', 'w', 'w', 'w', ' ', 'w'],
        ['w', ' ', ' ', ' ', 'w', 'w', ' ', 'w', 'w', ' ', 'w', ' ', 'w', 'w', 'w', ' ', 'w', 'w', 'w', 'w', ' ', 'w', 'w', 'w', 'w', ' ', 'w', 'w', ' ', 'w', 'w', 'w', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w'],
        ['w', 'w', ' ', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', 'w', 'w', ' ', ' ', 'w', ' ', 'w', ' ', ' ', ' ', 'w', 'w', ' ', 'w', 'w'],
        ['w', ' ', ' ', ' ', 'w', 'w', 'w', 'w', 'w', ' ', 'w', 'w', 'w', ' ', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', ' ', 'w', ' ', 'w', ' ', 'w', 'w', ' ', 'w', 'w', 'w', ' ', 'w', ' ', ' ', ' ', 'w'],
        ['w', ' ', ' ', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', ' ', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', ' ', 'w'],
        ['w', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', ' ', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'w'],
        ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        ]