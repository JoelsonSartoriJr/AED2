def makeCange(n):
    c = [100, 25, 10, 5, 1]
    s = [0]*len(c)
    i = 0
    while n != 0:
        if c[i] <= n:
            mod = n//c[i]
            s[i] = mod
            n = n%c[i]
        i += 1
    return s

print(makeCange(253))