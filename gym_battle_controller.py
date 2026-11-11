# gym_battle_controller.py

class GymBattleController:
    @staticmethod
    def ai_turn_decision(leader_data, active_mon, player_mon):
        """FireRed AI: हेल्थ 25% से कम होने पर पोशन, वरना बेस्ट मूव"""
        # 1. पोशन चेक (हेल्थ कम होने पर)
        if active_mon.current_hp < (active_mon.max_hp * 0.25) and len(leader_data["potions"]) > 0:
            potion = leader_data["potions"].pop(0)
            heal_amount = 200 if potion == "Full Restore" else (120 if potion == "Hyper Potion" else 50)
            active_mon.current_hp = min(active_mon.max_hp, active_mon.current_hp + heal_amount)
            return {"action": "USE_ITEM", "item": potion, "target": active_mon.species}

        # 2. मूव चुनना (सुपर इफेक्टिव को प्राथमिकता)
        # FireRed की तरह रैंडम मूव चुनने के बजाय डैमेजिंग मूव्स को वरीयता
        selected_move = active_mon.moves[0]
        return {"action": "ATTACK", "move": selected_move}

    @staticmethod
    def award_badge_and_unlock(player, leader_name):
        leader = BHARAT_GYM_LEADERS[leader_name]
        player.badges.append(leader["badge"])
        print("\n" + "=" * 50)
        print(f"🎖️ {leader['badge']} प्राप्त हुआ!")
        print(f"🎁 {leader['reward_tm']} भी इन्वेंटरी में जोड़ दिया गया!")
        print("=" * 50)
        
        # 8 बैज पूरे होने पर लीग अनलॉक
        if len(player.badges) >= 8:
            print("\n🏔️ बधाई! उत्तराखंड हिमालयन लीग का रास्ता खुल गया है!")
            player.league_unlocked = True
