# ==============================================================================
# 3. MAIN GAME RUNNER (main.py)
# ==============================================================================
import random
from engine import Pokemon, BattleEngine

def start_game():
    print("=" * 65)
    print("⚡ POKEMON: SHADOW GODS - SUPREME PROTOTYPE ENGINE (60 FPS)")
    print("=" * 65)

    # 1. स्टार्टर का चुनाव
    print("\nअपना स्टार्टर चुनें:")
    print("1. Tusklet (Ground)")
    print("2. Pyrohawk (Fire)")
    print("3. Tidaljaw (Water)")
    
    choice = input("नंबर डालें (1-3): ").strip()
    starter_map = {"1": "Tusklet", "2": "Pyrohawk", "3": "Tidaljaw"}
    p_name = starter_map.get(choice, "Tusklet")
    
    player_pokemon = Pokemon(p_name, level=5)
    print(f"\n🎉 आपने {player_pokemon.name} चुना!")

    # 2. तराणा कस्बे में प्रोफेसर नीम का इवेंट
    print("\n[इवेंट]: आप तराणा कस्बे में प्रोफेसर नीम की लैब पहुँचे...")
    print("👨‍🔬 प्रो. नीम: 'यह लो Tactical Watch! अब तुम्हारे पोकेमोन के 8 स्लॉट खुल गए!'")
    player_pokemon.unlock_8_moves()
    print(f"✅ {player_pokemon.name} के सभी 8 मूव अनलॉक हो चुके हैं:\n   {player_pokemon.moves}\n")

    # 3. एक्सप्लोरेशन व एनकाउंटर लूप
    while True:
        cmd = input("\nकमांड दें: 'w' (घास में आगे बढ़ें) | 'q' (बाहर निकलें): ").strip().lower()
        if cmd == 'q':
            print("गेम सुरक्षित बंद हो गया।")
            break
        elif cmd == 'w':
            if random.random() < 0.60:
                wild_mon = Pokemon("Duskulf", level=4)
                print("\n" + "=" * 45)
                print(f"⚠️ झाड़ियों से जंगली {wild_mon.name} बाहर आया!")
                print("=" * 45)

                while not player_pokemon.is_fainted() and not wild_mon.is_fainted():
                    print(f"\n[{player_pokemon.name}] HP: {player_pokemon.current_hp}/{player_pokemon.max_hp}")
                    print(f"[{wild_mon.name}] HP: {wild_mon.current_hp}/{wild_mon.max_hp}")
                    print("टैक्टिकल व्हील (Moves):")
                    for idx, m in enumerate(player_pokemon.moves):
                        print(f"  {idx+1}. {m}")
                    
                    m_choice = input("मूव चुनें (1-8): ").strip()
                    if m_choice.isdigit() and 1 <= int(m_choice) <= len(player_pokemon.moves):
                        chosen_move = player_pokemon.moves[int(m_choice) - 1]
                        BattleEngine.run_turn(player_pokemon, wild_mon, chosen_move)
                    else:
                        print("अमान्य नंबर! सही स्लॉट चुनें।")

                if not player_pokemon.is_fainted():
                    print(f"\n🏆 जीत! आपने {wild_mon.name} को हरा दिया!")
            else:
                print("रास्ता साफ़ है, कोई जंगली क्रिएचर नहीं दिखा।")

if __name__ == "__main__":
    start_game()
# main.py के overworld_loop फंक्शन के अंदर:
cmd = input("Command: ").strip().lower()

if cmd in ["w", "a", "s", "d"]:
    # movement logic...
    pass
elif cmd == "s":
    save_data = {
        "player_name": self.player_name,
        "current_region": "Bharat_MP",
        "player_pos": self.player_pos,
        "badges": self.badges,
        "party": [self.starter]
    }
    SaveLoadSystem.save_game(save_data)
elif cmd == "l":
    loaded_data = SaveLoadSystem.load_game(Pokemon)
    if loaded_data:
        self.player_name = loaded_data["player_name"]
        self.player_pos = loaded_data["player_pos"]
        self.badges = loaded_data["badges"]
        self.starter = loaded_data["party"][0]
        print(f"Swagat hai wapas, {self.player_name}! Position: {self.player_pos}")
import input_handler

# लूप के अंदर:
if not input_handler.handle_save_load(cmd, self, Pokemon):
    # बाकी मूवमेंट और बैटल कमांड्स
    pass
