#!/usr/bin/env python
# encoding: utf-8


__all__ = ["Menu"]

import cli

class Menu(object):
    """
    Simple menu object
    """
    menuCounter = 0
    
    def __init__(self, menuTitle = None, level = 0):
        """
        Init function of the menu object
        
        Args:
            menuTitel(str): titel of the menu
        """
        self.menuTitle = menuTitle
        if menuTitle == None:
            self.menuTitle = ''.join(["Menu - ",str(Menu.menuCounter)])
        
        self.level = level
                
        ## private members
        self.running = False
        
        self.menuEntries = []
        self.menuKeys    = []
        
        Menu.menuCounter =+ 1
        
    def set_level(self, level):
        """
        setter for the nested level of the menu
        
        Args: level(int): nested level of the menu
        """
        self.level = level
        
        
    def add_menu_entry(self, description, callback_function, *args, **kwargs):
        """
        Args:
            description(str): descriptive text of the menu entry
            call_back_function(function): call back function to envole if menu entry is triggered
        
        """
#         if keys are needed
#         # check if key in menu keys
#         menuKeys = [menuEntry.key for menuEntry in self.menuEntries]
#         if key in menuKeys:
#             raise KeyError("Key '{}' for menu entry '{}' is already defined, choose another one".format(key, description))
#         
        key = len(self.menuEntries)
        
        # check if callback_function is a submenu and adjust level if necessary
        if isinstance(callback_function,Menu):
            callback_function.set_level(self.level+1)
            
        # create entry object
        newEntry = cli.MenuEntry(key, description, callback_function, *args, **kwargs)
        # add entry object to list
        self.menuEntries.append(newEntry)
        
        
    def add_menu_entry_list(self, menuList, callback_function, *args, **kwargs):
        """
        Create the full menu from a list of strings.
        The key is an auto-generated number starting with 0.
        The description is equal to the string,
        and the call_back_function is a lambda function returning the choosen string.
        
        Args:
            menuList(list): list of strings for the menu
        """
        for description in menuList:
            self.add_menu_entry(description, callback_function, *args, **kwargs)
            
    def add_menu_entry_dict(self, menuDict , *args, **kwargs):
        """
        Create the full menu from a dict like {description: callback_function}.
        The key is an auto-generated number starting with 0.
        
        Args:
            menuDict(dcit): like {description: callback_function} to create the menu
        """
        for description,callback in menuDict.iteritems():
            self.add_menu_entry(description, callback, *args, **kwargs)
        
    def display(self):
        """
        Function to display show the menu in the console
        
        needs to handeld by the console print manager
        """
        
        indentTitle = ''.join(['   ' for i in xrange(self.level)])
        indentEntries = ''.join(['   ' for i in xrange(self.level+1)])
        # create string 
        displayList = ['\n',''.join([indentTitle,self.menuTitle]),'\n']
        displayList.extend([''.join([indentEntries,entry.display()]) for entry in self.menuEntries])
        displayOutput = '\n'.join(displayList)
        
        # push it to stdin handler instance
        print displayOutput
        
    def user_input_int(self):
        '''
        Question user to isert an integer number between minBound and maxBound
        
        Returns:
            int of user input or cli.baseObjects.Exit() instance if
            exit == True
        '''
        
        indent = ''.join(['   ' for i in xrange(self.level+1)])
        if self.level == 0:
            question = ''.join([indent,"insert your choice, (q)-quit: "])
        else:
            question = ''.join([indent,"insert your choice, (q)-back: "])
        
        minBound = 0
        maxBound = len(self.menuEntries)
        appropriateInputList = [str(int(i+minBound)) for i in xrange(maxBound-minBound)]
        userInput = "NONE"
        appropriateInputList.append('q')
        
        print ""
        while userInput not in appropriateInputList:
            userInput = raw_input(question)
        print ""
        
        return userInput
    
    def evaluate_user_input(self, userInput):
        """
        Function to evaluate the user input
        
        Args: userInput(str): string object of user input
        
        Returns:
            instance of cli.baseObjects.Exit() if userInput == q
            None elsewise
        """
        
        if userInput == 'q':
            return cli.baseObjects.Exit()
        else:
            self.menuEntries[int(userInput)].callback_function(int(userInput))
            return None
                
    def run(self):
        """
        Function that starts the application
        """        
        self.running = True
        while self.running == True:
            self.display()
            userInput  = self.user_input_int()
            resultOfDo = self.evaluate_user_input(userInput)
            if isinstance(resultOfDo, cli.baseObjects.Exit):
                self.running = False
        
    def __call__(self):
        self.run()
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()