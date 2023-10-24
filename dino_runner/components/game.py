import pygame
import time
import pygame.mixer


from dino_runner.utils.constants import PARALLAX, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, MOUNTAINS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

text_delay = 30
FONT_STYLE = "FixedSys.ttf"
pygame.mixer.init()
pygame.mixer.music.load("dino_runner/assets/sea_theme_1.wav")


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0
        self.x_pos_bg_parallax = 0
        self.update_time = time.time()

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score = 0
        self.game_speed = 20
        self.velocidade_parallax = 3
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score(self)
        self.power_up_manager.update(self)

    def update_score(self, game):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5
        if game.player.has_power_up and game.player.type == "boost":
            self.score += 20

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        parallax_width = PARALLAX.get_width()
        self.screen.blit(PARALLAX, (self.x_pos_bg_parallax, 0))
        self.screen.blit(PARALLAX, (self.x_pos_bg_parallax + parallax_width, 0))
        self.x_pos_bg_parallax -= self.velocidade_parallax
        if self.x_pos_bg_parallax <= -parallax_width:
            self.x_pos_bg_parallax = 0
        self.screen.blit(PARALLAX, (self.x_pos_bg_parallax + parallax_width, 0))

        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def render_text(self, text, font_size, color, x, y):
        font = pygame.font.Font(FONT_STYLE, font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_score(self):
        self.render_text (f"Score: {self.score}", 22, (0, 0, 0), 1000, 50)
        
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.render_text(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 22, (155, 0 ,0), 500, 50)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.blit(MOUNTAINS, (0, 0))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        frame_count = self.frame_count if hasattr(self, 'frame_count') else 0
        show_text = frame_count < text_delay

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

        if self.death_count == 0:
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 45))

            if show_text:
                self.render_text("Press any key to start", 30, (0, 80, 97), half_screen_width, half_screen_height + 20)
        else:
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 45))

            if show_text:
                self.render_text("Press any key to restart", 30, (0, 80, 97), half_screen_width, half_screen_height + 20)
                self.render_text(f"Score: {self.score}", 22, (0, 233, 0), half_screen_width, half_screen_height + 60)
                self.render_text(f"Death count: {self.death_count}", 22, (255, 0, 0), half_screen_width, half_screen_height + 95)
                
        frame_count += 1
        if frame_count >= 2 * text_delay:
            frame_count = 0

        self.frame_count = frame_count


        pygame.display.update()
        self.handle_events_on_menu()