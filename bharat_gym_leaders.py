# bharat_gym_leaders.py

BHARAT_GYM_LEADERS = {
    # -------------------------------------------------------------
    # 1. MP (Ujjain - Maati Gym)
    # -------------------------------------------------------------
    "Vikram": {
        "title": "Maati Akhada Master",
        "city": "Ujjain, Madhya Pradesh",
        "badge": "Maati Badge",
        "intro_dialogue": "राम-राम! यह मालवा का अखाड़ा है। यहाँ सिर्फ वही टिकता है जिसकी पकड़ मिट्टी जैसी पक्की हो!",
        "defeat_dialogue": "लाजवाब दांव! तुम्हारी ताकत में मिट्टी की खुशबू है। यह माटी बैज तुम्हारा हुआ।",
        "reward_tm": "TM39 - Rock Tomb",
        "ai_tier": "Basic_Aggressive",  # FireRed Brock AI: अटैक पर फोकस, कम स्टेटस मूव्स
        "potions": ["Potion"],
        "team": [
            {
                "species": "Mungor",
                "level": 12,
                "type": ["Ground"],
                "stats": {"hp": 38, "atk": 25, "def": 18, "spe": 28},
                "moves": ["Mud-Slap", "Scratch", "Defense Curl", "Sand Attack"]
            },
            {
                "species": "Gajarock",
                "level": 14,
                "type": ["Grass", "Ground"],
                "stats": {"hp": 52, "atk": 34, "def": 42, "spe": 20},
                "moves": ["Rock Tomb", "Mud Shot", "Tackle", "Harden"]
            }
        ]
    },

    # -------------------------------------------------------------
    # 2. West Bengal (Sundarban - Jwar Gym)
    # -------------------------------------------------------------
    "Arpana": {
        "title": "Tidal Guardian",
        "city": "Sundarban Delta, West Bengal",
        "badge": "Jwar Badge",
        "intro_dialogue": "सुंदरबन की लहरों और दलदल को हल्के में मत लेना। ज्वार-भाटे की तरह संभलकर लड़ना होगा!",
        "defeat_dialogue": "अद्भुत बहाव! तुमने मेरी तूफानी लहरों को भी पार कर लिया। यह ज्वार बैज संभालो।",
        "reward_tm": "TM03 - Water Pulse",
        "ai_tier": "Status_Inflictor",  # FireRed Misty AI: कन्फ्यूजन, पॉइज़न और रिकवर पर जोर
        "potions": ["Super Potion"],
        "team": [
            {
                "species": "Chitrapan",
                "level": 18,
                "type": ["Bug", "Water"],
                "stats": {"hp": 50, "atk": 28, "def": 30, "spe": 40},
                "moves": ["Water Pulse", "Poison Sting", "Bug Bite", "Supersonic"]
            },
            {
                "species": "Delta-Naga",
                "level": 21,
                "type": ["Poison", "Water"],
                "stats": {"hp": 65, "atk": 44, "def": 40, "spe": 52},
                "moves": ["Water Pulse", "Venoshock", "Wrap", "Recover"]
            }
        ]
    },

    # -------------------------------------------------------------
    # 3. Delhi (Metro Transit - Chakra Gym)
    # -------------------------------------------------------------
    "Kabir": {
        "title": "Transit Grid Overseer",
        "city": "Capital NCR, Delhi",
        "badge": "Chakra Badge",
        "intro_dialogue": "दिल्ली मेट्रो की रफ्तार और यहाँ के इलेक्ट्रिक ग्रिड को कोई रोक नहीं सकता! क्या तुम झेल पाओगे?",
        "defeat_dialogue": "शॉर्ट-सर्किट हो गया! तुम्हारी गति वाकई मेरे ग्रिड से भी तेज़ थी।",
        "reward_tm": "TM34 - Shock Wave",
        "ai_tier": "Speed_Buff",  # FireRed Surge AI: स्पीड और एक्यूरेसी अवॉइडेंस
        "potions": ["Super Potion"],
        "team": [
            {
                "species": "Magnemite",
                "level": 19,
                "type": ["Electric", "Steel"],
                "stats": {"hp": 48, "atk": 25, "def": 40, "spe": 32},
                "moves": ["Spark", "Sonic Boom", "Thunder Wave", "Tackle"]
            },
            {
                "species": "Glowtara",
                "level": 22,
                "type": ["Bug", "Electric"],
                "stats": {"hp": 55, "atk": 32, "def": 35, "spe": 55},
                "moves": ["Shock Wave", "Flash", "Signal Beam", "Quick Attack"]
            },
            {
                "species": "Lohashva",
                "level": 24,
                "type": ["Steel", "Electric"],
                "stats": {"hp": 72, "atk": 56, "def": 58, "spe": 60},
                "moves": ["Shock Wave", "Metal Claw", "Charge Beam", "Double Team"]
            }
        ]
    },

    # -------------------------------------------------------------
    # 4. Kerala (Silent Valley - Aranya Gym)
    # -------------------------------------------------------------
    "Keshavan": {
        "title": "Western Ghats Herbalist",
        "city": "Silent Valley, Kerala",
        "badge": "Aranya Badge",
        "intro_dialogue": "पश्चिमी घाट की जड़ी-बूटियाँ जितनी शांत हैं, उतनी ही घातक भी। वर्षावन की शक्ति देखो!",
        "defeat_dialogue": "वर्षावन तुम्हारे आगे नतमस्तक हुआ। यह अरण्य बैज तुम्हारी निष्ठा का प्रमाण है।",
        "reward_tm": "TM19 - Giga Drain",
        "ai_tier": "Status_Drain",  # FireRed Erika AI: स्लीप, स्टन और लाइफ ड्रेन
        "potions": ["Super Potion", "Super Potion"],
        "team": [
            {
                "species": "Koshak",
                "level": 24,
                "type": ["Bug", "Grass"],
                "stats": {"hp": 65, "atk": 32, "def": 50, "spe": 30},
                "moves": ["Sleep Powder", "Mega Drain", "Protect", "String Shot"]
            },
            {
                "species": "Bansurath",
                "level": 26,
                "type": ["Grass", "Steel"],
                "stats": {"hp": 70, "atk": 45, "def": 58, "spe": 42},
                "moves": ["Magical Leaf", "Echoed Voice", "Leech Seed", "Growth"]
            },
            {
                "species": "Vanarkesh",
                "level": 29,
                "type": ["Grass", "Fighting"],
                "stats": {"hp": 85, "atk": 74, "def": 62, "spe": 58},
                "moves": ["Giga Drain", "Arm Thrust", "Bullet Seed", "Stun Spore"]
            }
        ]
    },

    # -------------------------------------------------------------
    # 5. Maharashtra (Lonavala - Pashan Gym)
    # -------------------------------------------------------------
    "Tanvi": {
        "title": "Basalt Crag Raider",
        "city": "Lonavala Ridge, Maharashtra",
        "badge": "Pashan Badge",
        "intro_dialogue": "दक्कन का यह बेसाल्ट पठार लाखों साल की ज्वाला से बना है। इसे तोड़ना आसान नहीं!",
        "defeat_dialogue": "चट्टानें बिखर गईं! तुम्हारी रणनीति सच में अजेय निकली।",
        "reward_tm": "TM71 - Stone Edge",
        "ai_tier": "Defensive_Bruiser",  # FireRed Koga AI: टॉक्सिक, बल्क और हार्ड-हिटिंग
        "potions": ["Hyper Potion"],
        "team": [
            {
                "species": "Kurmadev",
                "level": 37,
                "type": ["Water", "Ground"],
                "stats": {"hp": 110, "atk": 65, "def": 95, "spe": 25},
                "moves": ["Rock Slide", "Mud Bomb", "Protect", "Curse"]
            },
            {
                "species": "Bhediator",
                "level": 39,
                "type": ["Ghost", "Dark"],
                "stats": {"hp": 82, "atk": 88, "def": 58, "spe": 85},
                "moves": ["Crunch", "Shadow Claw", "Confuse Ray", "Pursuit"]
            },
            {
                "species": "Rhydon",
                "level": 39,
                "type": ["Ground", "Rock"],
                "stats": {"hp": 120, "atk": 95, "def": 90, "spe": 38},
                "moves": ["Earthquake", "Rock Tomb", "Scary Face", "Horn Drill"]
            },
            {
                "species": "Shailasur",
                "level": 43,
                "type": ["Rock", "Dark"],
                "stats": {"hp": 115, "atk": 112, "def": 125, "spe": 45},
                "moves": ["Stone Edge", "Night Slash", "Iron Defense", "Toxic"]
            }
        ]
    },

    # -------------------------------------------------------------
    # 6. Rajasthan (Thar Desert - Marichika Gym)
    # -------------------------------------------------------------
    "Bhairav": {
        "title": "Desert Mirage Vanguard",
        "city": "Jaisalmer Dunes, Rajasthan",
        "badge": "Marichika Badge",
        "intro_dialogue": "रेगिस्तान की तपती धूप और रेत के बवंडर में सिर्फ भ्रम दिखता है... और हार!",
        "defeat_dialogue": "मरीचिका का पर्दा हट गया। तुमने रेगिस्तान की तपिश को भी मात दे दी।",
        "reward_tm": "TM38 - Fire Blast",
        "ai_tier": "Special_Sweeper",  # FireRed Sabrina AI: तेज़ स्पेशल अटैक्स और सैंडस्टॉर्म
        "potions": ["Hyper Potion"],
        "team": [
            {
                "species": "Marukantak",
                "level": 38,
                "type": ["Ground", "Fire"],
                "stats": {"hp": 85, "atk": 78, "def": 70, "spe": 65},
                "moves": ["Flamethrower", "Spikes", "Dig", "Sand Tomb"]
            },
            {
                "species": "Dromedar",
                "level": 39,
                "type": ["Ground", "Rock"],
                "stats": {"hp": 110, "atk": 85, "def": 75, "spe": 35},
                "moves": ["Earthquake", "Flame Burst", "Bulldoze", "Amnesia"]
            },
            {
                "species": "Bhavandar",
                "level": 43,
                "type": ["Flying", "Ground"],
                "stats": {"hp": 90, "atk": 80, "def": 75, "spe": 105},
                "moves": ["Air Slash", "Heat Wave", "Whirlwind", "Sandstorm"]
            }
        ]
    },

    # -------------------------------------------------------------
    # 7. Ladakh (Leh - Himshikhar Gym)
    # -------------------------------------------------------------
    "Tashi": {
        "title": "Glacier Peak Warden",
        "city": "Leh, Ladakh",
        "badge": "Himshikhar Badge",
        "intro_dialogue": "यहाँ ऑक्सीजन कम और ठंड हड्डियों तक जम जाती है। क्या तुम्हारा हौसला जमेगा नहीं?",
        "defeat_dialogue": "अडिग हौसला! तुमने लद्दाख की बर्फीली चट्टानों को भी पिघला दिया।",
        "reward_tm": "TM13 - Ice Beam",
        "ai_tier": "High_Power_Heavy",  # FireRed Blaine AI: भारी डैमेज मूव्स और ओला-वृष्टि
        "potions": ["Hyper Potion", "Hyper Potion"],
        "team": [
            {
                "species": "Himsnow",
                "level": 42,
                "type": ["Ice", "Ground"],
                "stats": {"hp": 125, "atk": 88, "def": 85, "spe": 40},
                "moves": ["Avalanche", "Iron Head", "Rest", "Snore"]
            },
            {
                "species": "Pangonix",
                "level": 44,
                "type": ["Ice", "Water"],
                "stats": {"hp": 95, "atk": 75, "def": 90, "spe": 82},
                "moves": ["Ice Beam", "Surf", "Dragon Breath", "Hail"]
            },
            {
                "species": "Ghorashim",
                "level": 47,
                "type": ["Ice", "Fighting"],
                "stats": {"hp": 95, "atk": 120, "def": 78, "spe": 110},
                "moves": ["Blizzard", "Close Combat", "Ice Shard", "Bulk Up"]
            }
        ]
    },

    # -------------------------------------------------------------
    # 8. Assam (Brahmaputra Valley - Megh Gym)
    # -------------------------------------------------------------
    "Anamika": {
        "title": "Sky Sovereignty Marshal",
        "city": "Brahmaputra Valley, Assam",
        "badge": "Megh Badge",
        "intro_dialogue": "ब्रह्मपुत्र के ऊपर बादलों में उड़ने वाले ड्रैगन्स ही अंतिम कसौटी हैं। अपनी पूरी ताकत दिखाओ!",
        "defeat_dialogue": "अभूतपूर्व शक्ति! 8वां और अंतिम बैज तुम्हारा हुआ। भारत लीग का रास्ता खुल चुका है!",
        "reward_tm": "TM26 - Earthquake",
        "ai_tier": "Boss_Setup_Sweeper",  # FireRed Giovanni AI: ड्रैगन डांस सेटअप और ऑल-आउट अटैक
        "potions": ["Full Restore", "Hyper Potion"],
        "team": [
            {
                "species": "Mayurak",
                "level": 45,
                "type": ["Flying", "Fairy"],
                "stats": {"hp": 88, "atk": 70, "def": 78, "spe": 95},
                "moves": ["Dazzling Gleam", "Air Slash", "Roost", "Feather Dance"]
            },
            {
                "species": "Gyarados",
                "level": 46,
                "type": ["Water", "Flying"],
                "stats": {"hp": 115, "atk": 118, "def": 82, "spe": 84},
                "moves": ["Dragon Dance", "Waterfall", "Crunch", "Dragon Rage"]
            },
            {
                "species": "Altaria",
                "level": 47,
                "type": ["Dragon", "Flying"],
                "stats": {"hp": 95, "atk": 75, "def": 95, "spe": 85},
                "moves": ["Dragon Pulse", "Cotton Guard", "Sky Attack", "Sing"]
            },
            {
                "species": "Garudragon",
                "level": 50,
                "type": ["Dragon", "Flying"],
                "stats": {"hp": 110, "atk": 130, "def": 95, "spe": 115},
                "moves": ["Outrage", "Brave Bird", "Earthquake", "Tailwind"]
            }
        ]
    }
}
