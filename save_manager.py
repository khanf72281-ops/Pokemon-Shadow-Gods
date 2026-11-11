# save_manager.py
import json
import os

SAVE_FILE = "save_game.json"

class SaveLoadSystem:
    @staticmethod
    def save_game(player_data):
        """Player ke current progress ko JSON format me write karta hai"""
        try:
            # Party ke Pokemon ko serializable dictionary me convert karna
            party_serialized = []
            for mon in player_data["party"]:
                party_serialized.append({
                    "name": mon.name,
                    "level": mon.level,
                    "type": mon.type,
                    "max_hp": mon.max_hp,
                    "current_hp": mon.current_hp,
                    "atk": mon.atk,
                    "defense": mon.defense,
                    "spe": mon.spe,
                    "moves": mon.moves
                })

            data_to_save = {
                "player_name": player_data["player_name"],
                "current_region": player_data["current_region"],
                "player_pos": player_data["player_pos"],
                "badges": player_data["badges"],
                "caught_dex": list(player_data.get("caught_dex", [])),
                "party": party_serialized
            }

            with open(SAVE_FILE, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, indent=4)
            print("💾 Game successfully save ho gaya (save_game.json)!")
            return True
        except Exception as e:
            print(f"❌ Save karne me dikkat aayi: {e}")
            return False

    @staticmethod
    def load_game(pokemon_class):
        """Save file check karta hai aur Pokemon objects recreate karta hai"""
        if not os.path.exists(SAVE_FILE):
            print("⚠️ Koi purana save file nahi mila!")
            return None

        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Rebuilding Pokemon objects from dictionary
            restored_party = []
            for mon_dict in data["party"]:
                mon = pokemon_class(mon_dict["name"], level=mon_dict["level"])
                mon.type = mon_dict["type"]
                mon.max_hp = mon_dict["max_hp"]
                mon.current_hp = mon_dict["current_hp"]
                mon.atk = mon_dict["atk"]
                mon.defense = mon_dict["defense"]
                mon.spe = mon_dict["spe"]
                mon.moves = mon_dict["moves"]
                restored_party.append(mon)

            data["party"] = restored_party
            print("📂 Purana save game safaltapoorvak load ho gaya!")
            return data
        except Exception as e:
            print(f"❌ Load karne me dikkat aayi: {e}")
            return None
