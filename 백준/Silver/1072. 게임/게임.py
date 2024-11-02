def solutions():
    x, y = map(int, input().split(" "))
    old_z = (y * 100) // x 
    if old_z >= 99:
        return -1
    
    left, right = 0, 1000000000
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        new_z = ((y + mid) * 100) // (x + mid)
        if new_z > old_z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

print(solutions())