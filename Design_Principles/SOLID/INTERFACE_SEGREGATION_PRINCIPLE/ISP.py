"""
    No client should be forced to depend on interfaces they don't use.

    The main idea behind ISP is to prevent the creation of "fat" or "bloated"
    interfaces that include methods that are not required by all clients.

    By segregating interfaces into smaller, more specific ones, clients only
    depend on the methods they actually need, promoting loose coupling and better
    code organization.

"""