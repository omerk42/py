from colorama import init, Fore, Back, Style

init(autoreset=True)

flag = True
flag1 = True
list = []



    
def exit(f):
    f = False
    print(SucssColor(" changes been saved "))
    return f

def show():
    print(list)

##////////////////////////////////////        ///////////////////////////////////////
## \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ STYLE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##////////////////////////////////////        ///////////////////////////////////////
def ElementColor(e):
    return Fore.BLUE + e + Fore.RESET

def IndexColor(e):
    return Fore.MAGENTA + str(e) + Fore.RESET    

def SucssColor(self):
        return Fore.GREEN + self + Fore.RESET +"\n"

def FailColor(self):
        return Fore.RED + self + Fore.RESET +"\n"

def space():
    print("  ")

def testC():
    print( Fore.BLUE + 'TEST')
    print( Fore.BLACK + 'TEST')        
    print( Fore.CYAN + 'TEST')
    print( Fore.GREEN + 'TEST')
    print( Fore.LIGHTBLACK_EX + Back.LIGHTBLUE_EX + Style.BRIGHT + 'TEST' )
    print( Fore.LIGHTBLUE_EX + 'TEST')
    print( Fore.LIGHTCYAN_EX + 'TEST')
    print( Fore.LIGHTBLUE_EX + 'TEST')
    print( Fore.LIGHTGREEN_EX + 'TEST')
    print( Fore.WHITE + 'TEST')
    print( Fore.YELLOW + 'TEST')
##////////////////////////////////////        ///////////////////////////////////////
## \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ENTER \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##////////////////////////////////////        ///////////////////////////////////////
def enter_element_to_begin(ls,E):
    ls.insert(0, E)
    print(ElementColor(E), "has been added to begin of list ")
    space()

def enter_element_by_index(ls,Ei,E):
    try:
        ls.insert(int(Ei), E)
        print(ElementColor(E), "has been added to {} index of list ".format(IndexColor(Ei)))
    except ValueError as error:
        print (error)  
        print ("index cannot be string")  
        space()

def enter_element_to_end(ls,E):
    ls.append(E)
    print(ElementColor(E), " has been added to end of list ")
    space()
##////////////////////////////////////        ///////////////////////////////////////
## \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ REMOVE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##////////////////////////////////////        ///////////////////////////////////////
def remove_element_from_begin(ls):
    try: 
        print(" the element {} been deleted from beginning of list".format(ElementColor(ls[0])))
        ls.pop(0)
    except IndexError as error:
        print(error)
        print(FailColor("there is no elements in list"))   
        space()

def remove_element_from_index(ls,Ei):
    try:
        print(" element with value {} in {} index been deleted".format(ElementColor(ls[int(Ei)]), IndexColor(Ei)))
        del list[int(Ei)]
    except IndexError as error:
        print(error)
        print(FailColor("there is no elements in that index"))   
        space()

def remove_element_by_value(ls,E):
    try:
        print(" the element {} been deleted from {} index ".format(ElementColor(E), IndexColor(ls.index(E))))
        ls.remove(E)
    except ValueError as error:
        print(error)
        print(FailColor("the element {} is not on list".format(ElementColor(E))))   
        space()  

def remove_element_from_end(ls):
    try:
        print(" the element with value {} in end of list been delete".format(ElementColor(ls[len(ls) - 1])))
        list.pop(len(ls) - 1)
    except IndexError as error:
        print(error)
        print(FailColor("there is no elements in the list"))

def remove_whole_list(ls):
    if len(ls) < 1:
        print(FailColor("there is no elements in the list"))
    else:
        ls.clear()
        print(" all elements in the list has been deleted")
        



  # TODO add list to view in all time   
  


