from pycon_decorators import use_unit


class Runner:
    def __init__(self, distance, duration):
        self.distance = distance
        self.duration = duration

    @use_unit("meters per second")
    def average_speed(self):
        return self.distance / self.duration


class Plane:
    def __init__(self, distance, duration):
        self.distance = distance
        self.duration = duration

    @use_unit("km per hour")
    def average_speed(self):
        return self.distance / self.duration
