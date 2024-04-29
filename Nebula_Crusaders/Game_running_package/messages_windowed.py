import pygame
import itertools


from Game_running_package.fonts import font_60, font_50, font_40, font_30
from Constants_package.constants import SCREEN_WIDTH, SCREEN_HEIGHT


# Display score (Windowed)
def display_scoreW(score, pos_x, pos_y, color, font, screen):
    score_surf = font.render(f'SCORE:{score}', False, color)
    score_rect = score_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(score_surf, score_rect)


# Display score (Windowed)
def display_timerW(timer, pos_x, pos_y, color, font, screen):
    timer_surf = font.render(f'TIME:{round(timer / 60, 1)}', False, color)
    timer_rect = timer_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(timer_surf, timer_rect)


# Display HP (Windowed)
def display_hpW(hp, pos_x, pos_y, color, font, screen):
    hp_surf = font.render(f'HP:{round(hp, 2)}', False, color)
    hp_rect = hp_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(hp_surf, hp_rect)


# Display stats (Windowed)
def display_statsW(speed, damage, fire_rate, pos_x, pos_y, color, font, screen):
    damage_surf = font.render(f'DMG:{round(damage, 2)}', False, color)
    damage_rect = damage_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(damage_surf, damage_rect)

    fire_rate_surf = font.render(f'FIRE RATE:{round(1 / fire_rate, 2)}', False, color)
    fire_rate_rect = fire_rate_surf.get_rect(center=(pos_x, pos_y + 28))
    screen.blit(fire_rate_surf, fire_rate_rect)

    speed_surf = font.render(f'SPEED:{round(speed, 2)}', False, color)
    speed_rect = speed_surf.get_rect(center=(pos_x, pos_y + 56))
    screen.blit(speed_surf, speed_rect)


# Display gun type (Windowed)
def display_gunW(gun_type, pos_x, pos_y, color, font, screen):
    gun_surf = font.render(f'GUN:{gun_type}', False, color)
    gun_rect = gun_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(gun_surf, gun_rect)


# Graphical availability of guns (Windowed)
def display_gun_availabilityW(gun_1, gun_2, gun_3, gun_4, gun_5, gun_6, screen):
    gun_1_image = pygame.Surface([15, 15])
    if gun_1:
        gun_1_image.fill('#60a05b')
    else:
        gun_1_image.fill('#e40b00')
    gun_1_image_rect = gun_1_image.get_rect()
    gun_1_image_rect.x = SCREEN_WIDTH / 2 - 50
    gun_1_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_1_image, gun_1_image_rect)

    gun_2_image = pygame.Surface([15, 15])
    if gun_2:
        gun_2_image.fill('#60a05b')
    else:
        gun_2_image.fill('#e40b00')
    gun_2_image_rect = gun_2_image.get_rect()
    gun_2_image_rect.x = SCREEN_WIDTH / 2 - 30
    gun_2_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_2_image, gun_2_image_rect)

    gun_3_image = pygame.Surface([15, 15])
    if gun_3:
        gun_3_image.fill('#60a05b')
    else:
        gun_3_image.fill('#e40b00')
    gun_3_image_rect = gun_3_image.get_rect()
    gun_3_image_rect.x = SCREEN_WIDTH / 2 - 10
    gun_3_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_3_image, gun_3_image_rect)

    gun_4_image = pygame.Surface([15, 15])
    if gun_4:
        gun_4_image.fill('#60a05b')
    else:
        gun_4_image.fill('#e40b00')
    gun_4_image_rect = gun_4_image.get_rect()
    gun_4_image_rect.x = SCREEN_WIDTH / 2 + 10
    gun_4_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_4_image, gun_4_image_rect)

    gun_5_image = pygame.Surface([15, 15])
    if gun_5:
        gun_5_image.fill('#60a05b')
    else:
        gun_5_image.fill('#e40b00')
    gun_5_image_rect = gun_5_image.get_rect()
    gun_5_image_rect.x = SCREEN_WIDTH / 2 + 30
    gun_5_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_5_image, gun_5_image_rect)

    gun_6_image = pygame.Surface([15, 15])
    if gun_6:
        gun_6_image.fill('#60a05b')
    else:
        gun_6_image.fill('#e40b00')
    gun_6_image_rect = gun_6_image.get_rect()
    gun_6_image_rect.x = SCREEN_WIDTH / 2 + 50
    gun_6_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_6_image, gun_6_image_rect)


# Display user input nickname (Windowed)
def display_user_input_nicknameW(nickname, pos_x, pos_y, color, font, screen):
    nickname_surf = font.render(f'{nickname}', False, color)
    nickname_rect = nickname_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(nickname_surf, nickname_rect)


