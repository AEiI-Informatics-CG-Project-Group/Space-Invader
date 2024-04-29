import pygame


from Constants_package.constants import players, SCALE


# Define the abstract Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Stats
        self.damage = 0
        self.hp = 0
        self.speed_x = 0 * SCALE
        self.speed_y = 0 * SCALE

        # Image data
        self.width = 0 * SCALE
        self.height = 0 * SCALE
        self.color = '#000000'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = self.width
        self.rect.y = self.height

    def movement_service(self):
        pass

    def melee_attack_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def range_attack_service(self):
        pass

    def hp_service(self):
        pass

    def update(self):
        self.movement_service()
        self.melee_attack_service()
        self.range_attack_service()
        self.hp_service()
