def format_training_time(calculations):
    output = ""
    output_array = []
    previous_rounded_value = None

    for (key, value) in calculations.items():
        rounded_value = value_rounding(value)
        if key == 'beginning':
            output_array.append(f"At the {key} of the semester, you wiil be {value_to_time(rounded_value)} \n")
            previous_rounded_value = rounded_value
        else:
            if rounded_value > previous_rounded_value:
                output_array.append(f"When {key} begins, you will become {value_to_time(rounded_value)} \n")
                previous_rounded_value = rounded_value
            elif rounded_value < previous_rounded_value:
                output_array.append(f"When {key} begins, you will drop to {value_to_time(rounded_value)} \n")
                previous_rounded_value = rounded_value

    output = "".join(output_array)

    return output

def value_rounding(value):
    if value >= 1:
        return 1
    elif value >= 0.75:
        return 0.75
    elif value >= 0.5:
        return 0.5
    elif value >= 0.25:
        return 0.25
    else:
        return 0

def value_to_time(value):
    if value == 1:
        return "full-time"
    elif value == 0.75:
        return "3/4-time"
    elif value == 0.5:
        return "half-time"
    elif value == 0.25:
        return "quarter-time"
    else:
        return "less than quarter-time"