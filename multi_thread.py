from time import sleep, perf_counter
from threading import Thread


def task():
    print('Starting a task...')
    sleep(1)
    print('done')


start_time = perf_counter()

# create two new threads
t1 = Thread(target=task)
t2 = Thread(target=task)
t3 = Thread(target=task)
t4 = Thread(target=task)
# start the threads
t1.start()
t2.start()
t3.start()
t4.start()

# wait for the threads to complete
t1.join()
t2.join()
t3.join()
t4.join()


end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')