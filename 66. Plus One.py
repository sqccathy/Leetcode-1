class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            else:
                digits[i] = 0
        digits.insert(0,1)
        return digits
        