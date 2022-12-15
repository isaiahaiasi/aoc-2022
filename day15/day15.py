import sys
import re

A_ROW = 2_000_000
B_MAX = 4_000_000


def merge_intervals(intervals: list[tuple[int, int]]):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_intervals[0]]
    for b_start, b_end in sorted_intervals[1:]:
        a_start, a_end = merged[-1]
        if b_start <= a_end:
            merged[-1] = a_start, max(a_end, b_end)
        else:
            merged.append((b_start, b_end))
    return merged


class Solver:
    def __init__(self,
                 sensors: dict[tuple[int, int], tuple[int, int]],
                 beacons: set[tuple[int, int]]):
        self.sensors = sensors
        self.beacons = beacons

    def get_row_coverage(self, y):
        coverage_intervals = []
        for sensor, delta in self.sensors.items():
            sx, sy = sensor
            coverage = (delta - abs(sy - y)) * 2 + 1
            if coverage > 0:
                interval = (sx - coverage // 2, sx + coverage // 2 + 1)
                coverage_intervals.append(interval)
        return merge_intervals(coverage_intervals)

    def get_positions_without_beacon_count(self, y):
        row_intervals = self.get_row_coverage(y)
        beacons_in_row = [b[0] for b in self.beacons if b[1] == y]
        count = 0
        for start, end in row_intervals:
            b_adj = 0
            for bx in beacons_in_row:
                if bx >= start and bx <= end:
                    b_adj += 1
            count += end - start - b_adj
        return count

    def get_distress_position(self):
        for row in range(B_MAX):
            intervals = self.get_row_coverage(row)
            if len(intervals) > 1:
                return intervals[0][1], row

    def get_distress_frequency(self):
        x, y = self.get_distress_position()
        return x * B_MAX + y


def load_input(path):
    sensors = {}
    beacons = set()
    with open(path, "r") as fp:
        for line in fp:
            sx, sy, bx, by = map(int, re.findall('[\-]?\d+', line.strip()))
            beacon = (bx, by)
            beacons.add(beacon)
            sensors[(sx, sy)] = abs(bx - sx) + abs(by - sy)
    return sensors, beacons


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './day15/test-input.txt'
    sensors, beacons = load_input(path)

    solver = Solver(sensors, beacons)

    print("PART A", solver.get_positions_without_beacon_count(A_ROW))
    print("PART B:", solver.get_distress_frequency())


if __name__ == "__main__":
    main()
