if __name__ == '__main__':
    student_number = int(input())
    records = []
    for _ in range(student_number):
        name = input()
        score = float(input())
        records.append([score, name])
    records.sort()
    minimum_score = records[0][0]
    while records != [] and records[0][0] == minimum_score:
        records.pop(0)
    if records != []:
        second_minimum_score = records[0][0]
        for j in records:
            if j[0] == records[0][0]:
                print(j[1])