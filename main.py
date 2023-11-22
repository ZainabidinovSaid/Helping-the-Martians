import random
def initialize_boxes():
    return [
        {"kilometers": random.randint(1, 10), "weight": random.randint(100, 300)},
        {"kilometers": random.randint(1, 10), "weight": random.randint(100, 300)},
        {"kilometers": random.randint(1, 10), "weight": random.randint(100, 300)}
    ]