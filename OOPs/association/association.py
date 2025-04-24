"""
    Association: a fundamental principle defining relationship between two or more objects

    It represents how objects interact with each other without depending on one-another.

    Association is not inheritance rather it's a way of communication between objects staying loosely coupled.

    Association is a connection between two classes, where one class is linked to another.

    It can be one to one, one to many, many to one, many to many.

    Key Characteristics of Association:
        - represents Uses-A and Knows-A relationship.
        - objects in association can exist independently.
        - can be unidirectional or bidirectional
        - Promotes modularity and code reusability

    Why to use Association:
        - Promotes Code Reusability : objects can be used across multiple associations without duplication
        - Encourages Loop Coupling : object interact with each other without interacting with internal implementation
        - Improves Maintainability : changing one object doesn't heavily impact others, making code easier to manage
        - Better System Design : Allows modeling of real-world relationships between entities effectively 
"""