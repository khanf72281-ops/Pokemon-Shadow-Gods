# auto_asset_downloader.py
import os
import pygame

def setup_placeholder_assets():
    dirs = [
        "assets/sprites/gen1",
        "assets/sprites/hisui_sinnoh",
        "assets/sprites/bharat",
        "assets/sprites/shadow_bosses",
        "assets/backgrounds",
        "assets/animations"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    
    pygame.init()
    # Dummy placeholder sprite
    surf = pygame.Surface((128, 128), pygame.SRCALPHA)
    pygame.draw.circle(surf, (100, 149, 237, 200), (64, 64), 50)
    pygame.image.save(surf, "assets/sprites/placeholder.png")

    # Dummy default background
    bg_surf = pygame.Surface((800, 600))
    bg_surf.fill((40, 44, 52))
    pygame.image.save(bg_surf, "assets/backgrounds/default_battle.png")
    
    print("✅ All directories and fallback assets initialized!")

if __name__ == "__main__":
    setup_placeholder_assets()
