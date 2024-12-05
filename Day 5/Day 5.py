def is_before(rules, pair):
    a, b = pair
    relevant_rules = [rule for rule in rules if rule.startswith(a)]

    for rule in relevant_rules:
        first, second = rule.split("|")
        if first == a and second == b:
            return True

    return False


def update_in_order(filename):
    with open(filename, "r") as f:
        content = f.read()

    rules, updates = content.split("\n\n")
    rules = [s.strip() for s in rules.splitlines()]
    updates = [s.strip() for s in updates.splitlines()]

    ordered_updates = []
    for update in updates:
        print(update)

        update = update.split(",")
        update_pairs = [update[i:i+2] for i in range(0, len(update), 1)]
        if len(update_pairs[-1]):
            del update_pairs[-1]

        ordered = True
        for pair in update_pairs:
            if not is_before(rules, pair):
                ordered = False

        if ordered:
            ordered_updates.append(update)

    total = 0
    for update in ordered_updates:
        middle = update[int(len(update)/2)]
        total += int(middle)

    print(f"total: {total}")


update_in_order("Day 5 Input")
