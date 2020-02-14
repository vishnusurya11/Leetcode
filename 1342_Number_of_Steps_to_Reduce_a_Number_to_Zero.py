class Solution:
    def numberOfSteps (self, num: int) -> int:
        step_counter = 0
        if num == 0 : return 0
        while num //2 :
            if num%2 == 0 :
                num = num /2
                step_counter = step_counter +1
            else:
                num = num - 1
                step_counter = step_counter +1

        return step_counter + 1 
        