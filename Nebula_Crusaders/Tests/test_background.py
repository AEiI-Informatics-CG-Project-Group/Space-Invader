import unittest
from unittest.mock import patch
import pygame
from Game_running_package.background import BG


class TestBGInitialization(unittest.TestCase):

    @patch('pygame.Surface')
    def test_bg_initialization(self, MockSurface):
        # Mock the surface and its methods
        mock_surface_instance = MockSurface.return_value
        mock_surface_instance.get_rect.return_value = pygame.Rect(0, 0, 800, 600)

        # Create an instance of BG
        bg = BG()

        # Assertions to check the initialization
        MockSurface.assert_called_once_with((800, 600))
        self.assertEqual(bg.color, (0, 0, 15))
        mock_surface_instance.fill.assert_called_once_with((0, 0, 15))
        self.assertEqual(bg.rect, pygame.Rect(0, 0, 800, 600))


if __name__ == '__main__':
    unittest.main()