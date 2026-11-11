# language.py

LANGUAGES = {
    "hi": {
        "title": "⚡ पोकेमोन: शैडो गॉड्स ⚡",
        "choose_starter": "अपना स्टार्टर पोकेमोन चुनें:",
        "starter_chosen": "🎉 आपने {name} को चुना!",
        "prof_event": "\n[इवेंट]: आप तराणा कस्बे में प्रोफेसर नीम की लैब पहुँचे...",
        "prof_dialogue": "👨‍🔬 प्रो. नीम: 'यह लो Tactical Watch! अब तुम्हारे पोकेमोन के 8 स्लॉट खुल गए!'",
        "moves_unlocked": "✅ {name} के सभी 8 मूव्स अनलॉक हो चुके हैं!",
        "walk_prompt": "\nकमांड दें: 'w' (आगे बढ़ें) | 'q' (बाहर निकलें): ",
        "game_quit": "गेम बंद हो गया। सुरक्षित रहें!",
        "wild_appear": "⚠️ झाड़ियों से जंगली {name} बाहर आया!",
        "status_player": "[आपकी स्थिति]: {name} (HP: {current}/{max})",
        "status_enemy": "[दुश्मन]: {name} (HP: {current}/{max})",
        "choose_move": "हमला चुनें (1-{count}): ",
        "used_move": "▶ [{side}] {attacker} ने '{move}' का इस्तेमाल किया!",
        "damage_dealt": "🩸 {defender} को {dmg} का डैमेज लगा!",
        "fainted": "💀 {name} फेंट हो गया!",
        "victory": "🏆 शानदार जीत! आपने {name} को हरा दिया!",
        "safe_path": "रास्ता एकदम साफ़ है, कोई जंगली क्रिएचर नहीं दिखा।",
        "invalid_choice": "अमान्य विकल्प! कृपया सही नंबर चुनें।"
    },
    "en": {
        "title": "⚡ POKEMON: SHADOW GODS ⚡",
        "choose_starter": "Choose your Starter Pokemon:",
        "starter_chosen": "🎉 You chose {name}!",
        "prof_event": "\n[Event]: You reached Professor Neem's lab in Tarana Town...",
        "prof_dialogue": "👨‍🔬 Prof. Neem: 'Take this Tactical Watch! Your 8 move slots are now unlocked!'",
        "moves_unlocked": "✅ All 8 moves for {name} are now unlocked!",
        "walk_prompt": "\nEnter command: 'w' (Walk forward) | 'q' (Quit): ",
        "game_quit": "Game closed. See you next time!",
        "wild_appear": "⚠️ A wild {name} appeared from the tall grass!",
        "status_player": "[Your Status]: {name} (HP: {current}/{max})",
        "status_enemy": "[Enemy]: {name} (HP: {current}/{max})",
        "choose_move": "Choose a move (1-{count}): ",
        "used_move": "▶ [{side}] {attacker} used '{move}'!",
        "damage_dealt": "🩸 {defender} took {dmg} damage!",
        "fainted": "💀 {name} fainted!",
        "victory": "🏆 Victory! You defeated {name}!",
        "safe_path": "The path is clear. No wild creatures spotted.",
        "invalid_choice": "Invalid choice! Please select a valid number."
    },
    "hinglish": {
        "title": "⚡ POKEMON: SHADOW GODS ⚡",
        "choose_starter": "Apna Starter Pokemon select karo:",
        "starter_chosen": "🎉 Tune {name} ko choose kiya!",
        "prof_event": "\n[Event]: Tum Tarana Town mein Professor Neem ki lab pahunche...",
        "prof_dialogue": "👨‍🔬 Prof. Neem: 'Ye lo Tactical Watch! Ab tumhare Pokemon ke 8 move slots open ho gaye!'",
        "moves_unlocked": "✅ {name} ke saare 8 moves unlock ho chuke hain!",
        "walk_prompt": "\nCommand do: 'w' (Aage badho) | 'q' (Quit karo): ",
        "game_quit": "Game close ho gaya!",
        "wild_appear": "⚠️ Grass se ek wild {name} samne aaya!",
        "status_player": "[Tumhari Status]: {name} (HP: {current}/{max})",
        "status_enemy": "[Enemy]: {name} (HP: {current}/{max})",
        "choose_move": "Move select karo (1-{count}): ",
        "used_move": "▶ [{side}] {attacker} ne '{move}' use kiya!",
        "damage_dealt": "🩸 {defender} ko {dmg} ka damage pada!",
        "fainted": "💀 {name} faint ho gaya!",
        "victory": "🏆 Jeet gaye! Tune {name} ko hara diya!",
        "safe_path": "Raasta clear hai, koi wild creature nahi mila.",
        "invalid_choice": "Galat option! Sahi number dalo."
    }
}

class LanguageManager:
    def __init__(self, lang_code="hi"):
        self.current_lang = lang_code if lang_code in LANGUAGES else "hi"

    def set_language(self, lang_code):
        if lang_code in LANGUAGES:
            self.current_lang = lang_code

    def get(self, key, **kwargs):
        text = LANGUAGES[self.current_lang].get(key, "")
        if kwargs:
            return text.format(**kwargs)
        return text
