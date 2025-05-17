import tkinter as tk

faction_label_dict = {}

def create_stats_window():
    global faction_label_dict
    root = tk.Tk()
    root.title("Faction Stats")
    root.geometry("400x430")

    from factions import faction_dict  # import here to avoid circular imports

    row = 0
    for name, faction in faction_dict.items():
        name_label = tk.Label(root, text=f"{faction.name}:", font=("Helvetica", 12, "bold"))
        name_label.grid(row=row, column=0, sticky="w", padx=10, pady=(10, 0))
        row += 1

        if faction.name == "The Iron Guard":
            val_label = tk.Label(root, text=f"Military Presence: {faction.presence}")
        else:
            val_label = tk.Label(root, text=f"Favor: {faction.favor}")
        val_label.grid(row=row, column=0, sticky="w", padx=20)
        row += 1

        susp_label = tk.Label(root, text=f"Suspicion: {faction.suspicion}")
        susp_label.grid(row=row, column=0, sticky="w", padx=20, pady=(0, 10))
        row += 1

        faction_label_dict[name] = (val_label, susp_label)

    return root

def update_stats():
    from factions import faction_dict
    for name, faction in faction_dict.items():
        val_label, susp_label = faction_label_dict[name]
        if faction.name == "The Iron Guard":
            val_label.config(text=f"Military Presence: {faction.presence}")
        else:
            val_label.config(text=f"Favor: {faction.favor}")
        susp_label.config(text=f"Suspicion: {faction.suspicion}")
