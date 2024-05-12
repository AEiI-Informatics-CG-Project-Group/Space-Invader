import pygame


from Enemies_package.enemy import Enemy
from Enemies_package.Enemy_gun_package.enemy_gun import Enemy_gun

from Constants_package.constants import players, enemies, enemies_laser_guns, SCREEN_WIDTH, SCREEN_HEIGHT, SCALE


# Define the Ghast_of_the_void class
class Ghast_of_the_void(Enemy):
    def __init__(self, pos_x=SCREEN_HEIGHT/16, pos_y=SCREEN_HEIGHT/16, move_direction=1, first_in_colony=False):
        super().__init__()

        # Stats
        self.damage = 1
        self.hp = 150
        self.speed_x = 4 * SCALE
        self.speed_y = 0 * SCALE
        self.move_direction = move_direction
        self.first_in_colony = first_in_colony

        # Timer
        self.ghast_of_the_void_timer = 0

        # Image data
        self.width = 45 * SCALE
        self.height = 70 * SCALE
        self.color = '#652EA3'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.center = (self.pos_x, self.pos_y)

        # Audio
        self.audio = pygame.mixer.Sound("Additional_resources/Audio/ghast_of_the_void.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):

        if self.first_in_colony:
            self.rect.x += self.speed_x * self.move_direction * 2
        else:
            self.rect.x += self.speed_x * self.move_direction

        if self.rect.left >= SCREEN_WIDTH:
            self.speed_x = self.speed_x * -1
            ghast_of_the_void = Ghast_of_the_void(SCREEN_WIDTH - 50 * SCALE, 50 * SCALE, -1)
            enemies.add(ghast_of_the_void)
            self.rect.top += 100 * SCALE
            self.first_in_colony = False

        if self.rect.right <= 0:
            self.speed_x = self.speed_x * -1
            ghast_of_the_void = Ghast_of_the_void()
            enemies.add(ghast_of_the_void)
            self.rect.top += 100 * SCALE
            self.first_in_colony = False

        if self.rect.top >= SCREEN_WIDTH + 100:
            self.kill()

    def melee_attack_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def range_attack_service(self):
        if self.ghast_of_the_void_timer <= 0:
            enemy_laser_gun = Enemy_gun(self.rect.center, 0.2, 2000, 15, 15, 45, "#FE1E1E")
            enemies_laser_guns.add(enemy_laser_gun)
            self.ghast_of_the_void_timer = enemy_laser_gun.fire_rate
        self.ghast_of_the_void_timer += -100

    def hp_service(self):
        if self.hp <= 100:
            self.image.fill('#A3702E')
        if self.hp <= 50:
            self.image.fill('#A3402E')
