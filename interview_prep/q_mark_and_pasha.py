def main():
    n = int(input())
    # if N is even, it's always possible to make it odd (N-1).
    # Odd number - any divisor results again to even result.
    # 2 is even, and it's the goal to have for the victory.
    print("Mark" if n % 2 else "Pasha")


if __name__ == "__main__":
    main()
