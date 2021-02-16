"""
Author: Eugene Bellau
"""






class My_Obj():
    """
    Title: My_Object
    Description: An object that will define a name and importance level
    Arguments: self.name and self.importance
    Returns: The object will return the defined name and importance level
    """

    def __init__(self, name, importance):
        self.name = name
        self.importance = importance

    def show(self):
        print(self.name, self.importance)

    def mod_name(self, name):
        self.name = name
