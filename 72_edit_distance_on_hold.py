import string
import math

# pull previous sumbol after matching current one; do this pull in case of *
# after initial preprocessing, PULL EVERYTHING to the right; by amount corresponding to * of middle elements
# PRIOR , AFTER fuzzy substring should be taken into consideration

class Solution:
    def NminDistance(self, word1: str, word2: str) -> int:
        letter_dict = {}
        for l in string.ascii_lowercase:
            letter_dict[l] = []

        for i in range(len(word1)):
            letter_dict[word1[i]].append(i)

        print("\n word1:", word1, "word2:", word2)
        for l in word2:
            print(l, ":", letter_dict[l])
        
        for l in word2:
            res = ""
            prev_dist = 0
            for i in range(len(letter_dict[l])):
                dist = letter_dict[l][i]
                res += (dist - prev_dist) * " " + "*"
                prev_dist = dist + 1
            print(l, ":", res)
        
    def bin_search(self, arr, start, end, left_bound):
        mid_f = math.floor((end - start) / 2)
        if left_bound == arr[mid_f]:
            return mid_f

        # arr[mid_f - 1] < left_bound < arr[mid_f]
        if left_bound < arr[mid_f]:
            if mid_f == 0 or left_bound > arr[mid_f - 1]:
                return mid_f
            else:
                return self.bin_search(arr, start, mid_f, left_bound)
        else:
            mid_c = math.ceil((end - start) / 2)
            if left_bound == arr[mid_c]:
                return mid_c

            # arr[mid_c] < left_bound < arr[mid_c + 1]
            if mid_c == len(arr) - 1 or left_bound < arr[mid_c + 1]:
                return mid_c + 1
            else:
                return self.bind_search(arr, mid_c, end, left_bound)            
    
    def find_first_occurance(self, occ_arr, left_bound):
        if len(occ_arr) == 0 or left_bound > occ_arr[-1]:
            return -1

        i = 0
        while occ_arr[i] < left_bound:
            i += 1
        return occ_arr[i]
    
    def minDistance(self, word1: str, word2: str) -> int:
        letter_dict = {}
        for l in string.ascii_lowercase:
            letter_dict[l] = []

        for i in range(len(word1)):
            letter_dict[word1[i]].append(i)

        res = []
        for start_idx in range(len(word2)):
            pos_arr = []
            last_letter_idx = self.find_first_occurance(letter_dict[word2[start_idx]], 0)
            if last_letter_idx != -1:
                left_bound_idx = last_letter_idx + 1
            else:
                left_bound_idx = 0


            pos_arr.append({word2[start_idx]: last_letter_idx})
            
            for i in range(start_idx + 1, len(word2)):
                last_letter_idx = self.find_first_occurance(letter_dict[word2[i]], left_bound_idx)
                if last_letter_idx != -1:
                    left_bound_idx = last_letter_idx + 1 # asdf asrrdf    rss ros
                pos_arr.append({word2[i]: last_letter_idx})
            res.append({word2[start_idx]: pos_arr})
        
        print("\nw1:", word1, "w2:", word2, res)

s = Solution()
s.minDistance("horse", "ros")
s.minDistance("intention", "execution")

# s.minDistance("asdfrorztrtotrdd", "frtrd")
# s.minDistance("dddfdkror", "ror")
# s.minDistance("asdfrorztrtotrdd", "zror")
# s.minDistance("troddrokzll", "zrok")
# s.minDistance("alaftaaabaaarqsadaaarta", "lbfdtrqs")
# s.minDistance("alaftaaabaaarqsadaaartaalaftaaabaaarqsadaaartaalafta", "lbfdtrqslbfdtrqslbfdtrqs")
# s.minDistance("abcdefghi", "ihgfedcba")
