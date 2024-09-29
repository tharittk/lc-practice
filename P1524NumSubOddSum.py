class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        prefix_sum = []
        odd_count_upto = []
        even_count_upto = []
        acc = arr[0]
        prefix_sum.append(arr[0])
        if arr[0] % 2 == 1:
            odd_count_upto.append(1)
            even_count_upto.append(1) # not taking any
        else:
            odd_count_upto.append(0)
            even_count_upto.append(2) # not taking any of first element

        for i in range(1,n):
            acc += arr[i]
            if acc % 2 == 0:
                even_count_upto.append(even_count_upto[i-1] + 1)
                odd_count_upto.append(odd_count_upto[i-1])

            else:
                odd_count_upto.append(odd_count_upto[i-1] + 1)
                even_count_upto.append(even_count_upto[i-1])
            
            prefix_sum.append(acc)

        count = 0
        for i in range(n):
            if prefix_sum[i] % 2 == 1:
                count += even_count_upto[i]
            else:
                count += odd_count_upto[i]
        return count %(1000000000 + 7)
