# league_data.py
# Kanto Secret Boss + Bharat Region (Universe 2) Elite Four & Champion

LEAGUE_BOSSES = {
    # --- KANTO SECRET POST-GAME BOSS ---
    "Prof_Oak": {
        "title": "Pokémon Master Emeritus",
        "region": "Kanto (Pallet Town)",
        "intro": "Aah! 150 Pokémon register kar liye tumne? Aao, dekhein aakhir Kanto ke naye champion me kitna dam hai!",
        "defeat": "Adbhut! Tumhari samajh aur prem ne mere sabhi vishleshan ko peeche chhod diya. Yeh Mew ab tumhara sathi hai!",
        "ai_tier": "Master_8Move",
        "reward_pokemon": "Mew",
        "team": [
            {
                "species": "Tauros", "level": 70, "type": ["Normal"],
                "moves": ["Body Slam", "Earthquake", "Hyper Beam", "Blizzard"]
            },
            {
                "species": "Charizard", "level": 71, "type": ["Fire", "Flying"],
                "moves": ["Flamethrower", "Air Slash", "Dragon Claw", "Solar Beam", "Blast Burn", "Roost", "Earth Power", "Overheat"]
            },
            {
                "species": "Arcanine", "level": 71, "type": ["Fire"],
                "moves": ["Flamethrower", "Extreme Speed", "Crunch", "Wild Charge"]
            },
            {
                "species": "Gyarados", "level": 72, "type": ["Water", "Flying"],
                "moves": ["Dragon Dance", "Waterfall", "Ice Fang", "Earthquake"]
            },
            {
                "species": "Dragonite", "level": 73, "type": ["Dragon", "Flying"],
                "moves": ["Outrage", "Thunder", "Fire Blast", "Wing Attack"]
            },
            {
                "species": "Mew", "level": 75, "type": ["Psychic"],
                "moves": ["Psystrike", "Aura Sphere", "Transform", "Recover", "Psychic", "Ice Beam", "Thunderbolt", "Flamethrower"]
            }
        ]
    },

    # --- BHARAT ELITE FOUR (Uttarakhand Bio-Dome Arena) ---
    "Elite_Samrat": {
        "title": "Dharohar Master",
        "specialty": "Ground/Rock",
        "intro": "Bharat ki zameen hazaron saal purani hai. Mere dharohar pokémon ke aage sab choor ho jate hain!",
        "defeat": "Tumhari jadhein sach me behad gahri hain...",
        "team": [
            {"species": "Kurmadev", "level": 54, "type": ["Water", "Ground"], "moves": ["Rock Slide", "Earthquake", "Curse", "Protect"]},
            {"species": "Steelix", "level": 55, "type": ["Steel", "Ground"], "moves": ["Iron Tail", "Stone Edge", "Earthquake", "Crunch"]},
            {"species": "Nakulor", "level": 56, "type": ["Ground", "Fighting"], "moves": ["Close Combat", "Earthquake", "Bulk Up", "Rock Slide"]},
            {"species": "Airavalon", "level": 57, "type": ["Grass", "Ground"], "moves": ["Tectonic Stomp", "Wood Hammer", "Heavy Slam", "Earthquake"]}
        ]
    },

    "Elite_Meera": {
        "title": "Tidal Mistress",
        "specialty": "Water/Poison",
        "intro": "Ganga aur Brahmaputra ke sangam ki dhara me behne ke liye taiyar ho jao!",
        "defeat": "Tumne tufani lehar ko bhi cheer diya...",
        "team": [
            {"species": "Kingler", "level": 56, "type": ["Water"], "moves": ["Crabhammer", "X-Scissor", "Swords Dance", "Agility"]},
            {"species": "Delta-Naga", "level": 57, "type": ["Poison", "Water"], "moves": ["Venoshock", "Hydro Pump", "Sludge Wave", "Recover"]},
            {"species": "Tentacruel", "level": 58, "type": ["Water", "Poison"], "moves": ["Surf", "Ice Beam", "Toxic", "Barrier"]},
            {"species": "Makardus", "level": 59, "type": ["Water", "Steel"], "moves": ["Chambal Surge", "Iron Head", "Crunch", "Hydro Pump"]}
        ]
    },

    "Elite_Devrath": {
        "title": "Agni Yoddha",
        "specialty": "Fire/Soul",
        "intro": "Meri aag sirf jalati nahi, aatma ko parakhti hai!",
        "defeat": "Tumhari aag mere tejas se bhi shreshtha nikli...",
        "team": [
            {"species": "Marukantak", "level": 58, "type": ["Ground", "Fire"], "moves": ["Flamethrower", "Earthquake", "Fire Blast", "Spikes"]},
            {"species": "Rapidash", "level": 59, "type": ["Fire"], "moves": ["Flare Blitz", "Megahorn", "Wild Charge", "High Horsepower"]},
            {"species": "Bhavandar", "level": 60, "type": ["Flying", "Ground"], "moves": ["Air Slash", "Heat Wave", "Sandstorm", "Tailwind"]},
            {"species": "Vyaghragni", "level": 61, "type": ["Fire", "Soul"], "moves": ["Infernal Pounce", "Flare Blitz", "Shadow Claw", "Extreme Speed"]}
        ]
    },

    "Elite_Yashodhara": {
        "title": "Cosmic Mystic",
        "specialty": "Psychic/Ghost",
        "intro": "Samay aur antariksh ke chakravyuh me swagat hai. Kya tum is maya ko tod paoge?",
        "defeat": "Kalchakra ne tumhara rasta aage badha diya...",
        "team": [
            {"species": "Alakazam", "level": 60, "type": ["Psychic"], "moves": ["Psychic", "Focus Blast", "Shadow Ball", "Calm Mind"]},
            {"species": "Gengar", "level": 61, "type": ["Ghost", "Poison"], "moves": ["Shadow Ball", "Sludge Bomb", "Thunderbolt", "Destiny Bond"]},
            {"species": "Bhediator", "level": 62, "type": ["Ghost", "Dark"], "moves": ["Crunch", "Shadow Claw", "Sucker Punch", "Will-O-Wisp"]},
            {"species": "Kaalchaya", "level": 63, "type": ["Ghost", "Cosmic"], "moves": ["Temporal Void", "Shadow Ball", "Psychic", "Calm Mind"]}
        ]
    },

    # --- BHARAT GRAND CHAMPION ---
    "Champion_Rishi": {
        "title": "Multiverse Guardian Champion",
        "intro": "Peshwa se lekar Ladakh tak, tumne pure Bharat ko jeeta hai. Lekin Universe 2 ko sanjoye rakhna aasan nahi. TYGRANTOX, jaago!",
        "defeat": "Tum sach me Universe 2 ke naye sanrakshak ho. Bharat League tumhare naam hui!",
        "team": [
            {"species": "Ghorashim", "level": 65, "type": ["Ice", "Fighting"], "moves": ["Blizzard", "Close Combat", "Ice Shard", "Bulk Up"]},
            {"species": "Lohashva", "level": 66, "type": ["Steel", "Electric"], "moves": ["Volt Tackle", "Flash Cannon", "Thunder Wave", "Iron Defense"]},
            {"species": "Garudragon", "level": 67, "type": ["Dragon", "Flying"], "moves": ["Dragon Pulse", "Brave Bird", "Earthquake", "Roost"]},
            {"species": "Lucario", "level": 68, "type": ["Fighting", "Steel"], "moves": ["Aura Sphere", "Meteor Mash", "Extreme Speed", "Swords Dance"]},
            {"species": "Tygrathor", "level": 69, "type": ["Soul", "Fire"], "moves": ["Soul Burn", "Flare Blitz", "Sacred Roar", "Dragon Claw"]},
            {
                "species": "TYGRANTOX", "level": 70, "type": ["Soul", "Poison"],
                "moves": [
                    "Eternal Soul Void", "Cataclysmic Decay", "Sludge Wave", "Shadow Force",
                    "Recover", "Hyper Voice", "Toxic Spikes", "Dragon Pulse"
                ]
            }
        ]
    }
}
