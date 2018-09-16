# gcd(greatest common divisor)

def gcd(m, n):
    if m<n: return gcd(n, m)
    r = m%n
    return gcd(n, r) if r else n

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a%b)
        y -= (a/b)*x
        return d, x, y
    else:
        return a, 1, 0