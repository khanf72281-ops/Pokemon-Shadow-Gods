# universe2_engine.py
import sys
import random
from universe2_dex import UNIVERSE2_POKEDEX
from bharat_regions_data import BHARAT_WORLD
from combat_resolver import resolve_attack
from save_manager import SaveLoadSystem

class Combatant:
    def __init__(self, name, level=5):
        self.name = name
        self.level = level
        spec = UNIVERSE2_POKEDEX.get(name, UNIVERSE2_POKEDEX["Tusklet"])
        self.type = spec["type"]
        self.max_hp = int(spec["stats"]["hp"] + (level * 2.2))
        self.current_hp = self.max_hp
        self.atk = int(spec["stats"]["atk"] + (level * 1.5))
        self.defense = int(spec["stats"]["def"] + (level * 1.5))
        self.spe = int(spec["stats"]["spe"] + (level * 1.2))
        self.moves = list(spec["moves"])

    def is_alive(self):
        return self.current_hp > 0

class Universe2Runtime:
    def __init__(self):
        self.player_name = "Cosmic Traveler"
        self.current_loc = "Tarana"
        self.party = []
        self.badges = []

    def start_tarana_rescue(self):
        print("\n" + "=" * 70)
        print("🌌 [CRASH LANDING: UNIVERSE 2 - TARANA, MADHYA PRADESH]")
        print("=" * 70)
        print("आप अनगिनत प्रकाश वर्ष के शून्य से निकलकर लाल मिट्टी के टीलों पर गिरे हैं...")
        print("जंगली पोकेमोन ने आपको घेर लिया था, तभी एक जोरदार गूंज सुनाई दी:")
        print("'AIRAVALON, USE TECTONIC STOMP!'")
        print("\n👨‍🔬 प्रोफेसर रहीम ने आपको संभाला और अपनी इको-आर्कियो लैब में ले आए।")
        print("प्रोफेसर रहीम: 'तुम एक अनंत कॉस्मिक शून्य को पार करके आए हो। यूनिवर्स 2 में तुम्हारा स्वागत है!'")
        print("\nअपना नया स्वदेशी साथी चुनें:")
        print("  1. Tusklet  (Grass/Ground) - मालवा का अडिग हाथी पोकेमोन")
        print("  2. Sherling (Fire)         - विंध्याचल का फुर्तीला शावक")
        print("  3. Gharikid (Water)        - चंबल का जलीय शिकारी")

        picks = {"1": "Tusklet", "2": "Sherling", "3": "Gharikid"}
        choice = input("विकल्प चुनें (1-3): ").strip()
        starter_name = picks.get(choice, "Tusklet")
        self.party.append(Combatant(starter_name, level=10))
        print(f"✅ [Lv.10 {starter_name}] अब आपकी टीम का मुख्य साथी है!")
        self.game_loop()

    def run_battle(self, enemy_team_data, title="Wild Encounter"):
        print(f"\n--- युद्ध आरंभ: {title} ---")
        enemy_party = [Combatant(name, lvl) for name, lvl in enemy_team_data]
        e_idx = 0
        p_mon = self.party[0]

        while p_mon.is_alive() and e_idx < len(enemy_party):
            e_mon = enemy_party[e_idx]
            print(f"\n[{p_mon.name} HP: {p_mon.current_hp}/{p_mon.max_hp}] VS [{e_mon.name} Lv.{e_mon.level} HP: {e_mon.current_hp}/{e_mon.max_hp}]")
            for i, mv in enumerate(p_mon.moves):
                print(f"  {i+1}. {mv}", end="")
            print()

            action = input("Move चुनें (1-8): ").strip()
            try:
                selected_move = p_mon.moves[int(action)-1]
            except Exception:
                selected_move = p_mon.moves[0]

            # Speed comparison turn
            if p_mon.spe >= e_mon.spe:
                resolve_attack(p_mon, e_mon, selected_move)
                if e_mon.is_alive():
                    resolve_attack(e_mon, p_mon, random.choice(e_mon.moves))
            else:
                resolve_attack(e_mon, p_mon, random.choice(e_mon.moves))
                if p_mon.is_alive():
                    resolve_attack(p_mon, e_mon, selected_move)

            if not e_mon.is_alive():
                print(f"🎯 {e_mon.name} परास्त हुआ!")
                e_idx += 1
                if e_idx < len(enemy_party):
                    print(f"विरोधी ने अगला पोकेमोन भेजा: {enemy_party[e_idx].name}!")

        if p_mon.is_alive():
            print("🏆 आप यह मुकाबला जीत गए!")
            return True
        else:
            print("💀 आपका पोकेमोन बेहोश हो गया! टीम को हील किया गया।")
            p_mon.current_hp = p_mon.max_hp
            return False

    def game_loop(self):
        while True:
            loc = BHARAT_WORLD[self.current_loc]
            print("\n" + "-" * 60)
            print(f"📍 वर्तमान स्थान: {self.current_loc} ({loc['state']}) | बैज: {len(self.badges)}/8")
            print(f"विवरण: {loc['description'] if 'description' in loc else loc['gym_name']}")
            print("कमांड्स: [M] यात्रा करें | [G] जिम चैलेंज | [H] हील | [S] सेव | [Q] बाहर निकलें")
            cmd = input("आदेश: ").strip().lower()

            if cmd == "m":
                destinations = loc["connected_to"]
                print("कहाँ जाना चाहते हैं?")
                for idx, d in enumerate(destinations):
                    print(f"  {idx+1}. {d}")
                dest_choice = input("चुनें: ").strip()
                try:
                    self.current_loc = destinations[int(dest_choice)-1]
                except Exception:
                    pass

            elif cmd == "g":
                if "leader" in loc:
                    if loc["badge"] in self.badges:
                        print("आप यहाँ का बैज पहले ही जीत चुके हैं!")
                    else:
                        print(f"\n🏛️ {loc['leader']} ({loc['gym_name']}) आपको ललकारते हैं!")
                        print(f"कानूनी अनुपालन: {loc['architecture_compliance']}")
                        win = self.run_battle(loc["team"], title=f"Gym Leader {loc['leader']}")
                        if win:
                            self.badges.append(loc["badge"])
                            print(f"🎖️ {loc['badge']} आपके नाम हुआ!")
                elif self.current_loc == "HimalayanLeague":
                    if len(self.badges) < 8:
                        print("🔒 हिमालयन लीग में प्रवेश के लिए सभी 8 राज्यों के बैज आवश्यक हैं!")
                    else:
                        self.trigger_apex_finale()
                else:
                    print("यहाँ कोई आधिकारिक जिम नहीं है।")

            elif cmd == "h":
                for m in self.party:
                    m.current_hp = m.max_hp
                print("🌿 सभी पोकेमोन पूर्ण रूप से स्वस्थ हो गए!")

            elif cmd == "s":
                save_dict = {
                    "player_name": self.player_name, "current_region": self.current_loc,
                    "player_pos": [0, 0], "badges": self.badges, "party": self.party
                }
                SaveLoadSystem.save_game(save_dict)

            elif cmd == "q":
                sys.exit()

    def trigger_apex_finale(self):
        print("\n" + "=" * 70)
        print("🏔️ [BHARAT LEAGUE APEX SHOWDOWN - UTTARAKHAND GEODESIC DOME]")
        print("=" * 70)
        print("ग्रैंड चैंपियन ऋषि: 'तुमने पूरे भारत के 8 राज्यों की आत्मा को समझा है.'")
        print("ग्रैंड चैंपियन ऋषि: 'मल्टीवर्स के इस छोर को सुरक्षित रखने के लिए अंतिम शक्ति को सिद्ध करो!'")
        champ_team = [
            ("Ghorashim", 65), ("Lohashva", 66), ("Garudragon", 67),
            ("Tygrathor", 69), ("TYGRANTOX", 70)
        ]
        cleared = self.run_battle(champ_team, title="Grand Champion Rishi & Apex TYGRANTOX")
        if cleared:
            print("\n" + "★" * 70)
            print("🌟 बधाई! आपने TYGRANTOX को शांत कर दिया!")
            print("यूनिवर्स 1 और यूनिवर्स 2 अब हमेशा के लिए संतुलित हो चुके हैं।")
            print("आप संपूर्ण मल्टीवर्स के सर्वोच्च ग्रैंड चैंपियन घोषित किए जाते हैं!")
            print("★" * 70)
            sys.exit()

if __name__ == "__main__":
    game = Universe2Runtime()
    game.start_tarana_rescue()
