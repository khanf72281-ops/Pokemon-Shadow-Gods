# move_animations.py
import pygame
import math
import random

class AttackAnimator:
    @staticmethod
    def play_move_effect(screen, move_name, start_pos, target_pos):
        """Custom particle-based VFX without needing heavy sprite-sheets"""
        if "Soul" in move_name or "Void" in move_name:
            # Purple / Cyan Swirling Void Particles
            for r in range(10, 80, 10):
                pygame.draw.circle(screen, (142, 68, 173), target_pos, r, 3)
                pygame.display.flip()
                pygame.time.delay(20)

        elif "Shadow" in move_name:
            # Black and Crimson Lightning Spikes
            for _ in range(8):
                end_x = target_pos[0] + random.randint(-40, 40)
                end_y = target_pos[1] + random.randint(-40, 40)
                pygame.draw.line(screen, (20, 20, 20), target_pos, (end_x, end_y), 4)
                pygame.draw.line(screen, (192, 57, 43), target_pos, (end_x, end_y), 2)
                pygame.display.flip()
                pygame.time.delay(25)

        elif "Flame" in move_name or "Fire" in move_name:
            # Fiery Explosion Burst
            for radius in range(5, 50, 8):
                pygame.draw.circle(screen, (230, 126, 34), target_pos, radius)
                pygame.draw.circle(screen, (241, 196, 15), target_pos, int(radius * 0.6))
                pygame.display.flip()
                pygame.time.delay(15)

        else:
            # Standard Tackle / Slash Impact
            pygame.draw.line(screen, (255, 255, 255), (target_pos[0]-30, target_pos[1]-30), (target_pos[0]+30, target_pos[1]+30), 5)
            pygame.display.flip()
            pygame.time.delay(40)
