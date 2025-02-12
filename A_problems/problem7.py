# 작업순서

def work_graph(info, V):
    '''
    노드 노드 사이의 연결된 정보와 총 노드 수를 이용하여
    단 방향 일 순서 그래프 만들기

    info 부모 자식 부모 자식 부모 자식 .. 이런 순으로 리스트에 저장되어 있다.
    '''

    graph = {}
    # 그래프 초기화
    for i in range(1, V + 1):
        graph[i] = []

    for i in range(0, len(info), 2):
        graph[info[i]].append(info[i + 1])

    return graph


def find_order(work, V):
    '''
    일의 순서를 찾는 함수
    '''
    order = []
    while work:
        all_nodes = set(range(1, V + 1))
        work_nodes = set()
        for values in work.values():
            work_nodes.update(values)

        possible_nodes = all_nodes - work_nodes  # 집합
        possible_nodes = possible_nodes & set(work.keys())
        possible_nodes = list(possible_nodes)
        order.extend(possible_nodes)
        remove_node(work, possible_nodes)

    return order


def remove_node(work, nodes):
    '''
    work 그래프에 있는 노드 제거
    '''
    for node in nodes:
        del work[node]


T = 10
results = []
for _ in range(T):
    V, E = map(int, input().split())
    info = list(map(int, input().split()))
    work = work_graph(info, V)
    results.append(find_order(work, V))

for i in range(T):
    print(f"#{i + 1} {' '.join(map(str, results[i]))}")