def convert_cel_to_far():
    tem = int(input("Enter a temperature in degrees F: "))
    changed_tem = round((tem - 32) * 5/9, 2)
    print(f"{tem} degrees F = {changed_tem} degrees C")
convert_cel_to_far()


def convert_far_to_cel():
    cel = int(input("Enter a temperature in degrees C: "))
    changed_cel = round(cel * 9/5 + 32, 2)
    print(f"{cel} degrees F = {changed_cel} degrees C")
convert_far_to_cel()