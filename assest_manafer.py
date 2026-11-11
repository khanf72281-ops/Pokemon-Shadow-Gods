# asset_manager.py
import os

class PokemonVisualEngine:
    def __init__(self, base_path="assets/pokemon/"):
        self.base_path = base_path
        # रैम बचाने के लिए कैशे (Cache) सिस्टम
        self.sprite_cache = {} 
        
        # फोल्डर स्ट्रक्चर सेट करना (e.g., assets/pokemon/gen1/, assets/pokemon/bharat/)
        self.regions = ["gen1_kanto", "gen2_johto", "gen3_hoenn", "gen4_sinnoh", 
                        "gen5_unova", "gen6_kalos", "hisui", "universe2_bharat"]

    def _get_pokemon_folder(self, dex_number: int, region: str):
        """पोकेमोन के नंबर और रीजन के आधार पर फोल्डर पाथ बनाना"""
        # संख्या को 3 डिजिट में बदलना (e.g., 1 -> 001)
        formatted_number = f"{dex_number:03d}"
        return os.path.join(self.base_path, region, formatted_number)

    def load_sprite(self, dex_number: int, region: str, view="front", shiny=False, female=False):
        """
        ज़रूरत के अनुसार सही स्प्राइट लोड करना।
        view: 'front' (सामने), 'back' (पीछे), 'icon' (छोटा आइकॉन)
        shiny: True/False
        female: True/False (अगर पोकेमोन का फीमेल रूप अलग है)
        """
        # यूनीक आईडी बनाना कैशे के लिए
        sprite_id = f"{region}_{dex_number}_{view}_{'s' if shiny else 'n'}_{'f' if female else 'm'}"
        
        # अगर इमेज पहले से लोड है, तो वही वापस करो
        if sprite_id in self.sprite_cache:
            return self.sprite_cache[sprite_id]
        
        # फाइल का नाम सेट करना
        filename = view
        if shiny: filename += "_shiny"
        if female: filename += "_female"
        filename += ".png"
        
        # पूरा पाथ
        folder_path = self._get_pokemon_folder(dex_number, region)
        full_path = os.path.join(folder_path, filename)
        
        # यहाँ इमेज लोडिंग लाइब्रेरी (e.g., Pygame) का इस्तेमाल होगा
        if os.path.exists(full_path):
            # उदाहरण के लिए हम अभी सिर्फ पाथ वापस कर रहे हैं
            # असली गेम में: image = pygame.image.load(full_path).convert_alpha()
            image_asset = f"[IMAGE_LOADED: {full_path}]" 
            
            # कैशे में सेव करो
            self.sprite_cache[sprite_id] = image_asset
            return image_asset
        else:
            print(f"⚠️ चेतावनी: स्प्राइट नहीं मिला - {full_path}")
            # अगर इमेज न मिले, तो एक 'MissingNo' या डिफॉल्ट इमेज लोड करो
            return "[DEFAULT_IMAGE]"

    def unload_unused_sprites(self):
        """रैम खाली करने के लिए पुराने कैशे को साफ़ करना (पोस्ट-बैटल)"""
        self.sprite_cache.clear()
        print("🧹 विज़ुअल कैशे साफ़ किया गया (रैम सुरक्षित)।")

# --- सिस्टम को टेस्ट करना ---
visual_engine = PokemonVisualEngine()

# 1. कांटो (Gen 1) के बुलबासौर (Dex #1) का फ्रंट स्प्राइट
# पाथ बनेगा: assets/pokemon/gen1_kanto/001/front.png
print(visual_engine.load_sprite(1, "gen1_kanto", view="front"))

# 2. जोहतो (Gen 2) के सिन्डाक्विल (Dex #155) का बैक स्प्राइट
# पाथ बनेगा: assets/pokemon/gen2_johto/155/back.png
print(visual_engine.load_sprite(155, "gen2_johto", view="back"))

# 3. भारत रीजन (Universe 2) के टस्कलेट (#001) का शाइनी फ्रंट स्प्राइट
# पाथ बनेगा: assets/pokemon/universe2_bharat/001/front_shiny.png
print(visual_engine.load_sprite(1, "universe2_bharat", view="front", shiny=True))
