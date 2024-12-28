#include<stdio.h>
int isPresent(int arr[], int size, int target){
    for(int i = 0 ; i < size; i++){
        if(arr[i] == target){
            return 1;
        }
    }
    return 0;
}
int distinctElements(int arr[], int size, int distinct[]){
    int index = 0;
    for(int i = 0; i < size; i++){
        int target = arr[i];
        if(!isPresent(distinct, index, target)){
            distinct[index++] = target;
        }
    }
    return index;
}
int main(){

    int arr[] = {4, 7, 7, 3, 2, 5, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    int distinct[size];

    int disSize = distinctElements(arr, size, distinct);

    printf("Distinct elements: ");
    for (int i = 0; i < disSize; i++) {
        printf("%d ", distinct[i]);
    }

    return 0;
}