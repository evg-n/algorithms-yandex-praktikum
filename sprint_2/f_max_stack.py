class StackMax:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not len(self.stack):
            print("error")
            return
        self.stack.pop()

    def get_max(self):
        if not len(self.stack):
            return "None"
        return max(self.stack)


def main():
    n = int(input())

    s = StackMax()
    for _ in range(n):
        command = input().split()
        if len(command) > 1:
            s.push(int(command[1]))
        elif command[0] == "get_max":
            print(s.get_max())
        else:
            s.pop()


if __name__ == "__main__":
    main()
