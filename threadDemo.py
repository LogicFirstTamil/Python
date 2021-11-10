import threading
import time


def update_db():
    print("Updating db...")
    time.sleep(5)
    print("Updated db")


def display_nums(num):
    for i in range(1, num + 1):
        print(i)

# update_db()
thread_db = threading.Thread(target=update_db)
thread_db.start()

display_nums(100)

print(threading.active_count())
print(threading.enumerate())

thread_db.join()
print("Bye")
