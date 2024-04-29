import pygame
import itertools

from Game_running_package.fonts import font_125, font_75, font_50
from Constants_package.constants import SCREEN_WIDTH, SCREEN_HEIGHT


# Display score (Fullscreen)
def display_score(score, pos_x, pos_y, color, font, screen):
    score_surf = font.render(f'SCORE:{score}', False, color)
    score_rect = score_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(score_surf, score_rect)


# Display gun type (Fullscreen)
def display_timer(timer, pos_x, pos_y, color, font, screen):
    timer_surf = font.render(f'TIME:{round(timer / 60, 1)}', False, color)
    timer_rect = timer_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(timer_surf, timer_rect)


# Display HP (Fullscreen)
def display_hp(hp, pos_x, pos_y, color, font, screen):
    hp_surf = font.render(f'HP:{round(hp, 2)}', False, color)
    hp_rect = hp_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(hp_surf, hp_rect)


# Display Stats (Fullscreen)
def display_stats(speed, damage, fire_rate, pos_x, pos_y, color, font, screen):
    damage_surf = font.render(f'DMG:{round(damage, 2)}', False, color)
    damage_rect = damage_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(damage_surf, damage_rect)

    fire_rate_surf = font.render(f'FIRE RATE:{round(1 / fire_rate, 2)}', False, color)
    fire_rate_rect = fire_rate_surf.get_rect(center=(pos_x, pos_y + 65))
    screen.blit(fire_rate_surf, fire_rate_rect)

    speed_surf = font.render(f'SPEED:{round(speed, 2)}', False, color)
    speed_rect = speed_surf.get_rect(center=(pos_x, pos_y + 130))
    screen.blit(speed_surf, speed_rect)


# Display gun type (Fullscreen)
def display_gun(gun_type, pos_x, pos_y, color, font, screen):
    gun_surf = font.render(f'GUN:{gun_type}', False, color)
    gun_rect = gun_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(gun_surf, gun_rect)


# Graphical availability of guns (Fullscreen)
def display_gun_availability(gun_1, gun_2, gun_3, gun_4, gun_5, gun_6, screen):
    gun_1_image = pygame.Surface([30, 30])
    if gun_1:
        gun_1_image.fill('#60a05b')
    else:
        gun_1_image.fill('#e40b00')
    gun_1_image_rect = gun_1_image.get_rect()
    gun_1_image_rect.x = SCREEN_WIDTH / 2 - 100
    gun_1_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_1_image, gun_1_image_rect)

    gun_2_image = pygame.Surface([30, 30])
    if gun_2:
        gun_2_image.fill('#60a05b')
    else:
        gun_2_image.fill('#e40b00')
    gun_2_image_rect = gun_2_image.get_rect()
    gun_2_image_rect.x = SCREEN_WIDTH / 2 - 60
    gun_2_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_2_image, gun_2_image_rect)

    gun_3_image = pygame.Surface([30, 30])
    if gun_3:
        gun_3_image.fill('#60a05b')
    else:
        gun_3_image.fill('#e40b00')
    gun_3_image_rect = gun_3_image.get_rect()
    gun_3_image_rect.x = SCREEN_WIDTH / 2 - 20
    gun_3_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_3_image, gun_3_image_rect)

    gun_4_image = pygame.Surface([30, 30])
    if gun_4:
        gun_4_image.fill('#60a05b')
    else:
        gun_4_image.fill('#e40b00')
    gun_4_image_rect = gun_4_image.get_rect()
    gun_4_image_rect.x = SCREEN_WIDTH / 2 + 20
    gun_4_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_4_image, gun_4_image_rect)

    gun_5_image = pygame.Surface([30, 30])
    if gun_5:
        gun_5_image.fill('#60a05b')
    else:
        gun_5_image.fill('#e40b00')
    gun_5_image_rect = gun_5_image.get_rect()
    gun_5_image_rect.x = SCREEN_WIDTH / 2 + 60
    gun_5_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_5_image, gun_5_image_rect)

    gun_6_image = pygame.Surface([30, 30])
    if gun_6:
        gun_6_image.fill('#60a05b')
    else:
        gun_6_image.fill('#e40b00')
    gun_6_image_rect = gun_6_image.get_rect()
    gun_6_image_rect.x = SCREEN_WIDTH / 2 + 100
    gun_6_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_6_image, gun_6_image_rect)


