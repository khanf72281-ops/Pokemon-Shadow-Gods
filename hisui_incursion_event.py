"""
Pokemon Multiverse Engine: Hisui Space-Time Incursion Event
Timeline: Modern Sinnoh/Universe 1 -> Ancient Hisui Era Rift

Key Mechanics:
1. Space-Time Distortion Zone: Sky turns purple, ancient wild alphas spawn.
2. Ancient Battle Styles:
   - Agile Style: Move power -20%, Priority/Speed +1 (Quick turn order).
   - Strong Style: Move power +30%, Turn recovery delay (Opponent gets priority).
3. Hisuian Form Trigger: Certain Pokemon evolve into or adapt their Hisuian variants.
4. Origin Dialga / Palkia Temporal Rift Bridge to Universe 2.
"""

from typing import Dict, List, Optional
from src.core.models import Pokemon, Move

class HisuiIncursionZone:
    def __init__(self):
        self.zone_name = "Corrupted Space-Time Rift (Ancient Hisui)"
        self.distortion_active = True
        self.weather = "Temporal Blizzard / Pitch-Black Sky"

    def apply_battle_style(self, move: Move, style: str) -> Dict[str, any]:
        """Strong Style aur Agile Style mechanics calculation."""
        base_power = move.power
        speed_modifier = 0

        if style.lower() == "agile":
            modified_power = int(base_power * 0.8)
            speed_modifier = 2  # Action priority increase
            action_desc = f"{move.name} executed in AGILE STYLE! Fast execution, lower base power."
        elif style.lower() == "strong":
            modified_power = int(base_power * 1.3)
            speed_modifier = -2  # Turn delay penalty
            action_desc = f"{move.name} executed in STRONG STYLE! Devastating blow with action delay."
        else:
            modified_power = base_power
            action_desc = f"{move.name} executed normally."

        return {
            "move_name": move.name,
            "style": style,
            "final_power": modified_power,
            "priority_shift": speed_modifier,
            "description": action_desc
        }

    def trigger_hisuian_form_adaptation(self, pokemon: Pokemon) -> Dict[str, str]:
        """Hisui era ke ancient rift exposure se specific Pokemon adapt hote hain."""
        adaptation_map = {
            "Typhlosion": {"types": ("Fire", "Ghost"), "ability": "Frisk"},
            "Samurott": {"types": ("Water", "Dark"), "ability": "Sharpness"},
            "Decidueye": {"types": ("Grass", "Fighting"), "ability": "Scrappy"},
            "Zoroark": {"types": ("Normal", "Ghost"), "ability": "Illusion"},
            "Braviary": {"types": ("Psychic", "Flying"), "ability": "Sheer Force"}
        }

        if pokemon.name in adaptation_map:
            new_data = adaptation_map[pokemon.name]
            pokemon.types = new_data["types"]
            pokemon.ability = new_data["ability"]
            return {
                "status": "adapted",
                "message": (
                    f"🌌 ANCIENT RIFT ENERGY RESONATES! {pokemon.name} has adapted "
                    f"into its Hisuian Form! New Typing: {pokemon.types[0]}/{pokemon.types[1]}!"
                )
            }
        
        return {
            "status": "unchanged",
            "message": f"{pokemon.name} holds standard form under Hisuian atmospheric pressure."
        }


if __name__ == "__main__":
    print("=" * 65)
    print("   HISUI INCLUSION EVENT: SPACE-TIME COLLAPSE SIMULATION")
    print("=" * 65)

    hisui_rift = HisuiIncursionZone()
    print(f"\n[Zone Alert] Active Field: {hisui_rift.zone_name}")
    print(f"             Weather: {hisui_rift.weather}")

    # Setup Hisui target
    zoroark = Pokemon(
        name="Zoroark",
        types=("Dark", None),
        max_hp=324, current_hp=324,
        attack=305, defense=219, sp_attack=339, sp_defense=219, speed=339,
        ability="Illusion",
        moveset=[
            Move("Bitter Malice", "Ghost", 75, 100, "Special", "Lowers target attack."),
            Move("Hyper Voice", "Normal", 90, 100, "Special", "Sound-based blast.")
        ]
    )

    print(f"\n[1] Entering Distortion: Current Zoroark Type: {zoroark.types[0]}")
    adapt_log = hisui_rift.trigger_hisuian_form_adaptation(zoroark)
    print(f"    {adapt_log['message']}")

    # Battle Styles Test
    attack_move = zoroark.moveset[0]
    print("\n[2] Ancient Battle Style Execution:")
    agile_calc = hisui_rift.apply_battle_style(attack_move, style="Agile")
    print(f"    -> {agile_calc['description']} (Power: {agile_calc['final_power']})")

    strong_calc = hisui_rift.apply_battle_style(attack_move, style="Strong")
    print(f"    -> {strong_calc['description']} (Power: {strong_calc['final_power']})")

    print("=" * 65)
