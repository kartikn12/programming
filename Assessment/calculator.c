#include<stdio.h>

// Function for addition
void addition() {
    int a, b;
    printf("\nEnter First Number: ");
    scanf("%d", &a);
    printf("Enter Second Number: ");
    scanf("%d", &b);
    printf("\nYour addition is %d\n", a + b);
}

// Function for subtraction
void subtraction() {
    int a, b;
    printf("\nEnter First Number: ");
    scanf("%d", &a);
    printf("Enter Second Number: ");
    scanf("%d", &b);
    printf("Your subtraction is %d\n", a - b);
}

// Function for multiplication
void multiplication() {
    int a, b;
    printf("\nEnter First Number: ");
    scanf("%d", &a);
    printf("Enter Second Number: ");
    scanf("%d", &b);
    printf("Your multiplication is %d\n", a * b);
}

// Function for division
void division() {
    int a, b;
    printf("\nEnter First Number: ");
    scanf("%d", &a);
    printf("Enter Second Number: ");
    scanf("%d", &b);
    printf("Your division is %d\n", a / b);
}

// Main function
 main() {
    while(1) {
        int ch;
        
        // Displaying the menu
        printf("--------------- MENU ----------------\n\n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");
        printf("5. Exit\n");
        printf("\nEnter your Choice: ");
        scanf("%d", &ch);
        
        // Handling user's choice
        if (ch == 1) {
            addition();
        } else if (ch == 2) {
            subtraction();
        } else if (ch == 3) {
            multiplication();
        } else if (ch == 4) {
            division();
        } else if (ch == 5) {
            printf("\nThank you!!\n");
            break; // Exit the loop and end the program
        } else {
            printf("\nInvalid Choice. Please enter a valid choice.\n");
        }
    }

    
}
