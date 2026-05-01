class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return(f'<{self.x},{self.y}>')
    def distance(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return (x_diff**2 + y_diff**2)**0.5

class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.den = d
    def __str__(self):
        return str(self.num / self.den)
    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)
    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)
    def invert(self):
        return Fraction(self.den, self.num)

s = { 0:0, 1:1 }
def fib_recur(n):
    if n in s:
        return s[n]
    else:
        v = fib_recur(n-1) + fib_recur(n-2)
        s[n] = v
        return v

def fib_iter(n):
    if n < 2:
        return n
    else:
        f0 = 0
        f1 = 1
        for i in range(n-1):
            f = f0 + f1
            f0 = f1
            f1 = f
        return f

def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)

def fact_iter(n):
    if n <= 1:
        return 1
    else:
        p = 1
        for i in range(2, n+1):
            p *= i
        return p

def bin_search(e, elist):
    def idx_search(e, elist, idx_lo, idx_hi):
        if idx_hi < idx_lo:
            return False
        elif idx_hi == idx_lo:
            return elist[idx_lo] == e
        else:
            idx_mi = (idx_hi + idx_lo) // 2
            if elist[idx_mi] == e:
                return True
            elif elist[idx_mi] > e:
                return idx_search(e, elist, idx_lo, idx_mi-1)
            else:
                return idx_search(e, elist, idx_mi+1, idx_hi)
    return idx_search(e, elist, 0, len(elist)-1)

# def genSubSets(elist):
#     if len(elist) == 0:
#         return [[]]
#     else:
#         e = elist.pop()
#         s = genSubSets(elist)
#         c = s.copy()
#         for i in c:
#             s.append(i + [e])
#         return s

def genSubSets(elist):
    if len(elist) == 0:
        return [[]]
    else:
        e = elist[-1:]
        s = genSubSets(elist[:-1])
        a = []
        for i in s:
            a.append(i + e)
        return s + a

