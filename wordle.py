from letter_state import LetterState


class Wordle:
    MAX_ATTEMPT = 6
    WORD_SIZE = 5

    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1].upper() == self.secret

    def attempt(self, word: str):
        self.attempts.append(word)

    def guess(self, word: str):
        result = []
        for i in range(self.WORD_SIZE):
            character = word[i].upper()
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            result.append(letter)
        return result

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPT - len(self.attempts)

    @property
    def is_attempt_allowed(self):
        return self.remaining_attempts > 0 and not self.is_solved
