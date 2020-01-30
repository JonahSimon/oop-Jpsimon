from wheel import Wheel

print(f"burst pressure ={Wheel.BURST_PRESSURE}")

wheel = Wheel(diameter = 13.0, pressure = 24.0)

print(f"pressure = {wheel.pressure}")
wheel.pressure = 10000.0
print(f"pressure = {wheel.pressure}")
print(f"Burst = {wheel.burst}")