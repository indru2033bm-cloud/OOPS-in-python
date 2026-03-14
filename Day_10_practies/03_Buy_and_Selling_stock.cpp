#include<iostream>
#include<vector>
using namespace std;
int Profit(vector<int> vec ){
    vector<int> bestbuy(vec.size());
    // vector<int> porfit;
    bestbuy[0] = INT16_MAX;
    // porfit[0] = INT16_MIN;
    int profit = 0;
    for(int i = 1 ; i < vec.size() ; i++){
        bestbuy[i] = min(bestbuy[i - 1] , vec[i - 1]);
    }
    for(int i = 0 ; i < vec.size(); i++){
        int currprofit = vec[i] - bestbuy[i];
        profit = max(profit , currprofit);
    }
    return profit;
}
int main(){
vector<int> vec = {7 ,1 ,5 ,3 ,6 ,4};
cout << Profit(vec) << "\n";
return 0;
}