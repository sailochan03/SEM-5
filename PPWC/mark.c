#include <stdio.h>
int mMidsem, mAss, mQuiz, mLab, mEndsem;
double mAtt;
int midsemScore, attendanceScore, endsemScore;

void enterDetails()
{
    printf("--- INTERNAL MARKS DETAILS ---\n");
    printf("Enter Marks in Mid-Sem (out of 30): ");
    scanf("%d", &mMidsem);
    printf("Enter assignment marks (out of 10): ");
    scanf("%d", &mAss);
    printf("Enter marks in Quizzes (out of 10): ");
    scanf("%d", &mQuiz);
    printf("Enter total Attendance (out of 100): ");
    scanf("%lf", &mAtt);

    printf("--- EXTERNAL MARKS DETAILS ---\n");
    printf("Enter Marks in End-Sem (out of 60): ");
    scanf("%d", &mEndsem);
    printf("Enter marks in Lab Test (out of 15): ");
    scanf("%d", &mLab);
}

int internalMark()
{
    midsemScore = mMidsem / 2;
    attendanceScore = (mAtt >= 75.0) ? 5 : 0;
    int internalScore = midsemScore + mAss + mQuiz + attendanceScore;
    return internalScore;
}

int externalMark()
{
    endsemScore = (mEndsem * 45) / 60;
    int externalScore = endsemScore + mLab;
    return externalScore;
}

int calculateTotal(int internalScore, int externalScore)
{
    return internalScore + externalScore;
}

char calculateGrade(int totalScore)
{
    if (totalScore >= 90)
        return 'O';
    else if (totalScore >= 80)
        return 'A';
    else if (totalScore >= 70)
        return 'B';
    else if (totalScore >= 60)
        return 'C';
    else if (totalScore >= 50)
        return 'D';
    else if (totalScore >= 40)
        return 'E';
    else
        return 'F';
}

void printDetails(int internalScore, int externalScore, int totalScore, char grade)
{
    printf("\n--- MARKS SUMMARY ---\n");
    printf("Marks secured in Mid-Sem (out of 15): %d\n", midsemScore);
    printf("Marks secured from Assignments: %d\n", mAss);
    printf("Marks secured from Quizzes: %d\n", mQuiz);
    printf("Marks secured from Attendance (out of 5): %d\n", attendanceScore);
    printf("TOTAL INTERNAL MARKS: %d/40\n", internalScore);

    printf("Marks secured in Lab Test: %d\n", mLab);
    printf("Marks secured in End-Sem (out of 45): %d\n", endsemScore);
    printf("TOTAL EXTERNAL MARKS: %d/60\n", externalScore);

    printf("\nTOTAL MARKS SECURED: %d/100\n", totalScore);
    printf("GRADE: %c\n", grade);
}

void checkPassFail(int internalScore, int externalScore, int totalScore, char grade)
{
    if (internalScore >= 16 && externalScore >= 24)
    {
        if (grade != 'F')
        {
            printf("\nResult: PASS\n");
        }
        else
        {
            printf("\nResult: FAIL\n");
        }
    }
    else
    {
        printf("\nResult: FAIL\n");
    }
}

int main()
{
    enterDetails();

    int internalScore = internalMark();
    int externalScore = externalMark();
    int totalScore = calculateTotal(internalScore, externalScore);
    char grade = calculateGrade(totalScore);

    printDetails(internalScore, externalScore, totalScore, grade);
    checkPassFail(internalScore, externalScore, totalScore, grade);

    return 0;
}
