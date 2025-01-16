#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> scores(N); //동적할당

    for(int i = 0; i < N; i++) {
        cin >> scores[i];
    }

    sort(scores.begin(), scores.end());

    cout << scores[N / 2] << endl;

    return 0;
}