def CustomerChoice ():
     " This function lets the user choose whether to create a new file or overwrite an old one. "
     while True:
         print ('Please select:')
         print (" To create a new 'clean' file, please input 'N'. ")
         print (" To overwrite the existing file, please input 'O'. ")
         Input = input('Your choice is: ...')
         if Input == 'N':
             return True
             break
         elif Input == 'O':
             return False
             break
         else :
             print " Error input, try again. "
            
 def LineProcess(eachLine):
     eachLine = eachLine[0: -1]
     beginCharacter = eachLine[0]
     endCharacter = eachLine [len(eachLine)-1]
     while beginCharacter == '':
         eachLine = eachLine[1:]
         beginCharacter = eachLine[0]
     while endCharacter == '':
         eachLine = eachLine[:-1]
         endCharacter = eachLine[len (eachLine)-1]
     return eachLine

 textFile = open('/Users/Uday/Desktop/words.txt','r')
 newLines = map(LineProcess, textFile)
 print(newLines)
 textFile.close()


 customerInput = CustomerChoice()
 if customerInput: # Create a new clean file newFile = open (r'd: \ newclean.txt ',' w ')
     for eachline in newLines:
         newFile.write(eachline + '\ n')
     newFile. close ()
 else : # overwrite the original file overwriteFile = open ('d: \ sample_11_11.txt', 'w')
     for eachline in newLines:
         overwriteFile.write(eachline + '\ n')
     overwriteFile. close () 