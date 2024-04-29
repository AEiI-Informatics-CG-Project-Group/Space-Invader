import pygame
import threading
import re

from Game_running_package.fonts import font_100, font_75, font_50, font_35

from Game_running_package.messages_fullscreen import display_score, display_timer, display_hp, display_leader_board, display_user_input_nickname, welcome_m, welcome_mR, nebula_m, nebula_mR, controls_m, \
    controls_mR, controls_m1, controls_mR1, controls_m1C, controls_mR1C, controls_m2, controls_mR2, controls_m2C, \
    controls_mR2C, controls_m3, controls_mR3, controls_m3C, controls_mR3C, to_play_m, to_play_mR, to_leave_m, \
    to_leave_mR, enter_nickname_m, enter_nickname_mR, incorrect_nickname, incorrect_nicknameR, leaderboard_m, \
    leaderboard_mR, to_play_leaderboard_m, to_play_leaderboard_mR

from Game_running_package.messages_windowed import display_scoreW, display_timerW, display_hpW, display_user_input_nicknameW, display_leader_boardW, welcome_mW,\
    welcome_mRW, nebula_mW, nebula_mRW, controls_mW, controls_mRW, controls_m1W, controls_mR1W, controls_m1CW, \
    controls_mR1CW, controls_m2W, controls_mR2W, controls_m2CW, controls_mR2CW, controls_m3W, controls_mR3W, \
    controls_m3CW, controls_mR3CW, to_play_mW, to_play_mRW, to_leave_mW, to_leave_mRW, enter_nickname_mW, \
    enter_nickname_mRW, incorrect_nicknameW, incorrect_nicknameRW, leaderboard_mW, leaderboard_mRW, \
    to_play_leaderboard_mW, to_play_leaderboard_mRW

from Constants_package.constants import players, enemies, SCREEN_WIDTH, SCREEN_HEIGHT, fullscreen_flag

from game_flags import game_over_flag, game_running_flag, game_first_run_flag, user_enters_nickname_flag, \
    incorrect_nickname_flag, asteroids_arrived_flag, first_stardust_wave_flag

from Player_package.player import Player

from Enemies_package.asteroid import Asteroid
from Enemies_package.stardust import Stardust

pygame.init()

# Game clock
clock = pygame.time.Clock()
SECOND = 60
game_timer = 0
game_score_timer = 0

# Player information
player_nickname = ''
player_score_map_input = {}
player_score_map_output = {}

