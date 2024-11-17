/* The break statement is used within a switch case to terminate a particular case's execution and exit the switch block. Without a break, the program continues executing subsequent cases until it encounters a break or reaches the end of the switch block. This behavior is known as "fall-through."*/

/* Yes, a switch case can work without a break, but it will exhibit fall-through behavior, meaning that if a case matches, the code for that case and all subsequent cases will execute until a break is encountered or the switch statement ends. This can be useful in some scenarios but may lead to unintended behavior if not handled carefully.*/

#include <stdio.h>
int main() {
    int day = 3;
    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break; 
        case 3:
            printf("Wednesday\n"); // No break statement here
        case 4:
            printf("Thursday\n");
            break;  
        case 5:
            printf("Friday\n");
            break;
        default:
            printf("Weekend\n");
    }
    return 0;
}

/* The switch statement checks the value of day.
When day is 3, it executes the code for case 3, printing "Wednesday."
Because there is no break statement after case 3, the control falls through to case 4, printing "Thursday" as well.
If there were a break after case 3, only "Wednesday" would be printed. */
