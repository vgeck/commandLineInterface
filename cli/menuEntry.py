#!/usr/bin/env python
# encoding: utf-8


__all__ = ["MenuEntry"]

class MenuEntry(object):
    """
    Simple menu object with key, description and callback function
    """
    
    def __init__(self, key, description, callback_function, *args, **kwargs):
        """
        Class for menu entries
        
        Args:
            key(str): key of the menu entry, input of key will trigger the callback_function
            description(str): descriptive text of the menu entry
            callback_function(function): call back function to envole if menu entry is triggered
        
        """
        self.key = key
        self.description = description
        self.callback = callback_function
    
        self.args = args
        self.kwargs = kwargs
    
    def callback_function(self, userInput):
        """
        
        """        
        if "userInput" in self.kwargs:
            self.kwargs['userInput'] = userInput 
                
        if self.args and self.kwargs:
            self.callback(self.args, self.kwargs)
        elif self.args:
            self.callback(self.args)
        elif self.kwargs:
            self.callback(self.kwargs)
        else:
            self.callback()
    
    def display(self):
        """
        Function which returns as string to display the menu entry
                
        Retruns
        
        """
        return "[ {:2} ] - {}".format(self.key,self.description)        
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()