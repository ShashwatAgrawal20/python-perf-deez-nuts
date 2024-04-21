import random
import timeit


def using_dict_fromkeys(setup_arr):
    return list(dict.fromkeys(setup_arr).keys())


def using_dict_fromkeys_without_keys(setup_arr):
    return list(dict.fromkeys(setup_arr))


def using_classing_loop_with_set(setup_arr):
    new_a = []
    seen = set()
    for i in setup_arr:
        if i in seen:
            continue
        new_a.append(i)
        seen.add(i)
    return new_a


def using_classing_loop(setup_arr):
    new_a = []
    for i in setup_arr:
        if i not in new_a:
            new_a.append(i)
    return new_a


a = []
for i in range(1000000):
    a.append(random.randint(0, 50))
print("loop done")


# let the benchmark begin
dict_time = timeit.timeit(
    'using_dict_fromkeys(a)', globals=globals(), number=100
)
print(f"Time using_dict_fromkeys: {dict_time} seconds")


dict_time = timeit.timeit(
    'using_dict_fromkeys_without_keys(a)', globals=globals(), number=100
)
print(f"Time using_dict_fromkeys_without_keys: {dict_time} seconds")


dict_time = timeit.timeit(
    'using_classing_loop_with_set(a)', globals=globals(), number=100
)
print(f"Time using_classing_loop_with_set: {dict_time} seconds")


loop_time = timeit.timeit(
    'using_classing_loop(a)', globals=globals(), number=100
)
print(f"Time using_classing_loop: {loop_time} seconds")
