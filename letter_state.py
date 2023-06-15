class LetterState:
    def __init__(self, character: str):
        self.character = character
        self.is_in_word : bool = False
        self.is_in_position : bool = False

    def __repr__(self):
        return f"[{self.character} is in the word {self.is_in_word} and in the position {self.is_in_position}]"

