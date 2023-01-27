def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

if __name__ == "main":
  numbers = list(map(int, input("Enter integer number with space: "))) 
  sorted_numbers = insertion_sort(numbers)
  print("Sorted number is", sorted_numbers)