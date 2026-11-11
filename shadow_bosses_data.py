# shadow_bosses_data.py

SHADOW_BOSS_ROSTER = {
    "Shadow_Ho_Oh": {
        "species": "Ho-Oh",
        "level": 75,
        "type": ["Shadow", "Fire"],
        "location": "Varanasi (Ganga River Corridor)",
        "sanctuary_cure": "Ajmer_Sharif",
        "purified_move": "Sacred Fire",
        "moves": [
            "Shadow Sacred Fire", "Shadow Blast", "Sunny Day", "Solar Beam",
            "Extrasensory", "Recover", "Ancient Power", "Burn Up"
        ]
    },
    "Shadow_Lugia": {
        "species": "Lugia",
        "level": 75,
        "type": ["Shadow", "Flying"],
        "location": "Sundarbans Core (West Bengal)",
        "sanctuary_cure": "Haji_Ali",
        "purified_move": "Aeroblast",
        "moves": [
            "Shadow Downpour", "Shadow Blast", "Hydro Pump", "Psychic",
            "Recover", "Calm Mind", "Ice Beam", "Dragon Rush"
        ]
    },
    "Shadow_Kyogre": {
        "species": "Kyogre",
        "level": 76,
        "type": ["Shadow", "Water"],
        "location": "Malabar Coast (Kerala Deep Waters)",
        "sanctuary_cure": "Haji_Ali",
        "purified_move": "Origin Pulse",
        "moves": [
            "Shadow Origin Surge", "Shadow Storm", "Thunder", "Ice Beam",
            "Water Spout", "Calm Mind", "Aqua Ring", "Body Slam"
        ]
    },
    "Shadow_Groudon": {
        "species": "Groudon",
        "level": 76,
        "type": ["Shadow", "Ground"],
        "location": "Deccan Basalt Caverns (Maharashtra)",
        "sanctuary_cure": "Ajmer_Sharif",
        "purified_move": "Precipice Blades",
        "moves": [
            "Shadow Precipice", "Shadow Storm", "Fire Blast", "Solar Beam",
            "Bulk Up", "Hammer Arm", "Earthquake", "Stone Edge"
        ]
    },
    "Shadow_Rayquaza": {
        "species": "Rayquaza",
        "level": 78,
        "type": ["Shadow", "Dragon"],
        "location": "Thar Desert Dune Summit (Rajasthan)",
        "sanctuary_cure": "Ajmer_Sharif",
        "purified_move": "Dragon Ascent",
        "moves": [
            "Shadow Ascent", "Shadow Blast", "Extreme Speed", "Outrage",
            "Dragon Dance", "Earthquake", "Hyper Beam", "Air Slash"
        ]
    },
    "Shadow_Dialga": {
        "species": "Dialga",
        "level": 80,
        "type": ["Shadow", "Dragon"],
        "location": "Siachen Glacier Ridge (Ladakh)",
        "sanctuary_cure": "Haji_Ali",
        "purified_move": "Roar of Time",
        "moves": [
            "Shadow Roar of Time", "Shadow Storm", "Flash Cannon", "Earth Power",
            "Aura Sphere", "Iron Defense", "Blizzard", "Slash"
        ]
    },
    "Shadow_Palkia": {
        "species": "Palkia",
        "level": 80,
        "type": ["Shadow", "Dragon"],
        "location": "Brahmaputra River Canyon (Assam)",
        "sanctuary_cure": "Haji_Ali",
        "purified_move": "Spacial Rend",
        "moves": [
            "Shadow Spacial Rend", "Shadow Storm", "Hydro Pump", "Aura Sphere",
            "Earth Power", "Power Gem", "Dragon Claw", "Bulk Up"
        ]
    },
    "Shadow_Giratina": {
        "species": "Giratina",
        "level": 82,
        "type": ["Shadow", "Ghost"],
        "location": "Silent Valley Rainforest (Kerala)",
        "sanctuary_cure": "Haji_Ali",
        "purified_move": "Shadow Force",
        "moves": [
            "Shadow Force Void", "Shadow Blast", "Dragon Pulse", "Aura Sphere",
            "Destiny Bond", "Calm Mind", "Earthquake", "Hex"
        ]
    },
    "Shadow_Mewtwo": {
        "species": "Mewtwo",
        "level": 85,
        "type": ["Shadow", "Psychic"],
        "location": "Ujjain Underground Crypts (Madhya Pradesh)",
        "sanctuary_cure": "Ajmer_Sharif",
        "purified_move": "Psystrike",
        "moves": [
            "Shadow Psy-Crush", "Shadow Blast", "Aura Sphere", "Recover",
            "Ice Beam", "Thunderbolt", "Nasty Plot", "Psychic"
        ]
    },
    "Shadow_Arceus": {
        "species": "Arceus",
        "level": 90,
        "type": ["Shadow", "Cosmic"],
        "location": "Nanda Devi Peak (Uttarakhand Himalayan Bio-Dome)",
        "sanctuary_cure": "Ajmer_Sharif",
        "purified_move": "Judgment",
        "moves": [
            "Shadow Judgment", "Shadow Blast", "Cosmic Power", "Recover",
            "Hyper Voice", "Earth Power", "Extreme Speed", "Giga Impact"
        ]
    }
}

SHADOW_MOVES_DATA = {
    "Shadow Sacred Fire": {"type": "Shadow", "power": 110, "acc": 95, "desc": "Ash-laden dark fire, 50% burn"},
    "Shadow Downpour":    {"type": "Shadow", "power": 110, "acc": 95, "desc": "Acidic void torrent"},
    "Shadow Origin Surge":{"type": "Shadow", "power": 120, "acc": 90, "desc": "Abyssal tide strike"},
    "Shadow Precipice":   {"type": "Shadow", "power": 120, "acc": 90, "desc": "Cracked tectonic dark spike"},
    "Shadow Ascent":      {"type": "Shadow", "power": 130, "acc": 95, "desc": "Sky-piercing void dive"},
    "Shadow Roar of Time":{"type": "Shadow", "power": 140, "acc": 90, "desc": "Freezes timeline turn"},
    "Shadow Spacial Rend":{"type": "Shadow", "power": 115, "acc": 95, "desc": "High critical rift slash"},
    "Shadow Force Void":  {"type": "Shadow", "power": 130, "acc": 100, "desc": "Bypasses Protect/Shields"},
    "Shadow Psy-Crush":   {"type": "Shadow", "power": 120, "acc": 100, "desc": "Breaks special barrier"},
    "Shadow Judgment":    {"type": "Shadow", "power": 150, "acc": 100, "desc": "Omni-void strike"},
    "Shadow Blast":       {"type": "Shadow", "power": 100, "acc": 95, "desc": "Condensed void energy ball"},
    "Shadow Storm":       {"type": "Shadow", "power": 95, "acc": 100, "desc": "Hits all opposing slots"}
}
