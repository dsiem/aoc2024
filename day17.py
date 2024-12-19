from collections.abc import Iterator


def run(ra: int, rb: int = 0, rc: int = 0, pointer: int = 0) -> Iterator[int]:
    while pointer < len(program):
        opcode, operand = program[pointer], program[pointer + 1]
        combo = [0, 1, 2, 3, ra, rb, rc][operand]

        if opcode == 0:  #   adv
            ra = ra >> combo
        elif opcode == 1:  # bxl
            rb = rb ^ operand
        elif opcode == 2:  # bst
            rb = combo & 7
        elif opcode == 3:  # jnz
            pointer = operand - 2 if ra else pointer
        elif opcode == 4:  # bxc
            rb = rb ^ rc
        elif opcode == 5:  # out
            yield combo & 7
        elif opcode == 6:  # bdv
            rb = ra >> combo
        elif opcode == 7:  # cdv
            rc = ra >> combo
        pointer += 2


def quinify(pointer: int, ra: int = 0) -> int | None:
    if pointer < 0:
        return ra
    for new_ra in (ra << 3 | tribit for tribit in range(8)):
        if next(run(new_ra)) == program[pointer] and (result := quinify(pointer - 1, new_ra)):
            return result


ra, rb, rc, _, program = open(0)
ra, rb, rc = (int(reg[12:]) for reg in (ra, rb, rc))
program = tuple(map(int, program[9:].split(",")))
print(*run(ra, rb, rc), sep=",")
print(quinify(len(program) - 1))
