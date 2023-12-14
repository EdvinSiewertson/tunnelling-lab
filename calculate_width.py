from sympy import symbols, tan, atan, sqrt, solve

# Define the symbol
m, V0, hbar, e, b, E = symbols('m V0 hbar e b E')

# Assign specific values to other variables
m = 0.067*9.109382e-31  # m_e in kg (effective mass)
e = 1.602176634e-19  # eU*0.3 (0.15 for Sample B)
V0 = 0.200 * e  # V0 in Joule
hbar = 1.05457e-34

def double_barrier(U, factor):
    E = e*U*factor*0.5 - V0

    # Define the equation
    equation = hbar * atan(sqrt((0.3 * U + 0.4) / (0.3 * U))) / sqrt(m * e * U * 0.3) - b

    # Solve the equation
    solutions = solve(equation, b)

    for sol in solutions:
        if sol.is_real and sol.evalf() > 0:       
            if factor==0.30:
                positive_solutions_2b = 2*sol.evalf(n=10)
                print("Solution for 2b (Sample A):")
            elif factor==0.15:
                positive_solutions_2b = sol.evalf(n=10)
                print("Solution for 2b (Sample B):")

    print(positive_solutions_2b)

double_barrier(0.3484, 0.30) # Sample A
double_barrier(0.2935, 0.15) # Sample B


