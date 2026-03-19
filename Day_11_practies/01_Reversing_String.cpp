#include<iostream>
#include<string>

using namespace std;
string reversing(string s){
    int si = 0 , ei = s.size() - 1;
    while(si <= ei){
        swap(s[si++] , s[ei--]);
    }
    cout << s<< "\n";
}
int main(){
    string s = "Hello";
    reversing(s);
    return 0;
}