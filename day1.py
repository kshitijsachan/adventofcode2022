# %%
with open("task/day1.txt") as f:
    max_cnt = 0
    curr_cnt = 0
    for line in f:
        line = line.strip()
        # print(line)
        if line == "":
            max_cnt = max(max_cnt, curr_cnt)
            curr_cnt = 0
        else:
            curr_cnt += int(line)

    max_cnt = max(max_cnt, curr_cnt)
    print(max_cnt)
    # print()

# %%
import heapq

with open("task/day1.txt") as f:
    max_cnts = []
    curr_cnt = 0
    for line in f:
        line = line.strip()
        # print(line)
        if line == "":
            heapq.heappush(max_cnts, curr_cnt)
            if len(max_cnts) > 3:
                heapq.heappop(max_cnts)
            curr_cnt = 0
        else:
            curr_cnt += int(line)

    heapq.heappush(max_cnts, curr_cnt)
    if len(max_cnts) > 3:
        heapq.heappop(max_cnts)
    print(sum(max_cnts))
