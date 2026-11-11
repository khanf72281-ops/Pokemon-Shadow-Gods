# bharat_game_engine.py
import math
import random
import sys

# ==========================================
# 1. POKEDEX & DATA
# ==========================================
BHARAT_DEX = {
    "Tusklet": {
        "type": "Grass/Ground",
        "hp": 65,
        "atk": 70,
        "def": 75,
        "spe": 40,
        "moves": ["Tackle", "Mud-Slap", "Vine Whip", "Trunk Slam"],
    },
    "Sherling": {
        "type": "Fire",
        "hp": 50,
        "atk": 75,
        "def": 45,
        "spe": 70,
        "moves": ["Scratch", "Ember", "Bite", "Flame Charge"],
    },
    "Gharikid": {
        "type": "Water",
        "hp": 55,
        "atk": 65,
        "def": 65,
        "spe": 55,
        "moves": ["Bite", "Water Gun", "Aqua Jet", "Crunch"],
    },
    "Mungor": {
        "type": "Ground",
        "hp": 45,
        "atk": 60,
        "def": 40,
        "spe": 75,
        "moves": ["Mud-Slap", "Scratch", "Sand Attack"],
    },
    "Gajarock": {
        "type": "Grass/Ground",
        "hp": 85,
        "atk": 90,
        "def": 95,
        "spe": 50,
        "moves": ["Rock Tomb", "Mud Shot", "Tackle", "Harden"],
    },
}

MOVES_DATABASE = {
    "Tackle": {"type": "Normal", "power": 40, "acc": 100},
    "Scratch": {"type": "Normal", "power": 40, "acc": 100},
    "Bite": {"type": "Dark", "power": 60, "acc": 100},
    "Mud-Slap": {"type": "Ground", "power": 20, "acc": 100},
    "Vine Whip": {"type": "Grass", "power": 45, "acc": 100},
    "Trunk Slam": {"type": "Ground", "power": 65, "acc": 95},
    "Ember": {"type": "Fire", "power": 40, "acc": 100},
    "Flame Charge": {"type": "Fire", "power": 50, "acc": 100},
    "Water Gun": {"type": "Water", "power": 40, "acc": 100},
    "Aqua Jet": {"type": "Water", "power": 40, "acc": 100},
    "Crunch": {"type": "Dark", "power": 80, "acc": 100},
    "Sand Attack": {"type": "Ground", "power": 0, "acc": 100},
    "Rock Tomb": {"type": "Rock", "power": 60, "acc": 95},
    "Mud Shot": {"type": "Ground", "power": 55, "acc": 95},
    "Harden": {"type": "Normal", "power": 0, "acc": 100},
}

GYMS = {
    "MP": {
        "leader": "Vikram",
        "badge": "Maati Badge",
        "team": [("Mungor", 12), ("Gajarock", 14)],
    },
    "Bengal": {
        "leader": "Arpana",
        "badge": "Jwar Badge",
        "team": [("Chitrapan", 18), ("Delta-Naga", 21)],
    },
    "Delhi": {
        "leader": "Kabir",
        "badge": "Chakra Badge",
        "team": [("Magnemite", 19), ("Lohashva", 24)],
    },
    "Kerala": {
        "leader": "Keshavan",
        "badge": "Aranya Badge",
        "team": [("Bansurath", 26), ("Vanarkesh", 29)],
    },
    "Maharashtra": {
        "leader": "Tanvi",
        "badge": "Pashan Badge",
        "team": [("Kurmadev", 37), ("Shailasur", 43)],
    },
    "Rajasthan": {
        "leader": "Bhairav",
        "badge": "Marichika Badge",
        "team": [("Marukantak", 38), ("Bhavandar", 43)],
    },
    "Ladakh": {
        "leader": "Tashi",
        "badge": "Himshikhar Badge",
        "team": [("Himsnow", 42), ("Ghorashim", 47)],
    },
    "Assam": {
        "leader": "Anamika",
        "badge": "Megh Badge",
        "team": [("Mayurak", 45), ("Garudragon", 50)],
    },
}

# ==========================================
# 2. POKEMON & BATTLE ENGINE
# ==========================================
class Pokemon:

  def __init__(self, name, level=5):
    self.name = name
    self.level = level
    data = BHARAT_DEX.get(
        name,
        {
            "type": "Normal",
            "hp": 50,
            "atk": 50,
            "def": 50,
            "spe": 50,
            "moves": ["Tackle"],
        },
    )
    self.type = data["type"]
    self.max_hp = int(data["hp"] + (level * 2.2))
    self.current_hp = self.max_hp
    self.atk = int(data["atk"] + (level * 1.5))
    self.defense = int(data["def"] + (level * 1.5))
    self.spe = int(data["spe"] + (level * 1.2))
    self.moves = list(data["moves"])

  def is_alive(self):
    return self.current_hp > 0


def calculate_damage(attacker, defender, move_name):
  move = MOVES_DATABASE.get(move_name, {"power": 40, "acc": 100})
  if move["power"] == 0:
    return 0
  base_dmg = (((2 * attacker.level / 5 + 2) * move["power"] * (attacker.atk / max(1, defender.defense))) / 50) + 2
  variance = random.uniform(0.85, 1.0)
  return int(base_dmg * variance)


