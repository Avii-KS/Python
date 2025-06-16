#any domino that starts out as left or right will always be a left or right, regardless of whether its leaning or fallen
#queue based solution
def pushDominoes(dominoes):
    n = 0
    while dominoes[n:]:  # Finding length of dominoes without len()
        n += 1

    forces = [0] * n  # Initialize force array with zeros

    # Apply forces from 'R'
    force = 0
    i = 0
    while i < n:
        if dominoes[i] == 'R':
            force = n  # Max force applied
        elif dominoes[i] == 'L':
            force = 0  # Reset force
        else:
            if force > 0:
                force -= 1  # Reduce force gradually
        forces[i] += force
        i += 1

    # Apply forces from 'L'
    force = 0
    i = n - 1
    while i >= 0:
        if dominoes[i] == 'L':
            force = n
        elif dominoes[i] == 'R':
            force = 0
        else:
            if force > 0:
                force -= 1
        forces[i] -= force
        i -= 1

    # Determine final state of dominoes
    result = []
    i = 0
    while i < n:
        if forces[i] > 0:
            result.append('R')
        elif forces[i] < 0:
            result.append('L')
        else:
            result.append('.')
        i += 1

    # Convert list to string without using join()
    final_state = ""
    i = 0
    while i < n:
        final_state += result[i]
        i += 1

    return final_state


# Example Usage
dominoes = "R.L"
print(pushDominoes(dominoes))  # Output: "R.L"

dominoes = ".L.R...LR..L.."
print(pushDominoes(dominoes))
