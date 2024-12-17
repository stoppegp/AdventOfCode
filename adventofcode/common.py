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

def run(cb = None, example_file = None, solution_file = None, *args, **kwargs):
    base_path = os.path.dirname(inspect.getframeinfo(inspect.getouterframes(inspect.currentframe())[1][0])[0])
    with open(os.path.join(base_path, "input")) as f:
        input = f.read()

    print(f"Running...")
    if example_file is not None:
        with open(os.path.join(base_path, example_file)) as f:
            example = f.read()
        try:
            with open(os.path.join(base_path, solution_file)) as f:
                solution = f.read()
        except:
            solution = ""
        solution_sim = cb(example, example=True, *args, **kwargs)
        if str(solution_sim) != solution and solution != "":
            print(f"Example did not run correctly! Was: {solution_sim} / Should be: {solution}")
            return
        elif str(solution_sim) == solution:
            print(f"Example was calculated correctly.")

    print(f"Running with real input...")
    start_time = time.process_time()
    input_solution = cb(input, *args, **kwargs)
    end_time = time.process_time()
    print(f"Solution: {input_solution}")
    print(f"Took {end_time-start_time}s")