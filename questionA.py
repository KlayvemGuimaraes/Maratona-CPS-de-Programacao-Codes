import sys

def calculate_mean(temperatures, M):
    min_mean = float('inf')
    max_mean = float('-inf')

    for i in range(len(temperatures) - M + 1):
        interval_sum = sum(temperatures[i:i + M])
        mean = interval_sum / M
        min_mean = min(min_mean, mean)
        max_mean = max(max_mean, mean)

    return min_mean, max_mean

def main():
    results = []
    test_number = 1

    while True:
        N, M = map(int, input().split())

        if N == 0 and M == 0:
            break

        temperatures = [int(input()) for _ in range(N)]
        min_mean, max_mean = calculate_mean(temperatures, M)

        results.append((test_number, (min_mean, max_mean)))
        test_number += 1

    for test_number, result in results:
        print(f"Test {test_number}")
        print(f"{result[0]:.0f} {result[1]:.0f}")
        print()

if __name__ == "__main__":
    main()
