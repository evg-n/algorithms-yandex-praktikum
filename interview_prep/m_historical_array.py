class HistoricalArray:
    def __init__(self, size) -> None:
        self.data = [0] * size
        self.current_era = 0

    def set(self, index, value) -> None:
        if self.data[index] == 0:
            self.data[index] = {}
        self.data[index][self.current_era] = value

    def get(self, index, era_id) -> int:
        if self.data[index] == 0:
            return 0
        if era_id not in self.data[index]:
            return 0
        return self.data[index][era_id]

    def begin_new_era(self, era_id) -> None:
        self.current_era = era_id


size = int(input())
q = int(input())
historical_array = HistoricalArray(size)
for i in range(q):
    query = input().split()
    query_type = query[0]
    if query_type == "set":
        historical_array.set(int(query[1]), int(query[2]))
    elif query_type == "begin_new_era":
        historical_array.begin_new_era(int(query[1]))
    else:
        print(historical_array.get(int(query[1]), int(query[2])))
