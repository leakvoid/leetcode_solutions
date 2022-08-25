import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
                 "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        letter_to_code = {}
        for i in range( len(string.ascii_lowercase) ):
            letter_to_code[ string.ascii_lowercase[i] ] = codes[i]
        
        wtc_set = set()
        for word in words:
            code = ""
            for l in word:
                code += letter_to_code[l]
            
            if code not in wtc_set:
                wtc_set.add(code)
        
        return len(wtc_set)
