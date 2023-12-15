from sympy import symbols, tan, atan, sqrt, solve

# Define the symbol
m, V0, hbar, e, b, E = symbols('m V0 hbar e b E')

# Assign specific values to variables
m = 0.067*9.109382e-31  # Effective mass
e = 1.602176634e-19
V0 = 0.200 * e  # V0 in J
hbar = 1.05457e-34 # in Js

def double_barrier(U, sample):
    # Define the equation
    equation = hbar * atan(sqrt((0.3 * U + 0.4) / (0.3 * U))) / sqrt(m * e * U * 0.3) - b

    # Solve the equation
    solutions = solve(equation, b)

    for sol in solutions:
        if sol.is_real and sol.evalf() > 0:       
            if sample=='A':
                positive_solutions_2b = 2*sol.evalf(n=10)
                print("Width of Sample A:", end=' ')
            elif sample=='B':
                positive_solutions_2b = sol.evalf(n=10)
                print("Width of Sample B:", end=' ')

    print(positive_solutions_2b)

double_barrier(0.3484, 'A') # Sample A
double_barrier(0.2935, 'B') # Sample B
