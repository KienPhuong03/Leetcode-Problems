def tictactoe(moves: list[list[int]]) -> str:
    rows = {0: [], 1: [], 2:[]}
    cols = {0: [], 1: [], 2:[]}
    diags = {"left": [], "right":[]}
    whose_move = {0: "A", 1:"B"}
    for ix, (i,j) in enumerate(moves):
        rows[i].append(whose_move[ix % 2])
        cols[j].append(whose_move[ix % 2])
        if i == j == 1:
            diags["left"].append(whose_move[ix % 2])
            diags["right"].append(whose_move[ix % 2])
        elif abs(i-j) == 2:
            diags["right"].append(whose_move[ix % 2])
        elif i == j:
            diags["left"].append(whose_move[ix % 2])
        for row_ix in rows:
            if len(rows[row_ix]) == 3 and all(letter == rows[row_ix][0] for letter in rows[row_ix]):
                return rows[row_ix][0]
        for col_ix in cols:
            if len(cols[col_ix]) == 3 and all(letter == cols[col_ix][0] for letter in cols[col_ix]):
                return cols[col_ix][0]
        for diag in diags:
            if len(diags[diag]) == 3 and all(letter == diags[diag][0] for letter in diags[diag]):
                return diags[diag][0]
    if len(moves) < 9:
        return "Pending"
    else:
        return "Draw"
        
print(tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))