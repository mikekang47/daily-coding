#include <iostream>
using namespace std;
int arr[] = {1,5,3,8,4,5,21,6};

// 퀵 정렬
void quickSort(int start, int end) {
   if(start >= end)
       return;
   int i = start+1, j = end, key = start;
   while(i <= j) {
       while(i <= end && arr[i] <= arr[key]) i++;
       while(j >= start && arr[j] >= arr[key]) j--;
       if(i > j) swap(arr[j], arr[key]);
       else swap(arr[i], arr[j]);
   }
   quickSort(start, j-1);
   quickSort(j+1, end);
}



int main() {

    // 선택 정렬
//    for(int i = 0; i < 8; i++) {
//        int min = 9999;
//        int index = 0;
//        for(int j = i; j < 8; j++) {
//            if(min > arr[j]) {
//                min = arr[j];
//                index = j;
//            }
//        }
//        swap(arr[index], arr[i]);
//    }

// 삽입 정렬

//    for(int i = 0; i < 7; i++) {
//        int j = i;
//        while(j >= 0 && arr[j] > arr[j+1]) {
//            swap(arr[j], arr[j+1]);
//            j--;
//        }
//    }


//    quickSort(0, 7);
//
//    for(int i : arr) {
//        cout << i << "\n";
//    }
//
//    return 0;




}

