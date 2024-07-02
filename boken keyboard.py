def solve(s):
    l, r = 0, 0

    ans = set()

    while r < len(s):
        if s[l] == s[r]:
            r += 1
        else:
            if (r - l) % 2 != 0:
                ans.add(s[l])
            l = r

    if (r - l) % 2 != 0:
        ans.add(s[l])

    return "".join(sorted(list(ans)))


for i in range(int(input())):
    s = input()
    print(solve(s))
