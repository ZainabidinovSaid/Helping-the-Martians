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

    while len(found_boxes) < 3:
        move_boxes()

        for i in range(3):
            kilometer = int(input(f"Enter kilometer mark {i + 1}: "))
            for box in boxes:
                if box["kilometer"] == kilometer:
                    print(f"Box found at kilometer {kilometer} with {box['weight']} kilograms.")
                    found_boxes.append(box)
                    boxes.remove(box)
                    break

        if not check_total_weight():
            print("Total weight is not 713 kilograms. Boxes will be moved to new locations.")
            found_boxes = []
            boxes = initialize_boxes()