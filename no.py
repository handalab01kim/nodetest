N, K = map(int, input().split())

count = 0
result = []
found = False

def dfs(depth, stack, path):
    global count, result, found

    if found:
        return

    if depth == N:
        if stack != 0:
            if count == K:
                result = path
                found = True
            count += 1
        return

    # 여는 괄호 추가
    dfs(depth + 1, stack + 1, path + ['('])
    if found:
        return

    # 닫는 괄호 추가
    if stack > 0:
        dfs(depth + 1, stack - 1, path + [')'])
    else:
        # invalid 괄호 바로 감지
        if count == K:
            result = path + [')'] + ['('] * (N - depth - 1)
            found = True
        count += 1

# 시작
dfs(0, 0, [])

if not result:
    print(-1)
else:
    print(''.join(result))
