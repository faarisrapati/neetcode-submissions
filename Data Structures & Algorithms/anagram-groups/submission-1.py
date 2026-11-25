class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #initialize a dictionary

        for s in strs:
            count = [0] * 26 #set a fixed sized array of 26 for each letter in alphabet
            for c in s: 
                count[ord(c)- ord("a")] +=1 # increment count by 1 for each occurance at index
            result[tuple(count)].append(s)
        return list(result.values())