from vpython import *

scene = canvas(title = "1D Kinematik Simulation", width = 800, height = 600, background=color.gray(0.1))

road = box(pos=vec(0, -0.5, 0), size=vec(100, 0.2, 4), color = color.gray(0.5))

car = box(pos=vec(-40, 0.5, 0), size=vec(4, 1.5, 2), color = color.cyan, make_trail = True, trail_color = color.yellow)

x = car.pos.x 
v = 2.0
a = 1.5
t = 0
dt = 0.01
graph_pos = gcurve(color = color.cyan, label = "Position x (m)")
graph_vel = gcurve(color = color.green, label = "Speed v (m/s)")
graph_acc = gcurve(color = color.red, label = "Acceleration a (m/s")
while car.pos.x < 40: 
    rate(100)
    v = v + a * dt
    x = x + v * dt
    t = t + dt
    car.pos.x = x 
    graph_pos.plot(t, x)
    graph_vel.plot(t, v)
    graph_acc.plot(t, a)
    print(f"Reached goald at t = {round(t, 2)} secs")


# Workshop Class notes
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

"""
class Person {
public:
    Person(std::string name, int alter) {
        this->name = name;
        this->alter = alter;
    }

private:
    std::string name;
    int alter;
};
"""
