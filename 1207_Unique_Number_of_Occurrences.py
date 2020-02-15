class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurance_dict = dict()
        for item in arr:
            if item in occurance_dict.keys():
                occurance_dict[item] = occurance_dict[item] +1
            else:
                occurance_dict[item] = 1
        if len(occurance_dict.values()) == len(set(occurance_dict.values())): return True
        else: return False
        