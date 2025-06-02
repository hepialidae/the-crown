decision_names = [
    [
        "The Arcanum asks to be permitted to research battle magic.\nOption A: Give them the permit. (+10 to Arcanum and -10 to Veiled)\nOption B: Reject them. (-10 to Arcanum)",
        True,
        [
            ["The Arcanum", "favor", 10], 
            ["The Veiled", "favor", -10]
        ],
        [
            ["The Arcanum", "favor", -10] 
        ],
        "battle magic research permit"
    ],
    [
        "The Commander of the Iron Guard requests more military bases around the city.\nOption A: Build military bases. (+10 presence to Iron Guard and +5 suspicion to all other factions)\nOption B: Reject them. (-10 favor to Iron Guard)",
        True,
        [
            ["The Iron Guard", "presence", 10], 
            ["The Arcanum", "suspicion", 5], 
            ["The Veiled", "suspicion", 5], 
            ["The Gilded", "suspicion", 5], 
            ["The Commoners", "suspicion", 5]
        ],
        [
            ["The Iron Guard", "suspicion", 5]
        ],
        "military bases"
    ],
    [
        "A merchant from the Gilded wants to screw over Commoners.\nOption A: Turn a blind eye. (+10 favor to Gilded and -10 favor to Commoners)\nOption B: Stop them. (-10 favor to Gilded and +10 favor to Commoners)",
        True,
        [
            ["The Gilded", "favor", 10], 
            ["The Commoners", "favor", -10]
        ],
        [
            ["The Gilded", "favor", -10], 
            ["The Commoners", "favor", 10]
        ],
        "Commoner scams"
    ],
    [
        "The Commoners want to build shelters for the homeless in place of a new military base.\nOption A: Reject plans for military base and build homeless shelter. (+10 favor to Commoners and -10 presence to Iron Guard)\nOption B: Reject the homeless. (-10 favor to Commoners)",
        True,
        [
            ["The Commoners", "favor", 10], 
            ["The Iron Guard", "presence", -10]
        ],
        [
            ["The Commoners", "favor", -10]
        ],
        "homeless shelters"
    ]
]