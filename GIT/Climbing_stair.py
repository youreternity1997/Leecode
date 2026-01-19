def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    
    # 初始化前兩項
    prev2 = 1  # 前兩階的方法數=1  f(n-2)
    prev1 = 2  # 前一階的方法數=2  f(n-1)
    
    # 從第 3 階開始計算
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    print(current)
    return prev1

climbStairs(4)
climbStairs(5)
climbStairs(6)