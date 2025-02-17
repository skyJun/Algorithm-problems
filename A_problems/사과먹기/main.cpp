// 사과 먹기 게임
// N by N 크기의 맵에서 캐릭터를 이동하여 사과를 먹는 게임
// 1번부터 M번 사과까지 순서대로 먹기만 하면 됨
// 플레이어는 항상 (0, 0)에서 오른쪽을 향한 상태에서 시작
// 오른쪽으로만 회전이 가능 오른쪽으로 회전 후 전진
// 최소 우회전 횟수
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T;
int N;

// 시계방향 순 탐색 0->1->2->3->0 반복
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

				// 0이 아닐때 가야할 좌표와 숫자
				number_idx.push_back({ row_idx, col_idx, input_num });
			}
		}

		// 숫자 별로 정렬
		sort(number_idx.begin(), number_idx.end(), compare);

		// 탐색 시작 초기값 설정 0,0 오른쪽 방향 진행
		int start_r = 0;
		int start_c = 0;
		int direction_type = 0;
		int total_turns = 0;

		for (int destination = 0; destination < number_idx.size(); destination++) {
			int target_r = number_idx[destination].r;
			int target_c = number_idx[destination].c;
			

			// 목표까지의 차이
			int dr = target_r - start_r;
			int dc = target_c - start_c;
			
			int target_direction;
			if (dr > 0) {
				// 남쪽으로 가야함
				target_direction = 1;
			}
			else if (dr < 0) {
				// 북쪽으로 가야함
				target_direction = 3;
			}
			else {
				target_direction = (dc > 0) ? 0 : 2;
			}
			
			
			if (target_direction == 1 || target_direction == 3) {
				if (dc != 0) {
					target_direction = (target_direction + 3) % 4;
				}
			}

			// 필요 회전 수 계산
			int need_turns = (target_direction - direction_type + 4) % 4;
			total_turns += need_turns;

			// 목표 도달 후 업데이트
			start_r = target_r;
			start_c = target_c;
			direction_type = target_direction;
		}
	
		cout << "#" << t << " " << direction_type;

	}


	return 0;
}