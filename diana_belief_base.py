from .belief_base import BeliefBase


class PrincessDianaBeliefBase(BeliefBase):
    """
    Belief base tailored to the hypothesis that Princess Diana's death
    was orchestrated by the royal family. Uses propositional logic.
    """

    def __init__(self):
        super().__init__()
        self.load_princess_diana_beliefs()

    def load_princess_diana_beliefs(self):
        """Loads initial beliefs about the Princess Diana case."""
        print("Initializing belief base for Princess Diana case...")
        self.clear()
        self.add("R")                        # Royal family had motive
        self.add("E")                        # Evidence of foul play
        self.add("M")                        # Media is covering up
        self.add("~R | ~E | ~M | D")         # (R ∧ E ∧ M) → D
        self.add("A | D")                    # ¬A → D
        self.add("A | D")                    # A ∨ D

    def believes_orchestration(self) -> bool:
        """Check whether the belief base entails that the death was orchestrated."""
        return self.resolution(Belief("D"))

    def revise_with_evidence(self, new_info: str):
        """Revise belief base with new evidence (e.g., ~E, ¬R, etc.)"""
        print(f"Revising belief base with new evidence: {new_info}")
        self.revise(new_info)

    def print_status(self):
        print("\nCurrent Belief Base:")
        self.display_belief()
        result = self.believes_orchestration()
        print(f"\n🧠 Believes Diana's death was orchestrated? {'Yes' if result else 'No'}")

