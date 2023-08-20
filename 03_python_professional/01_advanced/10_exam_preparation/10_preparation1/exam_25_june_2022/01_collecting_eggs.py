from collections import deque

eggs = deque(map(int, input().split(', ')))
papers = deque(map(int, input().split(', ')))
box_size = 50
count_boxes = 0
bad_luck_egg = 13

while eggs and papers:
    current_egg = eggs[0]
    current_paper = papers[-1]

    if current_egg <= 0:
        eggs.popleft()

    elif current_egg == bad_luck_egg:
        eggs.popleft()
        paper_1 = papers.popleft()
        paper_2 = papers.pop()
        papers.append(paper_1)
        papers.appendleft(paper_2)

    elif current_egg + current_paper <= 50:
        count_boxes += 1
        eggs.popleft()
        papers.pop()

    else:
        eggs.popleft()
        papers.pop()

if count_boxes > 0:
    print(f"Great! You filled {count_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(list(map(str, eggs)))}")
if papers:
    print(f"Pieces of paper left: {', '.join(list(map(str, papers)))}")
