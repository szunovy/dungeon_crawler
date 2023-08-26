import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Dungeon Crawler')
        self.clock = pygame.time.Clock()
        self.level = Level()

        self.font = pygame.font.Font(font_path, text_size)
        self.game_over_text = self.font.render('Game Over', False, 'Red')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.level.game_over:
                text_width = self.game_over_text.get_width()
                text_heigth = self.game_over_text.get_height()
                self.screen.blit(self.game_over_text, (WIDTH/2 - text_width/2, HEIGTH/2 - text_heigth/2))
                pygame.display.update()
            else:
                self.screen.fill((32,32,32))
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)



if __name__ == '__main__':
    game = Game()
    game.run()









# import pygame
# import os
# import numpy as np
#
# BACKGROUND = pygame.image.load(os.path.join('assets', 'background.jpg'))
#
# FPS = 60
#
# HERO = pygame.image.load(os.path.join('assets', 'knight_R.png'))
# tile = pygame.image.load(os.path.join('assets', 'wall.png'))
#
# #hero dimensions: 16x28
# #each map block 32x32
# #map dimension: 800x640
#
#
#
# array = np.array(MAP)
# spawn = np.argwhere(array == 's')
#
# HERO_WIDTH = 16
# HERO_HEIGHT = 28
# VELOCITY = 2
#
# width, height = 800, 640
# window = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Dungeon Crawler game")
#
# def draw_walls(MAP):
#     for y, line in enumerate(MAP):
#         for x, symbol in enumerate(line):
#             if symbol == "w":
#                 window.blit(tile, (x * 32, y * 32))
#
#
# def draw_window(heroPos):
#
#     window.blit(HERO, (heroPos.x, heroPos.y))
#     pygame.display.update()
#
# def hero_movement(keyPressed, heroPos):
#     if keyPressed[pygame.K_LEFT]:
#         heroPos.x -= VELOCITY
#     if keyPressed[pygame.K_RIGHT]:
#         heroPos.x += VELOCITY
#     if keyPressed[pygame.K_UP]:
#         heroPos.y -= VELOCITY
#     if keyPressed[pygame.K_DOWN]:
#         heroPos.y += VELOCITY
#
# def main():
#     heroPos = pygame.Rect(spawn[0][1] * 32 + 8, spawn[0][0] * 32 - 2, HERO_WIDTH, HERO_HEIGHT)
#     clock = pygame.time.Clock()
#     isRunning = True
#     while isRunning:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                isRunning = False
#
#         keyPressed = pygame.key.get_pressed()
#         window.fill((0, 0, 0))
#         hero_movement(keyPressed, heroPos)
#         draw_walls(MAP)
#         draw_window(heroPos)
#
#
#     pygame.quit()
#
# if __name__ == "__main__":
#     main()
#     print(spawn[0][1])
