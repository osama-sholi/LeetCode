class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        board = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']}

        comb_count = 1
        for i in range(len(digits)):
            comb_count *= len(board[digits[i]])
        result = [''] * comb_count

        portion_size = comb_count
        sep = portion_size
        for i in range(len(digits)):
            portion_size /= len(board[digits[i]])
            sep = portion_size
            j = 0
            k = 0
            for j in range(comb_count):
                if j == sep:
                    k = k + 1 if k < len(board[digits[i]]) - 1 else 0
                    sep += portion_size
                result[j] += board[digits[i]][k]
        
        return result

            


