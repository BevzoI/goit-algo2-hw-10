import random
import time
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

# Ініціалізація кольорового виводу
init(autoreset=True)

# Рандомізований QuickSort (опорний елемент — випадковий)
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Детермінований QuickSort (опорний елемент — середній)
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Вимірювання часу сортування
def measure_time(sort_function, arr, iterations=5):
    times = []
    for _ in range(iterations):
        test_arr = arr.copy()
        start_time = time.time()
        sort_function(test_arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)

# Розміри масивів
sizes = [10_000, 50_000, 100_000, 500_000]
results_randomized = []
results_deterministic = []

# Тестування алгоритмів
for size in sizes:
    test_array = [random.randint(0, 10**6) for _ in range(size)]
    random_time = measure_time(randomized_quick_sort, test_array)
    deterministic_time = measure_time(deterministic_quick_sort, test_array)

    results_randomized.append(random_time)
    results_deterministic.append(deterministic_time)

    # Кольоровий вивід у консоль
    print(Fore.YELLOW + f"Розмір масиву: {size}")
    print(Fore.GREEN + f"   Рандомізований QuickSort: {random_time:.4f} секунд")
    print(Fore.CYAN + f"   Детермінований QuickSort: {deterministic_time:.4f} секунд")

# Побудова та збереження графіка
plt.figure(figsize=(10, 6))
plt.plot(
    sizes, results_randomized, label="Рандомізований QuickSort", marker="o", color="green"
)
plt.plot(
    sizes, results_deterministic, label="Детермінований QuickSort", marker="s", color="blue"
)
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час (секунди)")
plt.title("Порівняння ефективності алгоритмів QuickSort")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Збереження графіка у файл
plt.savefig("quick_sort_comparison.png")

# Показ графіка
plt.show()
