"""
Pokemon: Shadow Gods - Universal FireRed-Style Cheat Console
Format: Classic GameShark / Action Replay Hex Codes
Rules:
  - Master Code activation required before execution.
  - Wild modifier covers native standard species across Gen 1-9 (Legendaries & Mythicals excluded).
  - Built-in toggles for WTW, 100% Shiny rate, and OHKO.
"""

from typing import Dict, Any, List

class FireRedCheatConsole:
    # Iconic FireRed Master Code
    MASTER_CODE = "000014D1 000A"
    
    # Classic Hex Mapping
    CODE_MAP = {
        "82025838 104E": "INFINITE_MONEY",
        "509197D3 542975F4": "WALK_THROUGH_WALLS",
        "167AE3E4 7E0AC77A": "SHINY_ENCOUNTER_100",
        "B7494816 432AC198": "ONE_HIT_KO",
        "82003884 0001": "GIVE_MASTER_BALLS",
        "82003884 0044": "GIVE_RARE_CANDIES",
        "82003884 0013": "INFINITE_FULL_RESTORES",
        "82003884 0019": "INFINITE_MAX_REVIVES",
        "82003884 0047": "INFINITE_PP_MAX",
        "82025840 0001": "UNLOCK_ALL_TMS_HMS_PC"
    }

    # Standard non-legendary wild pool (Gen 1-9 representation)
    ALLOWED_WILD_SPECIES = [
        "Pidgey", "Rattata", "Zubat", "Geodude", "Gastly", "Abra", "Machop",
        "Sentret", "Hoothoot", "Mareep", "Marill", "Wooper", "Swinub", "Larvitar",
        "Poochyena", "Zigzagoon", "Taillow", "Ralts", "Aron", "Spheal", "Bagon",
        "Starly", "Bidoof", "Shinx", "Gible", "Riolu", "Croagunk", "Snover",
        "Pidove", "Roggenrola", "Timburr", "Venipede", "Sandile", "Axew", "Deino",
        "Fletchling", "Bunnelby", "Honedge", "Goomy", "Phantump", "Noibat",
        "Pikipek", "Yungoos", "Rockruff", "Mareanie", "Mudbray", "Jangmo-o",
        "Rookidee", "Wooloo", "Chewtle", "Rolycoly", "Dreepy",
        "Lechonk", "Tarountula", "Pawmi", "Nacli", "Tinkatink", "Frigibax"
    ]

    def __init__(self, trainer_state: Dict[str, Any]):
        self.state = trainer_state
        self.master_code_active = False

    def activate_master_code(self, input_code: str) -> bool:
        if input_code.strip().upper() == self.MASTER_CODE:
            self.master_code_active = True
            print("🔑 [MASTER CODE ACCEPTED]: Hook active. Cheat memory unlocked.")
            return True
        print("❌ [ACCESS DENIED]: Invalid Master Code. Enter '000014D1 000A'.")
        return False

    def enter_code(self, raw_code: str):
        if not self.master_code_active:
            print("⚠️ [BLOCKED]: Pehle Master Code activate karna zaroori hai.")
            return

        code = raw_code.strip().upper()
        action = self.CODE_MAP.get(code)

        if not action:
            print(f"❌ [UNKNOWN CODE]: '{code}' is not recognized.")
            return

        # Execute mapped function
        if action == "INFINITE_MONEY":
            self.state["money"] = 999999
            print("💰 [CHEAT ON]: 999,999 Pokédollars added.")

        elif action == "WALK_THROUGH_WALLS":
            self.state["collision_disabled"] = not self.state.get("collision_disabled", False)
            status = "ENABLED" if self.state["collision_disabled"] else "DISABLED"
            print(f"🧱 [WTW {status}]: Collision checks bypassed.")

        elif action == "SHINY_ENCOUNTER_100":
            self.state["force_shiny"] = True
            print("✨ [SHINY ON]: All subsequent wild encounters will be Shiny.")

        elif action == "ONE_HIT_KO":
            self.state["ohko_active"] = True
            print("💥 [OHKO ON]: Enemy Pokémon faint in a single strike.")

        elif action == "GIVE_MASTER_BALLS":
            self.state.setdefault("bag", {})["Master Ball"] = self.state.get("bag", {}).get("Master Ball", 0) + 99
            print("🟣 [BAG]: 99x Master Balls received.")

        elif action == "GIVE_RARE_CANDIES":
            self.state.setdefault("bag", {})["Rare Candy"] = self.state.get("bag", {}).get("Rare Candy", 0) + 99
            print("🍬 [BAG]: 99x Rare Candies received.")

        elif action == "INFINITE_FULL_RESTORES":
            self.state.setdefault("bag", {})["Full Restore"] = 999
            print("🧪 [BAG]: 999x Full Restores stocked.")

        elif action == "INFINITE_MAX_REVIVES":
            self.state.setdefault("bag", {})["Max Revive"] = 999
            print("💎 [BAG]: 999x Max Revives stocked.")

        elif action == "INFINITE_PP_MAX":
            self.state.setdefault("bag", {})["PP Max"] = 999
            print("⚡ [BAG]: 999x PP Max stocked.")

        elif action == "UNLOCK_ALL_TMS_HMS_PC":
            all_items = [f"TM{str(i).zfill(2)}" for i in range(1, 101)] + [f"HM0{i}" for i in range(1, 9)]
            self.state.setdefault("pc_storage", {})["TM_HM_CASE"] = all_items
            print(f"💾 [PC STORAGE]: Sabhi 100 TMs aur 8 HMs PC inventory mein load ho gaye.")

    def set_wild_pokemon_modifier(self, species_name: str):
        """Standard Wild Pokémon Modifier (Legendaries/Mythicals excluded)."""
        if not self.master_code_active:
            print("⚠️ [BLOCKED]: Pehle Master Code activate karna zaroori hai.")
            return

        normalized = species_name.capitalize().strip()
        if normalized in self.ALLOWED_WILD_SPECIES:
            self.state["next_wild_encounter"] = normalized
            print(f"🎯 [WILD MODIFIER]: Next wild Pokémon locked to -> {normalized}!")
        else:
            print(f"⛔ [REJECTED]: '{species_name}' is invalid or protected (Legendaries/Mythicals excluded).")


if __name__ == "__main__":
    player = {
        "name": "Farhan",
        "money": 500,
        "bag": {},
        "pc_storage": {},
        "collision_disabled": False,
        "force_shiny": False,
        "ohko_active": False
    }

    console = FireRedCheatConsole(player)

    # 1. Activate Master Code
    console.activate_master_code("000014D1 000A")

    # 2. FireRed Style Codes Trigger
    console.enter_code("82025838 104E")        # Infinite Money
    console.enter_code("509197D3 542975F4")    # Walk Through Walls
    console.enter_code("167AE3E4 7E0AC77A")    # 100% Shiny
    console.enter_code("B7494816 432AC198")    # One-Hit KO
    console.enter_code("82025840 0001")        # All TMs & HMs to PC

    # 3. Wild Modifier (Gible allow hoga, Mew/Arceus reject honge)
    console.set_wild_pokemon_modifier("Gible")
    console.set_wild_pokemon_modifier("Mewtwo")
