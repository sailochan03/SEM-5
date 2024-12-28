#include<stdio.h>
int isPresent(int arr[], int size, int target){
    for(int i = 0 ; i < size; i++){
        if(arr[i] == target){
            return 1;
        }
    }
    return 0;
}
int repeatingChar(char str[], int size, int repeat[]){
    int index = 0;
    for(int i = 0; i < size; i++){
        char target = str[i];
        if(!isPresent(repeat, index, target)){
            repeat[index++] = target;
        }
        if (index == 1)
        break;
    }
    return index;
}
int main(){

    char str[] = "racecar";
    int size = sizeof(str) / sizeof(str[0]);
    int repeat[size];

    int disSize = repeatingChar(str, size, repeat);

    printf("First repeating character: ");
    for (int i = 0; i < disSize; i++) {
        printf("%c ", repeat[i]);
    }

    return 0;
}