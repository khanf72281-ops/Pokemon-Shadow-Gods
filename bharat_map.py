# bharat_map.py

BHARAT_WORLD_MAP = {
    # Starting Town
    "Tarana_Town": {
        "state": "Madhya Pradesh",
        "description": "Prof. Raheem ki eco-lab aur purane mitti ke teele.",
        "connections": {"North": "Route_1_Malwa"},
        "points_of_interest": ["Prof_Raheem_Lab", "Mitti_Rest_House"]
    },
    
    "Route_1_Malwa": {
        "state": "Madhya Pradesh",
        "wild_levels": (2, 5),
        "spawns": ["Mungor", "Chilbil"],
        "connections": {"South": "Tarana_Town", "North": "Ujjain_City"}
    },

    # Gym 1
    "Ujjain_City": {
        "state": "Madhya Pradesh",
        "gym": "Maati_Gym",
        "leader": "Vikram",
        "badge": "Maati Badge",
        "connections": {"South": "Route_1_Malwa", "East": "Route_2_Chambal_Bridge"}
    },

    # Gym 2 Road -> Bengal
    "Route_2_Chambal_Bridge": {
        "state": "Madhya Pradesh / Bengal Highway",
        "connections": {"West": "Ujjain_City", "East": "Sundarban_Delta"}
    },
    "Sundarban_Delta": {
        "state": "West Bengal",
        "gym": "Jwar_Gym",
        "leader": "Arpana",
        "badge": "Jwar Badge",
        "connections": {"West": "Route_2_Chambal_Bridge", "North": "Delhi_NCR"}
    },

    # Gym 3 -> Delhi
    "Delhi_NCR": {
        "state": "Delhi",
        "gym": "Chakra_Gym",
        "leader": "Kabir",
        "badge": "Chakra Badge",
        "connections": {"South": "Sundarban_Delta", "SouthWest": "Silent_Valley"}
    },

    # Gym 4 -> Kerala
    "Silent_Valley": {
        "state": "Kerala",
        "gym": "Aranya_Gym",
        "leader": "Keshavan",
        "badge": "Aranya Badge",
        "connections": {"North": "Delhi_NCR", "NorthWest": "Lonavala_Ridge"}
    },

    # Gym 5 -> Maharashtra
    "Lonavala_Ridge": {
        "state": "Maharashtra",
        "gym": "Pashan_Gym",
        "leader": "Tanvi",
        "badge": "Pashan Badge",
        "connections": {"South": "Silent_Valley", "North": "Thar_Jaisalmer"}
    },

    # Gym 6 -> Rajasthan
    "Thar_Jaisalmer": {
        "state": "Rajasthan",
        "gym": "Marichika_Gym",
        "leader": "Bhairav",
        "badge": "Marichika Badge",
        "connections": {"South": "Lonavala_Ridge", "North": "Leh_Plateau"}
    },

    # Gym 7 -> Ladakh
    "Leh_Plateau": {
        "state": "Ladakh",
        "gym": "Himshikhar_Gym",
        "leader": "Tashi",
        "badge": "Himshikhar Badge",
        "connections": {"South": "Thar_Jaisalmer", "East": "Brahmaputra_Pass"}
    },

    # Gym 8 -> Assam
    "Brahmaputra_Pass": {
        "state": "Assam",
        "gym": "Megh_Gym",
        "leader": "Anamika",
        "badge": "Megh Badge",
        "connections": {"West": "Leh_Plateau", "North": "Uttarakhand_Plateau"}
    },

    # Final League
    "Uttarakhand_Plateau": {
        "state": "Uttarakhand",
        "league": "Bharat_Pokemon_League",
        "requirement": 8,  # 8 Badges required
        "connections": {"South": "Brahmaputra_Pass"}
    }
}
