



def generate_parenthesis(n: int) -> list[str]:

    def dfs(current, open, closed):
        print(f"dfs called. {current}, {open}, {closed}")
        if open == 0 and closed == 0:
            print(f"reached depth")
            result.append(current)
        
        if open > 0:
            dfs(current + "(", open-1, closed)
        
        if closed > open:
            dfs(current + ")", open, closed-1)

        





    result = []
    dfs("", n, n)
    return result


print(generate_parenthesis(3))