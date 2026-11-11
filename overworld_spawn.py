# overworld_spawner.py
import random
import math

class OverworldPokemon:
    def __init__(self, name, level, x, y, behavior="calm"):
        self.name = name
        self.level = level
        self.x = x
        self.y = y
        self.behavior = behavior  # 'timid', 'aggressive', 'calm'
        self.is_active = True

    def update_position(self, player_x, player_y):
        """Player ki position dekh kar react karna"""
        # Player aur Pokemon ke beech ki doori
        distance = math.sqrt((self.x - player_x)**2 + (self.y - player_y)**2)

        if distance < 3.0:  # Agar player pass aa gaya
            if self.behavior == "aggressive":
                # Player ki taraf aage badhna (Attack stance)
                if self.x < player_x: self.x += 0.5
                elif self.x > player_x: self.x -= 0.5
                if self.y < player_y: self.y += 0.5
                elif self.y > player_y: self.y -= 0.5
                return "CHASE"
            
            elif self.behavior == "timid":
                # Player se dur bhagna
                if self.x < player_x: self.x -= 0.5
                elif self.x > player_x: self.x += 0.5
                return "FLEE"

        # Normal random wandering (Ghoomna)
        self.x += random.choice([-0.2, 0, 0.2])
        self.y += random.choice([-0.2, 0, 0.2])
        return "IDLE"

class MapSpawner:
    def __init__(self, zone_name):
        self.zone_name = zone_name
        self.active_spawns = []

    def spawn_wild_pokemon(self, spawn_table, max_count=5):
        """Map par visual Pokemon spawn karna"""
        while len(self.active_spawns) < max_count:
            mon_info = random.choice(spawn_table)
            # Random map coordinates (e.g. X: 5-50, Y: 5-50)
            spawn_x = random.randint(5, 50)
            spawn_y = random.randint(5, 50)
            
            mon = OverworldPokemon(
                name=mon_info["name"],
                level=random.randint(mon_info["min_lvl"], mon_info["max_lvl"]),
                x=spawn_x,
                y=spawn_y,
                behavior=mon_info["behavior"]
            )
            self.active_spawns.append(mon)
            print(f"👀 Ek jungle me [Lv.{mon.level} {mon.name}] ghoomta hua dikh raha hai! (X:{spawn_x}, Y:{spawn_y})")
