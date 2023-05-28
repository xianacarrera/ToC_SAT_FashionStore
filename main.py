from z3 import *
from fashion_options import Clothes, Colors

options = {
    "verbose": True,
    "possible_solution": True,
    "statistics": True
}

def add_fixed_constraints(solver):

    # ---------------------------------------- GARMENT CONTRAINTS ----------------------------------------
   
    # Constraint: Pairs of garments that cannot be together
    incompatible_garments = [["sandals", "socks"], ["skirt", "pants"], ["dress", "tshirt"], ["sandals", "shoes"]]
    for pair in incompatible_garments:
        solver.add(Or(Not(Clothes[pair[0]]), Not(Clothes[pair[1]])))
    
    # Constraint: Either shoes or sandals
    solver.add(Or(Clothes['shoes'], Clothes['sandals']))
    
    # Constraint: Either a dress or (a Tshirt and pants) or (a Tshirt and skirt)
    solver.add(Or(Clothes['dress'], And(Clothes['tshirt'], Clothes['pants']), 
               And(Clothes['tshirt'], Clothes['skirt'])))
    
    # Constraint: Shoes imply socks
    solver.add(Implies(Clothes['shoes'], Clothes['socks']))
    
    # Constraint: A dress implies a hat (for fancy purposes :))
    solver.add(Implies(Clothes['dress'], Clothes['hat']))

    # Implicit constraint: no repeated garments (checked outside of the solver)

    # ---------------------------------------- COLOR CONTRAINTS ----------------------------------------
    
    # Constraint: Pairs of colors that cannot be together
    incompatible_colors = [["blue", "green"], ["pink", "green"], ["green", "red"], ["blue", "red"], ["pink", "red"]]
    for pair in incompatible_colors:
        solver.add(Or(Not(Colors[pair[0]]), Not(Colors[pair[1]])))

    # Constraint: No more than 3 colors
    solver.add(AtMost(*[Colors[color] for color in Colors], 3))

    # Constraint: No monocolor outfit
    solver.add(AtLeast(*[Colors[color] for color in Colors], 2))

    # ---------------------------- GARMENTS AND COLORS COMBINATIONS CONTRAINTS --------------------------

    # Constraint: No violet hats with pink dresses, and no pink hats with violet dresses
    solver.add(Not(And(Clothes['hat'], Colors['violet'], Clothes['dress'], Colors['pink'])))
    
    

def add_input_constraints(solver, garment_vars, color_vars):
    clothes_copy = Clothes.copy()
    colors_copy = Colors.copy()

    chosen_garments = []
    chosen_colors = []

    for garment in garment_vars:
        chosen_garments.append(garment_vars[garment])
        clothes_copy.pop(garment)
    
    for color in color_vars:
        chosen_colors.append(color_vars[color])
        colors_copy.pop(color)

    # All the garments chosen by the user must be present in the solution
    solver.add(And(*chosen_garments))
    # All the colors chosen by the user must be present in the solution
    solver.add(And(*chosen_colors))

    # None of the garments not chosen by the user can be present in the solution
    solver.add(And(*[Not(clothes_copy[garment]) for garment in clothes_copy]))
    # None of the colors not chosen by the user can be present in the solution
    solver.add(And(*[Not(colors_copy[color]) for color in colors_copy]))

def get_possible_solution(solver):
    if solver.check():
        possible_sol = solver.model()
        print("\n\nPossible solution: ")
        for d in possible_sol.decls():
            print("%s = %s" % (d.name(), possible_sol[d]))

def encode_fashion_store_problem(garments, colors, options = {}):
    # Create a Z3 solver
    solver = Solver()
    # Dictionaries for the input variables
    garment_vars = {}
    color_vars = {}
    
    # Transform the user garments and colors into Z3 variables
    for garment in garments:
        garment_vars[garment] = Bool(garment)

    for color in colors:
        if color not in color_vars:
            color_vars[color] = Bool(color)

    # Add the contraints fixed by the store
    add_fixed_constraints(solver)

    # Get a possible solution with the fixed constraints
    if options.get("possible_solution", False):
        get_possible_solution(solver)

    # Transform the user input into Z3 constraints
    add_input_constraints(solver, garment_vars, color_vars)

    # Check if the problem is satisfiable
    result = solver.check()

    if options.get("verbose", False):
        # Print the contraints and the model if the problem is satisfiable
        print("\n\nContraints:")
        for c in solver.assertions():
            print(c)

        print("Result: ", result)
    
    if options.get("statistics", False):
        print("\n\nStatistics:")
        for k, v in solver.statistics():       # Performance statistics
            print("%s : %s" % (k, v))

    if result == sat:
        # Get the satisfying model
        model = solver.model()
        if options.get("verbose", False):
            print("model", model)
        return True 
    else:                            # unsat or unknown (failed to solve)
        return False


def check_input(garment, color, garments):
    # TODO: integrate this with the front end
    if garment not in Clothes:          # Not one of the garments the store sells
        print(f"Invalid garment: {garment}")
        exit(1)
    if color not in Colors:             # Not one of the colors the store sells
        print(f"Invalid color: {color}")
        exit(1)
    if garment in garments:             # Repeated garment
        print(f"Repeated garment: {garment}")
        exit(1)


# Read the input from a text file
def read_input_from_file(file_path):
    garments = []
    colors = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                splitted_line = line.split(',')

                # Each line must be of the format "garment, color"
                if len(splitted_line) != 2:   
                    # TODO: integrate this with the front end
                    print("Invalid input line: ", line)
                    exit(1)

                garment, color = splitted_line
                garment = garment.strip()
                color = color.strip()

                check_input(garment, color, garments)

                garments.append(garment)
                colors.append(color)
    return garments, colors


def run(file_path = "tests/test_list.txt", options = options):
    garments, colors = read_input_from_file(file_path)
    solution = encode_fashion_store_problem(garments, colors, options)

    print("\n\n")
    if solution:
        print("SATISFIABLE:")
        if options.get("verbose", False):
            for garment, color in zip(garments, colors):
                print(f"Garment: {garment}, Color: {color}")
        return True
    else:
        print("UNSATISFIABLE")
    return False

if __name__ == "__main__":
    run()

