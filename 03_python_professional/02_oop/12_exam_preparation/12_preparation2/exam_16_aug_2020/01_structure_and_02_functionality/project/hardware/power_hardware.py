from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    TYPE = "Power"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.TYPE, capacity, memory)
        self.name = name
        self.hardware_type = PowerHardware.TYPE
        self.capacity = int(capacity * 0.25)
        self.memory = int(memory * 1.75)

    def __str__(self):
        express_count = len([s for s in self.software_components if s.TYPE == "Express"])
        light_count = len([s for s in self.software_components if s.TYPE == "Light"])
        mem_us = sum([s.memory_consumption for s in self.software_components])
        total_us = sum([s.capacity_consumption for s in self.software_components])
        soft_names = [s.name for s in self.software_components]
        if soft_names:
            soft_names = ', '.join(soft_names)
        else:
            soft_names = "None"

        return f"Hardware Component - {self.name}\nExpress Software Components: {express_count}\n" \
               f"Light Software Components: {light_count}\nMemory Usage: {mem_us} / {self.memory}\n" \
               f"Capacity Usage: {total_us} / {self.capacity}\nType: {self.TYPE}\n" \
               f"Software Components: {soft_names}"
