def solve(a, b, c, d):
    if not ((a < b) and (c < d) or (a > b) and (c > d)):
        return "NO"
    if not ((a < c) and (b < d) or (a > c) and (b > d)):
        return "NO"
    
    return "YES"


for i in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    print(solve(a, b, c, d))