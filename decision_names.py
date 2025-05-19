decision_names = [
    [
        "The Arcanum asks to be permitted to research battle magic.\nOption A +10 to Arcanum and -10 to Veiled; Option B -10 to Arcanum.",
        True,
        [
            ["The Arcanum", "favor", 10], 
            ["The Veiled", "favor", -10]
        ],
        [
            ["The Arcanum", "favor", -10] 
        ]
    ],
    [
        "The Commander of the Iron Guard requests more military bases around the city.\nOption A +10 presence to Iron Guard and +5 suspicion to all other factions; Option B -10 favor to Iron Guard.",
        True,
        [
            ["The Iron Guard", "presence", 10], 
            ["The Arcanum", "suspicion", 5], 
            ["The Veiled", "suspicion", 5], 
            ["The Gilded", "suspicion", 5], 
            ["The Commoners", "suspicion", 5]
        ],
        [
            ["The Iron Guard", "favor", -10]
        ]
    ],
    [
        "A merchant from the Gilded wants to screw over Commoners.\nOption A +10 favor to Gilded and -10 favor to Commoners; Option B -10 favor to Gilded and +10 favor to Commoners.",
        True,
        [
            ["The Gilded", "favor", 10], 
            ["The Commoners", "favor", -10]
        ],
        [
            ["The Gilded", "favor", -10], 
            ["The Commoners", "favor", 10]
        ]
    ]
]