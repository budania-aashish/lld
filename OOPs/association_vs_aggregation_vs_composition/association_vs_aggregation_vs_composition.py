"""
    Feature                       Association               Aggregation                       Composition

    Relationship                  Knows-A                   Has-A                             Has-A

    Object Independence	          Objects are               Contained objects can             Contained objects can't
                                  independent               exist independently               exist independently

    Lifetime	                  Objects exist             Contained object outlive          Contained object can't
                                  independently             the container object              live without container
                                                                                              object & destroyed with it

    Example                       Teacher & Student         University & Professor            Car & Engine
"""