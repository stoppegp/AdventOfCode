import os
import inspect
import time


def parse_input(file):
    with open(file, "r") as f:
        text = f.read()
    lines = text.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    return lines

def input_to_lines(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    return lines

def input_to_grid(input):
    lines = input_to_lines(input)
    return [list(x) for x in lines]

def run(cb1 = None, cb2 = None):
    base_path = os.path.dirname(inspect.getframeinfo(inspect.getouterframes(inspect.currentframe())[1][0])[0])
    with open(os.path.join(base_path, "input")) as f:
        input = f.read()
        with open(os.path.join(base_path, "example")) as f:
            example = f.read()
    if cb1 is not None:
        print(f"Running part 1...")
        with open(os.path.join(base_path, "solution1")) as f:
            solution = f.read()
        solution_sim = cb1(example, part=1)
        if str(solution_sim) != solution and solution != "":
            print(f"Example did not run correctly! Was: {solution_sim} / Should be: {solution}")
        else:
            print(f"Example was calculated correctly. Running with real input...")
            start_time = time.process_time()
            input_solution = cb1(input, part=1)
            end_time = time.process_time()
            print(f"Solution: {input_solution}")
            print(f"Took {end_time-start_time}s")

    if cb2 is not None:
        print(f"Running part 2...")
        with open(os.path.join(base_path, "solution2")) as f:
            solution = f.read()
        solution_sim = cb2(example, part=2)
        if str(solution_sim) != solution and solution != "":
            print(f"Example did not run correctly! Was: {solution_sim} / Should be: {solution}")
        else:
            print(f"Example was calculated correctly. Running with real input...")
            start_time = time.process_time()
            input_solution = cb2(input, part=2)
            end_time = time.process_time()
            print(f"Solution: {input_solution}")
            print(f"Took {end_time-start_time}s")