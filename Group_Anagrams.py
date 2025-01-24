# brutefore way


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =[]
        unique_anagrams=[]
        for index in range(len(strs)):
            if sorted(strs[index]) in unique_anagrams:
                continue
            temp_list =[]
            temp_list.append(strs[index])
            for i in range( (index + 1),len(strs)):
                if sorted(list(strs[index])) == sorted(list(strs[i])):
                    temp_list.append(strs[i])
            result.append(temp_list)
            unique_anagrams.append(sorted(list(strs[index])))
        return result
    

# _____________________________
# best performance 
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dic = defaultdict(list)
        for st in strs :
            sorted_s = ''.join(sorted(st))
            anagrams_dic[sorted_s].append(st)
        
        return [val for val in anagrams_dic.values() ]
    
    