# ==============================================================================
# 1. POKEMON & MOVES DATABASE (pokemon_data.py)
# ==============================================================================

MOVE_DATABASE = {
    # नॉर्मल / बेसिक अटैक्स
    "Tackle": {"type": "Normal", "power": 40, "acc": 100, "cat": "Physical"},
    "Scratch": {"type": "Normal", "power": 40, "acc": 100, "cat": "Physical"},
    "Body Slam": {"type": "Normal", "power": 85, "acc": 100, "cat": "Physical"},
    
    # एलिमेंटल अटैक्स
    "Flamethrower": {"type": "Fire", "power": 90, "acc": 100, "cat": "Special"},
    "Ember": {"type": "Fire", "power": 40, "acc": 100, "cat": "Special"},
    "Surf": {"type": "Water", "power": 90, "acc": 100, "cat": "Special"},
    "Water Gun": {"type": "Water", "power": 40, "acc": 100, "cat": "Special"},
    "Earthquake": {"type": "Ground", "power": 100, "acc": 100, "cat": "Physical"},
    "Mud-Slap": {"type": "Ground", "power": 20, "acc": 100, "cat": "Special"},
    "Shadow Ball": {"type": "Ghost", "power": 80, "acc": 100, "cat": "Special"},
    "Close Combat": {"type": "Fighting", "power": 120, "acc": 100, "cat": "Physical"},
    "Stone Edge": {"type": "Rock", "power": 100, "acc": 80, "cat": "Physical"},
    "Thunderbolt": {"type": "Electric", "power": 90, "acc": 100, "cat": "Special"},
    "Dragon Claw": {"type": "Dragon", "power": 80, "acc": 100, "cat": "Physical"},

    # सोल टाइप (डिवाइन / लेजेंडरी एक्सक्लूसिव)
    "Soul Burn": {"type": "Soul", "power": 90, "acc": 100, "cat": "Special"},
    "Cataclysmic Decay": {"type": "Poison", "power": 130, "acc": 100, "cat": "Special"},

    # सपोर्ट व बफ मूव्स
    "Swords Dance": {"type": "Normal", "power": 0, "acc": 100, "cat": "Buff_Atk"},
    "Recover": {"type": "Normal", "power": 0, "acc": 100, "cat": "Heal"},
    "Soul Ward": {"type": "Soul", "power": 0, "acc": 100, "cat": "Shield"}
}

TYPE_ADVANTAGE = {
    "Fire": {"Grass": 2.0, "Water": 0.5, "Rock": 0.5},
    "Water": {"Fire": 2.0, "Grass": 0.5, "Ground": 2.0},
    "Ground": {"Fire": 2.0, "Electric": 2.0, "Grass": 0.5},
    "Ghost": {"Normal": 0.0, "Psychic": 2.0},
    "Fighting": {"Normal": 2.0, "Rock": 2.0, "Ghost": 0.0},
    # Soul Type: Normal हमलों का कोई प्रभाव नहीं (0.0x Immunity)
    "Soul": {"Ghost": 2.0, "Psychic": 2.0, "Dark": 2.0, "Normal": 1.0},
    "Normal": {"Ghost": 0.0, "Soul": 0.0}
}

POKEMON_DATABASE = {
    # स्टार्टर्स (Bharat Region)
    "Tusklet": {
        "type": "Ground",
        "base_hp": 160,
        "atk": 65,
        "defense": 60,
        "spd": 55,
        "base_moves": ["Mud-Slap", "Tackle", "Swords Dance", "Earthquake"],
        "unlocked_moves": ["Body Slam", "Recover", "Stone Edge", "Surf"]
    },
    "Pyrohawk": {
        "type": "Fire",
        "base_hp": 140,
        "atk": 75,
        "defense": 50,
        "spd": 80,
        "base_moves": ["Ember", "Scratch", "Flamethrower", "Swords Dance"],
        "unlocked_moves": ["Dragon Claw", "Recover", "Close Combat", "Stone Edge"]
    },
    "Tidaljaw": {
        "type": "Water",
        "base_hp": 150,
        "atk": 70,
        "defense": 65,
        "spd": 50,
        "base_moves": ["Water Gun", "Tackle", "Surf", "Recover"],
        "unlocked_moves": ["Earthquake", "Dragon Claw", "Body Slam", "Stone Edge"]
    },

    # वाइल्ड रूट्स के क्रिएचर्स
    "Duskulf": {
        "type": "Ghost",
        "base_hp": 120,
        "atk": 60,
        "defense": 45,
        "spd": 70,
        "base_moves": ["Shadow Ball", "Scratch", "Recover", "Thunderbolt"],
        "unlocked_moves": []
    },
    "Mungor": {
        "type": "Ground",
        "base_hp": 135,
        "atk": 68,
        "defense": 55,
        "spd": 60,
        "base_moves": ["Mud-Slap", "Scratch", "Earthquake", "Tackle"],
        "unlocked_moves": []
    },

    # लेजेंडरी टाइटन्स
    "Tygrathor": {
        "type": "Soul",
        "base_hp": 240,
        "atk": 130,
        "defense": 100,
        "spd": 110,
        "base_moves": ["Flamethrower", "Dragon Claw", "Soul Burn", "Soul Ward"],
        "unlocked_moves": ["Close Combat", "Earthquake", "Recover", "Stone Edge"]
    },
    "Corruptox": {
        "type": "Poison",
        "base_hp": 250,
        "atk": 110,
        "defense": 120,
        "spd": 85,
        "base_moves": ["Cataclysmic Decay", "Shadow Ball", "Earthquake", "Recover"],
        "unlocked_moves": ["Body Slam", "Close Combat", "Stone Edge", "Flamethrower"]
    }
}
