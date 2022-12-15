import sys
import re


def in_2d_range(pos, minpos, maxpos=None):
    x, y = pos
    minx, miny = minpos if maxpos else 0, 0
    maxx, maxy = maxpos if maxpos else minpos
    return x >= minx and y >= miny and x <= maxx and y <= maxy


def get_manhatten(xa, ya, xb, yb):
    return abs(xb - xa) + abs(yb - ya)


def walk_edge(sensor, sensor_range):
    sx, sy = sensor
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


class Solver:
    def __init__(self, sensors, beacons):
        self.sensors = sensors
        self.beacons = beacons


def get_coverage(sensors: dict, beacons, y, cmin=float('-inf'), cmax=float('inf')):
    coverage_set = set()
    for sensor, delta in sensors.items():
        sx, sy = sensor
        coverage = (delta - abs(sy - y)) * 2 + 1
        if coverage <= 0:
            continue
        cx = [x for x in range(sx - coverage // 2 - 1, sx + coverage // 2)]
        for x in cx:
            if x >= cmin and x <= cmax:
                coverage_set.add(x)
    for bx, by in beacons:
        if by == y:
            coverage_set.discard(bx)
    for bx, by in sensors.keys():
        if by == y:
            coverage_set.discard(bx)
    return len(coverage_set)


def has_sensor_coverage(sensors, pos):
    x, y = pos
    for spos, db in sensors.items():
        sbx, sby = spos
        sensor_delta = db - get_manhatten(sbx, sby, x, y)
        if sensor_delta >= 0:
            return True
    return False


# walk along the edge of each diamond
# see if it intersects another
# if not, then, maybe?
# to start, just get a set of non-intersections in range
def get_full_coverage(sensors, cmax):
    for sensor, delta in sensors.items():
        print(sensor)
        for pos in walk_edge(sensor, delta+1):
            if (in_2d_range(pos, (cmax, cmax))
                    and not has_sensor_coverage(sensors, pos)):
                return pos


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
    # pprint(sensors)

    print("PART A:", get_coverage(sensors, beacons, 2_000_000))

    unx, uny = get_full_coverage(sensors, 4_000_000)
    print(unx, uny)
    print("PART 2:", unx * 4_000_000 + uny)


if __name__ == "__main__":
    main()
