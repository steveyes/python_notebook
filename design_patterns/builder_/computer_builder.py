#!/usr/bin/env python3
#


class Computer:
    def __init__(self, serial_number) -> None:
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self) -> str:
        info = (f"Memory: {self.memory}",
                f"Hard Disk: {self.hdd}",
                f"Graphics Card: {self.gpu}",
                )
        return '\n'.join(info)


class ComputerBuilder:
    '''
    role: 建造者
    '''

    def __init__(self) -> None:
        self.computer = Computer('AG0234532')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    '''
    role: 指挥者
    '''

    def __init__(self) -> None:
        self.builder: ComputerBuilder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        list([step for step in (
            self.builder.configure_memory(memory),
            self.builder.configure_hdd(hdd),
            self.builder.configure_gpu(gpu)
        )])

    @property
    def computer(self):
        return self.builder.computer


if __name__ == '__main__':
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu="Gefore GTX 650 Ti")
    computer = engineer.computer
    print(computer)
