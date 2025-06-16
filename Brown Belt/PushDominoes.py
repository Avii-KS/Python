def pushDominoes(dominoes):
    n = len(dominoes)
    forces = [0] * n

    # Left-to-right pass
    force = 0
    for i in range(n):
        if dominoes[i] == 'R':
            force = n
        elif dominoes[i] == 'L':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] += force

    # Right-to-left pass
    force = 0
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            force = n
        elif dominoes[i] == 'R':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] -= force

    # Determining final state
    result = ""
    for f in forces:
        result += "R" if f > 0 else "L" if f < 0 else "."

    return result

# Taking input from the user
n = int(input())
dominoes = input().strip()

print(pushDominoes(dominoes))