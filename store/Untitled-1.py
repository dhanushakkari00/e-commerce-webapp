def getOutlierValue(arr):
    # Initialize a variable to store the smallest valid outlier
    smallest_outlier = None

    # Iterate over each number in the array
    for index, potential_outlier in enumerate(arr):
        # Calculate the sum of the array excluding the potential outlier
        remaining_sum = sum(arr) - potential_outlier

        # Create a copy of the array excluding the potential outlier
        reduced_array = arr[:index] + arr[index+1:]

        # Check if the sum of the remaining elements is equal to any of the remaining numbers
        if remaining_sum in reduced_array:
            # If this number meets the criteria and is smaller than the previously found, update it
            if smallest_outlier is None or potential_outlier < smallest_outlier:
                smallest_outlier = potential_outlier

    # Return the smallest outlier found or -1 if no valid outlier exists
    return smallest_outlier if smallest_outlier is not None else -1

def main():
    # Number of test cases
    num_cases = int(input("Enter the number of test cases: "))

    for _ in range(num_cases):
        # Number of elements in the array
        n = int(input("Enter the number of elements: "))
        arr = list(map(int, input("Enter the elements separated by space: ").split()))
        
        # Get the outlier value for the current array
        outlier = getOutlierValue(arr)
        print("The smallest outlier is:", outlier)

if __name__ == "__main__":
    main()
