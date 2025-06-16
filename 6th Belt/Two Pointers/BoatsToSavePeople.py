class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()  # Step 1: Sort people by weight (ascending)

        left, right = 0, len(people) - 1  # Two pointers: lightest and heaviest
        boats = 0  # Count of boats needed

        while left <= right:
            # If the lightest + heaviest can share a boat
            if people[left] + people[right] <= limit:
                left += 1  # Move left (lightest person used)

            # Heaviest person always boards the boat (alone or paired)
            right -= 1
            boats += 1  # One boat used

        return boats
