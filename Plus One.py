### GOOD (beat 79.11%)
def plusOne(self, digits: list[int]) -> list[int]:
    if not digits:
        return [1]
    if digits[-1] + 1 < 10:
        return digits.copy()[:-1] + [digits[-1] + 1]
    else:
        new_last_digit = [(digits[-1] + 1) % 10]
        new_prev_digits = self.plusOne(digits[:-1])
        return new_prev_digits + new_last_digit