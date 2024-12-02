def get_difference(report, i):
    level = int(report[i])
    next_level = int(report[i+1])

    return next_level - level


def find_unsafe_differences(report: list[int]):
    for i in range(len(report) - 1):
        diff = get_difference(report, i)

        if abs(diff) > 3:
            return False

    return True


def find_direction_change(report: list[int]):
    increasing = None
    for i in range(len(report) - 1):
        diff = get_difference(report, i)

        if i == 0:
            increasing = diff > 0
            if diff == 0:
                increasing = None
        else:
            currently_increasing = diff > 0
            if diff == 0:
                increasing = None

            if increasing != currently_increasing:
                return False

    return True


def safe_reports(filename: str):
    with open(filename, "r") as f:
        reports = f.readlines()

    reports_status = []
    for report in reports:
        report = list(map(int, report.strip().split(" ")))
        safe = find_unsafe_differences(report) and find_direction_change(report)

        reports_status.append(safe)

    return reports_status.count(True)


def safe_reports_with_dampener(filename: str):
    with open(filename, "r") as f:
        reports = f.readlines()

    reports_status = []
    for report in reports:
        report = list(map(int, report.strip().split(" ")))
        safe = find_unsafe_differences(report) and find_direction_change(report)

        if not safe:
            tests = []
            for i in range(len(report)):
                current_report = report[:i] + report[i+1:]
                test = find_unsafe_differences(current_report) and find_direction_change(current_report)
                tests.append(test)

            safe = any(tests)

        reports_status.append(safe)

    return reports_status.count(True)


print(safe_reports_with_dampener("Day 2 Input"))