while flag == True:
    show()
    print(" Enter num of operation ")
    print(" (1) enter element to list")
    print(" (2) remove element from list")
    print(" (3) edit element in list")
    print(" (4) information about list")
    print(" (5) Exit")
    OP0 = input()
    space()

    if int(OP0) == 1:
        flag1 = True
        while flag1 == True:
            show()
            print("Select type of insert")
            print(" (1) enter element to begin")
            print(" (2) enter element by index")
            print(" (3) enter element in end")
            print(" (4) Exit")
            OP1 = input()
            space()

            if int(OP1) == 1:
                Eb = input(" enter the element to enter ")
                enter_element_to_begin(list,Eb)

            elif int(OP1) == 2:
                Ei = input(" enter index ")
                Eie = input(" enter element to enter ")
                enter_element_by_index(list,Ei,Eie)

            elif int(OP1) == 3:
                Ee = input(" enter the element to enter ")
                enter_element_to_end(list,Ee)
                
            elif int(OP1) == 4:
                flag1 = exit(flag1)

    elif int(OP0) == 2:
        flag1 = True
        while flag1 == True:
            show()
            print("Select type of remove")
            print(" (1) remove element from begin")
            print(" (2) remove element by index")
            print(" (3) remove element by type it")
            print(" (4) remove element from end")
            print(" (5) remove whole list ")
            print(" (6) Exit")
            OP2 = input()
            space()

            # TODO are u sure massge

            if int(OP2) == 1:
                remove_element_from_begin(list)
                
            elif int(OP2) == 2:
                Ei = input(" enter index ")
                remove_element_from_index(list,Ei)
                
            elif int(OP2) == 3:
                E = input(" enter the element to delete ")
                remove_element_by_value(list,E) 

            elif int(OP2) == 4:
                remove_element_from_end(list)

            elif int(OP2) == 5:
                remove_whole_list(list)
                
            elif int(OP2) == 6:
                flag1 = exit(flag1)

    elif int(OP0) == 3:
        flag1 = True
        while flag1 == True:
            show()
            print("Select type of edit")
            print(" (1) edit index of element")
            print(" (2) edit value of index ")
            print(" (3) reverse whole list ")
            print(" (4) sort whole list ")
            print(" (5) Exit")
            OP3 = input()

            if int(OP3) == 1:
            # TODO remove from first index    
                eie = input(" enter element ")
                if eie not in list:
                    print(" %s is not in the list " % (Back.BLACK + Fore.RED + str(eie)))
                    continue
                eii = list.index(eie)
                print(" the element {} is in the {} index of the list ".format(Fore.BLUE + eie + Style.RESET_ALL , Fore.GREEN + str(eii) + Style.RESET_ALL))
                eiiu = input('enter index to transfer {} to '.format(Fore.BLUE + eie + Style.RESET_ALL))
                list.insert(int(eiiu), eie)
                print(" the element {} been transfer to {} index of the list ".format(Fore.BLUE + eie + Style.RESET_ALL,
                                                                                      Fore.GREEN + str(eiiu) + Style.RESET_ALL))

            elif int(OP3) == 2:
                # TODO remove old value of index 
                Ei = input(" enter index ")
                if int(Ei) > len(list) or not list:
                    print(" there is no element to edit")
                    continue
                Eie = list[int(Ei)]
                print(" the index {} has value of {}  ".format( Fore.GREEN + str(Ei) , Fore.BLUE + Eie))
                Eie = input(" enter value to edit ")
                list.insert(int(Ei), Eie)
                print(" the index {} been edited to value of {}  ".format(Fore.GREEN + str(Ei), Fore.BLUE + Eie))

            elif int(OP3) == 3:
                # TODO beter view 
                print(" current state of list :", list)
                print(" list after reverse: ", list.reverse())
          
            elif int(OP3) == 4:
                # TODO finsh it
                print("Select type of sort")
                print(" (1) ascending sort")
                print(" (2) descending sort ")
                print(" (3) length sort ")
                print(" (4) Exit")
                OP4 = input()
                match OP4:
                    case '1':
                       print(" current state of list :", list)
                       print(" list after ascending sort : ", list.sort)

                    case '2':
                        print(" current state of list :", list)
                        print(" list after ascending sort : ", list.sort(reverse=True))

                    case '3':
                        print(" current state of list :", list)
                    case '4':
                        print(" change been saved ")
                        flag1 = False
                
            elif int(OP3) == 5:
                flag1 = exit(flag1)            

    elif int(OP0) == 4:
        flag1 = True
        while flag1 == True:
            print("Select type of edit")
            print(" (1) print list")
            print(" (2) edit value of index ")
            print(" (3) reverse whole list ")
            print(" (4) sort whole list ")
            print(" (5) Exit")
            OP4 = input()
            match OP4:
                    case '1':
                       print(" list : \n", list)