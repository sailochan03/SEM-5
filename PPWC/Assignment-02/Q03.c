/* 
>> Break Statement
-Function: The break statement is used to terminate the loop immediately, regardless of the loop's iteration condition. Control is transferred to the statement following the loop.
-Usage: It is often used to exit a loop when a certain condition is met or when a specific situation arises (like finding a target value). 

>> Continue Statement
-Function: The continue statement skips the current iteration of the loop and moves directly to the next iteration. It effectively ignores the remaining code within the loop for that iteration.
-Usage: It is useful when you want to skip certain conditions or values without terminating the loop. 
*/
#include <stdio.h>
int main() {
    for (int i = 1; i <= 10; i++) {
        if (i == 5) {
            break;  // Exit the loop when i equals 5
        }
        printf("%d ", i);
    }
    printf("\n");
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            continue;  // Skip even numbers
        }
        printf("%d ", i);
    }
    return 0;
}
