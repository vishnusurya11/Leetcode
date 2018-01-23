class Solution {
public:
    bool isHappy(int n) {
        int sum(0),temp(0);
        while(n > 6){
            
            while(n>0){
                temp= n%10;
                sum=sum+ (temp*temp);
                n=n/10;
            }
            n=sum;
            sum=0;
        }
        
        if(n == 1) return true;
        else return false;
    }
};
