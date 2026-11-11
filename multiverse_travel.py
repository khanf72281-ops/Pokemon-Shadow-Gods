# multiverse_travel.py
import time

class MultiverseTravelGate:
    def __init__(self):
        self.regions_unlocked = ["Kanto"]
        self.kanto_dex_count = 0
        self.sinnoh_cleared = False
        self.hisui_cleared = False

    def check_kanto_dex_completion(self, player_dex):
        """जाँचता है कि कांतो के 150 पोकेमोन पकड़े गए हैं या नहीं"""
        self.kanto_dex_count = len(player_dex.get("Kanto", []))
        if self.kanto_dex_count >= 150:
            print("\n🌟 [KANTO DEX COMPLETE!] 150 पोकेमोन दर्ज हो चुके हैं!")
            print("प्रोफेसर ओक की गुप्त लैब (Pallet Town) का रास्ता अब खुल चुका है!")
            return True
        else:
            print(f"\n🔒 कांतो डेक्स प्रगति: {self.kanto_dex_count}/150. और पोकेमोन पकड़ें!")
            return False

    def trigger_time_collapse_to_hisui(self, player):
        """सिनोह चैंपियन बनने के बाद टाइम-कोलैप्स और हिसुई में प्रवेश"""
        print("\n" + "=" * 60)
        print("⚡ [TIME COLLAPSE EVENT TRIGGERED!]")
        print("=" * 60)
        print("स्पेस-टाइम रिफ्ट आसमान में फट चुका है... समय उल्टा बहने लगा है!")
        time.sleep(1)
        print("डायलगा और पाल्किया की ऊर्जा ने आपको प्राचीन हिसुई (Hisui) में खींच लिया है...")
        player.current_region = "Hisui_Ancient"
        self.regions_unlocked.append("Hisui_Ancient")
        print("📍 वर्तमान स्थान: माउंट कोरोनेट की प्राचीन तलहटी (हिसुई)")

    def trigger_universe_2_rift(self, player):
        """हिसुई क्रिएशन ट्रायो शांत करने के बाद यूनिवर्स 2 (भारत रीजन) में शिफ्ट"""
        print("\n" + "=" * 60)
        print("🌌 [DIMENSIONAL RIFT: UNIVERSE 2 SHIFT]")
        print("=" * 60)
        print("आर्केयस की ऊर्जा ने मल्टीवर्स का दूसरा छोर खोल दिया...")
        print("आप यूनिवर्स 2 के मध्य भारत (Tarana, MP) में गिर रहे हैं!")
        time.sleep(1)
        player.current_region = "Bharat_Universe_2"
        self.regions_unlocked.append("Bharat_Universe_2")
        print("📍 नया स्थान: तराना के प्राचीन खंडहर (मध्य प्रदेश)")
