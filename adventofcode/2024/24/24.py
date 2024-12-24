from adventofcode.common import run, input_to_grid, input_to_lines
import re


def puzzle(input, part=1, example=False, *args, **kwargs):
    if part==2 and example:
        return
    start_values = {}
    gates = {}
    gate_name_repl = {}

    lines = input_to_lines(input)
    for line in lines:
        if ":" in line:
            temp = line.split(":")
            start_values[temp[0]] = int(temp[1].strip())
        if "->" in line:
            temp = line.split()
            gate_name = temp[-1]
            op1 = temp[0]
            op2 = temp[2]
            #if ((temp[0][0] == "x" and temp[2][0] == "y") or (temp[0][0] == "y" and temp[2][0] == "x")) and temp[0][1:] == temp[2][1:]:
#                gate_name_repl[temp[-1]] = gate_name
#                gate_name = temp[1] + temp[0][1:]
            gates[gate_name] = ([temp[0], temp[2]], temp[1])

    z_wire_names = [x for x in gates.keys() if x[0] == "z"]
    wire_values = start_values.copy()

    def get_wire_value(wirename, wire_values, gates):
        (op1, op2), optype = gates[wirename]

        for operand in [op1, op2]:
            if operand not in wire_values.keys():
                get_wire_value(operand, wire_values, gates)
        if optype == "AND":
            wire_values[wirename] = wire_values[op1] & wire_values[op2]
        elif optype == "OR":
            wire_values[wirename] = wire_values[op1] | wire_values[op2]
        elif optype == "XOR":
            wire_values[wirename] = wire_values[op1] ^ wire_values[op2]
        else:
            raise Exception()
        return wire_values[wirename]

    if part == 1:
        for wirename in sorted(z_wire_names):
            get_wire_value(wirename, wire_values, gates)

        final_list = [str(wire_values[x]) for x in reversed(sorted(z_wire_names))]
        return int("".join(final_list), 2)

    def find_gate(op1, op2, opname):
        findings = []
        for wn, gate in gates.items():
            if op2 is None:
                if ((gate[0][0] == op1) or (gate[0][1] == op1)) and gate[1] == opname:
                    findings.append(wn)
            else:
                if ((gate[0][0] == op1 and gate[0][1] == op2) or (
                        gate[0][0] == op2 and gate[0][1] == op1)) and gate[1] == opname:
                    findings.append(wn)
        if len(findings) == 1:
            return findings[0]
        else:
            print(findings)
            raise Exception("too many or zero findings")

    def check_gate(gate, op1, op2, opname):
        return ((gate[0][0] == op1 and gate[0][1] == op2) or (
                gate[0][0] == op2 and gate[0][1] == op1)) and gate[1] == opname

    def find_switch(gates0, switches):
        gates = gates0.copy()

        for switch in switches:
            ng0 = gates[switch[1]]
            ng1 = gates[switch[0]]
            del gates[switch[0]]
            del gates[switch[1]]
            gates[switch[0]] = ng0
            gates[switch[1]] = ng1

        op1_old = ""
        op2_old = ""
        for ix, wirename in enumerate(sorted(z_wire_names)):
            if ix < 1:
                continue



            wireno = int(wirename[1:])
            wirenobef = wireno - 1
            (op1t, op2t), opname = gates[wirename]

            if ix == len(z_wire_names)-1:
                if opname != "OR":
                    raise Exception()
                if not (check_gate(gates[op1t], f"x{wirenobef:02}", f"y{wirenobef:02}", "AND") or check_gate(gates[op2t], f"x{wirenobef:02}", f"y{wirenobef:02}", "AND")):
                    raise Exception()
                if not (check_gate(gates[op1t], op1_old, op2_old, "AND") or check_gate(gates[op2t], op1_old, op2_old, "AND")):
                    raise Exception()
                return None

            if opname != "XOR":
                print(f"{wirename}: gate of {wirename} is completely wrong!")
                #print(wirename)
                print(gates[wirename])
                # gate of z is wrong
                # look for correct gate
                temp1 = find_gate(f"x{wireno:02}", f"y{wireno:02}", "XOR")
                temp2 = find_gate(temp1, None, "XOR")
                print(f"switch {wirename} with {temp2}")
                return (wirename, temp2)

            gate1t = gates[op1t]
            gate2t = gates[op2t]
            if gate1t[1] == "XOR" or gate2t[1] == "OR":
                gate1 = gate1t
                gate2 = gate2t
                op1 = op1t
                op2 = op2t
            else:
                gate2 = gate1t
                gate1 = gate2t
                op2 = op1t
                op1 = op2t
            #print(gate1)
            #print(gate2)

            error1 = False
            error2 = False

            # check gate 1
            if not check_gate(gate1, f"x{wireno:02}", f"y{wireno:02}", "XOR"):
                error1 = True

            if ix >= 2:
                # check gate 2
                wirenobef = wireno - 1
                if gate2[1] != "OR":
                    error2 = True

            if error1 and error2:
                print(f"{wirename}: Gates 1 and 2 are wrong!")
                #print(wirename)
                #print(gates[wirename])
                try:
                    temp1 = find_gate(f"x{wireno:02}", f"y{wireno:02}", "XOR")
                    temp2 = find_gate(temp1, None, "XOR")
                    print(f"switch {wirename} with {temp2}")
                    return (wirename, temp2)
                except:
                    try:
                        temp1 = find_gate(f"x{wireno:02}", f"y{wireno:02}", "XOR")
                        print(f"switch {op1} with {temp1}")
                        return (op1, temp1)
                    except:
                        temp1 = find_gate(f"x{wirenobef:02}", f"y{wirenobef:02}", "AND")
                        temp2 = find_gate(temp1, None, "OR")
                        # print(temp1)
                        print(f"switch {op2} with {temp2}")
                        return (op2, temp2)
            elif error1:
                print(f"{wirename}: Gate 1 is wrong!")
                #print(wirename)
                #print(gates[wirename])
                temp1 = find_gate(f"x{wireno:02}", f"y{wireno:02}", "XOR")
                print(f"switch {op1} with {temp1}")
                return (op1, temp1)
            elif error2:
                print(f"{wirename}: Gate 2 is wrong!")
                #print(wirename)
                #print(gates[wirename])
                temp1 = find_gate(f"x{wirenobef:02}", f"y{wirenobef:02}", "AND")
                temp2 = find_gate(temp1, None, "OR")
                #print(temp1)
                print(f"switch {op2} with {temp2}")
                return (op2, temp2)

            if ix >= 2:
                gate2at = gates[gate2[0][0]]
                gate2bt = gates[gate2[0][1]]
                if gate2at[0][0][0] in ["x", "y"]:
                    gate2a = gate2at
                    gate2b = gate2bt
                else:
                    gate2b = gate2at
                    gate2a = gate2bt

                # check gate 2a

                if not ((gate2a[0][0] == f"x{wirenobef:02}" and gate2a[0][1] == f"y{wirenobef:02}") or (gate2a[0][0] == f"y{wirenobef:02}" and gate2a[0][1] == f"x{wirenobef:02}")):
                    raise Exception()

                # check gate 2b
                if gate2b[1] != "AND":
                    raise Exception()
                if not ((gate2b[0][0] == op1_old and gate2b[0][1] == op2_old) or (gate2b[0][1] == op1_old and gate2b[0][0] == op2_old)):
                    raise Exception()

            op1_old = op1
            op2_old = op2
            #print(op1_old)
            #print(op2_old)

    if part == 2:


        switches = []

        while True:
            new_switches = find_switch(gates, switches)
            if new_switches is not None:
                switches = [*switches, new_switches]
            else:
                break
        return ",".join(sorted([y for x in switches for y in x]))
        #switches = []



    return None



if __name__ == '__main__':
    run(cb=puzzle, example_file="example", solution_file="solution1")
    run(cb=puzzle, example_file="example", solution_file="solution2", part=2)