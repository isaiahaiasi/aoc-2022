import sys
import re


def in_2d_range(pos, minpos, maxpos=None):
    x, y = pos
    minx, miny = minpos if maxpos else 0, 0
    maxx, maxy = maxpos if maxpos else minpos
    return x >= minx and y >= miny and x <= maxx and y <= maxy


def get_manhatten(xa, ya, xb, yb):
    return abs(xb - xa) + abs(yb - ya)


class Solver:
    def __init__(self, sensors: dict, beacons: set):
        self.sensors = sensors
        self.beacons = beacons

    def walk_edge(self, sensor: tuple[int, int]):
        sx, sy = sensor
        sensor_range = self.sensors[sensor] + 1  # one more to be outside edge
        # NW
        for i in range(sensor_range):
            yield sx - i, sy - sensor_range + i
        # SW
        for i in range(sensor_range):
            yield sx - sensor_range + i, sy + i
        # SE
        for i in range(sensor_range):
            yield sx + i, sy + sensor_range - i
        # NE
        for i in range(sensor_range):
            yield sx + sensor_range - i, sy - i

    def has_sensor_coverage(self, x, y):
        for spos, db in self.sensors.items():
            sbx, sby = spos
            sensor_delta = db - get_manhatten(sbx, sby, x, y)
            if sensor_delta >= 0:
                return True
        return False

    def get_row_coverage(self, y):
        coverage_set = set()
        for sensor, delta in self.sensors.items():
            sx, sy = sensor
            coverage = (delta - abs(sy - y)) * 2 + 1
            if coverage <= 0:
                continue
            cx = [x for x in range(sx - coverage // 2 - 1, sx + coverage // 2)]
            for x in cx:
                coverage_set.add(x)
        for bx, by in self.beacons:
            if by == y:
                coverage_set.discard(bx)
        for bx, by in self.sensors.keys():
            if by == y:
                coverage_set.discard(bx)
        return len(coverage_set)

    # walk edge of each diamond and find where it doesn't intersect another
    def get_distress_position(self, cmax):
        for sensor in self.sensors.keys():
            for x, y in self.walk_edge(sensor):
                if (in_2d_range((x, y), (cmax, cmax))
                        and not self.has_sensor_coverage(x, y)):
                    return (x, y)

    def get_distress_frequency(self):
        magic_num = 4_000_000  # why is it range and multiplier? magic!
        x, y = self.get_distress_position(magic_num)
        return x * magic_num + y


def load_input(path):
    sensors = {}
    beacons = set()
    with open(path, "r") as fp:
        for line in fp:
            sx, sy, bx, by = map(int, re.findall('[\-]?\d+', line.strip()))
            beacon = (bx, by)
            beacons.add(beacon)
            sensors[(sx, sy)] = get_manhatten(sx, sy, bx, by)
    return sensors, beacons


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './day15/test-input.txt'
    sensors, beacons = load_input(path)

    solver = Solver(sensors, beacons)

    result_a = solver.get_row_coverage(2_000_000)
    print("PART A:", result_a)
    print("part A match:", result_a == 6078701)

    result_b = solver.get_distress_frequency()
    print("PART B:", result_b)
    print("part B match:", result_b == 12567351400528)


if __name__ == "__main__":
    main()
