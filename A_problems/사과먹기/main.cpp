// 사과 먹기 게임
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <array>

using namespace std;

int T;
int N;

// 시계방향 순회 0->1->2->3->0 
int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

struct Coord {
	int r, c, number;
};

bool compare(Coord left, Coord right) {
	return left.number < right.number;
}

vector<Coord> number_idx;


int main() {
	cin >> T;
	for (int t = 1; t < T + 1; t++) {
		cin >> N;

		for (int row_idx = 0; row_idx < N; row_idx++) {
			for (int col_idx = 0; col_idx < N; col_idx++) {
				int input_num;
				cin >> input_num;
				if (input_num == 0) continue;

				number_idx.push_back({ row_idx, col_idx, input_num });
			}
		}

		sort(number_idx.begin(), number_idx.end(), compare);

		int start_r = 0;
		int start_c = 0;

		int direction_type = 0;
		int total_turns = 0;
		
		vector<vector<vector<int>>> dist(N, vector<vector<int>>(N, vector<int>(4, 1e9)));
		deque<array<int, 3>> que;
		que.push_back({start_r, start_c, direction_type});
		dist[start_r][start_c][direction_type] = 0;

		for (int destination = 0; destination < number_idx.size(); destination++) {
			int target_r = number_idx[destination].r;
			int target_c = number_idx[destination].c;
			
			while(!que.empty()) {
				auto [current_r, current_c, current_direction] = que.front();
				que.pop_front();
				int cost = dist[current_r][current_c][current_direction];

				// 목적지에 도달하면 탈출
				if (current_r == target_r && current_c == target_c) break;

				// 1 전진 비용 0
				int nr = current_r + dr[current_direction];
				int nc = current_c + dc[current_direction];

				if (0 <= nr && nr < N && 0 <= nc && nc < N ) {
					if(dist[nr][nc][current_direction] > cost) {
						// 현재 코스트가 더 낮으면 대입
						dist[nr][nc][current_direction] = cost;
						que.push_front({nr, nc, current_direction});
					}
				}

				// 2 회전 비용 1
				int nd = (current_direction + 1) % 4;
				nr = current_r + dr[nd];
				nc = current_c + dc[nd];

				if (0 <= nr && nr <N && 0 <= nc && nc <N ) {
					if(dist[nr][nc][nd] > cost+1) {
						// 현재 코스트가 더 낮으면 대입
						dist[nr][nc][nd] = cost+1;
						que.push_back({nr, nc, nd});
					}
				}
			}

			int best = 1e9;
			int best_direction;

			for (int d=0; d<4; d++) {
				if (dist[target_r][target_c][d] < best) {
					best = dist[target_r][target_c][d];
					best_direction = d;
				}
			}
			total_turns += best;

			// 업데이트
			start_r = target_r;
			start_c = target_c;
			direction_type = best_direction;
			dist.clear();
			que.clear();
		}
	
		cout << "#" << t << " " << total_turns;
		number_idx.clear();
	}


	return 0;
}