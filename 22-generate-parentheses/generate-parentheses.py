class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opened : int, closed : int, s : str):
            if opened + closed == n*2:
                res.append(s)
                return
            
            if opened < n:
                dfs(opened + 1, closed, s + "(")
            
            if closed < opened:
                dfs(opened,closed + 1, s + ")")
        
        dfs(0, 0, '')
        return res
