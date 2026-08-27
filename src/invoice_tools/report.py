from quickcalckit import add, mean


def line_totals(rows):
    return {"sum": add(sum(rows), 0), "avg": mean(rows)}
