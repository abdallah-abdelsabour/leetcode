class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for st in strs :
            result+=str(len(st))+'#' + st
        return result

        
        

    def decode(self, s: str) -> List[str]:
        i = 0 
        result = []
        while i < len(s):
            j = s.find('#',i)
            length =int(s[i:j])
            result.append(s[j+ 1 : j+1 + length])
            i = j + length + 1
        return result 