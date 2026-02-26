#include<iostream>

using namespace std;

int numstep(string s){
    int n = stoi(s);
    int dec = 0, pow = 1;
    while( n != 0){
        int la = n % 10;
        dec = dec + la * pow;
        pow *= 2;
        n /= 10;
    }
    int i = 0;
    // cout << dec <<endl;
    while(dec !=1){
        if(dec % 2 == 0){
            dec /= 2;
            i++;
        }
        else{
            dec += 1;
            i++;
        }
    }
    return i;
}

int main(){
    string s = "10";
    cout << numstep(s) << endl;

}