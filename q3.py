def newton_backward_interpolation(x, y, year):
    n = len(x)
    h = x[1] - x[0]
    
    # calculating backward diff table
    n = len(x)
    table = [[0] * n for _ in range(n)]

    for i in range(n):
        table[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]

    u = (year - x[-1]) / h

    result = table[-1][0]

    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (u + j) / (j + 1)
        result += term * table[-1 - i][i]

    return result

years = [1941, 1951, 1961, 1971, 1981, 1991]
pop = [12, 15, 20, 27, 39, 52]

population_1976 = newton_backward_interpolation(years, pop, 1976)
population_1978 = newton_backward_interpolation(years, pop, 1978)
increase_1976_to_1978 = population_1978 - population_1976

print(f"estimated population in 1976: {population_1976}")
print(f"estimated population in 1978: {population_1978}")
print(f"increase in population from 1976 to 1978: {increase_1976_to_1978}")