def maxim(arr):
    highest = arr[0]
    lowest = arr[0]

    for num in arr[1:]:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    return [lowest, highest]


# Example usage:
arr = [1, 54, 3, 78, 7, 45, 12]
arr1 = [2, 4, 1, 0, 2, -1]
arr2 = [100, -100]

low_high = maxim(arr1)
print("Highest Number is:", low_high[1])
print("Lowest Number is:", low_high[0])
