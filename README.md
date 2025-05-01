# Leave Request Chain of Responsibility

This project demonstrates the Chain of Responsibility design pattern implemented in Java and translated to Python. The pattern is used to process leave requests through a series of approvers: Supervisor, Manager, and Director. Each approver handles leave requests up to a certain number of days, and if it can't be processed by one, it is passed to the next approver in the chain.

## Design Pattern: Chain of Responsibility

The Chain of Responsibility pattern allows passing a request along a chain of handlers. The request is handled by the first handler that is capable of processing it, avoiding the need for a single class to know all the details about the request. This pattern decouples the sender of the request from its handlers.

## Classes Overview

1. **Approver (Abstract Class)**  
   This is the abstract base class for all approvers. It defines the method `process_leave_request` that must be implemented by all concrete handlers. It also holds a reference to the next approver in the chain.

2. **Supervisor (Concrete Handler)**  
   Handles leave requests up to 3 days. If the leave days are greater than 3, the request is passed to the next approver.

3. **Manager (Concrete Handler)**  
   Handles leave requests up to 7 days. If the leave days are greater than 7, the request is passed to the next approver.

4. **Director (Concrete Handler)**  
   Handles leave requests up to 14 days. If the leave days are greater than 14, the request is denied.

## Example

```python
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
```

Output
```nginx
Employee requests 10 days of leave.
Manager approved the leave.
```
