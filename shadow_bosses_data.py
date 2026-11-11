# shadow_bosses_data.py
# Bharat Region (Universe 2) Post-TYGRANTOX Shadow Bosses Database

SHADOW_BOSSES_DATABASE = {
    "Shadow_Ho_Oh": {
        "species": "Ho-Oh",
        "level": 80,
        "type": ["Shadow", "Fire"],
        "location": "Varanasi Ghats (Uttar Pradesh)",
        "sanctuary_affinity": "Khwaja_Ji_Ajmer",
        "hp": 106, "atk": 130, "def": 90, "spa": 110, "spd": 154, "spe": 90,
        "moves": [
            "Shadow Sacred Fire", "Shadow Blast", "Sacred Fire", "Brave Bird",
            "Earthquake", "Calm Mind", "Roost", "Solar Beam"
        ],
        "purified_move": "Sacred Fire"
    },
    "Shadow_Lugia": {
        "species": "Lugia",
        "level": 80,
        "type": ["Shadow", "Flying"],
        "location": "Deep Sundarbans Mangrove (West Bengal)",
        "sanctuary_affinity": "Haji_Ali_Mumbai",
        "hp": 106, "atk": 90, "def": 130, "spa": 90, "spd": 154, "spe": 110,
        "moves": [
            "Shadow Downpour", "Shadow Shed", "Aeroblast", "Hydro Pump",
            "Psychic", "Ice Beam", "Recover", "Calm Mind"
        ],
        "purified_move": "Aeroblast"
    },
    "Shadow_Kyogre": {
        "species": "Kyogre",
        "level": 82,
        "type": ["Shadow", "Water"],
        "location": "Malabar Oceanic Trench (Kerala Coast)",
        "sanctuary_affinity": "Haji_Ali_Mumbai",
        "hp": 100, "atk": 100, "def": 90, "spa": 150, "spd": 140, "spe": 90,
        "moves": [
            "Shadow Origin Surge", "Shadow Storm", "Water Spout", "Origin Pulse",
            "Thunder", "Ice Beam", "Calm Mind", "Aqua Ring"
        ],
        "purified_move": "Origin Pulse"
    },
    "Shadow_Groudon": {
        "species": "Groudon",
        "level": 82,
        "type": ["Shadow", "Ground"],
        "location": "Deccan Basalt Core (Maharashtra)",
        "sanctuary_affinity": "Haji_Ali_Mumbai",
        "hp": 100, "atk": 150, "def": 140, "spa": 100, "spd": 90, "spe": 90,
        "moves": [
            "Shadow Precipice", "Shadow Blast", "Precipice Blades", "Fire Blast",
            "Earthquake", "Solar Beam", "Bulk Up", "Stone Edge"
        ],
        "purified_move": "Precipice Blades"
    },
    "Shadow_Rayquaza": {
        "species": "Rayquaza",
        "level": 85,
        "type": ["Shadow", "Dragon"],
        "location": "Thar Desert Dune Peak (Rajasthan)",
        "sanctuary_affinity": "Khwaja_Ji_Ajmer",
        "hp": 105, "atk": 150, "def": 90, "spa": 150, "spd": 90, "spe": 95,
        "moves": [
            "Shadow Ascent", "Shadow Storm", "Dragon Ascent", "Outrage",
            "Extreme Speed", "Earthquake", "V-create", "Dragon Dance"
        ],
        "purified_move": "Dragon Ascent"
    },
    "Shadow_Dialga": {
        "species": "Dialga",
        "level": 85,
        "type": ["Shadow", "Dragon"],
        "location": "Siachen Glacier Ridge (Ladakh)",
        "sanctuary_affinity": "Khwaja_Ji_Ajmer",
        "hp": 100, "atk": 120, "def": 120, "spa": 150, "spd": 100, "spe": 90,
        "moves": [
            "Shadow Roar of Time", "Time Rupture", "Roar of Time", "Flash Cannon",
            "Earth Power", "Aura Sphere", "Iron Defense", "Dragon Pulse"
        ],
        "purified_move": "Roar of Time"
    },
    "Shadow_Palkia": {
        "species": "Palkia",
        "level": 85,
        "type": ["Shadow", "Dragon"],
        "location": "Brahmaputra River Canyon (Assam)",
        "sanctuary_affinity": "Haji_Ali_Mumbai",
        "hp": 90, "atk": 120, "def": 100, "spa": 150, "spd": 120, "spe": 100,
        "moves": [
            "Shadow Spacial Rend", "Spatial Rupture", "Spacial Rend", "Hydro Pump",
            "Aura Sphere", "Thunder", "Power Gem", "Earth Power"
        ],
        "purified_move": "Spacial Rend"
    },
    "Shadow_Giratina": {
        "species": "Giratina",
        "level": 88,
        "type": ["Shadow", "Ghost"],
        "location": "Silent Valley Rainforest Deep (Kerala)",
        "sanctuary_affinity": "Haji_Ali_Mumbai",
        "hp": 150, "atk": 120, "def": 100, "spa": 120, "spd": 100, "spe": 90,
        "moves": [
            "Shadow Force Void", "Temporal Decay", "Shadow Force", "Dragon Pulse",
            "Aura Sphere", "Earthquake", "Will-O-Wisp", "Destiny Bond"
        ],
        "purified_move": "Shadow Force"
    },
    "Shadow_Mewtwo": {
        "species": "Mewtwo",
        "level": 88,
        "type": ["Shadow", "Psychic"],
        "location": "Ujjain Underground Sanctum (Madhya Pradesh)",
        "sanctuary_affinity": "Khwaja_Ji_Ajmer",
        "hp": 106, "atk": 110, "def": 90, "spa": 154, "spd": 90, "spe": 130,
        "moves": [
            "Shadow Psy-Crush", "Shadow Blast", "Psystrike", "Aura Sphere",
            "Ice Beam", "Thunderbolt", "Recover", "Calm Mind"
        ],
        "purified_move": "Psystrike"
    },
    "Shadow_Arceus": {
        "species": "Arceus",
        "level": 95,
        "type": ["Shadow", "Cosmic"],
        "location": "Nanda Devi Himalayan Summit (Uttarakhand)",
        "sanctuary_affinity": "Both_Sanctuaries_Required",
        "hp": 120, "atk": 120, "def": 120, "spa": 120, "spd": 120, "spe": 120,
        "moves": [
            "Shadow Judgment", "Omni-Void Pulse", "Judgment", "Extreme Speed",
            "Recover", "Earth Power", "Dragon Claw", "Cosmic Power"
        ],
        "purified_move": "Judgment"
    }
}

