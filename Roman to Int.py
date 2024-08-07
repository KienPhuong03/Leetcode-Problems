def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        output = 0
        for ix in range(len(s) - 1, -1, -1):
            if ix == len(s) - 1:
                output += roman_to_int[s[len(s) - 1]]
            else:
                if s[ix] == "I":
                    if s[ix + 1] == "V" or s[ix + 1] == "X":
                        output -= 1
                    else:
                        output += 1
                elif s[ix] == "X":
                    if s[ix + 1] == "L" or s[ix + 1] == "C":
                        output -= 10
                    else:
                        output += 10
                elif s[ix] == "C":
                    if s[ix + 1] == "D" or s[ix + 1] == "M":
                        output -= 100
                    else:
                        output += 100
                else:
                    output += roman_to_int[s[ix]]
        return output
