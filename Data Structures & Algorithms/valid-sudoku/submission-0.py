class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_seen = [[False]*9 for _ in range(9)]
        c_seen = [[False]*9 for _ in range(9)]
        b_seen = [[[False]*9 for _ in range(3)] for _ in range(3)]
        for j, row in enumerate(board):
            for k, s_num in enumerate(row):
                if s_num == ".":
                    continue
                num = int(s_num)
                print(f"seen {num} in row {j},col {k}, block {j//3}{k//3}")
                if r_seen[j][num-1]:
                    print("row")
                    return False
                else:
                    r_seen[j][num-1] = True
                if c_seen[k][num-1]:
                    print("col")
                    return False
                else:
                    c_seen[k][num-1] = True
                if b_seen[j//3][k//3][num-1]:
                    return False
                else:
                    b_seen[j//3][k//3][num-1] = True
                
        return True