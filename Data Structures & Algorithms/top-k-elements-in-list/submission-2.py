class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # count number of times nums is in list and call it count
        result = [] #initialize an empty list

        #most_common gets the key and value pair. THen assign num to key(#) and count to       value(frequency).
        for num, count in count.most_common(k): 
            result.append(num) #Grab the key and append to our results list
        return result


