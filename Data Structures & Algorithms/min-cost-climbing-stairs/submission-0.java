class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] d= new int[cost.length+1];
        d[0] = cost[0];
        d[1] = cost[1];
        for(int i=2;i<cost.length;i++)
        {
            d[i] = cost[i]+Math.min(d[i-1],d[i-2]);
        }
        return Math.min(d[cost.length-1],d[cost.length-2]);
    }
}
