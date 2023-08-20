from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption):
        try:
            hardware = next(filter(lambda h: h.name == hardware_name, System._hardware))

        except StopIteration:
            return "Hardware does not exist"

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption):
        try:
            hardware = next(filter(lambda h: h.name == hardware_name, System._hardware))

        except StopIteration:
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        if hardware_name in [h.name for h in System._hardware] and \
                software_name in [s.name for s in System._software]:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = ["System Analysis", f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}"]

        total_op_memory = "Total Operational Memory: "
        soft_mem = sum([s.memory_consumption for s in System._software])
        hard_mem = sum([h.memory for h in System._hardware])
        total_op_memory += f"{soft_mem} / {hard_mem}"

        total_cap = "Total Capacity Taken: "
        soft_cap = sum([s.capacity_consumption for s in System._software])
        hard_cap = sum([h.capacity for h in System._hardware])
        total_cap += f"{soft_cap} / {hard_cap}"

        result.append(total_op_memory)
        result.append(total_cap)

        return '\n'.join(result)

    @staticmethod
    def system_split():
        result = []
        for h in System._hardware:
            result.append(str(h))

        return '\n'.join(result)
