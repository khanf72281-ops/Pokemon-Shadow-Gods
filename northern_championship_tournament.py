"""
Pokemon: Shadow Gods - Northern Region Master Championship
Location: Northern Ice Peak Stadium
Battle Protocol: Triple Phenomena Protocol (Max 3 phenomena per match)
Contenders:
  Round 1: Alain (Mega Evolution Specialist)
  Round 2: Leon (Gigantamax Monarch)
  Final Trial 1: Tobias (Darkrai & Latios Legendary Core)
  Final Trial 2: Living Legend Red (Triple Phenomena Duel)
"""

import time
from typing import List, Dict

class NorthernChampionship:
    def __init__(self, trainer_name: str = "Farhan"):
        self.trainer = trainer_name
        self.phenomena_used = 0
        self.max_phenomena = 3
        self.championship_won = False

    def trigger_phenomenon(self, pheno_type: str, pokemon: str):
        if self.phenomena_used < self.max_phenomena:
            self.phenomena_used += 1
            print(f"      ⚡ [PHENOMENA {self.phenomena_used}/3 ACTIVATED]: {self.trainer} triggered {pheno_type} on {pokemon}!")
            return True
        else:
            print(f"      ❌ [LIMIT REACHED]: Triple Phenomena Protocol max limit (3/3) exceeded!")
            return False

    def round_one_alain(self):
        print("\n" + "=" * 65)
        print("🏟️  ROUND 1: NORTHERN CHAMPIONSHIP QUARTER-FINAL")
        print("     Opponent: Alain (Kalos Champion League Master)")
        print("=" * 65)
        print("-> Alain sends out Tyranitar!")
        print(f"-> {self.trainer} counters with Lucario!")
        print("-> Alain withdraws and summons his Ace: Charizard!")
        print("-> Alain activates Mega Ring: Charizard Mega Evolves into MEGA CHARIZARD X!")
        
        self.trigger_phenomenon("Mega Evolution", "Mega Garchomp")
        print("-> Clash: Mega Garchomp's Earthquake vs Mega Charizard X's Dragon Claw!")
        print("-> CRITICAL HIT! Mega Charizard X falls!")
        print("🏆 Alain: 'Your dragon's strength is absolute. You've mastered Mega Evolution.'")

    def round_two_leon(self):
        print("\n" + "=" * 65)
        print("🏟️  ROUND 2: SEMI-FINAL CLASH OF KINGS")
        print("     Opponent: Leon (The Undefeated Galar Monarch)")
        print("=" * 65)
        print("-> Leon leads with Dragapult! Rapid Dragon Darts break the field.")
        print(f"-> {self.trainer} absorbs the pressure with Tyranitar's Sandstorm!")
        print("-> Leon brings in his Ace: Charizard!")
        print("-> Dynamax Band activates! Leon unleashes GIGANTAMAX CHARIZARD!")
        print("-> Leon triggers G-Max Wildfire!")
        
        self.trigger_phenomenon("Dynamax / Gigantamax", "Gigantamax Blastoise")
        print("-> Counter Strike: G-Max Cannonade floods G-Max Wildfire!")
        print("-> Gigantamax Charizard sustains catastrophic super-effective damage and faints!")
        print("🏆 Leon: 'What an unbelievable championship time! You pushed past my limit!'")

    def final_trial_tobias(self):
        print("\n" + "=" * 65)
        print("⚔️  FINAL TRIAL - PART 1: THE MYTHICAL GAUNTLET")
        print("     Opponent: Tobias (The Shadow Tactician)")
        print("=" * 65)
        print("-> Tobias summons DARKRAI!")
        print("-> Darkrai uses Dark Void! The arena sinks into pitch darkness.")
        print(f"-> {self.trainer}'s Mewtwo breaks the nightmare trance with Insomnia aura!")
        print("-> Mewtwo lands Focus Blast! Darkrai is eliminated!")
        print("-> Tobias summons LATIOS!")
        print("-> Latios fires high-speed Luster Purge!")
        
        self.trigger_phenomenon("Terastallization", "Tera-Steel Metagross")
        print("-> Metagross's Tera-Steel typing completely resists psychic radiation!")
        print("-> Meteor Mash delivers a clean knockout on Latios!")
        print("🏆 Tobias: 'Inconceivable... To conquer both the nightmare and the eon dragon!'")

    def grand_final_red(self):
        print("\n" + "=" * 65)
        print("👑  GRAND CLIMAX: THE BATTLE OF LEGENDS")
        print("     Opponent: Red (The Living Legend of Mt. Silver)")
        print("=" * 65)
        print("-> Red stands in silence... and releases Level 88 Light Ball Pikachu!")
        print("-> Volt Tackle collides with absolute lightning force across the ice peaks!")
        print("-> Red deploys Gigantamax Venusaur!")
        print("-> Red triggers Mega Charizard Y with Drought blazing heat!")
        print(f"-> {self.trainer} executes the ultimate combat chain: Mega -> G-Max -> Tera!")
        print("-> The stadium tremors as Red's final Pokémon is pushed to faint!")
        print("-> Red tips his cap, smiles, and extends his hand.")
        print("=" * 65)
        print(f"🌟🌟🌟 OFFICIAL TOURNAMENT DECLARATION 🌟🌟🌟")
        print(f"Trainer {self.trainer} has defeated Red and all regional champions!")
        print(f"{self.trainer} IS OFFICIALLY CROWNED: THE POKÉMON MASTER!")
        print("=" * 65)
        self.championship_won = True

    def run_tournament(self):
        self.round_one_alain()
        self.round_two_leon()
        self.final_trial_tobias()
        self.grand_final_red()
        print("\n🚨 [INCOMING PRIORITY TRANSMISSION]: Prof. Oak has issued an emergency summons to Pallet Town...")

if __name__ == "__main__":
    championship = NorthernChampionship(trainer_name="Farhan")
    championship.run_tournament()