# Display score (Windowed)
def display_leader_boardW(pos_x, pos_y, color, player_score_map_output, font, screen):
    with open("Leaderboard.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                key, value = line.split(":")
                player_score_map_output[key] = int(value)

    sorted_player_score_map_output = dict(sorted(player_score_map_output.items(), key=lambda x: x[1], reverse=True))

    for i, (key, value) in enumerate(itertools.islice(sorted_player_score_map_output.items(), 10)):
        if i < 9:
            text = f"{i + 1}.  {key} {value}"
            text_surface = font.render(text, True, color)
            screen.blit(text_surface, (pos_x, i * 50 + pos_y))
        else:
            text = f"{i + 1}. {key} {value}"
            text_surface = font.render(text, True, color)
            screen.blit(text_surface, (pos_x, i * 50 + pos_y))
        if i == 9:
            break


# Boss announcements (Windowed)
warning_mW = font_60.render('!!! WARNING WARNING WARNING !!!', False, '#FCFCF4')
warning_mRW = warning_mW.get_rect(center=(SCREEN_WIDTH / 2, 175))
star_lord_announcement_mW = font_30.render('Star lord has detected our presence in space', False, '#FCFCF4')
star_lord_announcement_mRW = star_lord_announcement_mW.get_rect(center=(SCREEN_WIDTH / 2, 225))
bounty_hunter_announcement_mW = font_30.render('Bounty hunter?\'s engines make the air vibrate', False, '#FCFCF4')
bounty_hunter_announcement_mRW = bounty_hunter_announcement_mW.get_rect(center=(SCREEN_WIDTH / 2, 225))
ghast_of_the_void_announcement_mW = font_30.render('The swarm queen is seen on the radar', False, '#FCFCF4')
ghast_of_the_void_announcement_mRW = ghast_of_the_void_announcement_mW.get_rect(center=(SCREEN_WIDTH / 2, 225))
galactic_devourer_announcement_mW = font_30.render('Unexplained anomaly ahead', False, '#FCFCF4')
galactic_devourer_announcement_mRW = galactic_devourer_announcement_mW.get_rect(center=(SCREEN_WIDTH / 2, 225))
galactic_devourer_announcement_m2W = font_60.render('WHAT IS IT???', False, '#FCFCF4')
galactic_devourer_announcement_mR2W = galactic_devourer_announcement_m2W.get_rect(center=(SCREEN_WIDTH / 2, 315))
boss_rush_announcement_mW = font_60.render('THAT\'S BOSS RUSH', False, '#FCFCF4')
boss_rush_announcement_mRW = boss_rush_announcement_mW.get_rect(center=(SCREEN_WIDTH / 2, 225))


# Game messages (Windowed)
welcome_mW = font_50.render('Welcome to', False, '#FCFCF4')
welcome_mRW = welcome_mW.get_rect(center=(SCREEN_WIDTH / 2, 150))

nebula_mW = font_50.render('Nebula Crusaders', False, '#FCFCF4')
nebula_mRW = nebula_mW.get_rect(center=(SCREEN_WIDTH / 2, 200))

controls_mW = font_50.render('CONTROLS:', False, '#FCFCF4')
controls_mRW = controls_mW.get_rect(center=(SCREEN_WIDTH / 2, 375))

controls_m1W = font_30.render('Movement:', False, '#FCFCF4')
controls_mR1W = controls_m1W.get_rect(center=(380, 425))

controls_m1CW = font_30.render('< ↑ > ↓', False, '#FCFCF4')
controls_mR1CW = controls_m1CW.get_rect(center=(380, 475))

controls_m2W = font_30.render('Switching guns:', False, '#FCFCF4')
controls_mR2W = controls_m2W.get_rect(center=(SCREEN_WIDTH / 2, 425))

controls_m2CW = font_30.render('1 2 3 4 5 6', False, '#FCFCF4')
controls_mR2CW = controls_m2CW.get_rect(center=(SCREEN_WIDTH / 2, 475))

controls_m3W = font_30.render('Shooting:', False, '#FCFCF4')
controls_mR3W = controls_m3W.get_rect(center=(900, 425))

controls_m3CW = font_30.render('SPACE', False, '#FCFCF4')
controls_mR3CW = controls_m3CW.get_rect(center=(900, 475))

to_play_mW = font_50.render('Press SPACE to play!', False, '#FCFCF4')
to_play_mRW = to_play_mW.get_rect(center=(SCREEN_WIDTH / 2, 600))

to_leave_mW = font_40.render('Press ESC to leave game at any time', False, '#FCFCF4')
to_leave_mRW = to_leave_mW.get_rect(center=(SCREEN_WIDTH / 2, 700))

to_play_leaderboard_mW = font_60.render('Press SPACE to play!', False, '#FCFCF4')
to_play_leaderboard_mRW = to_play_leaderboard_mW.get_rect(center=(SCREEN_WIDTH / 2, 700))

enter_nickname_mW = font_60.render('Enter your nickname:', False, '#FCFCF4')
enter_nickname_mRW = enter_nickname_mW.get_rect(center=(SCREEN_WIDTH / 2, 230))

leaderboard_mW = font_60.render('Leaderboard:', False, '#FCFCF4')
leaderboard_mRW = leaderboard_mW.get_rect(center=(SCREEN_WIDTH / 2, 100))

incorrect_nicknameW = font_60.render('INCORRECT NICKNAME', False, '#FF0000')
incorrect_nicknameRW = incorrect_nicknameW.get_rect(center=(SCREEN_WIDTH / 2, 700))
