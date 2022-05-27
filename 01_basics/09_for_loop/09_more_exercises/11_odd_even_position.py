import sys
count_num = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

if count_num > 0:
    for position in range(1, count_num + 1):
        num = float(input())
        if position % 2 == 0:
            even_sum += num
            if num < even_min:
                even_min = num
            if num > even_max:
                even_max = num

        else:
            odd_sum += num
            if num < odd_min:
                odd_min = num
            if num > odd_max:
                odd_max = num

    print(f"OddSum={odd_sum:.2f},")
    if odd_min == sys.maxsize and odd_max == -sys.maxsize:
        print(f"OddMin=No,")
        print(f"OddMax=No,")
    else:
        print(f"OddMin={odd_min:.2f},")
        print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    if even_min == sys.maxsize and even_max == -sys.maxsize:
        print(f"EvenMin=No,")
        print(f"EvenMax=No")
    else:
        print(f"EvenMin={even_min:.2f},")
        print(f"EvenMax={even_max:.2f}")

else:
    print(f"OddSum=0.00,")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum=0.00,")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
