class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(reverse=True)
        
        max_attack = properties[0][0]
        prev_max_defense = properties[0][1]
        
        i = 1
        while i < len(properties):
            if properties[i][0] != max_attack:
                break
            if properties[i][1] > prev_max_defense:
                prev_max_defense = properties[i][1]
            i += 1
        if i == len(properties):
            return 0
        
        weak_count = 0
        max_defense = prev_max_defense
        cur_attack = properties[i][0]
        for j in range(i, len(properties)):
            if properties[j][0] != cur_attack:
                cur_attack = properties[j][0]
                prev_max_defense = max_defense
            
            if properties[j][1] < prev_max_defense:
                weak_count += 1
            elif properties[j][1] > max_defense:
                max_defense = properties[j][1]
        
        return weak_count
