if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = sorted(set(arr))

    print(arr2[-2])