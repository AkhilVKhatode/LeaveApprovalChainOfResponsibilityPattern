from abc import ABC, abstractmethod

class Approver(ABC):
    def __init__(self):
        self._next_approver = None

    # Set the next handler in the chain
    def set_next_approver(self, next_approver):
        self._next_approver = next_approver

    # Abstract method to process the leave request
    @abstractmethod
    def process_leave_request(self, leave_days):
        pass


class Supervisor(Approver):
    def process_leave_request(self, leave_days):
        if leave_days <= 3:
            print("Supervisor approved the leave.")
        elif self._next_approver:
            self._next_approver.process_leave_request(leave_days)


class Manager(Approver):
    def process_leave_request(self, leave_days):
        if leave_days <= 7:
            print("Manager approved the leave.")
        elif self._next_approver:
            self._next_approver.process_leave_request(leave_days)


class Director(Approver):
    def process_leave_request(self, leave_days):
        if leave_days <= 14:
            print("Director approved the leave.")
        elif self._next_approver:
            self._next_approver.process_leave_request(leave_days)
        else:
            print("Leave request denied. Too many days!")


# Demo
if __name__ == "__main__":
    # Create handler instances
    supervisor = Supervisor()
    manager = Manager()
    director = Director()

    # Set up the chain: Supervisor -> Manager -> Director
    supervisor.set_next_approver(manager)
    manager.set_next_approver(director)

    # Process a leave request
    leave_days = 10
    print(f"Employee requests {leave_days} days of leave.")
    supervisor.process_leave_request(leave_days)
