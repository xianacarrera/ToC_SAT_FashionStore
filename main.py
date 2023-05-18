from z3 import *


Clothes = {
    'tshirt' : Bool('tshirt'),
    'pants' : Bool('pants'),
    'hat' : Bool('hat'),
    'shoes': Bool('shoes'),
    'socks': Bool('socks'),
    'dress': Bool('dress'),
    'skirt': Bool('skirt'),
    'sandals': Bool('sandals')
}

Colors = {
    'red' : Bool('red'),
    'blue' : Bool('blue'),
    'green' : Bool('green'),
    'violet' : Bool('violet'),
    'white': Bool('white'),
    'black': Bool('black'),
    'pink': Bool('pink')
}


def add_constraints(solver):
    # Constraint: At least one garment must be selected
    #solver.add(Or([garment_vars[garment] for garment in garment_vars]))

    # ---------------------------------------- GARMENT CONTRAINTS ----------------------------------------
   
    # Constraint: Pairs of garments that cannot be together
    incompatible_garments = [["sandals", "socks"], ["skirt", "pants"], ["dress", "tshirt"]]
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
    



def encode_fashion_store_problem(garments):
    # Create a Z3 solver
    solver = Solver()
    # solver.add(Bool('x'))
    # print(solver.check(), solver.model())
    # Define the variables
    garment_vars = {}
    color_vars = {}
    

    for garment, color in garments:
        if garment in garment_vars:
            print("Repeated garment: ", garment)
            exit(1)
        garment_vars[garment] = Bool(garment)
        if color not in color_vars:
            color_vars[color] = Bool(color)


    add_constraints(solver)

    print(solver.assertions)
    # Check if the problem is satisfiable
    if solver.check() == sat:
        # Get the satisfying model
        model = solver.model()
        print("model", model);
        
        # get satisfying garnments if any
        # true_items = [d() for d in model.decls() if is_true(model[d])]
        # satisfying_garments = []
        #print("true items ",true_items)

        # for i in range(len(garments)):
        #     if Bool(garments[i][0]) in true_items:
        #         satisfying_garments.append(garments[i])
        
        # return satisfying_garments
        return True 
    else:
        #print unsatisfiable cases
        # print("UNSATISFIABLE")
        # print(solver.model())
        return False

def check_input(garments):
    for garment, color in garments:
        if garment not in Clothes:
            print(f"Invalid garment: {garment}")
            return False
        if color not in Colors:
            print(f"Invalid color: {color}")
            return False
    return True


# Read the input from a text file
def read_input_from_file(file_path):
    garments = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                splitted_line = line.split(',')
                if len(splitted_line) != 2:
                    # TODO: integrate this with the front end
                    print(line)
                    exit(1)
                garment, color = splitted_line
                garments.append((garment.strip(), color.strip()))
    print(garments)
    return garments

# TESTING
file_path = "test_list.txt"
garments = read_input_from_file(file_path)
if not check_input(garments):
    # TODO: integrate this with the front end
    exit(1)
solution = encode_fashion_store_problem(garments)

if solution:
    print (solution)
    print("Satisfiable:")
    for garment, color in garments:
        print(f"Garment: {garment}, Color: {color}")
else:
    print("UNSATISFIABLE")

