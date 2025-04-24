"""
    The relationships between the classes are as follows:

    Inheritance: Dog and Cat inherit from Animal.

    Realization/Implementation: Dog and Cat implement the Pet interface.

    Aggregation: Person has an aggregation relationship with Pet,
                indicating that a person can have multiple pets.

    Composition: Person has a composition relationship with Address,
                indicating that an address cannot exist without a person.

    Association: Person has an association relationship with Phone,
                indicating that a person can have multiple phone numbers.

    Dependency: Phone depends on the PhoneType enumeration for the phoneType attribute.

    Among the six types of relationships, the code structure of composition,
    aggregation, and association is the same, and it can be understood from
    the strength of the relationship.


    The order from strong to weak is:

    inheritance → implementation → composition → aggregation → association → dependency
"""