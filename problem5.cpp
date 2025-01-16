#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        
        vector<vector<string>> matrix(N, vector<string>(N));
        for (int i = 0; i<N; i++) {
            for (int j = 0; j < N; j++){
                cin >> matrix[i][j];
            }
        }

        //회전 배열 저장
        vector<vector<string>> rot90(N, vector<string>(N));
        vector<vector<string>> rot180(N, vector<string>(N));
        vector<vector<string>> rot270(N, vector<string>(N));

        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                rot90[i][j] = matrix[N - 1 -j][i];
                rot180[i][j] = matrix[N - 1 - i][N - 1 - j];
                rot270[i][j] = matrix[j][N-1 - i];
            }
        }

        cout << "#" << t << "\n";
        for (int i = 0; i< N; i++){
            string row90, row180, row270;
            for(int j = 0; j < N; j++){
                row90 += rot90[i][j];
                row180 += rot180[i][j];
                row270 += rot270[i][j];
            }

            cout << row90 << " " << row180 << " " << row270 << "\n";
        }
    }

    return 0;
}