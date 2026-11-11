# bharat_regions_data.py

BHARAT_WORLD = {
    "Tarana": {
        "state": "Madhya Pradesh",
        "type": "Origin Hub",
        "description": "Archaeo-Lab founded by Prof. Raheem outside ASI prohibited perimeters.",
        "connected_to": ["Ujjain"]
    },
    "Ujjain": {
        "state": "Madhya Pradesh",
        "gym_name": "Maati Akhada",
        "leader": "Vikram",
        "badge": "Maati Badge",
        "architecture_compliance": "AMASR Act compliant: Teakwood & rammed red soil outdoor pavilion.",
        "team": [("Mungor", 12), ("Gajarock", 14)],
        "connected_to": ["Tarana", "Sundarban"]
    },
    "Sundarban": {
        "state": "West Bengal",
        "gym_name": "Jwar Arena",
        "leader": "Arpana",
        "badge": "Jwar Badge",
        "architecture_compliance": "CRZ-I compliant: Floating pontoon platforms, zero concrete in mangroves.",
        "team": [("Gharikid", 18), ("Delta-Naga", 21)],
        "connected_to": ["Ujjain", "Delhi"]
    },
    "Delhi": {
        "state": "Delhi NCR",
        "gym_name": "Chakra Transit Hub",
        "leader": "Kabir",
        "badge": "Chakra Badge",
        "architecture_compliance": "NBC 2016 verified: High-efficiency solar grid & certified emergency exits.",
        "team": [("Mungor", 20), ("Lohashva", 24)],
        "connected_to": ["Sundarban", "SilentValley"]
    },
    "SilentValley": {
        "state": "Kerala",
        "gym_name": "Aranya Canopy",
        "leader": "Keshavan",
        "badge": "Aranya Badge",
        "architecture_compliance": "Forest Conservation Act compliant: Non-invasive suspension bridge ring.",
        "team": [("Tusklet", 25), ("Vanarkesh", 29)],
        "connected_to": ["Delhi", "Lonavala"]
    },
    "Lonavala": {
        "state": "Maharashtra",
        "gym_name": "Pashan Amphitheatre",
        "leader": "Tanvi",
        "badge": "Pashan Badge",
        "architecture_compliance": "Geological Survey norm: Natural basalt plateau, zero explosives used.",
        "team": [("Nakulor", 37), ("Shailasur", 43)],
        "connected_to": ["SilentValley", "Jaisalmer"]
    },
    "Jaisalmer": {
        "state": "Rajasthan",
        "gym_name": "Marichika Haveli",
        "leader": "Bhairav",
        "badge": "Marichika Badge",
        "architecture_compliance": "Heritage Sandstone structure: Passive wind-catchers & rainwater cisterns.",
        "team": [("Sherling", 38), ("Bhavandar", 43)],
        "connected_to": ["Lonavala", "Leh"]
    },
    "Leh": {
        "state": "Ladakh",
        "gym_name": "Himshikhar Monastery",
        "leader": "Tashi",
        "badge": "Himshikhar Badge",
        "architecture_compliance": "Seismic Zone V compliant: Passive-solar trombe wall rammed-earth dome.",
        "team": [("Gharikid", 42), ("Ghorashim", 47)],
        "connected_to": ["Jaisalmer", "Brahmaputra"]
    },
    "Brahmaputra": {
        "state": "Assam",
        "gym_name": "Megh Pavilion",
        "leader": "Anamika",
        "badge": "Megh Badge",
        "architecture_compliance": "Disaster management compliant: Elevated bamboo suspension terrace.",
        "team": [("Delta-Naga", 45), ("Garudragon", 50)],
        "connected_to": ["Leh", "HimalayanLeague"]
    },
    "HimalayanLeague": {
        "state": "Uttarakhand",
        "type": "Multiverse Summit",
        "description": "Zero-footprint geothermal domes on the Himalayan ridge.",
        "connected_to": ["Brahmaputra"]
    }
}
