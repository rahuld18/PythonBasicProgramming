
run=True
while run:
     command = input('> ')
     if command.upper()=="HELP":
      help='''
    1. Start
    2. Stop
    3. Quit
    '''
      print(help)

     elif command.upper()=="START":
      print('CAr is started........')

     elif command.upper()=="STOP":
      print('Car is stopped')

     elif command.upper() == "QUIT":
      print('Game quit')
      run=False
     else:
         print("Sorry I dont't understand..")