#include<stdio.h>

int main(int argc, char const *argv[])
{
    float CR, CD, WeaCR, WeaCD;
    printf("\n\tCrit Value Calculator\n");

    printf("\nEnter character's Crit Rate: ");
    scanf("%f", &CR);
    printf("Enter character weapon's Crit Rate. If not available, type 0: ");
    scanf("%f", &WeaCR);
    printf("\nEnter character's Crit Damage: ");
    scanf("%f", &CD);
    printf("Enter character weapon's Crit Damage. If not available, type 0: ");
    scanf("%f", &WeaCD);

    float NewCR = ((CR - (5.0 + WeaCR)) * 2.0);
    float NewCD = (CD - (50.0 + WeaCD));

    float CritValue = NewCR + NewCD;

    printf("\nCalculating...\n");
    printf("Character's Crit Value: %.1f\n", CritValue);

    if (CritValue >= 0.0 && CritValue < 90.0) {
        printf("Your character's Crit Value is too low.\n");
    } else if (CritValue >= 90.0 && CritValue < 150.0) {
        printf("Your character's Crit Value is decent.\n");
    } else if (CritValue >= 150.0 && CritValue < 180.0) {
        printf("Your character's Crit Value is moderate.\n");
    } else if (CritValue >= 180.0 && CritValue < 200.0) {
        printf("Your character's Crit Value is good!.\n");
    } else if (CritValue >= 200.0) {
        printf("Your character's Crit Value is enough, go do a Spiral Abyss!.\n");
    } else {
        printf("Invalid input. Please check your values.\n");
    }

    return 0;
}
