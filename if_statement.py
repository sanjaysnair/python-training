speed = int(input('Enter your vehicle speed: '))
mood = input('Enter police mood(terrible / bad / cool): ')

if speed >= 80:
    print('License and registration please')
    if mood == 'terrible' or speed >= 100:
      print('You have the right to remain silent.')
    elif mood == 'bad' or speed >= 90:
      print("I'm going to have to write you a ticket.")
      #write_ticket()
    else:
      print("Let's try to keep it under 80 ok?")
else:
    print("You drive safe :)")
