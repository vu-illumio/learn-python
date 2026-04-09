class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, point):
        x_diff = self.x - point.x
        y_diff = self.y - point.y
        return (x_diff**2 + y_diff**2)**0.5
    def __str__(self):
        return(f'<{self.x},{self.y}>')

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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_prev2 = 0
        fib_prev1 = 1
        for i in range(1, n):
            fib = fib_prev1 + fib_prev2
            fib_prev2 = fib_prev1
            fib_prev1 = fib
        return fib

def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)

def fact_iter(n):
    if n <= 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact = i * fact
        return fact

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
                idx_search(e, elist, idx_lo, idx_mi-1)
            else:
                idx_search(e, elist, idx_mi+1, idx_hi)
    idx_search(e, elist, 0, len(elist)-1)

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

