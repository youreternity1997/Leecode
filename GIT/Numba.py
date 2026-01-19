import time
from numba import jit

def slow_function(x):
    total = 0
    for i in range(x):
        total += i ** 2
    return total


@jit(nopython=True)  # JIT 編譯成機器碼
def fast_function(x):
    total = 0
    for i in range(x):
        total += i ** 2
    return total

t1 = time.time()
result = slow_function(1000000)
t2 = time.time()
print("Slow Time:", t2 - t1)

# 第一次調用會編譯，之後會非常快 # 預熱
t1 = time.time()
result = fast_function(1000000)
t2 = time.time()
print("Fast Time:", t2 - t1)


# 更好的方法：多次測試取平均
print("\n=== 多次測試 ===")
import statistics
slow_times = []
fast_times = []
for _ in range(10):
    t1 = time.perf_counter()  # 高精度計時器
    slow_function(1000000)
    slow_times.append(time.perf_counter() - t1)
    
    t1 = time.perf_counter()
    fast_function(1000000)
    fast_times.append(time.perf_counter() - t1)

print("slow_times=", [f"{t:.6f}" for t in slow_times])
print("fast_times=", [f"{t:.6f}" for t in fast_times])
print(f"\nSlow avg: {statistics.mean(slow_times):.6f}s")
print(f"Fast avg: {statistics.mean(fast_times):.6f}s")
print(f"Speedup: {statistics.mean(slow_times) / statistics.mean(fast_times):.2f}x")