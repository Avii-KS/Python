class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n  # Step 1: Initialize a list to track forces at each index

        # -----------------------
        # LEFT TO RIGHT PASS 🡆 (Handling rightward pushes)
        # -----------------------
        force = 0  # This variable will represent how strong the 'R' push is
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # Set force to max when we see 'R'
            elif dominoes[i] == 'L':
                force = 0  # 'L' stops any rightward force
            else:
                force = max(force - 1, 0)  # Decrease force as it travels further

            forces[i] += force  # Add this rightward force to the index

        # -----------------------
        # RIGHT TO LEFT PASS 🡄 (Handling leftward pushes)
        # -----------------------
        force = 0  # Reset force for leftward direction
        for i in range(n - 1, -1, -1):  # Go from right to left
            if dominoes[i] == 'L':
                force = n  # Full force when we see 'L'
            elif dominoes[i] == 'R':
                force = 0  # 'R' stops any leftward force
            else:
                force = max(force - 1, 0)  # Decrease force as it travels further

            forces[i] -= force  # Subtract because it's a leftward force

        # -----------------------
        # FINAL PASS 🏁 (Build final state based on net forces)
        # -----------------------
        result = []  # To store the final characters

        for f in forces:
            if f > 0:
                result.append('R')  # More rightward force
            elif f < 0:
                result.append('L')  # More leftward force
            else:
                result.append('.')  # Balanced forces → domino stays upright

        return ''.join(result)  # Convert list of characters to string
