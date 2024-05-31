def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        sarr = sorted(arr)
        diff = sarr[1] - sarr[0]
        i = 0
        while i < len(sarr) - 1:
            if sarr[i + 1] - sarr[i] != diff:
                return False
            else:
                i += 1
        return True
