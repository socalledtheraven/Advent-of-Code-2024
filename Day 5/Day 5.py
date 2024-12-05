from functools import cmp_to_key


def ordering(a, b):
    # a, b = pair
    relevant_rules = [rule for rule in rules if rule.startswith(a) or rule.startswith(b)]

    for rule in relevant_rules:
        first, second = rule.split("|")
        # first goes before second
        if first == a and second == b:
            return -1
        elif first == b and second == a:
            return 1

    return 0


def update_in_order():
    unordered_updates = []
    for update in updates:
        update = update.split(",")
        update_pairs = [update[i:i+2] for i in range(0, len(update), 1)]
        if len(update_pairs[-1]):
            del update_pairs[-1]

        ordered = True
        for pair in update_pairs:
            if ordering(pair[0], pair[1]) > 0:
                ordered = False

        if not ordered:
            unordered_updates.append(update)

    total = 0
    for upd in unordered_updates:
        upd = sorted(upd, key=cmp_to_key(ordering))
        middle = upd[int(len(upd)/2)]
        total += int(middle)

    print(f"total: {total}")


filename = "Day 5 Input"
with open(filename, "r") as f:
    content = f.read()

rules, updates = content.split("\n\n")
rules = [s.strip() for s in rules.splitlines()]
updates = [s.strip() for s in updates.splitlines()]
update_in_order()
