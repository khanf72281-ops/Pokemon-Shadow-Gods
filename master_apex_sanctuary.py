"""
Pokemon: Shadow Gods - The Master's Apex Sanctuary
Progression:
1. Northern Championship Victory -> Unlocks the legendary item: "Master's Apex Map".
2. Apex Map decodes coordinates to the summit of 'Mt. Origin'.
3. The Reigning Pokemon Master (Reigning Monarch Red / Sovereign Champion) challenges the player.
4. Defeating the Reigning Master grants the official 'POKEMON MASTER' mantle.
5. Immediate Emergency Alert: Prof. Oak triggers the Pallet Town singularity summons.
"""

from typing import Dict, List

class ApexSanctuaryEngine:
    def __init__(self, trainer_name: str = "Farhan"):
        self.trainer_name = trainer_name
        self.has_apex_map = False
        self.map_coordinates = "Coordinates Hidden"
        self.is_true_pokemon_master = False

    def award_apex_map(self):
        """Northern Championship jeetne par tournament committee ye map deti hai."""
        self.has_apex_map = True
        self.map_coordinates = "Mt. Origin Summit (Beyond Cloud Layer, Latitude 0.00)"
        print("\n" + "=" * 65)
        print("📜 [TOURNAMENT REWARD] You received the MASTER'S APEX MAP!")
        print("=" * 65)
        print("  Official: 'Northern Championship sirf ek qualifying test tha!'")
        print("  Official: 'Asli Pokemon Master is duniya ke top peak par rehte hain.'")
        print(f"  Map Decoded: {self.map_coordinates}")
        print("=" * 65)

    def climb_to_sanctuary(self):
        """Map ke through summit par reach karne ka event."""
        if not self.has_apex_map:
            print("\n[LOCKED] Aapko pehle Northern Championship jeet kar Apex Map lena hoga!")
            return False

        print(f"\n🏔️  {self.trainer_name} climbs the treacherous frozen paths of Mt. Origin...")
        print("    -> Atmospheric pressure drops.")
        print("    -> The clouds clear, revealing the ancient Sky Temple Arena.")
        print("    -> Standing at the center is the CURRENT POKÉMON MASTER!")
        return True

    def battle_reigning_master(self):
        """Reigning Master ke khilaf final 6v6 gauntlet."""
        print("\n" + "=" * 65)
        print("👑 DUEL FOR THE THRONE: CHALLENGING THE REIGNING MASTER")
        print("=" * 65)
        print("Reigning Master: '...So, another challenger has crossed the Northern gates.'")
        print("Reigning Master sends out: Level 90 Pikachu with Light Ball aura!")
        print(f"-> {self.trainer_name} counters with high-tier competitive strategy!")
        print("-> Reigning Master activates Triple Phenomena: Mega -> Gigantamax -> Tera!")
        print(f"-> {self.trainer_name} executes tactical counters with flawless precision!")
        print("-> The Master's final ace falls!")
        
        self.is_true_pokemon_master = True
        print("\n" + "*" * 65)
        print(f"🏆 ALL HAIL! {self.trainer_name} HAS DEFEATED THE REIGNING MASTER! 🏆")
        print(f"👑 {self.trainer_name} IS NOW OFFICIALLY THE NEW POKÉMON MASTER! 👑")
        print("*" * 65)
        return True

    def emergency_oak_transmission(self):
        """Master banne ke turant baad Prof. Oak ka emergency call."""
        if not self.is_true_pokemon_master:
            return

        print("\n🚨 [COMMUNICATION DEVICE BEEPING AGGRESSIVELY] 🚨")
        print("Prof. Oak: 'Farhan! Congratulations on becoming the Pokemon Master!'")
        print("Prof. Oak: 'Lekin جشن manane ka waqt nahi hai... Space-time fabric crack ho raha hai!'")
        print("Prof. Oak: 'Turant Pallet Town lab report karo. Door lock kar raha hoon. Universe 2 awaits!'")

if __name__ == "__main__":
    game = ApexSanctuaryEngine(trainer_name="Farhan")
    game.award_apex_map()
    if game.climb_to_sanctuary():
        game.battle_reigning_master()
        game.emergency_oak_transmission()
