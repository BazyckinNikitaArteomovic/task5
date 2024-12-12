import heapq

WEIGHTS = {
    "road": 1,
    "ground": 2,
    "sand": 3,
    "obstacle": float('inf')
}


def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    priority_queue = [(0, start)]
    prev = [[None] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while priority_queue:
        current_distance, (x, y) = heapq.heappop(priority_queue)
        if (x, y) == end:
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_distance = current_distance + WEIGHTS[grid[nx][ny]]
                if new_distance < distances[nx][ny]:
                    distances[nx][ny] = new_distance
                    prev[nx][ny] = (x, y)
                    heapq.heappush(priority_queue, (new_distance, (nx, ny)))

    path = []
    current = end
    while current:
        path.append(current)
        current = prev[current[0]][current[1]]
    path.reverse()
    if distances[end[0]][end[1]] == float('inf'):
        return None, float('inf')

    return path, distances[end[0]][end[1]]


if __name__ == "__main__":
    grid = [
        ["road", "road", "sand", "obstacle"],
        ["road", "ground", "sand", "road"],
        ["road", "road", "road", "road"],
        ["obstacle", "sand", "ground", "road"]
    ]

    start = (0, 0)
    end = (3, 3)

    path, length = dijkstra(grid, start, end)

    if path:
        print("Найденный путь:", path)
        print("Длина пути:", length)
    else:
        print("Путь не найден")
