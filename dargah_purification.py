# dargah_purification.py

SANCTUARIES = {
    "Ajmer_Sharif": {
        "location": "Rajasthan",
        "description": "Khwaja Ji ki Dargah - Roohani shanti ka markaz jahan gussa aur nafrat pighal jaate hain.",
        "effect": "Calms inner rage & unblocks Heart Gauge"
    },
    "Haji_Ali": {
        "location": "Mumbai (Arabian Sea)",
        "description": "Samundar ke beech Noorani aalam jo cosmic void energy ko dho deta hai.",
        "effect": "Cleanses void radiation & establishes absolute loyalty"
    }
}

class DargahPurificationSystem:
    @staticmethod
    def purify_shadow_legendary(pokemon_name, sanctuary_name, player):
        if sanctuary_name not in SANCTUARIES:
            print("Ye koi recognized spiritual sanctuary nahi hai.")
            return False

        s = SANCTUARIES[sanctuary_name]
        print("\n" + "=" * 65)
        print(f"🕊️ {sanctuary_name} Dargah Shareef: {s['location']}")
        print("=" * 65)
        print(f"{s['description']}")
        print(f"✨ {pokemon_name} ki aakhon se kaala andhera gayab hone laga...")
        print(f"🕊️ {pokemon_name} ka Heart-Lock poori tarah toot gaya aur wo shaant ho gaya!")
        print(f"🤝 {pokemon_name} ne aapke saamne sar jhuka diya—ab wo hamesha aapka kehna maanega!")
        print("=" * 65)
        return True
