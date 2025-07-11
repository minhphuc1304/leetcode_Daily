class Solution {
    public:
        bool prm[1000001] = {true};
        vector<int> closestPrimes(int left, int right) {
            if(left<=2 && right>=3) return {2,3};
            int k = int(sqrt(right)+1);
            memset(prm, true, sizeof prm);
            prm[1] = false;
            for(int i=2; i<=k; i++){
                if(prm[i]){
                    for(int j=i*i; j<=right; j+=i) prm[j]=false;
                }
            }
            int n1=-1, n2=-1;
            int mn = 1e9;
            int a=-1, b=-1;
            for(int i=left; i<= right; i++){
                if(prm[i]){
                    if(a==-1) a = i;
                    else if(b==-1) {
                        b = i;
                        if(b-a < mn){
                            mn = b-a;
                            n1 = a;
                            n2 = b;
                        }
                    }
                    else{
                        a = b;
                        b = i;
                        if(b-a < mn){
                            mn = b-a;
                            n1 = a;
                            n2 = b;
                        }
                    }
                }
            }
            return {n1, n2};
        }
    };