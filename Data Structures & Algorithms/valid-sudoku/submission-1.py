class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # go through whole board and skip "."
        # for each spot, check whether its been seen in that rows hashset, that columns hashset or that squares hashset
        # do this in a single pass

        subbox = set()
        rowset = set()
        columnset = set()

        for i in range(len(board)):
            # i is index of the row
            rowset.clear()
            for j in range(len(board[i])):
                square = board[i][j]

                if square == ".":
                    continue

                if square in rowset:
                    return False
                else: 
                    rowset.add(square)

                if ((j,square)) in columnset:
                    return False
                else: 
                    columnset.add((j,square))
                if ((i//3,j//3,square)) in subbox:
                    return False
                else:
                    subbox.add((i//3,j//3,square))
        return True
