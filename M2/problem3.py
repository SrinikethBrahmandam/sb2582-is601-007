a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value
    output_tuples = []

    # Iterate through the input array
    for item in arr:
        # Check the datatype of the input item
        item_type = type(item)

        # Convert the item to its positive version while preserving datatype
        if item_type in (int, float):
            positive_item = abs(item)
        elif item_type == str:
            try:
                # Attempt to convert the string to a numeric type and then take its absolute value
                numeric_item = eval(item)
                positive_item = abs(numeric_item)
            except (ValueError, SyntaxError):
                # If conversion to a numeric type fails, keep the original string
                positive_item = item
        else:
            # If the datatype is not supported, keep the original item
            positive_item = item

        # Append a tuple of (original value, positive value) to the output list
        output_tuples.append((item, positive_item))

    # Print the output values and their corresponding data values
    for original_value, positive_value in output_tuples:
        print("Data Value: {}, Positive Value: {}".format(original_value, positive_value))

print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)