def bubble_sort(self, numbers):
  n = len(numbers)
  for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1] :
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
if __name__ == "__main__":
 numbers = list(map(int, input("Enter integer number with space: ")))
 sorted_numbers = bubble_sort(numbers)
 print("Sorted number is", sorted_numbers)