def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def main():
    # Input a list of numbers
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        unsorted_list = [int(num) for num in input_str.split()]
    except ValueError:
        print("Invalid input. Please enter a list of numbers.")
        return

    # Call the heap_sort function to sort the list
    heap_sort(unsorted_list)

    # Display the sorted list
    print("Sorted List:", unsorted_list)

if __name__ == "__main__":
    main()
