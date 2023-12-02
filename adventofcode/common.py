def parse_input(file):
    with open(file, "r") as f:
        text = f.read()
    lines = text.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    return lines
