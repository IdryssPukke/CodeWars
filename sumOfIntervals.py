def sum_of_intervals(intervals):
    
    intervals=sorted(intervals)
    left, right = intervals[0]
    sum = right - left
    
    for interval in intervals[1:]:
        if interval[0] > right:
            sum += interval[1] - interval[0]
            left, right = interval
        elif interval[0] >= left and interval[1] <= right:
            continue
        else:
            sum += interval[1] - right
            right = interval[1]
    return sum

print(sum_of_intervals([
    (-100, 4), (7, 10), (2, 3)
]))