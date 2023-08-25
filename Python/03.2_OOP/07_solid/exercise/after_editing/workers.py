from abc import ABC, abstractmethod


class AverageWorker(ABC):

    @abstractmethod
    def work(self):
        pass


class Worker(AverageWorker):
    def work(self):
        print("I'm working!!")


class LazyWorker(AverageWorker):
    def work(self):
        print("I pretend to work.. Doesn't mean I'm lazy!!!")


class QuickWorker(AverageWorker):
    def work(self):
        print("I could help someone with their project because I have completed my tasks.")


class SuperWorker(AverageWorker):
    def work(self):
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, AverageWorker):
            raise AssertionError(f"`worker` must be of type {AverageWorker}")

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

quick_worker = QuickWorker()
lazy_worker = LazyWorker()
super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()

    manager.set_worker(quick_worker) # бонус тест
    manager.manage()

    manager.set_worker(lazy_worker) # бонус тест
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
