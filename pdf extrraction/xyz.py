# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
# Example 1:

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
# Example 2:

# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
# Example 3:

# Input: rating = [1,2,3,4]
# Output: 4
#  Constraints:

# n == rating.length
# 3 <= n <= 1000
# 1 <= rating[i] <= 105
# All the integers in rating are unique.
# class Solution:
#     @staticmethod
#     def ascending(arr,left,right,middle):
#         count=0
#         while left<right:
#             if arr[left]<arr[right]:
#                 if arr[left]<arr[middle]:
#                     if arr[middle]<arr[right]:
#                         count+=1
#                     else:

#         return count
#     def numTeams(self, rating: list[int]) -> int:
#         left=0
#         right=0
#         for val in rating:
#             right+=1
#         right=right-1
#         count=0

# #          return count
# class Solution:
#     @staticmethod
#     def subarray_producer():

#         return 1
#     def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
#         nums.sort()
#         starter=1
#         my_set=set()

# x=[1,7,3,9,2]
# x.sort()
# print(x)

