from z3 import *

def encode_fashion_store_problem(garments):
    # Create a Z3 solver
    solver = Solver()

    # Define the variables
    garment_vars = {}
    color_vars = {}
    for garment, color in garments:
        garment_vars[garment] = Bool(garment)
        if color not in color_vars:
            color_vars[color] = Bool(color)

    # Add constraints
    # for g1, c1 in garments:
    #     for g2, c2 in garments:
    #         # Constraint: Garments with the same type cannot be together
    #         if g1 != g2:
    #             solver.add(Or(Not(garment_vars[g1]), Not(garment_vars[g2])))

    #         # Constraint: Garments with the same color cannot be together
    #         if c1 == c2 and g1 != g2:
    #             solver.add(Or(Not(garment_vars[g1]), Not(garment_vars[g2])))
    # print("Garment Variables: ", garment_vars)
    # print("Color Variables: ", color_vars)

    # Constraint: At least one garment must be selected
    solver.add(Or([garment_vars[garment] for garment in garment_vars]))
    # print(solver)

    print(solver.assertions)
    # Check if the problem is satisfiable
    if solver.check() == sat:
        # Get the satisfying model
        model = solver.model()
        satisfying_garments = [(garment, color) for garment, var in garment_vars.items() if is_true(model[var])
                               for color, var in color_vars.items() if is_true(model[var])]
        return satisfying_garments
    else:
        #print unsatisfiable cases
        print("UNSATISFIABLE")
        print(solver.model())
        return None

# Read the input from a text file
def read_input_from_file(file_path):
    garments = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                garment, color = line.split(',')
                garments.append((garment.strip(), color.strip()))
    return garments

# TESTING
file_path = "test_list.txt"
garments = read_input_from_file(file_path)
solution = encode_fashion_store_problem(garments)

if solution:
    print("Satisfiable:")
    for garment, color in solution:
        print(f"Garment: {garment}, Color: {color}")
else:
    print("UNSATISFIABLE")