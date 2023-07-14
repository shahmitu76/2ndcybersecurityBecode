class Blackboard:
    """Class defining a surface on which to write,
    that can be read and deleted, by a set of methods. The modified attribute
    is "surface" """

    def __init__(self):
        """By default, our surface is empty"""
        self.__surface = ""

    def write(self, message_written):
        """Method for writing on the surface of the table.
        If the surface is not empty, we skip a line before adding
        the message to be written"""

        if self.__surface != "":
            self.__surface += "\n"
        self.__surface += message_written

    def read(self):
        return print(self.__surface)

board = Blackboard()
board.__surface = "Hello guys"
board.read()