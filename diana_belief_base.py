def load_princess_diana_beliefs(self):
        """Preloads the belief base with the Princess Diana hypothesis beliefs."""
        print("Loading Princess Diana beliefs...")
        self.clear()
        self.add("R")  # Royal family had motive
        self.add("E")  # Evidence of foul play
        self.add("M")  # Media is covering up
        self.add("~R | ~E | ~M | D")  # (R ∧ E ∧ M) → D
        self.add("A | D")  # ¬A → D
        self.add("A | D")  # A ∨ D
        

belief_base_cnf = [
    {"R"},
    {"E"},
    {"M"},
    {"¬R", "¬E", "¬M", "D"},
    {"A", "D"},  
]
