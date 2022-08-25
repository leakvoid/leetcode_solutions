import string
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        letter_to_bit = {}
        for i in range( len(string.ascii_lowercase) ):
            letter_to_bit[ string.ascii_lowercase[i] ] = pow(2, i)
        
        words_bitmap = {}
        for word in words:
            bitmap = 0
            for l in word:
                bitmap |= letter_to_bit[ l ]
            if bitmap in words_bitmap:
                if len(word) > words_bitmap[bitmap]:
                    words_bitmap[bitmap] = len(word)
            else:
                words_bitmap[bitmap] = len(word)
        
        max_mult = 0
        keys = list(words_bitmap.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if keys[i] & keys[j] == 0:
                    mult = words_bitmap[ keys[i] ] * words_bitmap[ keys[j] ]
                    if mult > max_mult:
                        max_mult = mult
        return max_mult
