#include <iostream>
using namespace std;

int main() {
    int month, year;
    cout << "Enter month (1-12): ";
    cin >> month;
    cout << "Enter year: ";
    cin >> year;

    int days;

    // Check for valid month
    if (month < 1 || month > 12) {
        cout << "Invalid month!" << endl;
        return 0;
    }

    // Determine number of days
    switch (month) {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            days = 31;
            break;
        case 4: case 6: case 9: case 11:
            days = 30;
            break;
        case 2:
            // Leap year check
            if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
                days = 29;
            else
                days = 28;
            break;
    }

    cout << "Number of days = " << days << endl;
    return 0;
}