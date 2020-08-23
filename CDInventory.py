#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []   #List of Dictionaries
dicRow = {}  # User Data Input Dictionary
strFileName = 'CDInventory.txt'  # data storage file
objFile = '' # file object

# -- PROCESSING -- #
class DataProcessor:
    # TODO add functions for processing here
    def data_add(dtpl):
        dicRow = {}
        dicRow['ID'] = (dtpl[0])
        dicRow['Title'] = (dtpl[1])
        dicRow['Artist'] =(dtpl[2])
        global lstTbl
        lstTbl.append(dicRow)
        return lstTbl
    def data_del(lstTbl):
        IO.show_inventory(lstTbl)
        #show_inventory(lstTbl)
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        # TODO move processing code into function
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                   del lstTbl[intRowNr]
                   blnCDRemoved = True
                   break
            if blnCDRemoved:
                print('The CD was removed')
            else:
                print('Could not find this CD!')
        IO.show_inventory(lstTbl)
    @staticmethod
    def table_clear():
        lstTbl.clear()
        
class FileProcessor:
    """Processing the data to and from text file"""
    @staticmethod
    def read_file(strFileName = 'CDInventory.txt', table= lstTbl ):
            dicRow ={}
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled  :')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                table.clear()  # this clears existing data and allows to load data from file
                objFile = open(strFileName, 'r')
                for line in objFile:
                    data = line.strip().split(',')
                    dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                    global lstTbl
                    lstTbl.append(dicRow)
                objFile.close()
                return lstTbl
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstTbl)
    @staticmethod
    def write_file(strFileName = 'CDInventory.txt', table= lstTbl):
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            objFile = open(strFileName, 'w')
            for row in lstTbl:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        print()
        print()
        print('{:*^60}'.format('Welcome To CD_Inventory Menu'))
        print()
        print('{:@^60}'.format('  Please Make Your Choice  '))
        print("""
              A) ADD NEW ENTRY
              
              I) DISPLAY CURRENT INVENTORY

              S) SAVE DATA TO fILE
              
              L) LOAD DATA FROM FILE
          
              D) DELETE DATA FROM INVENTORY
              
              X) EXIT tHE PROGRAMM
                                              """)

    @staticmethod
    def menu_choice():
        choice = ''
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
            print()  # Add extra space for layout
        return choice

    @staticmethod
    def usr_input():
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return int(strID), strTitle, stArtist
    
    
    def show_inventory(lsttab):
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lsttab:
            print('{:<6}{:20}{:20}'.format(row['ID'], row['Title'], row['Artist']))
        print('======================================')


# M A I N   B O D Y
# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file()
# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        FileProcessor.read_file()
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        dtpl=IO.usr_input()
        DataProcessor.data_add(dtpl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        DataProcessor.data_del(lstTbl)
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        FileProcessor.write_file()
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')



