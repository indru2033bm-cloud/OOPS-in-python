#include<iostream>

using namespace std;

string sum(string a , string b){
        
        int n1 = stoi(a);
        int n2 = stoi(b);
        int dec1 = 0 , decdig= 0 , pow = 1 , sum  , n ,bin ;
        while( n1 != 0){
            int la = n1 % 10 ;
            dec1 += (la * pow );
            n1 /= 10 ;
            pow *= 2 ;
        }

        while( n2 != 0){
            int la = n2 % 10 ;
            decdig += (la * pow) ;
            n2 /= 10 ;
            // pow *= 2 ;
 
        }

        // cout << dec2 <<endl;
        // sum = dec1 + dec2 ;
        string x = to_string(decdig);
        return x ;
        // string s = to_string(sum) ;
        // return s ;

         
        
    }
int main(){
    cout << sum("11","11") <<endl;
}