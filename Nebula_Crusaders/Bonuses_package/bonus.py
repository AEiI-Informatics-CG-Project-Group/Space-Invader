import pygame


from Constants_package.constants import SCREEN_HEIGHT


# Define the abstract Bonus class
class Bonus(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()

        # Stats
        self.speed = 2 * SCREEN_HEIGHT / 800
        self.score_bonus = 0

        # Image data
        self.color = '#000000'
        self.height = 0 * SCREEN_HEIGHT / 800
        self.width = 0 * SCREEN_HEIGHT / 800

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def movement_service(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT + 100:
            self.kill()

    def collision_with_player_service(self):
        pass

    def update(self):
        self.movement_service()
        self.collision_with_player_service()
