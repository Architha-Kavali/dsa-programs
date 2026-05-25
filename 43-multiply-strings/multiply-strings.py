class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # Edge case
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        # Maximum length can be n + m
        result = [0] * (n + m)

        # Traverse from right to left
        for i in range(n - 1, -1, -1):

            for j in range(m - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                multiplication = digit1 * digit2

                # Positions
                p1 = i + j
                p2 = i + j + 1

                # Add current value already present
                total = multiplication + result[p2]

                # Store ones digit
                result[p2] = total % 10

                # Carry goes left
                result[p1] += total // 10

        # Convert array to string
        answer = ""

        for num in result:

            # Skip leading zero
            if not (len(answer) == 0 and num == 0):
                answer += str(num)

        return answer