SHADOW_MOVES_INFO = {
    "Shadow Sacred Fire": {"type": "Shadow", "power": 110, "acc": 95, "desc": "Corrupted holy flames that burn the soul."},
    "Shadow Blast":       {"type": "Shadow", "power": 100, "acc": 100, "desc": "Concentrated blast of multiversal dark energy."},
    "Shadow Downpour":    {"type": "Shadow", "power": 115, "acc": 90,  "desc": "Acidic rain of void matter."},
    "Shadow Shed":        {"type": "Shadow", "power": 0,   "acc": 100, "desc": "Cleanses user stat drops while lowering foe defense."},
    "Shadow Origin Surge":{"type": "Shadow", "power": 120, "acc": 85,  "desc": "Deep black water wave from the abyss."},
    "Shadow Storm":       {"type": "Shadow", "power": 95,  "acc": 100, "desc": "Violent whirlwind filled with shadow particles."},
    "Shadow Precipice":   {"type": "Shadow", "power": 125, "acc": 85,  "desc": "Tectonic magma spikes infused with void."},
    "Shadow Ascent":      {"type": "Shadow", "power": 120, "acc": 100, "desc": "Dark ozone dive that breaks barriers."},
    "Shadow Roar of Time":{"type": "Shadow", "power": 130, "acc": 90,  "desc": "Distorts temporal flow and inflicts void recoil."},
    "Time Rupture":       {"type": "Shadow", "power": 90,  "acc": 100, "desc": "Freezes target movement for 1 turn."},
    "Shadow Spacial Rend":{"type": "Shadow", "power": 115, "acc": 95,  "desc": "Tears fabric of reality dealing critical damage."},
    "Spatial Rupture":    {"type": "Shadow", "power": 85,  "acc": 100, "desc": "Swaps active battlefield attributes."},
    "Shadow Force Void":  {"type": "Shadow", "power": 130, "acc": 100, "desc": "Strikes from the anti-matter dimension."},
    "Temporal Decay":     {"type": "Shadow", "power": 80,  "acc": 100, "desc": "Drains target HP over successive turns."},
    "Shadow Psy-Crush":   {"type": "Shadow", "power": 110, "acc": 100, "desc": "Crushing mental void wave."},
    "Shadow Judgment":    {"type": "Shadow", "power": 140, "acc": 100, "desc": "Ultimate corrupted decree that hits all types neutral or super effective."},
    "Omni-Void Pulse":    {"type":
