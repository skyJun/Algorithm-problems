#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    string s = to_string(N);
    int sum = 0;
    for (char c : s){
        sum += (c - '0'); //정수 변환
    }

    cout << sum << endl;

    return 0;
}