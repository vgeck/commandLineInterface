#!/usr/bin/env python
# encoding: utf-8


def foo():
    print "foo"
    
def bar():
    print "bar"

def printName(name):
    name = name[0][0]
    print "your name is {}".format(name)
    
def enterYourName(name):
    input = raw_input("enter your name: ")
    name[0][0] = input

def indexedCallback(args, kwargs):
    
    inputList = args[0]
    userInput = kwargs['userInput'] # this is the way to get the user input
    
    print "you choosed ", inputList[userInput]
    
    
    
if __name__ == "__main__":
    
    import cli
        
    foobarMenu = cli.Menu('Das Foobar Menü')
    foobarMenu.add_menu_entry('print foo', foo)
    foobarMenu.add_menu_entry('print bar', bar)
    
        
    myName = ["Vinzenz"]
    
    enterNameMenu = cli.Menu('Das Enter Name Menü')
    enterNameMenu.add_menu_entry('print my name', printName, myName)
    enterNameMenu.add_menu_entry('enter your name', enterYourName, myName)
    
    
    listMenu = cli.Menu('Das Test List Menü')
    
    inputList = ['test1', 'test2' , 'test3']
    listMenu.add_menu_entry_list(inputList, indexedCallback, inputList, userInput = 0)  # this is the way to forward the user input to the callback function
    
      
    hauptmenu = cli.Menu('Mein Hauptmenü')
    hauptmenu.add_menu_entry('open foo bar menu', foobarMenu)
    hauptmenu.add_menu_entry('open enter-name menu', enterNameMenu)
    hauptmenu.add_menu_entry('open list menu', listMenu)
            
    hauptmenu.run()        
    