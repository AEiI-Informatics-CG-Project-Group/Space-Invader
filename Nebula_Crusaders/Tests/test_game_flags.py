import unittest
from Game_running_package import game_flags


class TestGameFlags(unittest.TestCase):

    def test_initial_game_flags(self):
        # Test the initial state of game flags
        self.assertFalse(game_flags.game_over_flag)
        self.assertFalse(game_flags.game_running_flag)
        self.assertTrue(game_flags.game_first_run_flag)
        self.assertTrue(game_flags.user_enters_nickname_flag)
        self.assertFalse(game_flags.showing_leaderboard_flag)
        self.assertFalse(game_flags.incorrect_nickname_flag)

        # Bosses flags
        self.assertFalse(game_flags.asteroids_arrived_flag)
        self.assertFalse(game_flags.star_lord_arrived_flag)
        self.assertFalse(game_flags.bounty_hunter_arrived_flag)
        self.assertFalse(game_flags.ghast_of_the_void_arrived_flag)
        self.assertFalse(game_flags.galactic_devourer_arrived_flag)
        self.assertFalse(game_flags.boss_rush_arrived_flag1)
        self.assertFalse(game_flags.boss_rush_arrived_flag2)
        self.assertFalse(game_flags.boss_rush_arrived_flag3)
        self.assertFalse(game_flags.first_stardust_wave_flag)


if __name__ == '__main__':
    unittest.main()