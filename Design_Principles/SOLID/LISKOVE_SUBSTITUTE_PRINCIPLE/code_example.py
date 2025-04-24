class Vehicle:
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("starting car engine...")


class Bike(Vehicle):
    def start_engine(self):
        pass  # doesn't make sense for Bike to have start engine method's implementation


"""
    In this example, the Bicycle class violates the LSP because it provides an implementation
    for the start_engine method, which doesn't make sense for a bicycle.
    
    If we try to substitute a Bicycle instance where a Vehicle instance is expected,
    it might lead to unexpected behavior or errors.
    
"""


class Vehicle:
    def start(self):
        raise NotImplementedError


class Car(Vehicle):
    def start(self):
        print("Starts car engine")


class Bike(Vehicle):
    def start(self):
        print("Paddling the cycle")


"""
    Here, we've replaced the start_engine method with a more general start method in the base class Vehicle. 
    The Car class implements the start method to start the engine, while the Bicycle class implements the start
    method to indicate that the rider is pedaling.
    
    Now, instances of Car and Bicycle can be safely substituted for instances of Vehicle without any unexpected 
    behavior or errors.
    
"""
