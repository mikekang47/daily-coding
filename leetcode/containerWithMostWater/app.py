from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0;
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_area = self.get_area(left, height[left], right, height[right])
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def get_area(self, left_index, left_height, right_index, right_height):
        return (right_index - left_index) * min(left_height, right_height)