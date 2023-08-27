import pygame
from settings import enemies_stats
from entity import Entity



class Enemy(Entity):
    def __init__(self, pos, groups, obstacle_sprites, images,  monster_type):

        # general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics setup
        self.images = images #dictionary with frames for each animation
        self.orientation = 'L'
        self.move_status = 'idle'
        self.image = self.images[self.move_status + '_' + self.orientation][self.frame_index]
        # check if attack state and animation is present, if not parts of code are not executed
        self.has_attack =  ('attack_L' in self.images.keys())

        # movement
        self.rect = self.image.get_rect(topleft=pos)
        # self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # stats
        self.monster_type= monster_type
        self.health = enemies_stats[self.monster_type]['hp']
        self.exp = enemies_stats[self.monster_type]['exp']
        self.speed = enemies_stats[self.monster_type]['speed']
        self.damage = enemies_stats[self.monster_type]['damage']
        self.aggro_radius = enemies_stats[self.monster_type]['aggro_radius']
        self.attack_radius = 10


        # player interaction
        self.can_be_attacked = True
        self.attack_time = None
        self.attack_cooldown = 200



    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_be_attacked and self.has_attack:
            if self.move_status != 'attack':
                self.frame_index = 0
            self.move_status = 'attack'
        elif distance <= self.aggro_radius:
            self.move_status = 'run'
        else:
            self.move_status = 'idle'

    def actions(self, player):
        if self.move_status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            print('attack')
        elif self.move_status == 'run':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()
        if self.direction[0] < 0:
            self.orientation = 'L'
        else:
            self.orientation = 'R'

    def animation(self):
        animation = self.images[self.move_status + '_' + self.orientation]
        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.move_status == 'attack':
                self.can_be_attacked = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        # self.rect = self.image.get_rect(center=self.hitbox.center)

    def cooldown(self):
        if not self.can_be_attacked:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_be_attacked = True

    def get_damage(self, damage, killer, direction):
        self.health -= damage
        self.attack_time = pygame.time.get_ticks()
        self.can_be_attacked = False
        if direction == 'up':
            self.rect.y += 7
        elif direction == 'down':
            self.rect.y -= 7
        elif direction == 'left':
            self.rect.x += 7
        else:
            self.rect.x -= 8
        print('enemy hit')
        if self.health <= 0:
            self.kill()
            killer.exp += self.exp

    def update(self):
        self.move(self.speed)
        self.animation()
        self.cooldown()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)