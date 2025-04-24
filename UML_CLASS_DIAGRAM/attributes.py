"""
    2. Attribute:

    Attributes in a UML class diagram represent the properties or data fields of a class.

    Attributes are typically written in the format:

    visibility name: type [multiplicity] = defaultValue

    Name: The name of the attribute.

    Type: The data type of the attribute.

    Multiplicity: (Optional) Indicates how many instances of the type are allowed.

    Default Value: (Optional) The initial value of the attribute.

    - name : string
    # age : int
    + email : string [0..1]
    ~ phone_number : string = "+1-555-666-9999"

"""