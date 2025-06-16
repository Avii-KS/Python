class Solution:
    def dividePlayers(self, skill) -> int:
        skill.sort()  # Sort the players by skill
        total_chemistry = 0
        n = len(skill)

        target_sum = skill[0] + skill[-1]  # All pairs must sum to this

        left, right = 0, n - 1
        while left < right:
            # Current pair sum should match target
            if skill[left] + skill[right] != target_sum:
                return -1  # Impossible to form equal-skill teams

            # Add chemistry for this team
            total_chemistry += skill[left] * skill[right]

            left += 1
            right -= 1

        return total_chemistry  # Total chemistry of all valid teams
