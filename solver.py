import time

from driver import Driver

class SquarewordSolver:
    def __init__(self, driver):
        self.driver = driver

    def solve(self, first_guess="moist"):
        self.driver.submit_guess(first_guess)

if __name__ == '__main__':
    with Driver() as driver:
        solver = SquarewordSolver(driver)
        solved_data = solver.solve()
        time.sleep(5)
