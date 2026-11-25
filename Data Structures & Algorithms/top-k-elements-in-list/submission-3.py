class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # count number of times nums is in thde list and call it count
        result = [] #initialize an empty list

        #most_common gets  key and value pair. Then assign num to the key(#) and count to the     value(frequency).
        for num, count in count.most_common(k): 
            result.append(num) #Grab  key and append to  results list
        return result


