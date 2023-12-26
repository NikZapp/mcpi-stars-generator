from mcpi import minecraft
from mcpi.vec3 import Vec3
from random import randint

mc = minecraft.Minecraft.create()

def scatter(points, max_displacement, min_amount, max_amount):
    new_points = []
    for point in points:
        for i in range(randint(min_amount, max_amount)):
            m = max_displacement
            displacement = Vec3(
                randint(-m.x, m.x),
                randint(-m.y, m.y),
                randint(-m.z, m.z)
            )
            
            new_points.append(point + displacement)
    return new_points

def place(points, block, id_):
    for point in points:
        if mc.getBlock(point) == 0:
            mc.setBlock(point, block, id_)

points = [Vec3(0, 60, 0)]

points = scatter(points, Vec3(64, 10, 64), 6, 10)
points = scatter(points, Vec3(20, 15, 20), 4, 10)
points = scatter(points, Vec3(6, 6, 6), 3, 8)
points = scatter(points, Vec3(3, 6, 3), 1, 2)

place(points, 51, 1)

points = []
for x in range(-120, 140, 20):
    for z in range(-120, 140, 20):
        points.append(Vec3(x, 60, z))

points = scatter(points, Vec3(30, 15, 30), 1, 4)
points = scatter(points, Vec3(6, 8, 6), 3, 5)
points = scatter(points, Vec3(3, 6, 3), 1, 2)

place(points, 51, 1)
