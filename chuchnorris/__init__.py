import schedule
import time
from .jokescript.retrievejokes import jokes

def run_jokes_collector():
    jokes_random = jokes()
    jokes_final = jokes_random.run()
    return jokes_final
   

def main():
    print("starting with jokes...!")
    schedule.every(6).seconds.do(run_jokes_collector)

    while True:
        schedule.run_pending()
        time.sleep(1)
        

if __name__ == "__main__":
   main()
