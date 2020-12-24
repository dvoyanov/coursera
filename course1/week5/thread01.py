from concurrent.futures import ThreadPoolExecutor, as_completed

def f(a):
    return a*a

with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(f, i) for i in range(10)]

    print(results[9].result())
    print(results[8].result())
    print(results[7].result())
    print(results)
    for future in as_completed(results):
        print(future.result())
