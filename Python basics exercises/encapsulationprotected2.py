class Blackboard:
    """Class defining a surface on which to write,
    that can be read and deleted, by a set of methods. The modified attribute
    is "surface" """

    def __init__(self):
        """By default, our surface is empty"""
        self._surface = ""

    def write(self, message_written):
        """Method for writing on the surface of the table.
        If the surface is not empty, we skip a line before adding
        the message to be written"""

        if self._surface != "":
            self._surface += "\n"
        self._surface += message_written

    def read(self):
        return print(self._surface)
board = Blackboard()
board.write("another message")
board._surface = "Hello guys"
board.read()
     