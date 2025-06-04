from may_change import advisor_names

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
        "battle magic research permit",
        {
            advisor_names[0]: f"Your Eminence, the research is a great idea. Not only will we be able to advance the study of magic, we will also be able to conquer cities and gain influence throughout the land. I highly encourage you to permit the research.",
            advisor_names[1]: f"Your Eminence, this matter does not concern me, but it would be in your best interest to ensure the citizens are not harmed by this new magic.",
            advisor_names[2]: f"Well, well, well. I've listened to the {advisor_names[0]}, and the conquering cities part sounds extremely intriguing. Let's permit it and see what happens, shall we?",
            advisor_names[3]: f"Your Eminence, battle magic would greatly strengthen our city's defenses. Allow the research.",
            advisor_names[4]: f"Your Eminence! This is a terrible idea. Nearby cities will treat the research permit as a declaration of war, and then where will our hard-earned peace treaties go?"
        }
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