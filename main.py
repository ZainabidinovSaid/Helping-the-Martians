import random
def initialize_boxes():
    return [
        {"kilometers": random.randint(1, 10), "weight": random.randint(100, 300)},
        {"kilometers": random.randint(1, 10), "weight": random.randint(100, 300)},
        {"kilometers": random.randint(1, 10), "weight": random.randint(100, 300)}
    ]
def move_boxes():
    for box in boxes:
        box["kilometer"] = random.randint(1, 10)

def check_total_weight():
    total_weight = sum(box["weight"] for box in found_boxes)
    return total_weight == 713

def main():
    global boxes, found_boxes
    boxes = initialize_boxes()
    found_boxes = []

    print("Welcome to the Martian Cargo Recovery Program!")
    print("Enter the kilometer marks one by one to find the cargo.")