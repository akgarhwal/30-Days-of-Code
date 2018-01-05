#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    double meal_cost,tip,tax;
    cin>> meal_cost >> tip >> tax;
    double total_bill = meal_cost + (meal_cost*tip/100.0) + (meal_cost*tax/100.0);
    cout<< "The total meal cost is "  << round(total_bill) << " dollars." << endl;
    return 0;
}
