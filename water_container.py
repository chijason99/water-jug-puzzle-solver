"""Module providing the WaterContainer class."""

class WaterContainer:
    """Class representing a Water Container. It can be either a jug or a glass."""

    def __init__(self, capacity: int, current_state: int):
        self.capacity: int = capacity
        self.current_state: int = current_state

    @property
    def remaining_capacity(self) -> int:
        """Returns the remaining capacity of the container."""
        return self.capacity - self.current_state

    def revert_state(self, previous_state: int) -> None:
        """Revert the state of the container."""
        self.current_state = previous_state

class Jug(WaterContainer):
    """Class representing a Jug.""" 

    def pour_water_to(self, other_jug: 'WaterContainer') -> int:
        """Pour water from this Jug to another container."""
        amount_poured: int = (min(self.current_state, other_jug.remaining_capacity)
                                if self.current_state > other_jug.remaining_capacity or other_jug is not Jug
                                else other_jug.remaining_capacity)

        self.current_state -= amount_poured
        other_jug.current_state += amount_poured

        return amount_poured
