def fib_DyPro(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_DyPro(n-1, d) + fib_DyPro(n-2, d)
        d[n] = ans
        return ans

d ={1:1, 2:2}
print(fib_DyPro(5,d))
