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
                if r_seen[j][num-1] | c_seen[k][num-1] | b_seen[j//3][k//3][num-1]:
                    return False
                r_seen[j][num-1] = True
                c_seen[k][num-1] = True
                b_seen[j//3][k//3][num-1] = True        
        return True