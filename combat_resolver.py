# combat_resolver.py
import random

TYPE_EFFECTIVENESS = {
    "Normal": {"Rock": 0.5, "Ghost": 0.0, "Steel": 0.5},
    "Fire": {"Grass": 2.0, "Ice": 2.0, "Bug": 2.0, "Steel": 2.0, "Water": 0.5, "Fire": 0.5, "Rock": 0.5, "Dragon": 0.5},
    "Water": {"Fire": 2.0, "Ground": 2.0, "Rock": 2.0, "Water": 0.5, "Grass": 0.5, "Dragon": 0.5},
    "Grass": {"Water": 2.0, "Ground": 2.0, "Rock": 2.0, "Fire": 0.5, "Grass": 0.5, "Poison": 0.5, "Flying": 0.5, "Bug": 0.5, "Dragon": 0.5, "Steel": 0.5},
    "Electric": {"Water": 2.0, "Flying": 2.0, "Electric": 0.5, "Grass": 0.5, "Ground": 0.0, "Dragon": 0.5},
    "Ice": {"Grass": 2.0, "Ground": 2.0, "Flying": 2.0, "Dragon": 2.0, "Fire": 0.5, "Water": 0.5, "Ice": 0.5, "Steel": 0.5},
    "Fighting": {"Normal": 2.0, "Ice": 2.0, "Rock": 2.0, "Dark": 2.0, "Steel": 2.0, "Poison": 0.5, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Ghost": 0.0},
    "Poison": {"Grass": 2.0, "Poison": 0.5, "Ground": 0.5, "Rock": 0.5, "Ghost": 0.5, "Steel": 0.0},
    "Ground": {"Fire": 2.0, "Electric": 2.0, "Poison": 2.0, "Rock": 2.0, "Steel": 2.0, "Grass": 0.5, "Bug": 0.5, "Flying": 0.0},
    "Flying": {"Grass": 2.0, "Fighting": 2.0, "Bug": 2.0, "Electric": 0.5, "Rock": 0.5, "Steel": 0.5},
    "Psychic": {"Fighting": 2.0, "Poison": 2.0, "Psychic": 0.5, "Steel": 0.5, "Dark": 0.0},
    "Bug": {"Grass": 2.0, "Psychic": 2.0, "Dark": 2.0, "Fire": 0.5, "Fighting": 0.5, "Poison": 0.5, "Flying": 0.5, "Ghost": 0.5, "Steel": 0.5},
    "Rock": {"Fire": 2.0, "Ice": 2.0, "Flying": 2.0, "Bug": 2.0, "Fighting": 0.5, "Ground": 0.5, "Steel": 0.5},
    "Ghost": {"Psychic": 2.0, "Ghost": 2.0, "Normal": 0.0, "Dark": 0.5},
    "Dragon": {"Dragon": 2.0, "Steel": 0.5},
    "Steel": {"Ice": 2.0, "Rock": 2.0, "Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Steel": 0.5},
    "Dark": {"Psychic": 2.0, "Ghost": 2.0, "Fighting": 0.5, "Dark": 0.5},
    "Soul": {"Soul": 2.0, "Ghost": 2.0, "Dark": 1.5, "Normal": 0.5}
}

MOVE_DB = {
    "Tackle": (40, "Normal"), "Scratch": (40, "Normal"), "Mud-Slap": (20, "Ground"),
    "Vine Whip": (45, "Grass"), "Trunk Slam": (75, "Ground"), "Rock Tomb": (60, "Rock"),
    "Mud Shot": (55, "Ground"), "Harden": (0, "Normal"), "Bulldoze": (60, "Ground"),
    "Tectonic Stomp": (105, "Ground"), "Wood Hammer": (120, "Grass"), "Earthquake": (100, "Ground"),
    "Heavy Slam": (100, "Steel"), "Stone Edge": (100, "Rock"), "Ember": (40, "Fire"),
    "Bite": (60, "Dark"), "Flame Charge": (50, "Fire"), "Flame Burst": (70, "Fire"),
    "Slash": (70, "Normal"), "Fire Fang": (65, "Fire"), "Infernal Pounce": (95, "Fire"),
    "Flare Blitz": (120, "Fire"), "Shadow Claw": (70, "Ghost"), "Extreme Speed": (80, "Normal"),
    "Soul Burn": (110, "Soul"), "Close Combat": (120, "Fighting"), "Water Gun": (40, "Water"),
    "Aqua Jet": (40, "Water"), "Crunch": (80, "Dark"), "Water Pulse": (60, "Water"),
    "Aqua Tail": (90, "Water"), "Chambal Surge": (95, "Water"), "Iron Head": (80, "Steel"),
    "Hydro Pump": (110, "Water"), "Sand Attack": (0, "Ground"), "Dig": (80, "Ground"),
    "Bulk Up": (0, "Fighting"), "Rock Slide": (75, "Rock"), "Venoshock": (65, "Poison"),
    "Sludge Wave": (95, "Poison"), "Recover": (0, "Normal"), "Volt Tackle": (120, "Electric"),
    "Flash Cannon": (80, "Steel"), "Thunder Wave": (0, "Electric"), "Giga Drain": (75, "Grass"),
    "Night Slash": (70, "Dark"), "Air Slash": (75, "Flying"), "Heat Wave": (95, "Fire"),
    "Sandstorm": (0, "Rock"), "Blizzard": (110, "Ice"), "Ice Shard": (40, "Ice"),
    "Outrage": (120, "Dragon"), "Brave Bird": (120, "Flying"), "Eternal Soul Void": (135, "Soul"),
    "Cataclysmic Decay": (115, "Poison"), "Shadow Force": (120, "Ghost"), "Hyper Voice": (90, "Normal"),
    "Dragon Pulse": (85, "Dragon")
}

def resolve_attack(attacker, defender, move_name):
    power, m_type = MOVE_DB.get(move_name, (40, "Normal"))
    multiplier = 1.0
    for d_type in defender.type:
        multiplier *= TYPE_EFFECTIVENESS.get(m_type, {}).get(d_type, 1.0)
    
    dmg = int((((2 * attacker.level / 5 + 2) * power * (attacker.atk / max(1, defender.defense))) / 50) + 2)
    dmg = int(dmg * multiplier * random.uniform(0.85, 1.0))
    defender.current_hp = max(0, defender.current_hp - dmg)
    
    status_str = " (Super Effective!)" if multiplier > 1.0 else (" (Not very effective...)" if 0 < multiplier < 1.0 else (" (No effect!)" if multiplier == 0 else ""))
    print(f"💥 {attacker.name} ne {move_name} use kiya! {dmg} damage diya{status_str}")
    return dmg
