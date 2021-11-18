# Define the functions
def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight


def cal_ave_weight(beep_weight, bop_weight):
    average_weight = beep_weight + bop_weight / 2
    return average_weight


def run():
    print("What is Beep's weight?")
    beep_weight = float(input())
    print("What is Bop's weight")
    bop_weight = float(input())
    print("What would you like to calculate? (sum or average)")
    action = input()

    if action == 'sum':
        answer = sum_weights(beep_weight, bop_weight)
        print(f"The total weight is {answer:.2f}")
    elif action == 'average':
        answer = cal_ave_weight(beep_weight, bop_weight)
        print(f"The average weight is {answer:.2f}")
    else:
        print("I don't know how to do that")


# Call the run function
run()
