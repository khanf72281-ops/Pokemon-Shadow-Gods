"""
Pokemon Multiverse Engine: Universe 1 Complete Storyline Progression
Flow:
1. Gen 1-9 Regional Mastery & 100% Dex Verification
2. Northern Region Championship (Triple Phenomena Master Trial)
3. Return to Pallet Town: Prof. Oak Primal Watcher Reveal
4. Climax Trial: Prof. Oak & Primal Mew 6v6 Battle
5. Mew Capture & Unlocking DNA Splice Ring + 8-Move Slots Watch
6. Departure to PokeDon2 Transit Route (Universe 2 Gateway)
"""

from typing import List, Dict

class StoryProgressionEngine:
    def __init__(self, trainer_name: str = "Farhan"):
        self.trainer_name = trainer_name
        self.badges_collected = 0
        self.dex_100_percent = False
        self.is_pokemon_master = False
        self.oak_trial_beaten = False
        self.mew_captured = False
        self.dna_splice_unlocked = False
        self.eight_move_watch_unlocked = False
        self.current_location = "Pallet Town"

    def complete_gen_1_to_9(self):
        """Step 1: 9 Regions, All Badges aur 100% Dex Register"""
        self.badges_collected = 72  # 8 badges x 9 regions
        self.dex_100_percent = True
        print(f"\n[EVENT] {self.trainer_name} completed all 9 Regions (Kanto to Paldea)!")
        print(f"        All 1025 Pokemon registered in National Dex. 100% Dex Status: VERIFIED.")

    def enter_northern_championship(self):
        """Step 2: Northern Master League with Triple Phenomena Rule"""
        if not self.dex_100_percent:
            print("\n[BLOCKED] Northern Championship requires 100% National Dex completion!")
            return False

        print("\n[EVENT] Entering the Northern Ice Peak Stadium Championship...")
        print("        [BATTLE PROTOCOL]: Triple Phenomena rule is active!")
        print("        Match 1: Alain (Mega Evolution Mastery) -> VICTORY")
        print("        Match 2: Leon (Gigantamax Clash) -> VICTORY")
        print("        Match 3: Tobias & Mt. Silver Red (Ultimate Trial) -> VICTORY")
        self.is_pokemon_master = True
        print(f"        👑 CONGRATULATIONS! {self.trainer_name} is crowned the POKEMON MASTER! 👑")
        return True

    def pallet_town_anomaly(self):
        """Step 3: Prof. Oak Lab Lockdown & Primal Watcher Reveal"""
        if not self.is_pokemon_master:
            print("\n[BLOCKED] You must be the Pokemon Master to trigger this event.")
            return False

        self.current_location = "Pallet Town (Oak's Secret Underground Lab)"
        print(f"\n[EVENT] {self.trainer_name} returns to Pallet Town.")
        print("        Prof. Oak locks the laboratory doors from the inside...")
        print("        Oak reveals his secret identity: 'The Primal Watcher of Universe 1 & 2'.")
        print("        Oak: 'Universe 2 me dark singularity jaag chuki hai jo dono universes ko mita degi!'")
        print("        Oak: 'Universe 2 me jane se pehle tumhe mere aur Mew ke samne khud ko prove karna hoga!'")
        return True

    def battle_prof_oak_and_mew(self):
        """Step 4 & 5: Oak & Primal Mew 6v6 Battle, Capture & Unlock Items"""
        print("\n[CLIMAX BATTLE] Prof. Oak challenges you to a 6v6 Primal Trial!")
        print("        Oak's Vanguard: Charizard, Blastoise, Venusaur, Tauros, Snorlax...")
        print("        Oak's Final Anchor: PRIMAL MEW!")
        print("        [MEW MECHANICS]: Dynamic type-shift per turn + Protect-bypassing Origin Pulse.")
        print("        Triple Phenomena Chain executed by Player: Mega -> Z-Move -> Tera!")
        print("        Primal Mew is defeated and acknowledges your bond.")
        
        self.oak_trial_beaten = True
        self.mew_captured = True
        self.dna_splice_unlocked = True
        self.eight_move_watch_unlocked = True

        print(f"\n[REWARDS UNLOCKED]:")
        print("        ✨ Mew caught and registered to your party!")
        print("        ✨ DNA Splice Ring acquired (Fuse 2 Pokemon into Hybrid Form)!")
        print("        ✨ 8-Move Slots Watch equipped (Expanded tactical move pool)!")
        return True

    def initiate_universe_transit(self):
        """Step 6: PokeDon2 Departure to Universe 2 (Bharat Region)"""
        if not (self.dna_splice_unlocked and self.eight_move_watch_unlocked):
            print("\n[ERROR] Prerequisites missing for Universe transit.")
            return False

        print("\n[VOYAGE BEGINS] Oak directs you to the Forgotten Ocean gateway...")
        print("        -> Sea voyage through the dimensional squall")
        print("        -> Cave of Emptiness (Ceiling collapse locks the exit)")
        print("        -> Space-Time Gravity Rift entered...")
        print("        -> TRANSITING TO UNIVERSE 2 (BHARAT REGION) OUTPOST...")
        self.current_location = "Universe 2: Tarana Outpost"
        return True


if __name__ == "__main__":
    game_story = StoryProgressionEngine(trainer_name="Farhan")
    
    # Execute full Universe 1 storyline
    game_story.complete_gen_1_to_9()
    game_story.enter_northern_championship()
    game_story.pallet_town_anomaly()
    game_story.battle_prof_oak_and_mew()
    game_story.initiate_universe_transit()