def run_battle(player_mon, enemy_mon):
  print(f"\n--- BATTLE SHURU: [Lv.{player_mon.level} {player_mon.name}] VS [Lv.{enemy_mon.level} {enemy_mon.name}] ---")
  while player_mon.is_alive() and enemy_mon.is_alive():
    print(f"\nYour HP: {player_mon.current_hp}/{player_mon.max_hp} | Enemy HP: {enemy_mon.current_hp}/{enemy_mon.max_hp}")
    print("Moves:")
    for idx, m in enumerate(player_mon.moves):
      print(f"  {idx + 1}. {m}")
    choice = input("Move number chuno (ya 'run' likho): ").strip()
    if choice.lower() == "run":
      print("Aap ladai se bhaag gaye!")
      return "RUN"

    try:
      chosen_move = player_mon.moves[int(choice) - 1]
    except (ValueError, IndexError):
      chosen_move = player_mon.moves[0]

    # Turn Order by Speed
    first, second = ((player_mon, enemy_mon) if player_mon.spe >= enemy_mon.spe else (enemy_mon, player_mon))
    m1 = chosen_move if first == player_mon else random.choice(enemy_mon.moves)
    m2 = random.choice(enemy_mon.moves) if first == player_mon else chosen_move

    # Attacker 1
    dmg1 = calculate_damage(first, second, m1)
    second.current_hp = max(0, second.current_hp - dmg1)
    print(f"{first.name} ne {m1} use kiya! {dmg1} damage!")
    if not second.is_alive():
      break

    # Attacker 2
    dmg2 = calculate_damage(second, first, m2)
    first.current_hp = max(0, first.current_hp - dmg2)
    print(f"{second.name} ne {m2} use kiya! {dmg2} damage!")

  if player_mon.is_alive():
    print(f"\n🏆 Badhai! Aapne [Lv.{enemy_mon.level} {enemy_mon.name}] ko hara diya!")
    return "WIN"
  else:
    print(f"\n💀 {player_mon.name} behosh ho gaya! Battle Lost.")
    return "LOSE"


# ==========================================
# 3. OVERWORLD & STORY CONTROLLER
# ==========================================
class BharatEngine:

  def __init__(self):
    self.player_name = "Trainer"
    self.starter = None
    self.badges = []
    self.player_pos = [10, 10]

  def start_game(self):
    print("=" * 60)
    print("       POKEMON MULTIVERSE: UNIVERSE 2 (BHARAT REGION)       ")
    print("=" * 60)
    # Rescue Scene
    print("\n📍 Sthan: Tarana ke Purane Khandahar (Madhya Pradesh)")
    print("Wild Pokemon aapko gher rahe the ki achanak ek aawaz aayi...")
    print("'HAATO WAHAN SE! AIRAVALON, USE EARTH POWER!'")
    print("Prof. Raheem ne aapko bacha liya aur apni Tarana Lab le gaye.")

    # Starter Pick
    print("\nProf. Raheem: 'Tarana me aage badhne ke liye ek sathi chuno:'")
    print("  1. Tusklet  (Grass/Ground) - MP Elephant Tank")
    print("  2. Sherling (Fire)         - Forest Striker Cub")
    print("  3. Gharikid (Water)        - Chambal Snapping Hunter")

    choices = {"1": "Tusklet", "2": "Sherling", "3": "Gharikid"}
    p_choice = input("Chuno (1-3): ").strip()
    starter_name = choices.get(p_choice, "Tusklet")
    self.starter = Pokemon(starter_name, level=5)
    print(f"✅ Shandar! Aapko mila apna starter [Lv.5 {self.starter.name}]!")

    self.overworld_loop()

  def overworld_loop(self):
    while True:
      print("\n" + "=" * 40)
      print(f"📍 Location: Malwa Outskirts | Pos: {self.player_pos} | Badges: {len(self.badges)}/8")
      print("Actions: [W/A/S/D] Walk | [G] MP Gym Challenge | [H] Heal | [Q] Quit")
      cmd = input("Command: ").strip().lower()

      if cmd in ["w", "a", "s", "d"]:
        if cmd == "w":
          self.player_pos[1] += 1
        elif cmd == "s":
          self.player_pos[1] -= 1
        elif cmd == "a":
          self.player_pos[0] -= 1
        elif cmd == "d":
          self.player_pos[0] += 1

        # Wild Encounter Chance
        if random.random() < 0.4:
          wild_mon = Pokemon("Mungor", level=random.randint(2, 4))
          print(f"\n⚠️ Jhaadiyon se ek wild [Lv.{wild_mon.level} {wild_mon.name}] bahar kud pada!")
          res = run_battle(self.starter, wild_mon)
          if res == "LOSE":
            self.starter.current_hp = self.starter.max_hp
            print("🏥 Aap behosh hue aur Prof. Raheem ki lab me jaage.")

      elif cmd == "h":
        self.starter.current_hp = self.starter.max_hp
        print("🌿 Team fully healed!")

      elif cmd == "g":
        self.trigger_gym_battle("MP")

      elif cmd == "q":
        print("Game progress memory saved. Alvida!")
        sys.exit()

  def trigger_gym_battle(self, state_name):
    gym = GYMS[state_name]
    print("\n" + "=" * 50)
    print(f"🏛️ Entering {state_name} Gym! Leader: {gym['leader']}")
    print(f"{gym['leader']}: 'Malwa ki mitti me dum dekhna chahte ho? Aao!'")

    for mon_name, lvl in gym["team"]:
      boss_mon = Pokemon(mon_name, level=lvl)
      result = run_battle(self.starter, boss_mon)
      if result != "WIN":
        print(f"\n❌ Gym Leader {gym['leader']} se aap haar gaye!")
        return

    print(f"\n🏆 BHARAT GYM CLEARED! Aapko mila '{gym['badge']}'!")
    if gym["badge"] not in self.badges:
      self.badges.append(gym["badge"])


# ==========================================
# RUN
# ==========================================
if __name__ == "__main__":
  game = BharatEngine()
  game.start_game()
