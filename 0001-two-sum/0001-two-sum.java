class Solution {
    public int[] twoSum(int[] a, int t) {
        int b[]=new int[2];
        int i=0;
        while(i<a.length)
        {
            int j=i+1;
            while( j<a.length)
            {  
            if(a[i]+a[j]==t){
                b[0]=i;
                b[1]=j;
                break;
            }
            j++;
        }
        i++;

    }
    return b;
    }
}