# Display user input nickname (Fullscreen)
def display_user_input_nickname(nickname, pos_x, pos_y, color, font, screen):
    nickname_surf = font.render(f'{nickname}', False, color)
    nickname_rect = nickname_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(nickname_surf, nickname_rect)


def display_leader_board(pos_x, pos_y, color, player_score_map_output, font, screen):
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
            screen.blit(text_surface, (pos_x, i * 100 + pos_y))
        else:
            text = f"{i + 1}. {key} {value}"
            text_surface = font.render(text, True, color)
            screen.blit(text_surface, (pos_x, i * 100 + pos_y))
        if i == 9:
            break


# Boss announcements (Fullscreen)
warning_m = font_125.render('!!! WARNING WARNING WARNING !!!', False, '#FCFCF4')
warning_mR = warning_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
star_lord_announcement_m = font_75.render('Star lord has detected our presence in space', False, '#FCFCF4')
star_lord_announcement_mR = star_lord_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))
bounty_hunter_announcement_m = font_75.render('Bounty hunter?\'s engines make the air vibrate', False, '#FCFCF4')
bounty_hunter_announcement_mR = bounty_hunter_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))
ghast_of_the_void_announcement_m = font_75.render('The swarm queen is seen on the radar', False, '#FCFCF4')
ghast_of_the_void_announcement_mR = ghast_of_the_void_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))
galactic_devourer_announcement_m = font_75.render('Unexplained anomaly ahead', False, '#FCFCF4')
galactic_devourer_announcement_mR = galactic_devourer_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))
galactic_devourer_announcement_m2 = font_125.render('WHAT IS IT???', False, '#FCFCF4')
galactic_devourer_announcement_mR2 = galactic_devourer_announcement_m2.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 6))
boss_rush_announcement_m = font_125.render('THAT\'S BOSS RUSH', False, '#FCFCF4')
boss_rush_announcement_mR = boss_rush_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))

# Game messages (Fullscreen)
welcome_m = font_125.render('Welcome to', False, '#FCFCF4')
welcome_mR = welcome_m.get_rect(center=(SCREEN_WIDTH / 2, 200))

nebula_m = font_125.render('Nebula Crusaders', False, '#FCFCF4')
nebula_mR = nebula_m.get_rect(center=(SCREEN_WIDTH / 2, 300))

controls_m = font_125.render('CONTROLS:', False, '#FCFCF4')
controls_mR = controls_m.get_rect(center=(SCREEN_WIDTH / 2, 650))

controls_m1 = font_75.render('Movement:', False, '#FCFCF4')
controls_mR1 = controls_m1.get_rect(center=(700, 750))

controls_m1C = font_75.render('< ↑ > ↓', False, '#FCFCF4')
controls_mR1C = controls_m1C.get_rect(center=(700, 850))

controls_m2 = font_75.render('Switching guns:', False, '#FCFCF4')
controls_mR2 = controls_m2.get_rect(center=(SCREEN_WIDTH / 2, 750))

controls_m2C = font_75.render('1 2 3 4 5 6', False, '#FCFCF4')
controls_mR2C = controls_m2C.get_rect(center=(SCREEN_WIDTH / 2, 850))

controls_m3 = font_75.render('Shooting:', False, '#FCFCF4')
controls_mR3 = controls_m3.get_rect(center=(1860, 750))

controls_m3C = font_75.render('SPACE', False, '#FCFCF4')
controls_mR3C = controls_m3C.get_rect(center=(1860, 850))

to_play_m = font_125.render('Press SPACE to play!', False, '#FCFCF4')
to_play_mR = to_play_m.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT * 3 / 4)))

to_leave_m = font_50.render('Press ESC to leave game at any time', False, '#FCFCF4')
to_leave_mR = to_leave_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100))

play_again_m = font_125.render('Press SPACE to play again!', False, '#FCFCF4')
play_again_mR = play_again_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))

to_play_leaderboard_m = font_125.render('Press SPACE to play!', False, '#FCFCF4')
to_play_leaderboard_mR = to_play_leaderboard_m.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT - 150)))

enter_nickname_m = font_125.render('Enter your nickname:', False, '#FCFCF4')
enter_nickname_mR = enter_nickname_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))

leaderboard_m = font_125.render('Leaderboard:', False, '#FCFCF4')
leaderboard_mR = leaderboard_m.get_rect(center=(SCREEN_WIDTH / 2, 100))

incorrect_nickname = font_125.render('INCORRECT NICKNAME', False, '#FF0000')
incorrect_nicknameR = incorrect_nickname.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 4))
