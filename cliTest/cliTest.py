#!/usr/bin/env python
# encoding: utf-8


def foo():
    print("foo")


def bar():
    print("bar")


def print_name(name):
    name = name[0][0]
    print("your name is {}".format(name))


def enter_your_name(name):
    user_input = input("enter your name: ")
    name[0][0] = user_input


def indexed_callback(args, kwargs):
    input_list = args[0]
    user_input = kwargs['user_input']  # this is the way to get the user input
    
    print(f"you choosed {input_list[user_input]}")
    

if __name__ == "__main__":
    
    import cli
        
    foobar_menu = cli.Menu('The foobar menu')
    foobar_menu.add_menu_entry('print foo', foo)
    foobar_menu.add_menu_entry('print bar', bar)

    my_name = ["vgeck"]

    enter_name_menu = cli.Menu('the name menu')
    enter_name_menu.add_menu_entry('print my name', print_name, my_name)
    enter_name_menu.add_menu_entry('enter your name', enter_your_name, my_name)
    
    list_menu = cli.Menu('the test list menu')
    
    input_list = ['test1', 'test2' , 'test3']
    list_menu.add_menu_entry_list(input_list, indexed_callback, input_list, user_input=0)  # this is the way to forward the user input to the callback function

    main_menu = cli.Menu('The main menu')
    main_menu.add_menu_entry('open foo bar menu', foobar_menu)
    main_menu.add_menu_entry('open enter-name menu', enter_name_menu)
    main_menu.add_menu_entry('open list menu', list_menu)
            
    main_menu.run()
    