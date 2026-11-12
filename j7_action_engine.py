# j7_action_engine.py
import pygame
import math
import random
import json
import os
import sys

# J7 Nxt Optimized Resolution (Lightweight 16:9)
WIDTH, HEIGHT = 800, 450
FPS = 60

pygame.init()
# Hardware acceleration flag for smooth mobile rendering
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Pokemon: Shadow Gods - Action Edition")
clock = pygame.time.Clock()
font_sm = pygame.font.Font(None, 22)
font_md = pygame.font.Font(None, 28)

# Colors
BG_GRASS = (34, 139, 34)
BG_PATH = (194, 178, 128)
WHITE = (255, 255, 255)
BLACK = (15, 15, 20)
CYAN = (0, 220, 255)
CRIMSON = (220, 40, 60)
GOLD = (255, 200, 40)
PURPLE = (150, 60, 220)

class OfflineSaveSystem:
    FILE_NAME = "bharat_save.json"

    @staticmethod
    def load():
        if os.path.exists(OfflineSaveSystem.FILE_NAME):
            with open(OfflineSaveSystem.FILE_NAME, "r") as f:
                return json.load(f)
        return {"player_name": "Rishi", "partner": "Sherling", "level": 15, "caught": ["Sherling"], "x": 400, "y": 225}

    @staticmethod
    def save(data):
        with open(OfflineSaveSystem.FILE_NAME, "w") as f:
            json.dump(data, f)

class TouchControls:
    """On-screen Virtual Joystick & Action Buttons for Android Touch"""
    def __init__(self):
        self.joy_center = (100, 350)
        self.joy_radius = 45
        self.knob_pos = [100, 350]
        self.dx, self.dy = 0.0, 0.0
        
        # Action Buttons (Right Side)
        self.btn_attack = pygame.Rect(680, 330, 75, 75)   # Primary Move
        self.btn_dodge = pygame.Rect(590, 350, 65, 65)    # Z-A Dodge Roll
        self.btn_ball = pygame.Rect(695, 240, 60, 60)     # Let's Go Catch Throw

    def handle_input(self, mouse_pos, is_pressed):
        self.dx, self.dy = 0.0, 0.0
        self.knob_pos = list(self.joy_center)
        action = None

        if is_pressed:
            mx, my = mouse_pos
            # Check Joystick area (Left half of screen)
            dist = math.hypot(mx - self.joy_center[0], my - self.joy_center[1])
            if mx < WIDTH // 2 and dist < 130:
                angle = math.atan2(my - self.joy_center[1], mx - self.joy_center[0])
                clamped = min(dist, self.joy_radius)
                self.knob_pos[0] = self.joy_center[0] + math.cos(angle) * clamped
                self.knob_pos[1] = self.joy_center[1] + math.sin(angle) * clamped
                self.dx = math.cos(angle)
                self.dy = math.sin(angle)

            # Check Action Buttons
            if self.btn_attack.collidepoint(mx, my):
                action = "ATTACK"
            elif self.btn_dodge.collidepoint(mx, my):
                action = "DODGE"
            elif self.btn_ball.collidepoint(mx, my):
                action = "CATCH"

        return action

    def draw(self, surf):
        # Joystick Base & Knob
        pygame.draw.circle(surf, (255, 255, 255, 80), self.joy_center, self.joy_radius, 2)
        pygame.draw.circle(surf, CYAN, (int(self.knob_pos[0]), int(self.knob_pos[1])), 18)

        # Attack Button
        pygame.draw.circle(surf, CRIMSON, self.btn_attack.center, 36)
        surf.blit(font_sm.render("ATK", True, WHITE), (self.btn_attack.centerx - 15, self.btn_attack.centery - 8))

        # Dodge Button
        pygame.draw.circle(surf, GOLD, self.btn_dodge.center, 30)
        surf.blit(font_sm.render("DODGE", True, BLACK), (self.btn_dodge.centerx - 24, self.btn_dodge.centery - 8))

        # Catch Ball Button
        pygame.draw.circle(surf, PURPLE, self.btn_ball.center, 28)
        surf.blit(font_sm.render("BALL", True, WHITE), (self.btn_ball.centerx - 18, self.btn_ball.centery - 8))

