class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        maxFruits = 0
        fruitType = {}

        for right in range(len(fruits)):
            fruitType[fruits[right]] = fruitType.get(fruits[right], 0) + 1

            while len(fruitType) > 2:
                fruitType[fruits[left]] -= 1
                if fruitType[fruits[left]] == 0:
                    fruitType.pop(fruits[left]) 
                left += 1

            maxFruits = max(maxFruits, right - left + 1)

        return maxFruits
