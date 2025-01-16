#include<iostream>
#include <vector>
#include <queue>
using namespace std;

static const int dr[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
static const int dc[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

bool inRange(int r, int  c, int N) {
    return (0<= r && r < N && 0<= c && c < N);
}

void bfs(int r, int c, int N, vector<vector<int>>& adj_mine, vector<vector<bool>>& visited) {
    queue<pair<int, int>> q;
    q.push({r, c});
    visited[r][c] = true;
    while(!q.empty()) {
        r = q.front().first;
        c = q.front().second;
        q.pop();

        if (adj_mine[r][c] == 0) {
            for (int dir = 0; dir <8; dir++) {
                int nr = r + dr[dir];
                int nc = c + dc[dir];

                if (inRange(nr, nc, N)) {
                    if (adj_mine[nr][nc] != -1 && !visited[nr][nc]) {
                        visited[nr][nc] = true;
                        q.push({nr, nc});
                    }
                }
            }
        }

    }
}


int main() {    
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        vector<string> board(N); //일차원 보드 입력판
        vector<vector<int>> adj_mine(N, vector<int>(N, 0));  //인접 지뢰 개수 배열
        
        //보드 입력
        for (int i = 0; i < N; i++) {
            cin >> board[i];
        }

        //인접 지뢰 개수 초기 입력
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (board[r][c] == '*') {
                    adj_mine[r][c] = -1;
                }
                else {
                    int mineCnt = 0;
                    for (int dir = 0; dir < 8; dir++) {
                        int nr = r + dr[dir];
                        int nc = c + dc[dir];

                        if (inRange(nr, nc, N)) {
                            if (board[nr][nc] == '*') {
                                mineCnt++;
                            }
                        }
                    }
                    adj_mine[r][c] = mineCnt;
                }
            }
        }

        vector<vector<bool>> visited(N, vector<bool>(N, false));  //방문여부 판단 배열

        int clicks = 0;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (adj_mine[r][c] == 0 && !visited[r][c]) {
                    clicks++;
                    bfs(r, c, N, adj_mine, visited);
                }
            }
        }

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (adj_mine[r][c] != -1 && !visited[r][c]) {
                    clicks++;
                }
            }
        }
    
    cout << "#" << t << " " << clicks << "\n" ;
    }

    return 0;
}