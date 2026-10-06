class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        first = {p[0]: p for p in pieces}
        i = 0
        while i < len(arr):
            piece = first.get(arr[i])
            if piece is None or arr[i:i + len(piece)] != piece:
                return False
            i += len(piece)
        return True


s = Solution()
print(s.canFormArray([15, 88], [[88], [15]]))                  # True
print(s.canFormArray([49, 18, 16], [[16, 18, 49]]))            # False
print(s.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))  # True
print(s.canFormArray([1, 3, 5, 7], [[2, 4, 6, 8]]))            # False
print(s.canFormArray([1, 2, 3], [[1, 3], [2]]))                # False