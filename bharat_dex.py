# bharat_dex.py

BHARAT_DEX = {
    # --- MP / CENTRAL FOREST ZONE ---
    1: {
        "name": "Tusklet",
        "type": "Grass/Ground",
        "base_stats": {"hp": 65, "atk": 70, "def": 75, "spa": 45, "spd": 55, "spe": 40},
        "abilities": ["Overgrow", "Thick Fat"],
        "signature_move": "Trunk Slam",
        "evolution": {"level": 16, "to": "Gajarock"}
    },
    2: {
        "name": "Gajarock",
        "type": "Grass/Ground",
        "base_stats": {"hp": 85, "atk": 90, "def": 95, "spa": 60, "spd": 70, "spe": 50},
        "abilities": ["Overgrow", "Thick Fat"],
        "evolution": {"level": 34, "to": "Airavalon"}
    },
    3: {
        "name": "Airavalon",
        "type": "Grass/Ground",
        "base_stats": {"hp": 105, "atk": 115, "def": 120, "spa": 75, "spd": 85, "spe": 60},
        "abilities": ["Overgrow", "Tectonic Guard"],
        "signature_move": "Tectonic Stomp"
    },
    4: {
        "name": "Sherling",
        "type": "Fire",
        "base_stats": {"hp": 50, "atk": 75, "def": 45, "spa": 60, "spd": 50, "spe": 70},
        "abilities": ["Blaze", "Moxie"],
        "signature_move": "Ember Claw",
        "evolution": {"level": 16, "to": "Jwalashardul"}
    },
    5: {
        "name": "Jwalashardul",
        "type": "Fire",
        "base_stats": {"hp": 65, "atk": 95, "def": 60, "spa": 75, "spd": 65, "spe": 90},
        "abilities": ["Blaze", "Moxie"],
        "evolution": {"level": 36, "to": "Vyaghragni"}
    },
    6: {
        "name": "Vyaghragni",
        "type": "Fire/Soul",
        "base_stats": {"hp": 80, "atk": 125, "def": 75, "spa": 90, "spd": 75, "spe": 115},
        "abilities": ["Blaze", "Soul Roar"],
        "signature_move": "Infernal Pounce"
    },
    7: {
        "name": "Gharikid",
        "type": "Water",
        "base_stats": {"hp": 55, "atk": 65, "def": 65, "spa": 50, "spd": 50, "spe": 55},
        "abilities": ["Torrent", "Strong Jaw"],
        "signature_move": "Aqua Snap",
        "evolution": {"level": 18, "to": "Tidaljaw"}
    },
    8: {
        "name": "Tidaljaw",
        "type": "Water",
        "base_stats": {"hp": 75, "atk": 85, "def": 85, "spa": 65, "spd": 65, "spe": 65},
        "abilities": ["Torrent", "Strong Jaw"],
        "evolution": {"level": 35, "to": "Makardus"}
    },
    9: {
        "name": "Makardus",
        "type": "Water/Steel",
        "base_stats": {"hp": 95, "atk": 110, "def": 125, "spa": 70, "spd": 85, "spe": 75},
        "abilities": ["Torrent", "Iron Jaw"],
        "signature_move": "Chambal Surge"
    },

    # --- EARLY ROUTE ENCOUNTERS ---
    10: {
        "name": "Mungor",
        "type": "Ground",
        "base_stats": {"hp": 45, "atk": 60, "def": 40, "spa": 30, "spd": 40, "spe": 75},
        "abilities": ["Run Away", "Quick Feet"],
        "evolution": {"level": 20, "to": "Nakulor"}
    },
    11: {
        "name": "Duskulf",
        "type": "Ghost",
        "base_stats": {"hp": 50, "atk": 70, "def": 45, "spa": 50, "spd": 50, "spe": 65},
        "abilities": ["Infiltrator", "Shadow Tag"],
        "evolution": {"level": 25, "to": "Bhediator"}
    },

    # --- LEGENDARY APEX BOSSES ---
    497: {
        "name": "Corruptox",
        "type": "Poison/Dark",
        "base_stats": {"hp": 115, "atk": 110, "def": 120, "spa": 135, "spd": 110, "spe": 90},
        "abilities": ["Toxic Miasma"],
        "signature_move": "Cataclysmic Decay"
    },
    498: {
        "name": "Tygrathor",
        "type": "Soul/Fire",
        "base_stats": {"hp": 110, "atk": 135, "def": 100, "spa": 120, "spd": 95, "spe": 120},
        "abilities": ["Sacred Aura"],
        "signature_move": "Soul Burn"
    },
    500: {
        "name": "TYGRANTOX",
        "type": "Soul/Poison",
        "base_stats": {"hp": 140, "atk": 155, "def": 135, "spa": 155, "spd": 125, "spe": 110},
        "abilities": ["Multiverse Void"],
        "signature_move": "Eternal Soul Void"
    }
}

class BharatPokedexManager:
    def __init__(self):
        self.dex = BHARAT_DEX

    def get_pokemon_info(self, dex_no: int):
        return self.dex.get(dex_no, None)

    def search_by_name(self, name: str):
        for dex_no, data in self.dex.items():
            if data["name"].lower() == name.lower():
                return dex_no, data
        return None, None
