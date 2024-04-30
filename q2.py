from sympy import symbols, solve, diff

x, y, z, r, M, q = symbols('x y z r M q')

# equations
eq1 = 1 - 2*M/r + 3*M*q**2/r**3 - x**2/r**2
eq2 = ((1 - 2*M/r + 3*M*q**2/r**3)**(-1) - y**2*(x + z*r)**2)
eq3 = diff(((1 - 2*M/r + 3*M*q**2/r**3)**(-1) - y**2*(x + z*r)**2), r)

# solving equations
sol_x = solve(eq1, x)
sol_y = solve(eq2.subs(x, sol_x[0]), y)
sol_z = solve(eq3.subs([(x, sol_x[0]), (y, sol_y[0])]), z)
 
print("expression for x:", sol_x[0])
print("expression for y:", sol_y[0])
print("expression for z:", sol_z[0])
