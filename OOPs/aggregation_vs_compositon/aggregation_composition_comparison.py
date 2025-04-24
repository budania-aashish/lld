"""
    Both of these have Has-A [relationship]

    In Aggregation contained object can live without container object. [Ownership]
    In Composition contained object can't live without container object. [Ownership]

    In Aggregation lifecycle of contained object can be more than container object. [LifeCycle]
    In Composition lifecycle of contained object is finished with container object. [LifeCycle]

    Example : University & Professors [Aggregation]
            : Car & Engine [Composition]


    When to use aggregation
    - Promotes Code Reusability - aggregated objects can be used at multiple places without getting
                                  tightly coupled to the container class
    - Encourages Loose Coupling - aggregation allows objects to interact independently without affecting
                                  the lifecycle of the other objects
    - Better maintainability -    changes in one class doesn't heavily affect the other class, keeping
                                  the code easier to modify/extend
    - Real Word Applications -    Many of the use cases including schools & teachers, company and employees
                                  already fit to the aggregation model 

"""