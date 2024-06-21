def solve(s):
    output = set()

    if len(s) == 1:
        return s[0]

    if s[0] != s[1]: output.add(s[0])
    if s[-1] != s[-2]: output.add(s[-1])

    l, r = 0, 1
    while r < len(s):
        if s[r] != s[l]:
            if (r - l) % 2 != 0:
                output.add(s[l])
            l = r

        if r == len(s) - 1:
            if (r - l + 1) % 2 != 0:
                output.add(s[r])

        r += 1

    return "".join(sorted(list(output)))


for i in range(int(input())):
    s = input()

    print(solve(s))
