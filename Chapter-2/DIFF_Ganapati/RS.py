import math
def richardson_extrapolation(T, x, h, k):
    n = len(T)  # Number of components in tensor vector
    derivatives = [0] * n

    for i in range(n):
        D = []
        for j in range(k + 1):
            step_size = h / (2 ** j)
            D.append((T[i](x + step_size) - T[i](x)) / step_size)

        # Richardson's extrapolation
        for j in range(k):
            for m in range(k - j):
                D[m] = (4 ** (j + 1) * D[m + 1] - D[m]) / (4 ** (j + 1) - 1)

        derivatives[i] = D[0]

    return derivatives

def T1(x): return math.exp(x)
def T2(x): return math.sin(x)
def T3(x): return x**2


T = [T1, T2, T3]
x = 1
h = 0.1
k = 2

derivatives = richardson_extrapolation(T, x, h, k)
print(derivatives)