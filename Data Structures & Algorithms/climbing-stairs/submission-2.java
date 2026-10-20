class Solution {

    public int getSteps(int n)
    {
        if(n==0)
        {
            return 0;
        }
        if(n==1)
        {
            return 1;
        }
        if(n==2)
        {
            return 2;
        }
        return (getSteps(n-1)+getSteps(n-2));
    }
    public int climbStairs(int n) {
        int[] steps = new int[n+1];
        steps[0]=0;
        steps[1] =1;
        if(n<2){
            return steps[1];
        }
        steps[2] = 2;
        for(int i=3;i<=n;i++)
        {
            steps[i] = steps[i-1]+steps[i-2];
        }
        return steps[n];
    }
}
