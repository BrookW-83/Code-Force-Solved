class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        power = x. token = [y]
        if len(token) =1:  #token=[100] power = 150
            power == token[i]
            return 1
        else: 
            if power < token[i]
            return 0
        #[200,300,400]
        power = 300  sore* = 0
        power* = 700
        """
        
        if len(tokens) == 1 and power >= tokens[0]:
            return 1
        elif len(tokens) == 1 and power < tokens[0]:
            return 0
        
        score = 0
        i = 0
        
        while tokens:
            if tokens[i] <= power:
                power -= tokens[i]
                score +=1
                i += 1;
                
                if len(tokens) > 2:
                    power += tokens[-1]
                    score -= 1
                    i += 1
                    while power > tokens[i]:
                        power -= tokens[i]
                        score += 1
                        i += 1
        return score