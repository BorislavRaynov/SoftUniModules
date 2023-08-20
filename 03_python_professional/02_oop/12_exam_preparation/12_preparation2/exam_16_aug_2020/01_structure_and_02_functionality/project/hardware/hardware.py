from abc import ABC

from project.software.software import Software


class Hardware(ABC):
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        current_used_capacity = sum([s.capacity_consumption for s in self.software_components])
        current_used_memory = sum([m.memory_consumption for m in self.software_components])
        if self.capacity - current_used_capacity >= software.capacity_consumption \
                and self.memory - current_used_memory >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
