import random
import time


def name_gen():
    name = ''
    for i in range(5):
        name += str(random.randint(0,9))
    name += '.py'
    return name


file_name = name_gen
count = 1
OE = 'Odd'
with open(name_gen(), "x") as file:
    file.write(f"num = 69\n"
               f"if num == {count}:\n"
               f"   print(\"{OE}\")\n")
    start_time = time.perf_counter()
    for i in range(99999):
        if count % 2 == 0:
            OE = 'Even'
        else:
            OE = 'Odd'
        file.write(f"elif num == {count}:\n"
                   f"   print(\"{OE}\")\n")
        count += 1
    end_time = time.perf_counter()
    timer = end_time - start_time
    print(f"Took {timer:.5f} Sec")
