class Solution:
    def getFolderNames(self, names):
        names_dict = {}
        res = []
        for name in names:
            if name not in names_dict:
                names_dict[name] = 0
                res.append(name)
            else:
                names_dict[name] += 1
                while True:
                    tmp_name = name + "(" + str(names_dict[name]) + ")"
                    if tmp_name in names_dict:
                        names_dict[name] += 1
                    else:
                        names_dict[tmp_name] = 0
                        res.append(tmp_name)
                        break
        
        return res