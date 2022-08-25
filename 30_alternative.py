class Solution:
    def shifted_parse_string(self, s, word_dict, min_segment_len, word_len, start):
        res = []
        
        r = []
        segment_start = start
        for i in range(start, len(s), word_len):
            word = s[i:i+word_len]
            if word in word_dict:
                r.append(word)
            else:
                if len(r) >= min_segment_len:
                    res.append( (segment_start, r) )
                
                r = []
                segment_start = i + word_len
        
        if len(r) >= min_segment_len:
            res.append( (segment_start, r) )
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
            parsed_string = self.shifted_parse_string(s, word_dict, target_word_count, word_len, shift)
            
            for parsed_segment in parsed_string:
                parsed_segment_start = parsed_segment[0]
                parsed_substring = parsed_segment[1]
                
                dict_count = 0
                segment_start = 0
                segment_end = target_word_count - 1
                for i in range(segment_start, segment_end + 1):
                    word = parsed_substring[i]
                    
                    if word_dict[word][0] == word_dict[word][1]:
                        dict_count -= 1
                    word_dict[word][1] += 1
                    if word_dict[word][0] == word_dict[word][1]:
                        dict_count += 1
                
                if dict_count == target_dict_count:
                    res.append(parsed_segment_start + segment_start * word_len)
                
                segment_start += 1
                segment_end += 1
                while segment_end < len(parsed_substring):
                    word = parsed_substring[segment_end]
                    if word_dict[word][0] == word_dict[word][1]:
                        dict_count -= 1
                    word_dict[word][1] += 1
                    if word_dict[word][0] == word_dict[word][1]:
                        dict_count += 1
                    
                    old_word = parsed_substring[segment_start - 1]
                    if word_dict[old_word][0] == word_dict[old_word][1]:
                        dict_count -= 1
                    word_dict[old_word][1] -= 1
                    if word_dict[old_word][0] == word_dict[old_word][1]:
                        dict_count += 1
                    
                    if dict_count == target_dict_count:
                        res.append(parsed_segment_start + segment_start * word_len)
                    segment_start += 1
                    segment_end += 1
                
                for key in word_dict:
                    word_dict[key][1] = 0
        
        return res
