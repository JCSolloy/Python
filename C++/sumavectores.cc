//suma de arrays
#include <iostream>
using namespace std;

int main(){
    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[5] = {6, 7, 8, 9, 10};
    int arr3[5];

    for (int i = 0; i < 5; i++) {
        arr3[i] = arr1[i] + arr2[i];
        cout << arr3[i] << " ";
    }
    cout << endl;

    return 0;
}
// Output: 7 9 11 13 15