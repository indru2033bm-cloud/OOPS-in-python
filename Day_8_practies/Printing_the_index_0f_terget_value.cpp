#include<iostream>

using namespace std;
int printing_index(int *arr , int terget ,int n){
    int i , j ;
    for(int i = 0 ; i < n ; i++){
        for(int j = i + 1 ; j < n ; j++ ){
            if(arr[i] + arr[j] == terget){
                return  i , j;
            }
        }
    }
}

int main(){
    int arr[] = { 1 , 2 , 3 , 4 };
    int n = sizeof(arr) / sizeof(int) ;
    int terget = 6;
    // cout << printing_index(arr , terget , n ) << endl;
        int i , j ;
    for(i = 0 ; i < n ; i++){
        for(j = i + 1 ; j < n ; j++ ){
            if(arr[i] + arr[j] == terget){
                cout <<"[" << i << " , " << j << "]" << endl;
            }
        }
    }

}