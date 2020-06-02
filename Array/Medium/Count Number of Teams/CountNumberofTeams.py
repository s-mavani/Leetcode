# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

# Example 1:

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
# 
# Constraints:

# n == rating.length
# 1 <= n <= 200
# 1 <= rating[i] <= 10^5 

from collections import defaultdict
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        greater = defaultdict(int)
        lesser = defaultdict(int)
        result = 0
        for i in range(len(rating)-1):
            for j in range(i+1,len(rating)):
                if rating[i] < rating[j]:
                    greater[i] +=1
                else:
                    lesser[i] +=1
        for i in range(len(rating)-2):
            for j in range(i+1,len(rating)-1):
                if rating[i]<rating[j]:
                    result += greater[j]
                else:
                    result += lesser[j]
        return result