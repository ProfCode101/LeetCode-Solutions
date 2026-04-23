#merge sorted array
#This is basically the merge part implemetation of the algoritm merge sort


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = []
        i = 0
        j = 0

        while(i<m and j<n):
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                temp.append(nums2[j])
                j+=1
        
        while(i<m):
            temp.append(nums1[i])
            i+=1
        while(j<n):
            temp.append(nums2[j])
            j+=1

        for i in range(len(temp)):
            nums1[i] = temp[i]

        
        return nums1

        
