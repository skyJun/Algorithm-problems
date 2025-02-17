// 원자 소멸
// 원자들이 소멸되면서 방출되는 에너지 총합
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int T;
int N;

struct Atom {
	int x, y, direction, energy;
	int live = 1;
};

struct collison {
	double t;
	int atom1, atom2;
};

bool compare(collison left, collison right){
	return left.t < right.t;
}

// 상하좌우
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };

pair<bool, double> is_annihilation(Atom atom1, Atom atom2) {
	double t_x, t_y;
	if (atom1.direction == atom2.direction) {
		// 움직이는 방향이 같으면 절대 충돌나지 않으므로 false
		return { false, -1 };
	}

	t_x = (dx[atom2.direction] - dx[atom1.direction]) ? abs(atom1.x - atom2.x) / abs(dx[atom2.direction] - dx[atom1.direction]) : -1;
	t_y = (dy[atom2.direction] - dy[atom1.direction]) ? abs(atom1.y - atom2.y) / abs(dy[atom2.direction] - dy[atom1.direction]) : -1;


	// x와 y가 같아지는 시간이 동일하면 충돌
	bool annihilation = (t_x == t_y) && (t_x > 0);
	return { annihilation, (annihilation) ? t_x : -1 };
}

vector<Atom> information;
int main() {
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> N;
		information.clear();  // 이전 케이스 데이터 초기화

		for (int i = 0; i < N; i++) {
			int x_i, y_i, direction_i, energy_i;
			cin >> x_i >> y_i >> direction_i >> energy_i;
			information.push_back({ x_i, y_i, direction_i, energy_i });
		}

		vector<collison> atoms_pair;
		bool annihilation;
		double time;
		// 원자 2개 선택해 충돌여부 확인 후 입력값 넣기
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				pair<bool, double> case_result = is_annihilation(information[i], information[j]);
				bool case_annihilation = case_result.first;
				double case_time = case_result.second;

				if (case_annihilation) {
					atoms_pair.push_back({ case_time, i, j });
				}

			}
		}

		sort(atoms_pair.begin(), atoms_pair.end(), compare);
		int energy = 0;
		for (int index = 0; index < atoms_pair.size(); index++) {
			int atom1 = atoms_pair[index].atom1;
			int atom2 = atoms_pair[index].atom2;

			if (!information[atom1].live || !information[atom2].live){
				// 소멸된 원자가 있으면 스킵
				continue;
		}


			// 죽은 처리
			information[atom1].live = 0;
			information[atom2].live = 0;
			// 에너지 값 추가
			energy += information[atom1].energy;
			energy += information[atom2].energy;

		}
		
		cout << "#" << t << " " << energy << endl;
		atoms_pair.clear();
	}


	return 0;
}