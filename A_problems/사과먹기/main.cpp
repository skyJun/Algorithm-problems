// ��� �Ա� ����
// N by N ũ���� �ʿ��� ĳ���͸� �̵��Ͽ� ����� �Դ� ����
// 1������ M�� ������� ������� �Ա⸸ �ϸ� ��
// �÷��̾�� �׻� (0, 0)���� �������� ���� ���¿��� ����
// ���������θ� ȸ���� ���� ���������� ȸ�� �� ����
// �ּ� ��ȸ�� Ƚ��
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T;
int N;

// �ð���� �� Ž�� 0->1->2->3->0 �ݺ�
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

				// 0�� �ƴҶ� ������ ��ǥ�� ����
				number_idx.push_back({ row_idx, col_idx, input_num });
			}
		}

		// ���� ���� ����
		sort(number_idx.begin(), number_idx.end(), compare);

		// Ž�� ���� �ʱⰪ ���� 0,0 ������ ���� ����
		int start_r = 0;
		int start_c = 0;
		int direction_type = 0;
		int total_turns = 0;

		for (int destination = 0; destination < number_idx.size(); destination++) {
			int target_r = number_idx[destination].r;
			int target_c = number_idx[destination].c;
			

			// ��ǥ������ ����
			int dr = target_r - start_r;
			int dc = target_c - start_c;
			
			int target_direction;
			if (dr > 0) {
				// �������� ������
				target_direction = 1;
			}
			else if (dr < 0) {
				// �������� ������
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

			// �ʿ� ȸ�� �� ���
			int need_turns = (target_direction - direction_type + 4) % 4;
			total_turns += need_turns;

			// ��ǥ ���� �� ������Ʈ
			start_r = target_r;
			start_c = target_c;
			direction_type = target_direction;
		}
	
		cout << "#" << t << " " << direction_type;

	}


	return 0;
}