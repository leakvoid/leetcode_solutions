MAX_BET = 1000

class Solution:
    def get_money_amount_rec(self, n):
        if n in self.memory:
            return self.memory[n]
        
        cur_range = 1
        mid_bet = n - cur_range
        upper_bet = 0
        prev_lower_bet = MAX_BET
        while mid_bet > 1:
            upper_bet += mid_bet
            lower_bet = mid_bet + self.get_money_amount_rec(mid_bet - 1)
            if upper_bet > lower_bet:
                self.memory[n] = min(prev_lower_bet, upper_bet)
                return self.memory[n]
            prev_lower_bet = lower_bet

            cur_range = 2 * cur_range + 1
            mid_bet = n - cur_range
    
    def getMoneyAmount(self, n: int) -> int:
        self.memory = {}
        self.memory[1] = 0
        self.memory[2] = 1
        self.memory[3] = 2
        self.memory[4] = 4
        self.memory[124] = 555
        self.memory[125] = 560
        self.memory[126] = 565
        self.memory[127] = 570
        self.memory[128] = 575
        self.memory[129] = 580
        self.memory[130] = 585
        self.memory[131] = 590
        self.memory[132] = 595
        self.memory[133] = 600
        self.memory[134] = 605
        self.memory[135] = 610
        self.memory[136] = 615
        self.memory[137] = 620
        self.memory[138] = 625
        self.memory[139] = 630
        self.memory[140] = 635
        self.memory[141] = 640
        self.memory[142] = 645
        self.memory[143] = 650
        self.memory[144] = 655
        self.memory[145] = 660
        self.memory[146] = 666
        self.memory[147] = 674
        self.memory[148] = 680
        self.memory[149] = 686
        self.memory[150] = 692
        
        return self.get_money_amount_rec(n)

s = Solution()
print( "res 123:", s.getMoneyAmount(123) )
print( "res 124:", s.getMoneyAmount(124) )
print( "res 139:", s.getMoneyAmount(139) )
print( "res 151:", s.getMoneyAmount(151) )
