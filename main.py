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

        #sound
        main_sound = pygame.mixer.Sound('assets/sounds/main2.mp3')
        main_sound.set_volume(0.3)
        main_sound.play(loops = -1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.level.game_over:  # stopping game and printing 'GAME OVER'
                text_width = self.game_over_text.get_width()
                text_heigth = self.game_over_text.get_height()
                self.screen.blit(self.game_over_text, (WIDTH/2 - text_width/2, HEIGTH/2 - text_heigth/2))
                pygame.display.update()
            else:  # game runs normally
                self.screen.fill((32,32,32))
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)



if __name__ == '__main__':
    game = Game()
    game.run()
