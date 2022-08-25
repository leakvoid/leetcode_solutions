class Solution:
    def shifted_parse_string(self, s, word_dict, word_len, start):
        res = []
        for i in range(start, len(s), word_len):
            word = s[i:i+word_len]
            if word in word_dict:
                res.append(word)
            else:
                res.append('')
        return res
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        
        word_dict = {}
        
        for w in words:
            if w in word_dict:
                word_dict[w][0] += 1
            else:
                word_dict[w] = [1, 0]
        
        target_dict_count = len(word_dict)
        target_word_count = len(words)
        
        word_len = len(words[0])
        for shift in range(word_len):
            parsed_string = self.shifted_parse_string(s, word_dict, word_len, shift)

            segment_start = 0
            segment_end = target_word_count - 1
            while segment_end < len(parsed_string):
                reset_segment = False
                dict_count = 0
                
                for i in range(segment_start, segment_end + 1):
                    word = parsed_string[i]
                    
                    if word == '':
                        for j in range(segment_start, i):
                            word_dict[parsed_string[j]][1] = 0
                        segment_start = i + 1
                        segment_end = segment_start + target_word_count - 1
                        reset_segment = True
                        break
                    
                    if word_dict[word][0] == word_dict[word][1]:
                        dict_count -= 1
                    word_dict[word][1] += 1
                    if word_dict[word][0] == word_dict[word][1]:
                        dict_count += 1
                
                if reset_segment:
                    continue
                if dict_count == target_dict_count:
                    res.append(shift + segment_start * word_len)

                segment_start += 1
                segment_end += 1
                while segment_end < len(parsed_string):
                    word = parsed_string[segment_end]
                    if word == '':
                        for key in word_dict:
                            word_dict[key][1] = 0
                        segment_start = segment_end + 1
                        segment_end = segment_start + target_word_count - 1
                        break
                    
                    if word_dict[word][0] == word_dict[word][1]:
                        dict_count -= 1
                    word_dict[word][1] += 1
                    if word_dict[word][0] == word_dict[word][1]:
                        dict_count += 1
                    
                    old_word = parsed_string[segment_start - 1]
                    if word_dict[old_word][0] == word_dict[old_word][1]:
                        dict_count -= 1
                    word_dict[old_word][1] -= 1
                    if word_dict[old_word][0] == word_dict[old_word][1]:
                        dict_count += 1
                    
                    if dict_count == target_dict_count:
                        res.append(shift + segment_start * word_len)

                    segment_start += 1
                    segment_end += 1
                for key in word_dict:
                    word_dict[key][1] = 0
        
        return res
