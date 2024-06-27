import unittest
from unittest.mock import patch, MagicMock
import pygame
from Game_running_package.messages_fullscreen import display_score


class TestMessageDisplay(unittest.TestCase):

    @patch('pygame.font.Font')
    @patch('pygame.display.get_surface')
    def test_display_score(self, mock_get_surface, mock_font):
        # Mock the display surface and font rendering
        mock_surface = MagicMock()
        mock_get_surface.return_value = mock_surface
        mock_font_instance = mock_font.return_value
        mock_text_surface = MagicMock()
        mock_font_instance.render.return_value = mock_text_surface

        # Call the display_score function
        display_score(100, 200, 12345)

        # Assertions to ensure the function works as expected
        mock_font.assert_called_once()
        mock_font_instance.render.assert_called_once_with('Score: 12345', True, (255, 255, 255))
        mock_surface.blit.assert_called_once_with(mock_text_surface, (100, 200))


if __name__ == '__main__':
    unittest.main()