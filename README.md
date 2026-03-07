# Algo Programming Assignment 2
# Cache Eviction Policy Simulator

## Team Members
* Carlo Fraley (Enter UFID later)
* 

## Compilation & Execution
[Add instructions later once completed]

## Assumptions
* **Environment:** The scripts are written in Python 3. It utilizes f-strings for the terminal output, so it is assumed the testing environment is running on a similar version.
* **Dependencies:** The code uses only standard Python libraries (`sys`). There are no external packages/installations required.
* **Input Formatting:** The input file contains only valid, whitespace-separated integers. It assumes the first integer is the cache capacity `k`, the second integer is the total number of requests `m`, and all subsequent integers are the request sequence.
* **OPTFF Tie-Breaking:** If the cache is full and the OPTFF algorithm identifies multiple items in the cache that will never be requested again, it assumes evicting any of those items is equally optimal, and it simply evicts the first one it finds.

## Written Solutions

### Question 1: Empirical Comparison

| Input File | k | m | FIFO | LRU | OPTFF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| File1.in | 3 | 50 | 50 | 50 | 19 |
| File2.in | 8 | 50 | 48 | 48 | 32 |
| File3.in | 12 | 50 | 35 | 30 | 20 |

**Does OPTFF have the fewest misses?**
Yes, OPTFF has the fewest misses across all three test files. This was expected since it is the optimal algorithm that can see ahead. It looks ahead at the future request sequence to make the best eviction choice, meaning it is impossible for LRU or FIFO to beat it.

**How does FIFO compare to LRU?**
In File 3, where numbers are grouped and repeated near each other, LRU performs noticeably better than FIFO (30 vs 35 misses). However, in File 1 (a repeating loop larger than the cache) and File 2 (mostly random requests), LRU and FIFO perform identically because the recent past doesn't offer a predictable advantage for those specific sequences. In many real world scenarios where recently used items are more likely to be frequently used, LRU would do better.

---

### Question 2: Bad Sequence for LRU or FIFO

**Sequence:** `1, 2, 3, 4, 1` with a cache capacity of `k = 3` (look at question2.in and question2.out files).

* **LRU Miss Count:** 5
* **OPTFF Miss Count:** 4

**Explanation:**
In this sequence, LRU misses on every single request. When the cache becomes full `[1, 2, 3]` and `4` is requested, LRU evicts `1` because it is the oldest. Then, the next request is `1`, causing another miss. OPTFF incurs strictly fewer misses because it looks ahead. When `4` is requested, OPTFF looks into the future array and sees that `1` will be needed next, but `2` and `3` will never be used again. Therefore, it evicts `2` (or it could also do `3`), keeping `1` safely in the cache. When `1` is called on the final step, OPTFF registers a hit.