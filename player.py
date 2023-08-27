import pygame
from os import walk
import files_handling
from settings import player_stats

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, enemy_sprites):
        super().__init__(groups)
        # self.images = {}

        self.images = files_handling.load_images('player', 0)
        self.sword_texture = pygame.image.load('./assets/player/weapons/weapon_knight_sword.png')
        self.sword = None

        # for animation_set in self.images.keys():
        #     path = './assets/player/' + animation_set
        #     for _,__,frames_names in walk(path):
        #         for frame_name in frames_names:
        #             # all images in assets faces right so a flip is needed
        #             if animation_set[-1] == "L":
        #                 frame = pygame.transform.flip(pygame.image.load('./assets/frames/' + frame_name).convert_alpha(), 1, 0)
        #             else:
        #                 frame = pygame.image.load('./assets/frames/' + frame_name).convert_alpha()
        #             self.images[animation_set].append(frame)
        # stats

        self.speed = player_stats['speed']
        self.hp = player_stats['hp']
        self.damage = player_stats['damage']
        self.weapon = player_stats['weapon']
        self.exp = player_stats['exp']

        self.image = self.images['idle_L'][0]
        self.rect = self.image.get_rect(topleft = pos)
        self.orientation = 'L'
        self.move_status = 'idle'
        self.frame_index = 0

        self.screen = pygame.display.get_surface()

        self.animation_speed = 0.10
        self.obstacle_sprites = obstacle_sprites
        self.enemy_sprites = enemy_sprites
        # self.hitbox = self.rect
        self.direction = pygame.math.Vector2()

        self.invulnerable = False
        self.invulnerability_duration = 600
        self.hit_time = None

        self.attack_cooldown = False
        self.attack_cooldown_duration = 300
        self.attack_direction = 'U'
        self.attacking = False
        self.begin_attack = False
        self.attack_animation_duration = 150
        self.attack_orientation = self.orientation
    def input(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.attacking:
            self.begin_attack = True
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.attack_orientation = 'U'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.attack_orientation = 'D'
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.orientation = 'R'
            self.attack_orientation = 'R'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.attack_orientation = 'L'
        else:
            self.direction.x = 0


    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.move_status = 'run'
            self.direction = self.direction.normalize()
        else:
            self.move_status = 'idle'

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')


    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # moving left
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # moving up
                        self.rect.top = sprite.rect.bottom


    def animation(self):
        animation = self.images[self.move_status + '_' + self.orientation]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        # self.rect = self.image.get_rect(topleft = pos)

    def get_damage(self, enemy):
        self.hp -= enemy.damage
        self.invulnerable = True
        self.hit_time = pygame.time.get_ticks()
        print('player hit')

    def attack(self):
        if not self.attack_cooldown and self.begin_attack:
            self.begin_attack = False
            self.attacking = True
            self.attack_cooldown = True
            self.attack_time = pygame.time.get_ticks()
            if self.orientation == "R" and not self.direction.y:
                self.attack_direction = self.attack_orientation
            elif self.orientation == "L" and not self.direction.y:
                # self.sword = self.screen.blit(pygame.transform.rotate(self.sword_texture, 90), [self.rect.x - 24, self.rect.y + 16])
                self.attack_direction = self.attack_orientation
            elif self.direction.y > 0:
                # self.sword = self.screen.blit(pygame.transform.rotate(self.sword_texture, 180), [self.rect.x + 4, self.rect.y + 16])
                self.attack_direction = self.attack_orientation
            elif self.direction.y < 0:
                # self.sword = self.screen.blit(self.sword_texture, [self.rect.x + 4, self.rect.y - 16])
                self.attack_direction = self.attack_orientation
            print(self.attack_direction)


    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.invulnerable:
            if current_time - self.hit_time >= self.invulnerability_duration:
                self.invulnerable = False

        if self.attack_cooldown:
            if current_time - self.attack_time >= self.attack_cooldown_duration:
                self.attack_cooldown = False


        if self.attacking:
            if current_time - self.attack_time <= self.attack_animation_duration:
                print('wepon on')
                self.create_weapon()
            else:
                self.attacking = False

    def update(self):
        self.animation()
        self.input()
        self.move(self.speed)
        self.cooldowns()

    def create_weapon(self):
        print('create weapon')
        if self.attack_direction == 'R':
            self.sword = self.screen.blit(pygame.transform.rotate(self.sword_texture, 270),
                                      [self.rect.x + 12, self.rect.y + 16])
        if self.attack_direction == 'L':
            self.sword = self.screen.blit(pygame.transform.rotate(self.sword_texture, 90),
                                          [self.rect.x - 24, self.rect.y + 16])
        if self.attack_direction == 'D':
            self.sword = self.screen.blit(pygame.transform.rotate(self.sword_texture, 180),
                                          [self.rect.x + 4, self.rect.y + 16])
        if self.attack_direction == 'U':
            self.sword = self.screen.blit(self.sword_texture, [self.rect.x + 4, self.rect.y - 16])

