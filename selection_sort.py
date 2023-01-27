def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "main":
  numbers = list(map(int, input("Enter integer number with space: "))) 
  sorted_numbers = selection_sort(numbers)
  print("Sorted number is", sorted_numbers)