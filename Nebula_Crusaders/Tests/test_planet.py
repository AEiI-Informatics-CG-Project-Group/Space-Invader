import unittest
from unittest.mock import patch, MagicMock
import pygame
from Game_running_package.planet import Planet


class TestPlanetInitialization(unittest.TestCase):

    @patch('pygame.sprite.Sprite')
    def test_planet_initialization(self, MockSprite):
        # Mock groups
        mock_groups = pygame.sprite.Group()

        # Create an instance of Planet
        planet = Planet(mock_groups)

        # Assertions to check the initialization
        self.assertIsNotNone(planet.image)
        self.assertIsNotNone(planet.rect)
        self.assertIsInstance(planet, pygame.sprite.Sprite)

    @patch('pygame.sprite.Sprite')
    def test_planet_update(self, MockSprite):
        # Mock groups
        mock_groups = pygame.sprite.Group()

        # Create an instance of Planet
        planet = Planet(mock_groups)

        # Mock the method move
        planet.move = MagicMock()

        # Call the update method
        planet.update()

        # Assertion to check if move method was called during update
        planet.move.assert_called_once()


if __name__ == '__main__':
    unittest.main()