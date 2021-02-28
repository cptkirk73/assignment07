#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.Creating a more robust inventory system
# Change Log: (akirkland- updated code added in new functions and orginazation and changed data type)
# Andrew Kirkland, 2021-Feb-28, Created File
#------------------------------------------#

# -- DATA -- #
import pickle
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
#binaryfile = 'CDInventory.dat' #binary storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:

    @staticmethod
    def deleteProcesser(table, id_to_remove):
        '''
        Deleting the data from the files 
    
         Args:
         table--Dictionay we have added           
          id_to_remove--This removes the line associated with they id   
        
        Returns:
            blnCDRemoved which is a bool
        '''
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == id_to_remove:
                del table[intRowNr]
                blnCDRemoved = True
                break
            
        return blnCDRemoved
    
    
    @staticmethod
    def add_CD(str_ID, str_title,str_Artist, table):
        
        '''
        Adding the users data to the dictionary and storing as dictionary 
        
         Args:
            str_ID--Id used to identify the number of CD's'
            str_Title--CD title
            str_Artist--Artist of CD
            table-dictionary table 
            
        Returns:
            none
            
        '''
        
        #Adding to list of dictionaries
        intID = int(str_ID)
        dicRow = {'ID': intID, 'Title': str_title, 'Artist': str_Artist}
        table.append(dicRow)



class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file

        #objFile = open(file_name, 'r')
        #for line in objFile:
            #data = line.strip().split(',')
            #dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            #table.append(dicRow)
        #objFile.close()
        with open(file_name,'rb') as fileobj:
            data = pickle.load(fileobj)
        return data

    @staticmethod
    def write_file(file_name, table):
        ''' 
        Saving the data as a binary file withthe pickle.dump method

        Args:
            file_name--the .dat file 

        Returns:
            None.         
        '''
  
        #objFile = open(file_name, 'a')
        #strRow = ''
        #for item in table:            
            #strRow += ("{},{},{}\n".format(*item.values()))
            
        #strRow = strRow[:-1] + '\n'
        #objFile.write(strRow)
        #objFile.close()
        with open(file_name,'wb') as fileobj:
            pickle.dump(table,fileobj)


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
    
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            try:
                choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
                print()  # Add extra space for layout
            except: 
                print('ERROR! Please select from the list')
        return choice
    

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
      
    @staticmethod    
    def newCdinput():
        
        ''' 
        Args:
            None.

        Returns:
            None.
        '''

        #Taking in user input 
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        
        return strID,strTitle, stArtist

           # Adding to list of dictionaries
        #intID = int(strID)
        #dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        #lstTbl.append(dicRow)
        #IO.show_inventory(lstTbl)
             # start loop back at top.



# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

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
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        try:
            if strYesNo.lower() == 'yes':
                print('reloading...')
                FileProcessor.read_file(strFileName, lstTbl)
                IO.show_inventory(lstTbl)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstTbl)
            continue # start loop back at top.
        except:
            print('Error File not found')
    # 3.3 process add a CD
    elif strChoice == 'a':
        #Ask user for new ID, CD Title and Artist
        #process display current inventory
        #IO.newCdinput()
        strID, strTitle, strArtist = IO.newCdinput()
        DataProcessor.add_CD(strID, strTitle, strArtist, lstTbl)
        continue
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        except:
            print('There was an error, please enter an integer')

        # 3.5.2 search thru table and delete CD
        blnCDRemoved = DataProcessor.deleteProcesser(lstTbl, intIDDel)
        
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        continue

    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        try:
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        except:
            print('General Error')
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




