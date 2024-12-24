"""Module containing the ContainerState class."""

from water_container import WaterContainer, Jug

class ContainerState:
    """Class representing a state of the containers."""
    def __init__(self, state: tuple[int]):
        self.saved_state: tuple[int] = state
        self.jugs: list[Jug] = []
        self.cups: list[WaterContainer] = []

        for i, amount in enumerate(state):
            if i < 2:
                self.jugs.append(Jug(capacity=8, current_state=amount))
            elif i == 2:
                self.jugs.append(Jug(capacity=3, current_state=amount))
            else:
                self.cups.append(WaterContainer(capacity=999, current_state=amount))

    def current_state(self) -> tuple[int]:
        """Return the current state of the containers."""
        return tuple(jug.current_state for jug in self.jugs) + tuple(cup.current_state for cup in self.cups)

    def is_possible_solution(self, state: tuple[int]) -> bool:
        """Check if the state is a possible solution. For now, I am checking if any cups exceeded 4L, which would cause the criteria to fail."""
        for i, amount in enumerate(state):
            if i < 3:
                continue

            if amount > 4:
                return False

        return True

    def get_next_states(self) -> list[tuple[int]]:
        """Return the next possible states."""
        next_states: list[tuple[int]] = []

        for jug in self.jugs:
            for container in [wc for wc in self.cups + self.jugs if wc is not jug]:
                jup_state = jug.current_state
                cup_state = container.current_state

                jug.pour_water_to(container)
                if self.is_possible_solution(self.current_state()):
                    next_states.append(self.current_state())

                jug.revert_state(jup_state)
                container.revert_state(cup_state)

        return next_states
