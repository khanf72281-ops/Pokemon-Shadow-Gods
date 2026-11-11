# ==============================================================================
# 2. COMBAT & CORE LOGIC ENGINE (engine.py)
# ==============================================================================
import random
from pokemon_data import MOVE_DATABASE, TYPE_ADVANTAGE, POKEMON_DATABASE

class Pokemon:
    def __init__(self, name: str, level: int = 5):
        data = POKEMON_DATABASE[name]
        self.name = name
        self.level = level
        self.type = data["type"]
        self.max_hp = data["base_hp"] + (level * 2)
        self.current_hp = self.max_hp
        self.atk = data["atk"] + level
        self.defense = data["defense"] + level
        self.spd = data["spd"] + level
        self.moves = list(data["base_moves"])
        self.atk_mult = 1.0

    def unlock_8_moves(self):
        """प्रोफेसर नीम से वॉच मिलने के बाद बाकी 4 स्लॉट अनलॉक"""
        extra = POKEMON_DATABASE[self.name]["unlocked_moves"]
        self.moves.extend(extra)
        self.moves = self.moves[:8]

    def is_fainted(self):
        return self.current_hp <= 0

class BattleEngine:
    @staticmethod
    def calculate_damage(attacker: Pokemon, defender: Pokemon, move_name: str) -> int:
        move = MOVE_DATABASE[move_name]
        if move["power"] == 0:
            return 0

        # टाइप एडवांटेज
        multiplier = TYPE_ADVANTAGE.get(move["type"], {}).get(defender.type, 1.0)
        
        # क्रिटिकल हिट (10% चांस)
        crit = 1.5 if random.random() < 0.10 else 1.0
        
        base = (((2 * attacker.level / 5 + 2) * move["power"] * (attacker.atk * attacker.atk_mult / defender.defense)) / 50) + 2
        dmg = int(base * multiplier * crit)

        if crit > 1.0:
            print("💥 [CRITICAL HIT!] घातक वार!")
        if multiplier > 1.0:
            print("⚡ [SUPER EFFECTIVE!] यह हमला बहुत असरदार था!")
        elif multiplier == 0.0:
            print("🚫 [NO EFFECT!] सोल टाइप पर नॉर्मल हमले का कोई असर नहीं हुआ!")
            return 0
        elif multiplier < 1.0:
            print("🛡️ [NOT VERY EFFECTIVE] हमले का असर कम हुआ...")

        return dmg

    @staticmethod
    def run_turn(player_mon: Pokemon, enemy_mon: Pokemon, p_move: str):
        e_move = random.choice(enemy_mon.moves)
        order = [(player_mon, enemy_mon, p_move, "Player"), (enemy_mon, player_mon, e_move, "Enemy")]
        
        # स्पीड के आधार पर टर्न क्रम
        if enemy_mon.spd > player_mon.spd:
            order.reverse()

        for atk, dfd, m_name, side in order:
            if atk.is_fainted():
                continue

            print(f"\n▶ [{side}] {atk.name} ने '{m_name}' का उपयोग किया!")
            m_info = MOVE_DATABASE[m_name]

            if m_info["cat"] == "Buff_Atk":
                atk.atk_mult += 0.5
                print(f"🔥 {atk.name} का Attack जोश से बढ़ गया!")
            elif m_info["cat"] == "Heal":
                heal = int(atk.max_hp * 0.5)
                atk.current_hp = min(atk.max_hp, atk.current_hp + heal)
                print(f"💚 {atk.name} ने अपनी HP रिकवर की! ({atk.current_hp}/{atk.max_hp})")
            else:
                dmg = BattleEngine.calculate_damage(atk, dfd, m_name)
                dfd.current_hp = max(0, dfd.current_hp - dmg)
                print(f"🩸 {dfd.name} को {dmg} का डैमेज लगा! (HP: {dfd.current_hp}/{dfd.max_hp})")

            if dfd.is_fainted():
                print(f"💀 {dfd.name} फेंट हो गया!")
                break
