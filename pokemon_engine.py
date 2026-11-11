"""
Pokemon Multiverse Battle & Campaign Simulation Engine
Complete with DNA Splice Ring, 8-Move Slots Watch, & The Eternal Void Boss Fight
"""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Dict

@dataclass
class Move:
    name: str
    move_type: str
    power: int
    accuracy: int
    category: str  # Physical, Special, Status
    description: str = ""

@dataclass
class Pokemon:
    name: str
    types: Tuple[str, Optional[str]]
    max_hp: int
    current_hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    ability: str
    moveset: List[Move] = field(default_factory=list)
    stat_stages: Dict[str, int] = field(default_factory=lambda: {
        "attack": 0, "defense": 0, "sp_attack": 0, "sp_defense": 0, "speed": 0
    })
    is_fused: bool = False

    def take_damage(self, amount: int) -> int:
        actual_dmg = min(self.current_hp, amount)
        self.current_hp -= actual_dmg
        return actual_dmg

    def heal(self, amount: int):
        self.current_hp = min(self.max_hp, self.current_hp + amount)

    @property
    def is_fainted(self) -> bool:
        return self.current_hp <= 0


class DNASpliceRing:
    """
    Unlocked via Prof. Oak & Mew Primal Climax Trial.
    Combines two Pokemon into an 8-Move Tactical Hybrid.
    """
    @staticmethod
    def fuse(pokemon_a: Pokemon, pokemon_b: Pokemon) -> Pokemon:
        hybrid_name = f"{pokemon_a.name[:4]}-{pokemon_b.name[-4:]}"
        hybrid_types = (pokemon_a.types[0], pokemon_b.types[1] if pokemon_b.types[1] else pokemon_b.types[0])
        
        combined_max_hp = int((pokemon_a.max_hp + pokemon_b.max_hp) * 0.85)
        combined_atk = max(pokemon_a.attack, pokemon_b.attack) + 30
        combined_def = max(pokemon_a.defense, pokemon_b.defense) + 25
        combined_sp_atk = max(pokemon_a.sp_attack, pokemon_b.sp_attack) + 30
        combined_sp_def = max(pokemon_a.sp_defense, pokemon_b.sp_defense) + 25
        combined_speed = max(pokemon_a.speed, pokemon_b.speed) + 20
        
        merged_moves = pokemon_a.moveset + pokemon_b.moveset
        seen = set()
        unique_8_moves = []
        for m in merged_moves:
            if m.name not in seen and len(unique_8_moves) < 8:
                seen.add(m.name)
                unique_8_moves.append(m)

        return Pokemon(
            name=hybrid_name,
            types=hybrid_types,
            max_hp=combined_max_hp,
            current_hp=combined_max_hp,
            attack=combined_atk,
            defense=combined_def,
            sp_attack=combined_sp_atk,
            sp_defense=combined_sp_def,
            speed=combined_speed,
            ability=f"{pokemon_a.ability} + {pokemon_b.ability} (Hybrid Resonance)",
            moveset=unique_8_moves,
            is_fused=True
        )


class EternalVoidBoss:
    """
    The Ultimate Singularity Boss of Universe 2.
    Rule: 500 Flat True Damage per turn bypassing all defenses.
    """
    def __init__(self):
        self.name = "The Eternal Void"
        self.max_hp = 3500
        self.current_hp = 3500
        self.flat_true_damage = 500

    def execute_turn_end_oblivion(self, target: Pokemon) -> Dict[str, str]:
        results = {}
        for stat in target.stat_stages:
            if target.stat_stages[stat] > 0:
                target.stat_stages[stat] = 0
        results["stat_reset"] = "All target stat boosts wiped into the Void."

        damage_dealt = target.take_damage(self.flat_true_damage)
        results["damage"] = f"{target.name} suffered {damage_dealt} Flat True Damage from Absolute Oblivion!"
        
        if target.is_fainted:
            results["faint"] = f"{target.name} was erased by The Eternal Void!"
        return results

    def take_boss_damage(self, amount: int):
        self.current_hp = max(0, self.current_hp - amount)


if __name__ == "__main__":
    print("Pokemon Multiverse Engine Loaded Successfully!")
