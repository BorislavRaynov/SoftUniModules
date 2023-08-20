from project.software.software import Software


class LightSoftware(Software):
    TYPE = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.TYPE, capacity_consumption, memory_consumption)
        self.name = name
        self.software_type = LightSoftware.TYPE
        self.capacity_consumption = int(capacity_consumption * 1.5)
        self.memory_consumption = int(memory_consumption * 0.5)
