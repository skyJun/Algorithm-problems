# 배수 스위치

# 전구 N개를 가지고 있다. 1번부터 N번까지 전구는 켜져있거나 꺼져있음
# 모든 전구를 끄려고 함 스위치 N개를 가지고 있고 i번 스위치는 i의 배수 번호를 가지고 있는 전구 상태를 반전

lights_states = input()
lights_list = [None]
for state in lights_states:
    if state == 'Y':
        lights_list.append(1)
    else:
        lights_list.append(0)

switch_count = 0  # 스위치 작동 수
for idx in range(1, len(lights_list)):
    state = lights_list[idx]
    if state == 0:
        continue
    
    # 스위치 작동 시킬때 작은 인덱스 번호 부터 시작 그 이유 큰 번호는 작은 번호를 건들 수 없기 때문
    # idx 배수로 작동
    switch_count += 1
    for change_idx in range(idx, len(lights_list), idx):
        lights_list[change_idx] = 0 if lights_list[change_idx] == 1 else 1
    
    if sum(lights_list[1:]) == 0:
        # 다 0으로 만든거기 때문에 탈출
        break

if sum(lights_list[1:]) != 0:
    print(-1)
else:
    print(switch_count)