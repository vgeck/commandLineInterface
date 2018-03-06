#!/usr/bin/env python
# encoding: utf-8


__all__ = ["Menu"]

import cli


class Menu(object):
    """
    Simple menu object
    """
    menuCounter = 0
    
    def __init__(self, menu_title=None, level=0):
        """
        Init function of the menu object
        
        Args:
            menuTitel(str): titel of the menu
        """
        self.menu_title = menu_title
        if menu_title == None:
            self.menu_title = ''.join(["Menu - ", str(Menu.menuCounter)])
        
        self.level = level
                
        ## private members
        self.running = False
        
        self.menu_entries = []
        self.menu_keys = []
        
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
#         menu_keys = [menuEntry.key for menuEntry in self.menu_entries]
#         if key in menu_keys:
#             raise KeyError("Key '{}' for menu entry '{}' is already defined, choose another one".format(key, description))
#         
        key = len(self.menu_entries)
        
        # check if callback_function is a submenu and adjust level if necessary
        if isinstance(callback_function, Menu):
            callback_function.set_level(self.level+1)

        # create entry object
        new_entry = cli.MenuEntry(key, description, callback_function, *args, **kwargs)
        # add entry object to list
        self.menu_entries.append(new_entry)

    def add_menu_entry_list(self, menu_list, callback_function, *args, **kwargs):
        """
        Create the full menu from a list of strings.
        The key is an auto-generated number starting with 0.
        The description is equal to the string,
        and the call_back_function is a lambda function returning the choosen string.
        
        Args:
            menu_list(list): list of strings for the menu
        """
        for description in menu_list:
            self.add_menu_entry(description, callback_function, *args, **kwargs)
            
    def add_menu_entry_dict(self, menuDict , *args, **kwargs):
        """
        Create the full menu from a dict like {description: callback_function}.
        The key is an auto-generated number starting with 0.
        
        Args:
            menuDict(dcit): like {description: callback_function} to create the menu
        """
        for description, callback in menuDict.iteritems():
            self.add_menu_entry(description, callback, *args, **kwargs)
        
    def display(self):
        """
        Function to display show the menu in the console
        
        needs to handeld by the console print manager
        """
        
        indent_title = ''.join(['   ' for i in range(self.level)])
        indent_entries = ''.join(['   ' for i in range(self.level+1)])
        # create string 
        display_list = ['\n',''.join([indent_title, self.menu_title]), '\n']
        display_list.extend([''.join([indent_entries,entry.display()]) for entry in self.menu_entries])
        display_output = '\n'.join(display_list)
        
        # push it to stdin handler instance
        print(display_output)
        
    def user_input_int(self):
        '''
        Question user to insert an integer number between min_bound and max_bound
        
        Returns:
            int of user input or cli.baseObjects.Exit() instance if
            exit == True
        '''
        
        indent = ''.join(['   ' for i in range(self.level+1)])
        if self.level == 0:
            question = ''.join([indent,"insert your choice, (q)-quit: "])
        else:
            question = ''.join([indent,"insert your choice, (q)-back: "])
        
        min_bound = 0
        max_bound = len(self.menu_entries)
        appropriate_input_list = [str(int(i+min_bound)) for i in range(max_bound-min_bound)]
        user_input = "NONE"
        appropriate_input_list.append('q')
        
        print("")
        while user_input not in appropriate_input_list:
            user_input = input(question)
        print("")
        
        return user_input
    
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
            self.menu_entries[int(userInput)].callback_function(int(userInput))
            return None
                
    def run(self):
        """
        Function that starts the application
        """        
        self.running = True

        while self.running:
            self.display()
            user_input  = self.user_input_int()
            result_of_do = self.evaluate_user_input(user_input)
            if isinstance(result_of_do, cli.baseObjects.Exit):
                self.running = False
        
    def __call__(self):
        self.run()
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()