# Screen
if fullscreen_flag:
    screen_background_position = (0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    background_graphics = pygame.image.load('Additional_resources/Graphics/background_f.png').convert()
else:
    screen_background_position = (0, 0)
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    background_graphics = pygame.image.load('Additional_resources/Graphics/background_w.png').convert()

pygame.display.set_caption('Nebula Crusaders')
pygame.mouse.set_visible(False)

# Game Audio
background_audio = pygame.mixer.Sound("Additional_resources/Audio/main_theme.mp3")
background_audio.play(loops=-1)
background_audio.set_volume(0.2)


# Welcome screen
def welcome_screen(fullscreen):
    if fullscreen:
        screen.blit(background_graphics, screen_background_position)
        screen.blit(welcome_m, welcome_mR)
        screen.blit(nebula_m, nebula_mR)
        screen.blit(controls_m, controls_mR)
        screen.blit(controls_m1, controls_mR1)
        screen.blit(controls_m1C, controls_mR1C)
        screen.blit(controls_m2, controls_mR2)
        screen.blit(controls_m2C, controls_mR2C)
        screen.blit(controls_m3, controls_mR3)
        screen.blit(controls_m3C, controls_mR3C)
        screen.blit(to_play_m, to_play_mR)
        screen.blit(to_leave_m, to_leave_mR)
    else:
        screen.blit(background_graphics, screen_background_position)
        screen.blit(welcome_mW, welcome_mRW)
        screen.blit(nebula_mW, nebula_mRW)
        screen.blit(controls_mW, controls_mRW)
        screen.blit(controls_m1W, controls_mR1W)
        screen.blit(controls_m1CW, controls_mR1CW)
        screen.blit(controls_m2W, controls_mR2W)
        screen.blit(controls_m2CW, controls_mR2CW)
        screen.blit(controls_m3W, controls_mR3W)
        screen.blit(controls_m3CW, controls_mR3CW)
        screen.blit(to_play_mW, to_play_mRW)
        screen.blit(to_leave_mW, to_leave_mRW)


# Gameplay HUD screen
def gameplay_HUD(fullscreen):
    if fullscreen:
        display_score(player.score, SCREEN_WIDTH / 2, 75, '#FCFCF4', font_100, screen)
        display_timer(game_timer, SCREEN_WIDTH / 2, 170, '#FCFCF4', font_75, screen)
        display_hp(player.hp, SCREEN_WIDTH - 180, SCREEN_HEIGHT - 60, '#FCFCF4', font_100, screen)
    else:
        display_scoreW(player.score, 640, 30, '#FCFCF4', font_50, screen)
        display_timerW(game_timer, 640, 70, '#FCFCF4', font_35, screen)
        display_hpW(player.hp, 1200, 765, '#FCFCF4', font_50, screen)


# Entering nickname screen
def enter_nickname_screen(fullscreen):
    if fullscreen:
        screen.blit(background_graphics, screen_background_position)
        screen.blit(enter_nickname_m, enter_nickname_mR)
        display_score(player.score, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 12, '#FCFCF4',
                      font_100, screen)
        display_user_input_nickname(player_nickname, SCREEN_WIDTH / 2,
                                    SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 10, '#FCFCF4', font_100, screen)
    else:
        screen.blit(background_graphics, screen_background_position)
        screen.blit(enter_nickname_mW, enter_nickname_mRW)
        display_scoreW(player.score, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 12, '#FCFCF4',
                       font_50, screen)
        display_user_input_nicknameW(player_nickname, SCREEN_WIDTH / 2,
                                     SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 10, '#FCFCF4', font_50, screen)


# Possible incorrect nickname message
def incorrect_nickname_message(fullscreen, incorrect):
    if incorrect:
        if fullscreen:
            screen.blit(incorrect_nickname, incorrect_nicknameR)
        else:
            screen.blit(incorrect_nicknameW, incorrect_nicknameRW)


# Leaderboard screen
def leaderboard_screen(fullscreen):
    if fullscreen:
        screen.blit(background_graphics, screen_background_position)
        screen.blit(leaderboard_m, leaderboard_mR)
        display_leader_board(SCREEN_WIDTH / 2 - SCREEN_WIDTH / 5 + SCREEN_WIDTH / 30, 300, '#FCFCF4',
                             player_score_map_output, font_75, screen)
        screen.blit(to_play_leaderboard_m, to_play_leaderboard_mR)
    else:
        screen.blit(background_graphics, screen_background_position)
        screen.blit(leaderboard_mW, leaderboard_mRW)
        display_leader_boardW(SCREEN_WIDTH / 2 - SCREEN_WIDTH / 5 + SCREEN_WIDTH / 30, 135, '#FCFCF4',
                              player_score_map_output, font_35, screen)
        screen.blit(to_play_leaderboard_mW, to_play_leaderboard_mRW)


def reset_game():
    enemies.empty()
    players.empty()


def draw_sprites():
    players.draw(screen)
    enemies.draw(screen)


def update_sprites():
    players.update()
    enemies.update()


reset_game_thread = threading.Thread(target=reset_game)
draw_sprites_thread = threading.Thread(target=draw_sprites)
update_sprites_thread = threading.Thread(target=update_sprites)

reset_game_thread.start()
draw_sprites_thread.start()
update_sprites_thread.start()

adding_enemies_mutex = threading.Lock()

while not game_over_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_flag = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over_flag = True

        if not game_running_flag:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_first_run_flag:
                reset_game()

                game_over_flag = False
                game_running_flag = False
                game_first_run_flag = True
                user_enters_nickname_flag = True
                showing_leaderboard_flag = False
                incorrect_nickname_flag = False
                asteroids_arrived_flag = False
                first_stardust_wave_flag = False

                game_timer = 0

                player = Player()
                players.add(player)

                game_running_flag = True
                game_first_run_flag = False
            else:
                if user_enters_nickname_flag:
                    if event.type == pygame.KEYDOWN and event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN and event.key != pygame.K_SPACE:
                        player_nickname += event.unicode
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                        player_nickname = player_nickname[:-1]
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                        nickname_pattern = re.compile(r'^[a-zA-Z0-9]{1,12}$')

                        if nickname_pattern.match(player_nickname):
                            player_score_map_input = {player_nickname: player.score}

                            with open("Leaderboard.txt", "a") as f:
                                for key, value in player_score_map_input.items():
                                    f.write(key + ":" + str(value) + "\n")

                            player_score_map_input.clear()
                            player_nickname = ''

                            user_enters_nickname_flag = False
                            incorrect_nickname_flag = False
                        else:
                            player_nickname = ''
                            incorrect_nickname_flag = True
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        reset_game()

                        game_over_flag = False
                        game_running_flag = False
                        game_first_run_flag = True
                        user_enters_nickname_flag = True
                        showing_leaderboard_flag = False
                        incorrect_nickname_flag = False
                        asteroids_arrived_flag = False
                        first_stardust_wave_flag = False

                        game_timer = 0

                        player = Player()
                        players.add(player)

                        user_enters_nickname_flag = True
                        game_first_run_flag = False
                        game_running_flag = True
    if game_running_flag:
        screen.blit(background_graphics, screen_background_position)
        draw_sprites()
        update_sprites()
        gameplay_HUD(fullscreen_flag)

        # is Player alive
        if not players:
            game_running_flag = False

        # Timer
        game_timer += 1

        # Score update
        game_score_timer += 1
        if game_score_timer >= 180 and player.score > 0:
            player.score += -10
            game_score_timer = 0

        # Game script
        if game_timer >= 1 * SECOND and not asteroids_arrived_flag:
            asteroids_arrived_flag = True
            for i in range(5):
                asteroid = Asteroid()
                adding_enemies_mutex.acquire()
                enemies.add(asteroid)
                adding_enemies_mutex.release()

        if game_timer >= 30 * SECOND and not first_stardust_wave_flag:
            first_stardust_wave_flag = True
            for i in range(50):
                stardust = Stardust()
                adding_enemies_mutex.acquire()
                enemies.add(stardust)
                adding_enemies_mutex.release()

        if game_timer >= 360 * SECOND:
            game_running_flag = False

    else:
        if game_first_run_flag:
            welcome_screen(fullscreen_flag)
        else:
            if user_enters_nickname_flag:
                enter_nickname_screen(fullscreen_flag)
                incorrect_nickname_message(fullscreen_flag, incorrect_nickname_flag)
            else:
                leaderboard_screen(fullscreen_flag)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
