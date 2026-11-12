# visual_battle_engine.py
import pygame
import sys
import time
from asset_loader import get_pokemon_sprite, get_arena_background

class VisualBattleScene:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.init()
        self.width = screen_width
        self.height = screen_height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pokemon: Shadow Gods - Universe 2 Battle")
        self.font = pygame.font.Font(None, 28)
        self.clock = pygame.time.Clock()

    def draw_hp_bar(self, x, y, current_hp, max_hp, name):
        ratio = max(0, current_hp) / max_hp
        bar_width = 180
        bar_height = 14
        
        # Name tag
        label = self.font.render(f"{name}: {current_hp}/{max_hp}", True, (255, 255, 255))
        self.screen.blit(label, (x, y - 25))
        
        # Outer border & background
        pygame.draw.rect(self.screen, (50, 50, 50), (x, y, bar_width, bar_height))
        
        # Health fill (Green to Red transition)
        fill_color = (46, 204, 113) if ratio > 0.5 else ((241, 196, 15) if ratio > 0.2 else (231, 76, 60))
        pygame.draw.rect(self.screen, fill_color, (x, y, int(bar_width * ratio), bar_height))
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, bar_width, bar_height), 2)

    def trigger_attack_animation(self, anim_type="claw_slash"):
        """Simple visual impact flash & screen shake effect"""
        shake_offset = 10
        for _ in range(3):
            self.screen.scroll(dx=shake_offset, dy=0)
            pygame.display.flip()
            pygame.time.delay(30)
            self.screen.scroll(dx=-shake_offset, dy=0)
            pygame.display.flip()
            pygame.time.delay(30)

    def render_turn(self, player_mon, enemy_mon, arena_key="tarana_lab", message=""):
        # 1. Background draw
        bg_path = get_arena_background(arena_key)
        try:
            bg_surf = pygame.image.load(bg_path)
            bg_surf = pygame.transform.scale(bg_surf, (self.width, self.height))
            self.screen.blit(bg_surf, (0, 0))
        except Exception:
            self.screen.fill((30, 30, 45))  # Fallback solid color

        # 2. Sprites draw
        # Enemy sprite (Top Right)
        e_sprite_path = get_pokemon_sprite(enemy_mon.name, category="bharat")
        try:
            e_img = pygame.image.load(e_sprite_path)
            e_img = pygame.transform.scale(e_img, (180, 180))
            self.screen.blit(e_img, (520, 100))
        except Exception:
            pygame.draw.circle(self.screen, (200, 50, 50), (600, 180), 60)

        # Player sprite (Bottom Left)
        p_sprite_path = get_pokemon_sprite(player_mon.name, category="bharat")
        try:
            p_img = pygame.image.load(p_sprite_path)
            p_img = pygame.transform.scale(p_img, (220, 220))
            self.screen.blit(p_img, (100, 280))
        except Exception:
            pygame.draw.circle(self.screen, (50, 150, 200), (200, 380), 70)

        # 3. HUD / HP Bars
        self.draw_hp_bar(520, 80, enemy_mon.current_hp, enemy_mon.max_hp, enemy_mon.name)
        self.draw_hp_bar(100, 250, player_mon.current_hp, player_mon.max_hp, player_mon.name)

        # 4. Dialogue / Status Box
        pygame.draw.rect(self.screen, (10, 10, 20), (50, 480, 700, 90), border_radius=8)
        pygame.draw.rect(self.screen, (200, 200, 200), (50, 480, 700, 90), 3, border_radius=8)
        
        msg_surf = self.font.render(message, True, (255, 255, 255))
        self.screen.blit(msg_surf, (70, 510))

        pygame.display.flip()
        self.clock.tick(60)
