def hot_potato(players, passes):
    queue = list(players)
    while len(queue) > 1:
        for _ in range(passes):
            queue.append(queue.pop(0))
        queue.pop(0)
    return queue[0] if queue else None


winner = hot_potato(["Ana", "Luis", "Mia", "Leo"], 2)
