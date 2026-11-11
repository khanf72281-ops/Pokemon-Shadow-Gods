# ultimate_master_trial.py
import time

class OakUltimateMasterTrial:
    # Universe 1 ke sabhi cosmic entities ke Shiny Forms
    REQUIRED_SHINIES = {
        # Kanto & Johto
        "Shiny_Mewtwo", "Shiny_Mew", "Shiny_Lugia", "Shiny_Ho-Oh", "Shiny_Celebi",
        # Hoenn
        "Shiny_Kyogre", "Shiny_Groudon", "Shiny_Rayquaza", "Shiny_Jirachi", "Shiny_Deoxys",
        # Sinnoh
        "Shiny_Dialga", "Shiny_Palkia", "Shiny_Giratina", "Shiny_Darkrai", "Shiny_Arceus",
        # Unova
        "Shiny_Reshiram", "Shiny_Zekrom", "Shiny_Kyurem", "Shiny_Victini", "Shiny_Genesect",
        # Kalos
        "Shiny_Xerneas", "Shiny_Yveltal", "Shiny_Zygarde", "Shiny_Diancie", "Shiny_Volcanion",
        # Alola (Legendaries & Ultra Beasts)
        "Shiny_Solgaleo", "Shiny_Lunala", "Shiny_Necrozma", "Shiny_Nihilego", 
        "Shiny_Buzzwole", "Shiny_Pheromosa", "Shiny_Xurkitree", "Shiny_Celesteela", 
        "Shiny_Kartana", "Shiny_Guzzlord", "Shiny_Poipole", "Shiny_Stakataka", "Shiny_Blacephalon",
        # Galar & Paldea
        "Shiny_Zacian", "Shiny_Zamazenta", "Shiny_Eternatus", "Shiny_Koraidon", "Shiny_Miraidon", "Shiny_Terapagos"
    }

    @staticmethod
    def oak_briefing(player):
        print("\n" + "=" * 70)
        print("🏛️ PALLET TOWN: PROFESSOR OAK'S RESTRICTED ARCHIVE")
        print("=" * 70)
        print("Prof. Oak: 'Champion... Universe 2 koi aam dimension nahi hai.'")
        print("Prof. Oak: 'Wo cosmos ke itne anant aur gahre shoonya me hai jahan aam physics kaam nahi karti.'")
        print("Prof. Oak: 'Wahan ka portal kholne ke liye tumhe prove karna hoga ki tum itihaas ke sabse mahaan master ho.'")
        print("\n⚡ [THE ULTIMATE MASTER TRIAL]")
        print("Prof. Oak: 'Aasman me achanak sabhi Legendaries, Mythicals aur Ultra Beasts ke Shiny roop prakat hue hain.'")
        print("Prof. Oak: 'Jab tak tum har ek Shiny Cosmic Entity ko dhoondh kar tame nahi kar lete, tab tak'")
        print("Prof. Oak: 'wo dimensional bridge activate nahi hoga. Unki combined aura hi tumhe us anant safar me zinda rakhegi!'")
        print(f"Kul Lakshya: {len(OakUltimateMasterTrial.REQUIRED_SHINIES)} Shiny Cosmic Pokemon.")
        print("=" * 70)

    @staticmethod
    def check_portal_readiness(player_shinies_caught):
        missing = OakUltimateMasterTrial.REQUIRED_SHINIES - set(player_shinies_caught)
        total = len(OakUltimateMasterTrial.REQUIRED_SHINIES)
        caught_count = total - len(missing)

        print(f"\n📊 Master Trial Progress: {caught_count}/{total} Shiny Legends/UBs")

        if len(missing) == 0:
            print("\n🌟 [PORTAL STABILIZED!] Sabhi Shiny Legendaries, Mythicals aur UBs ne apni shakti ektrit kar li hai!")
            print("Universe 1 ka core kaanp utha hai... Anant shoonya ka darwaza ab khul chuka hai!")
            return True
        else:
            print(f"🔒 Portal abhi shant hai. Baki bache: {len(missing)} creatures.")
            return False
