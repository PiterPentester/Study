import pygame
from settings import Settings
from ship import Ship
import game_function as g_f
from pygame.sprite import Group

def init_game():
    pygame.init()

    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    ship = Ship(screen)
    pygame.display.set_caption("Mine Game")
    bullets = Group()
    while True:
        g_f.check_events(game_settings, ship, screen, bullets)
        g_f.update_screen(screen, game_settings, ship, bullets)
        ship.update()
        bullets.update()

init_game()


