from dataclasses import dataclass
from typing import List, Tuple

file = open("./data/day17.txt", "r")
input = file.read()
rs, ps = input.split("\n\n")
rs = rs.split("\n") 

registers = [0, 0, 0]
for j in range(0, len(rs)):
    registers[j] = int(rs[j].split(": ")[1])

instructions = [int(x) for x in ps.split(": ")[1].split(",")]

@dataclass
class VM:
    instructions: List[int]
    instruction_pointer: int
    registers: List[int] 

def eval_operand(vm: VM, x: int):
    if x >= 4 and x < 7: return vm.registers[x - 4]
    return x

ops = []
result = []

def eval_opcode(vm: VM, op: int, x: int):
    return ops[op](vm, x)

def adv(vm: VM, x: int): vm.registers[0] >>= x
def bdv(vm: VM, x: int): vm.registers[1] = vm.registers[0] >> x
def cdv(vm: VM, x: int): vm.registers[2] = vm.registers[0] >> x
def bst(vm: VM, x: int): vm.registers[1] = x % 8
def bxl(vm: VM, x: int): vm.registers[1] ^= x
def bxc(vm: VM, x: int): vm.registers[1] ^= vm.registers[2]
def out(vm: VM, x: int): result.append(x % 8)

def jnz(vm: VM, x: int):
    if vm.registers[0] == 0: return
    vm.instruction_pointer = x
    eval(vm)

def noop(vm: VM, x: int): return
    
ops = {
    0: adv,
    1: bxl,
    2: bst, 
    3: noop,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

op_names = [x.__name__ for x in ops.values()]

def eval(vm: VM):
    opcode = vm.instructions[vm.instruction_pointer]
    operand = vm.instructions[vm.instruction_pointer + 1]
    if opcode != 1: operand = eval_operand(vm, operand) # bxl uses LITERAL operand
    # print(op_names[opcode], opcode, operand, operand, vm.registers, vm.instruction_pointer)
    vm.instruction_pointer += 2
    eval_opcode(vm, opcode, operand)

def eval_all(vm: VM):
    while vm.instruction_pointer < len(vm.instructions): 
        eval(vm)

vm = VM(instructions, 0, [0, 0, 0])

def last(x): 
    if (len(x) == 0): return None
    return x[len(x) - 1]

def replace_values(target, source):
    for i in range(0, len(source)): target[i] = source[i]

prev_registers = [0, 0, 0]

for i in range(0, len(instructions)):    
    last_instruction = instructions[len(instructions) - i - 1]
    vm.instruction_pointer = 0
    prev_registers[0] <<= 3
    replace_values(vm.registers, prev_registers)

    for j in range(0, 8):        
        eval_all(vm)
        last_result = last(result)

        # print(i, j, prev_registers, last_result, last_instruction)

        if last_result == last_instruction: break

        result.pop()
        vm.instruction_pointer = 0
        prev_registers[0] += 1
        replace_values(vm.registers, prev_registers)

print(prev_registers[0], result)    

result.clear()
vm = VM(instructions, 0, [prev_registers[0], 0, 0])    
ops[3] = jnz

eval_all(vm)
print(result)







# print(result)

