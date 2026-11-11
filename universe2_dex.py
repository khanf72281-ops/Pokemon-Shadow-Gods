# universe2_dex.py

UNIVERSE2_POKEDEX = {
    # --- STARTER LINES ---
    "Tusklet": {
        "num": 1, "type": ["Grass", "Ground"], "stats": {"hp": 65, "atk": 70, "def": 75, "spa": 45, "spd": 55, "spe": 40},
        "moves": ["Tackle", "Mud-Slap", "Vine Whip", "Trunk Slam"], "evo": (16, "Gajarock")
    },
    "Gajarock": {
        "num": 2, "type": ["Grass", "Ground"], "stats": {"hp": 85, "atk": 90, "def": 95, "spa": 60, "spd": 70, "spe": 50},
        "moves": ["Rock Tomb", "Mud Shot", "Tackle", "Harden", "Trunk Slam", "Bulldoze"], "evo": (34, "Airavalon")
    },
    "Airavalon": {
        "num": 3, "type": ["Grass", "Ground"], "stats": {"hp": 105, "atk": 115, "def": 120, "spa": 75, "spd": 85, "spe": 60},
        "moves": ["Tectonic Stomp", "Wood Hammer", "Earthquake", "Heavy Slam", "Stone Edge", "Synthesis", "Bulk Up", "Giga Drain"]
    },
    "Sherling": {
        "num": 4, "type": ["Fire"], "stats": {"hp": 50, "atk": 75, "def": 45, "spa": 60, "spd": 50, "spe": 70},
        "moves": ["Scratch", "Ember", "Bite", "Flame Charge"], "evo": (16, "Jwalashardul")
    },
    "Jwalashardul": {
        "num": 5, "type": ["Fire"], "stats": {"hp": 65, "atk": 95, "def": 60, "spa": 75, "spd": 65, "spe": 90},
        "moves": ["Flame Burst", "Slash", "Fire Fang", "Agility", "Roar", "Crunch"], "evo": (36, "Vyaghragni")
    },
    "Vyaghragni": {
        "num": 6, "type": ["Fire", "Soul"], "stats": {"hp": 80, "atk": 125, "def": 75, "spa": 90, "spd": 75, "spe": 115},
        "moves": ["Infernal Pounce", "Flare Blitz", "Shadow Claw", "Extreme Speed", "Will-O-Wisp", "Soul Burn", "Close Combat", "Overheat"]
    },
    "Gharikid": {
        "num": 7, "type": ["Water"], "stats": {"hp": 55, "atk": 65, "def": 65, "spa": 50, "spd": 50, "spe": 55},
        "moves": ["Bite", "Water Gun", "Aqua Jet", "Crunch"], "evo": (18, "Tidaljaw")
    },
    "Tidaljaw": {
        "num": 8, "type": ["Water"], "stats": {"hp": 75, "atk": 85, "def": 85, "spa": 65, "spd": 65, "spe": 65},
        "moves": ["Water Pulse", "Ice Fang", "Aqua Tail", "Protect", "Crunch", "Bite"], "evo": (35, "Makardus")
    },
    "Makardus": {
        "num": 9, "type": ["Water", "Steel"], "stats": {"hp": 95, "atk": 110, "def": 125, "spa": 70, "spd": 85, "spe": 75},
        "moves": ["Chambal Surge", "Iron Head", "Hydro Pump", "Crunch", "Aqua Jet", "Flash Cannon", "Rain Dance", "Iron Defense"]
    },

    # --- ROUTE & REGIONAL ENCOUNTERS ---
    "Mungor": {
        "num": 10, "type": ["Ground"], "stats": {"hp": 45, "atk": 60, "def": 40, "spa": 30, "spd": 40, "spe": 75},
        "moves": ["Mud-Slap", "Scratch", "Sand Attack", "Dig"], "evo": (20, "Nakulor")
    },
    "Nakulor": {
        "num": 11, "type": ["Ground", "Fighting"], "stats": {"hp": 80, "atk": 105, "def": 75, "spa": 45, "spd": 65, "spe": 95},
        "moves": ["Close Combat", "Earthquake", "Bulk Up", "Rock Slide", "Sucker Punch", "Poison Jab", "Detect", "Agility"]
    },
    "Delta-Naga": {
        "num": 25, "type": ["Poison", "Water"], "stats": {"hp": 85, "atk": 75, "def": 80, "spa": 105, "spd": 90, "spe": 85},
        "moves": ["Venoshock", "Hydro Pump", "Sludge Wave", "Recover", "Toxic", "Dark Pulse", "Protect", "Aqua Ring"]
    },
    "Lohashva": {
        "num": 42, "type": ["Steel", "Electric"], "stats": {"hp": 90, "atk": 105, "def": 95, "spa": 95, "spd": 80, "spe": 115},
        "moves": ["Volt Tackle", "Flash Cannon", "Thunder Wave", "Iron Defense", "Wild Charge", "Magnet Rise", "Autotomize", "Thunderbolt"]
    },
    "Vanarkesh": {
        "num": 55, "type": ["Grass", "Fighting"], "stats": {"hp": 85, "atk": 110, "def": 80, "spa": 60, "spd": 75, "spe": 90},
        "moves": ["Giga Drain", "Close Combat", "Wood Hammer", "Mach Punch", "Bulk Up", "Leech Seed", "Acrobatics", "Spore"]
    },
    "Shailasur": {
        "num": 68, "type": ["Rock", "Dark"], "stats": {"hp": 115, "atk": 112, "def": 125, "spa": 55, "spd": 75, "spe": 45},
        "moves": ["Stone Edge", "Night Slash", "Iron Defense", "Toxic", "Earthquake", "Stealth Rock", "Crunch", "Roar"]
    },
    "Bhavandar": {
        "num": 77, "type": ["Flying", "Ground"], "stats": {"hp": 90, "atk": 80, "def": 75, "spa": 105, "spd": 80, "spe": 105},
        "moves": ["Air Slash", "Heat Wave", "Sandstorm", "Tailwind", "Earth Power", "Hurricane", "Roost", "Whirlwind"]
    },
    "Ghorashim": {
        "num": 89, "type": ["Ice", "Fighting"], "stats": {"hp": 95, "atk": 120, "def": 78, "spa": 60, "spd": 80, "spe": 110},
        "moves": ["Blizzard", "Close Combat", "Ice Shard", "Bulk Up", "Icicle Crash", "Superpower", "Avalanche", "Taunt"]
    },
    "Garudragon": {
        "num": 99, "type": ["Dragon", "Flying"], "stats": {"hp": 110, "atk": 130, "def": 95, "spa": 90, "spd": 90, "spe": 115},
        "moves": ["Outrage", "Brave Bird", "Earthquake", "Tailwind", "Dragon Dance", "Roost", "Dragon Claw", "Defog"]
    },

    # --- COSMIC & APEX ENTITIES ---
    "Tygrathor": {
        "num": 499, "type": ["Soul", "Fire"], "stats": {"hp": 110, "atk": 135, "def": 100, "spa": 120, "spd": 95, "spe": 120},
        "moves": ["Soul Burn", "Flare Blitz", "Sacred Roar", "Dragon Claw", "Extreme Speed", "Will-O-Wisp", "Earth Power", "Aura Sphere"]
    },
    "TYGRANTOX": {
        "num": 500, "type": ["Soul", "Poison"], "stats": {"hp": 140, "atk": 155, "def": 135, "spa": 155, "spd": 125, "spe": 110},
        "moves": ["Eternal Soul Void", "Cataclysmic Decay", "Sludge Wave", "Shadow Force", "Recover", "Hyper Voice", "Toxic Spikes", "Dragon Pulse"]
    }
}
