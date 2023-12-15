def open_or_senior(data):
    results = []
    for element in data:
        if element[0] > 54 and element[1] > 7: results.append("Senior")
        else: results.append("Open")
    return results

def open_or_senior2(data):
    return ["Senior" if age > 55 and handicap > 7 else "Open" for (age, handicap) in data]

print(open_or_senior2([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))