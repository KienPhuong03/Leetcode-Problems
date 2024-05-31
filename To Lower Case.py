def toLowerCase(self, s: str) -> str:
        output = ""
        for char in s:
            if 65 <= ord(char) <= 90:
                output += chr(ord(char) + 32)
            else:
                output += char
        return output