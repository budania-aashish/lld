"""
    1. Class:

    A class is a blueprint or template that defines the properties and behavior of an object.

            BankAccount

    - account_number : string
    # balance : double

    + deposit (amount : double) :: void
    + withdraw (amount: double) :: void
    - update_balance (amount: double) :: void
    ~ get_account_info() :: string


    Represented as rectangles, classes are divided into three compartments:


    Name (top compartment): The unique identifier of the class (e.g., BankAccount).

    Attributes (middle compartment): The properties or data associated with the class
                                     (e.g., accountNumber, balance).

    Operations (bottom compartment): The actions or methods that can be performed by objects of the class
                                    (e.g., deposit(), updateBalance()).


    Visibility Markers: Visibility markers indicate the accessibility of attributes and methods within a class.

    + (Public): The attribute or method is accessible from any class.

    - (Private): The attribute or method is only accessible within the same class.

    # (Protected): The attribute or method is accessible within the same class and its subclasses.

    ~ (Package): The attribute or method is accessible within the same package.

"""