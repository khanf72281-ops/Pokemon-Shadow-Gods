"""
Pokemon: Shadow Gods - Official Learnset & Moves Engine (Gen 1 - Gen 9)
========================================================================
Purely authentic mechanics based on official Pokemon Company / Showdown logic.
Features:
  - Exact Level-up progression
  - Official TM/HM compatibility per species
  - Dynamic 4-move / 8-move tactical watch slot support
  - Auto move replacement / learner prompt simulation
"""

import json
from typing import Dict, List, Any, Optional

class OfficialMovesEngine:
    def __init__(self, data_file: str = "pokemon_learnsets_gen1_to_9.json"):
        self.data_file = data_file
        self.learnsets: Dict[str, Any] = {}
        self.load_database()

    def load_database(self):
        """Loads the official learnsets database."""
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.learnsets = data.get("pokemon_learnsets", {})
                print(f"✅ Loaded official learnsets for {len(self.learnsets)} species.")
        except FileNotFoundError:
            print(f"⚠️ Warning: '{self.data_file}' not found. Initializing in-memory fallback.")
            self.learnsets = {}

    def get_moves_at_level(self, species: str, level: int) -> List[str]:
        """Returns the official moves unlocked at an exact level."""
        data = self.learnsets.get(species)
        if not data:
            return []
        
        moves = [
            entry["move"] 
            for entry in data.get("level_up_moves", []) 
            if entry["level"] == level
        ]
        return moves

    def can_learn_tm(self, species: str, tm_id: str) -> bool:
        """Verifies if the species is officially compatible with the TM/HM."""
        data = self.learnsets.get(species)
        if not data:
            return False
        return tm_id in data.get("compatible_tms", [])

    def learn_move(
        self, 
        pokemon: Dict[str, Any], 
        new_move: str, 
        replace_index: Optional[int] = None
    ) -> bool:
        """
        Teaches a move to a Pokemon.
        Supports up to 4 moves normally, or 8 moves if 'has_8_move_watch' is True.
        """
        current_moves = pokemon.setdefault("current_moves", [])
        max_slots = 8 if pokemon.get("has_8_move_watch") else 4

        if new_move in current_moves:
            print(f"⚠️ {pokemon['species']} already knows {new_move}.")
            return False

        if len(current_moves) < max_slots:
            current_moves.append(new_move)
            print(f"🎉 {pokemon['species']} learned {new_move}! ({len(current_moves)}/{max_slots} slots)")
            return True
        else:
            if replace_index is not None and 0 <= replace_index < max_slots:
                old_move = current_moves[replace_index]
                current_moves[replace_index] = new_move
                print(f"🔄 1, 2, and... Poof! {pokemon['species']} forgot {old_move} and learned {new_move}!")
                return True
            else:
                print(f"⚠️ Move pool full ({max_slots}/{max_slots}). Choose a slot (0 to {max_slots-1}) to replace.")
                return False

    def handle_level_up(self, pokemon: Dict[str, Any], new_level: int):
        """Simulates level-up and prompts for official new moves."""
        species = pokemon["species"]
        unlocked = self.get_moves_at_level(species, new_level)
        
        for move in unlocked:
            print(f"\n✨ {species} wants to learn official move: '{move}' at Level {new_level}!")
            # Auto-learn if empty slots available
            self.learn_move(pokemon, move)


if __name__ == "__main__":
    # Test Run
    engine = OfficialMovesEngine()

    dummy_rhydon = {
        "species": "Tyranitar",
        "level": 40,
        "has_8_move_watch": True,
        "current_moves": ["Rock Slide", "Payback", "Bite"]
    }

    # Level up to 41 (Officially learns Crunch)
    engine.handle_level_up(dummy_rhydon, 41)

    # TM Compatibility Check (TM26 Earthquake)
    if engine.can_learn_tm("Tyranitar", "TM26"):
        print("✅ Official TM Check: Tyranitar can learn TM26 (Earthquake).")
        engine.learn_move(dummy_rhydon, "Earthquake")
