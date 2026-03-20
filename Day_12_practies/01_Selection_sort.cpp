#include<iostream>

using namespace std;
void SelectionSort(int *arr ,int n){
    for(int i = 0 ; i < n ; i++){
        int minIdx = i;
        for(int j = i + 1 ; j < n ; j++){
            if(arr[j] < arr[minIdx] ){
                minIdx = j;
            }
        }
        swap(arr[minIdx] , arr[i]);
    }
}
void printarray(int *arr , int n){
    for(int i = 0 ; i < n ; i++){
        cout << arr[i] << " ";
    }
}
int main(){
    int arr[] = {5 , 1 , 3 , 4 , 2};
    int n = sizeof(arr) / sizeof(int);
    SelectionSort(arr , n);
    printarray(arr , n);
    return 0;
}