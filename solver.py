import time

from driver import Driver

def main():
    with Driver() as driver:
        driver.submit_guess("moist")
        time.sleep(5)

if __name__ == '__main__':
    main()
