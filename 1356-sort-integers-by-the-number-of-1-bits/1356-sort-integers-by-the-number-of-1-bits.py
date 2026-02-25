class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_count(x: int) -> int:
            return bin(x).count("1")

        arr.sort(key=lambda x: (bit_count(x), x))
        return arr
        