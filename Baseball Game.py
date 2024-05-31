def calPoints(self, operations: list[str]) -> int:
        record = []
        for token in operations:
            if token == "+":
                record.append(record[-1] + record[-2])
            elif token == "C":
                record.pop()
            elif token == "D":
                record.append(record[-1]*2)
            else:
                record.append( int(token))
        return sum(record)