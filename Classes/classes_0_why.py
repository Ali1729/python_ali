def horn(num_of_wheels, kind):
    if num_of_wheels > 10 and num_of_wheels < 20 and kind == "truck":
        print("big_horn")

    if num_of_wheels > 20 and kind == "train":
        print("Train chugga chugga choo choo")

    if num_of_wheels > 20 and kind == "train":
        print("Train chugga chugga choo choo")

    if num_of_wheels <= 10 and num_of_wheels > 5:
        print("air horn")

    if num_of_wheels < 4 and num_of_wheels > 2:
        print("small horn")

    if num_of_wheels > 0 and num_of_wheels <= 2:
        print("bike horn")


def print_color_hex(color, kind):
    if kind == "truck" and color == "blue":
        print("Truck is in blue color")


truck = {"kind": "truck", "wheels": 10}
horn(truck["wheels"], truck["kind"])


list1= [1,2,3,4]

truck.horn

horn(truck)