class Entity:
    def __init__(self, x, y, name, hp, color, is_boss=False):
        self.x = float(x)
        self.y = float(y)
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.color = color
        self.is_boss = is_boss
        self.dodge_timer = 0
        self.atk_cooldown = 0

def run_j7_game():
    save_data = OfflineSaveSystem.load()
    controls = TouchControls()

    player = Entity(save_data["x"], save_data["y"], "Trainer", 100, WHITE)
    partner = Entity(player.x - 35, player.y + 15, save_data["partner"], 120, GOLD)
    
    # Wild / Shadow Boss Spawn in Overworld (No Loading Screen!)
    enemy = Entity(600, 160, "Shadow Tygrantox", 300, PURPLE, is_boss=True)

    projectiles = []   # Pooled lightweight projectiles
    pokeballs = []
    status_msg = f"Offline Mode Ready! Partner: {partner.name} (Lv.{save_data['level']})"
    save_timer = 0

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        save_timer += dt

        # Auto-save every 15 seconds offline
        if save_timer >= 15.0:
            save_data["x"], save_data["y"] = int(player.x), int(player.y)
            OfflineSaveSystem.save(save_data)
            save_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                OfflineSaveSystem.save(save_data)
                pygame.quit()
                sys.exit()

        # Touch + Keyboard Hybrid Support
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        action = controls.handle_input(mouse_pos, mouse_pressed)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: controls.dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: controls.dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]: controls.dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: controls.dy = 1
        if keys[pygame.K_SPACE]: action = "ATTACK"
        if keys[pygame.K_LSHIFT]: action = "DODGE"
        if keys[pygame.K_c]: action = "CATCH"

        # 1. Player & Partner Movement
        speed = 260 if player.dodge_timer > 0 else 150
        player.x = max(20, min(WIDTH - 20, player.x + controls.dx * speed * dt))
        player.y = max(40, min(HEIGHT - 20, player.y + controls.dy * speed * dt))

        # Partner follows smoothly (Let's Go Pikachu style)
        dist_p = math.hypot(player.x - partner.x, player.y - partner.y)
        if dist_p > 42:
            ang = math.atan2(player.y - partner.y, player.x - partner.x)
            partner.x += math.cos(ang) * 145 * dt
            partner.y += math.sin(ang) * 145 * dt

        # Cooldowns
        if player.dodge_timer > 0: player.dodge_timer -= dt
        if partner.atk_cooldown > 0: partner.atk_cooldown -= dt

        # 2. Actions (Z-A Real-Time Combat & Catching)
        if action == "DODGE" and player.dodge_timer <= 0:
            player.dodge_timer = 0.35
            status_msg = "⚡ Quick Dodge! Invincible!"

        elif action == "ATTACK" and partner.atk_cooldown <= 0 and enemy.hp > 0:
            partner.atk_cooldown = 0.6
            ang = math.atan2(enemy.y - partner.y, enemy.x - partner.x)
            projectiles.append({"x": partner.x, "y": partner.y, "vx": math.cos(ang)*380, "vy": math.sin(ang)*380, "owner": "PLAYER"})
            status_msg = f"🔥 {partner.name} used Soul Flame!"

        elif action == "CATCH" and len(pokeballs) == 0 and enemy.hp > 0:
            ang = math.atan2(enemy.y - player.y, enemy.x - player.x)
            pokeballs.append({"x": player.x, "y": player.y, "vx": math.cos(ang)*320, "vy": math.sin(ang)*320})
            status_msg = "🔴 Threw Bharat Ultra Ball!"

        # 3. Enemy Real-Time AI (Dodges & Fires Shadow Orbs)
        if enemy.hp > 0:
            enemy.atk_cooldown -= dt
            # Gentle floating patrol
            enemy.y += math.sin(pygame.time.get_ticks() * 0.003) * 40 * dt
            if enemy.atk_cooldown <= 0:
                enemy.atk_cooldown = 1.8
                ang = math.atan2(player.y - enemy.y, player.x - enemy.x)
                projectiles.append({"x": enemy.x, "y": enemy.y, "vx": math.cos(ang)*220, "vy": math.sin(ang)*220, "owner": "ENEMY"})

        # 4. Update Projectiles & Collisions
        for p in projectiles[:]:
            p["x"] += p["vx"] * dt
            p["y"] += p["vy"] * dt
            if not (0 <= p["x"] <= WIDTH and 0 <= p["y"] <= HEIGHT):
                projectiles.remove(p)
                continue

            if p["owner"] == "PLAYER" and enemy.hp > 0:
                if math.hypot(p["x"] - enemy.x, p["y"] - enemy.y) < 30:
                    enemy.hp = max(0, enemy.hp - 25)
                    projectiles.remove(p)
                    if enemy.hp == 0:
                        status_msg = f"🏆 {enemy.name} Pacified! +1 Level!"
                        save_data["level"] += 1
                        OfflineSaveSystem.save(save_data)

            elif p["owner"] == "ENEMY":
                if math.hypot(p["x"] - player.x, p["y"] - player.y) < 22 and player.dodge_timer <= 0:
                    player.hp = max(0, player.hp - 15)
                    projectiles.remove(p)
                    status_msg = "💥 Hit by Shadow Orb! Use DODGE!"

        # 5. Update Pokeball Catch Mechanic
        for b in pokeballs[:]:
            b["x"] += b["vx"] * dt
            b["y"] += b["vy"] * dt
            if math.hypot(b["x"] - enemy.x, b["y"] - enemy.y) < 28:
                catch_chance = 0.85 if enemy.hp < 100 else 0.25
                if random.random() < catch_chance:
                    status_msg = f"✨ GOTCHA! {enemy.name} joined your squad!"
                    if enemy.name not in save_data["caught"]:
                        save_data["caught"].append(enemy.name)
                    OfflineSaveSystem.save(save_data)
                    enemy.hp = 0
                else:
                    status_msg = "❌ Broke free! Lower its HP first!"
                pokeballs.remove(b)
            elif not (0 <= b["x"] <= WIDTH and 0 <= b["y"] <= HEIGHT):
                pokeballs.remove(b)

        # --- RENDERING (Lightweight 60 FPS) ---
        screen.fill(BG_GRASS)
        pygame.draw.rect(screen, BG_PATH, (0, 190, WIDTH, 70))  # Bharat Trail Path

        # Draw Enemy Boss
        if enemy.hp > 0:
            pygame.draw.circle(screen, enemy.color, (int(enemy.x), int(enemy.y)), 28)
            pygame.draw.circle(screen, CRIMSON, (int(enemy.x), int(enemy.y)), 32, 2)
            # Enemy HP Bar
            pygame.draw.rect(screen, BLACK, (enemy.x - 35, enemy.y - 45, 70, 8))
            pygame.draw.rect(screen, CRIMSON, (enemy.x - 35, enemy.y - 45, int(70 * (enemy.hp / enemy.max_hp)), 8))

        # Draw Partner & Player
        pygame.draw.circle(screen, partner.color, (int(partner.x), int(partner.y)), 14)
        p_col = CYAN if player.dodge_timer > 0 else WHITE
        pygame.draw.circle(screen, p_col, (int(player.x), int(player.y)), 16)

        # Draw Projectiles & Pokeballs
        for p in projectiles:
            col = GOLD if p["owner"] == "PLAYER" else PURPLE
            pygame.draw.circle(screen, col, (int(p["x"]), int(p["y"])), 7)

        for b in pokeballs:
            pygame.draw.circle(screen, CRIMSON, (int(b["x"]), int(b["y"])), 8)
            pygame.draw.circle(screen, WHITE, (int(b["x"]), int(b["y"])), 8, 2)

        # Top HUD Bar
        pygame.draw.rect(screen, (15, 15, 25), (0, 0, WIDTH, 34))
        hud_txt = font_md.render(f"HP: {player.hp}/100 | {status_msg}", True, WHITE)
        screen.blit(hud_txt, (12, 7))

        # Virtual Touch Controls
        controls.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    run_j7_game()
