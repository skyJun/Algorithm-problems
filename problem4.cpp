#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false); // C++의 cin/cout과 C의 scanf/printf 사이의 동기화를 끄는 역할
    cin.tie(nullptr); //cin과 cout간의 자동묶임을 끊는 역할

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, M;
        cin >> N >> M;
        vector<int> A(N), B(M);

        for (int i = 0; i < N; i++){
            cin >> A[i];
        }
        for (int j = 0; j < M; j++){
            cin >> B[j];
        }

        vector<int> short_arr, long_arr;
        if (N < M) {
            short_arr = A;
            long_arr = B;
        }
        else {
            short_arr = B;
            long_arr = A;
        }

        int len_s = short_arr.size();
        int len_l = long_arr.size();

        long long max_sum = -1000000000000000LL;
        for (int start = 0; start <= len_l - len_s; start++){
            long long cur_sum = 0;
            for (int k = 0; k < len_s; k++) {
                cur_sum += (long long) short_arr[k] * long_arr[start + k];
            }
            if (cur_sum > max_sum) {
                max_sum = cur_sum;
            }
        }

        cout << "#" << t << " " <<max_sum << "\n";

    }

    return 0;

}