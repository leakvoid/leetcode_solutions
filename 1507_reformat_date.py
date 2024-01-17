class Solution:
    def reformatDate(self, date: str) -> str:
        months_map = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
        'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

        date_list = date.split(" ")

        year = date_list[2]
        month = months_map[date_list[1]]
        day = date_list[0][:-2]
        if len(day) == 1:
            day = "0" + day

        return year + "-" + month + "-" + day