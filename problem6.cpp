#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    for (int t = 1; t<= T; t++){
        int N, M;
        cin >> N >> M;

        vector<vector<int>> grid(N, vector<int>(N));
        for(int i = 0; i< N; i++) {
            for(int j = 0; j < N; j++){
                cin >> grid[i][j];
            }
        }

        long long max_flies = 0;

        for (int r = 0; r< N; r++){
            for (int c = 0; c < N; c++){
                long long sum_plus = grid[r][c];
                for(int step = 1; step < M; step++){
                    
                    int nr_up = r - step;
                    if (nr_up >= 0) {
                        sum_plus += grid[nr_up][c];
                    }
                    
                    int nr_down = r + step;
                    if (nr_down < N) {
                        sum_plus += grid[nr_down][c];
                    }
                    
                    int nc_left = c - step;
                    if (nc_left >= 0) {
                        sum_plus += grid[r][nc_left];
                    }
                    
                    int nc_right = c + step;
                    if (nc_right < N) {
                        sum_plus += grid[r][nc_right];
                    }
                }

                long long sum_x = grid[r][c];
                for(int step = 1; step < M; step++) {
                    
                    int nr_lu = r - step;
                    int nc_lu = c - step;
                    if (nr_lu >= 0 && nc_lu >= 0) {
                        sum_x += grid[nr_lu][nc_lu];
                    }
                    
                    int nr_ru = r - step;
                    int nc_ru = c + step;
                    if (nr_ru >= 0 && nc_ru < N) {
                        sum_x += grid[nr_ru][nc_ru];
                    }
                    
                    int nr_ld = r + step;
                    int nc_ld = c - step;
                    if (nr_ld < N && nc_ld >= 0) {
                        sum_x += grid[nr_ld][nc_ld];
                    }
                    
                    int nr_rd = r + step;
                    int nc_rd = c + step;
                    if (nr_rd < N && nc_rd < N) {
                        sum_x += grid[nr_rd][nc_rd];
                    }
                }

                long long local_max = max(sum_plus, sum_x);
                if (local_max > max_flies){
                    max_flies = local_max;
                }

            }
        }

        cout << "#"<< t << " " << max_flies << "\n";

    }



    return 0;
}