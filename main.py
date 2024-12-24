from collections import deque
from container_state import ContainerState

initial_state: tuple[int] = (8, 8, 0, 0, 0, 0, 0)
target_state: tuple[int] = (0, 0, 0, 4, 4, 4, 4)

visited_states: set[tuple[int]] = set()

queue = deque([(initial_state, [])])

while queue:
    current_state, path = queue.popleft()

    if current_state == target_state:
        print("Solution found!")
        print(path)
        break

    if current_state in visited_states:
        continue

    visited_states.add(current_state)

    container_state = ContainerState(current_state)
    for next_state in container_state.get_next_states():
        if next_state not in visited_states:
            queue.append((next_state, path + [next_state]))

print("No solution found.")