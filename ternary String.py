def solve(s):
    ptr1 = ptr2 = ptr3 = None
    ans = float("inf")

    for i in range(len(s)):
        if s[i] == "1": ptr1 = i + 1
        elif s[i] == "2": ptr2 = i + 1
        elif s[i] == "3": ptr3 = i + 1

        if ptr1 and ptr2 and ptr3:
            curr_len = max(ptr1, ptr2, ptr3) - min(ptr1, ptr2, ptr3) + 1
            ans = min(ans, curr_len)

    if ans == float("inf"): ans = 0
    print(ans)


for i in range(int(input())):
    s = input()

    solve(s)