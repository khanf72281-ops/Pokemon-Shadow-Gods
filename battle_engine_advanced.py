# battle_engine_advanced.py
import random

TYPE_CHART = {
    "Normal":   {"Rock": 0.5, "Ghost": 0.0, "Steel": 0.5},
    "Fire":     {"Fire": 0.5, "Water": 0.5, "Grass": 2.0, "Ice": 2.0, "Bug": 2.0, "Rock": 0.5, "Dragon": 0.5, "Steel": 2.0},
    "Water":    {"Fire": 2.0, "Water": 0.5, "Grass": 0.5, "Ground": 2.0, "Rock": 2.0, "Dragon": 0.5},
    "Grass":    {"Fire": 0.5, "Water": 2.0, "Grass": 0.5, "Poison": 0.5, "Ground": 2.0, "Flying": 0.5, "Bug": 0.5, "Rock": 2.0, "Dragon": 0.5, "Steel": 0.5},
    "Electric": {"Water": 2.0, "Grass": 0.5, "Electric": 0.5, "Ground": 0.0, "Flying": 2.0, "Dragon": 0.5},
    "Ice":      {"Fire": 0.5, "Water": 0.5, "Grass": 2.0, "Ice": 0.5, "Ground": 2.0, "Flying": 2.0, "Dragon": 2.0, "Steel": 0.5},
    "Fighting": {"Normal": 2.0, "Ice": 2.0, "Poison": 0.5, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Rock": 2.0, "Ghost": 0.0, "Dark": 2.0, "Steel": 2.0},
    "Poison":   {"Grass": 2.0, "Poison": 0.5, "Ground": 0.5, "Rock": 0.5, "Ghost": 0.5, "Steel": 0.0},
    "Ground":   {"Fire": 2.0, "Electric": 2.0, "Grass": 0.5, "Poison": 2.0, "Flying": 0.0, "Bug": 0.5, "Rock": 2.0, "Steel": 2.0},
    "Flying":   {"Grass": 2.0, "Electric": 0.5, "Fighting": 2.0, "Bug": 2.0, "Rock": 0.5, "Steel": 0.5},
    "Psychic":  {"Fighting": 2.0, "Poison": 2.0, "Psychic": 0.5, "Dark": 0.0, "Steel": 0.5},
    "Bug":      {"Fire": 0.5, "Grass": 2.0, "Fighting": 0.5, "Poison": 0.5, "Flying": 0.5, "Psychic": 2.0, "Ghost": 0.5, "Dark": 2.0, "Steel": 0.5},
    "Rock":     {"Fire": 2.0, "Ice": 2.0, "Fighting": 0.5, "Ground": 0.5, "Flying": 2.0, "Bug": 2.0, "Steel": 0.5},
    "Ghost":    {"Normal": 0.0, "Psychic": 2.0, "Ghost": 2.0, "Dark": 0.5},
    "Dragon":   {"Dragon": 2.0, "Steel": 0.5},
    "Steel":    {"Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Ice": 2.0, "Rock": 2.0, "Steel": 0.5},
    "Dark":     {"Fighting": 0.5, "Psychic": 2.0, "Ghost": 2.0, "Dark": 0.5},
    "Soul":     {"Soul": 2.0, "Ghost": 2.0, "Dark": 1.5, "Normal": 0.5}  # Custom Universe 2 Type
}

ADVANCED_MOVES = {
    # 8-Move Master Signature Moves
    "Eternal Soul Void": {"type": "Soul", "power": 130, "acc": 90, "effect": "toxic_burn"},
    "Cataclysmic Decay": {"type": "Poison", "power": 110, "acc": 95, "effect": "decay"},
    "Psystrike":         {"type": "Psychic", "power": 100, "acc": 100, "effect": "physical_defense_calc"},
    "Tectonic Stomp":    {"type": "Ground", "power": 100, "acc": 100, "effect": "flinch"},
    "Infernal Pounce":   {"type": "Fire", "power": 95, "acc": 100, "effect": "speed_boost"},
    "Chambal Surge":     {"type": "Water", "power": 95, "acc": 100, "effect": "lower_speed"},
    "Temporal Void":     {"type": "Ghost", "power": 100, "acc": 95, "effect": "paralyze"},
    "Soul Burn":         {"type": "Soul", "power": 110, "acc": 90, "effect": "burn"}
}

def get_type_multiplier(move_type, target_types):
    multiplier = 1.0
    for t in target_types:
        if move_type in TYPE_CHART and t in TYPE_CHART[move_type]:
            multiplier *= TYPE_CHART[move_type][t]
    return multiplier

def execute_turn(attacker, defender, move_name):
    """डैमेज, टाइप एडवांटेज और 8-मूव स्लॉट एक्ज़ीक्यूशन"""
    move = ADVANCED_MOVES.get(move_name, {"type": "Normal", "power": 50, "acc": 100})
    
    # Accuracy check
    if random.randint(1, 100) > move.get("acc", 100):
        print(f"💨 {attacker.name} का {move_name} मिस हो गया!")
        return 0

    mult = get_type_multiplier(move["type"], defender.type if isinstance(defender.type, list) else [defender.type])
    base_dmg = (((2 * attacker.level / 5 + 2) * move["power"] * (attacker.atk / max(1, defender.defense))) / 50) + 2
    total_dmg = int(base_dmg * mult * random.uniform(0.85, 1.0))
    defender.current_hp = max(0, defender.current_hp - total_dmg)

    print(f"💥 {attacker.name} ने {move_name} इस्तेमाल किया! ({total_dmg} डैमेज)")
    if mult > 1.0:
        print("🎯 यह बहुत असरदार था (Super Effective)!")
    elif mult < 1.0 and mult > 0:
        print("🛡️ यह ज्यादा असरदार नहीं था...")
    elif mult == 0:
        print("❌ इसका कोई असर नहीं हुआ!")

    return total_dmg
