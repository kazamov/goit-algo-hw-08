import heapq


def minimum_cost(cable_length: list[int]):
    heapq.heapify(cable_length)
    total_cost = 0
    while len(cable_length) > 1:
        cost = heapq.heappop(cable_length) + heapq.heappop(cable_length)
        total_cost += cost
        heapq.heappush(cable_length, cost)
    return total_cost


if __name__ == "__main__":
    cable_length = [8, 6, 4, 12]
    print(minimum_cost(cable_length))
