user_input = ""
started = False

while user_input.upper() != "QUIT":
    user_input = input(">").upper()
    
    if user_input == "QUIT":
        print("bye")
    elif user_input == "START":
        if started:
            print("the car is already started")
        else:
            print("Car started... Ready to go!")
            started = True
    elif user_input == "STOP":
        if not started:
            print("THE CAR IS ALREADY STOPPED, YOU BUFFOON!")
        else:
            print("Car stopped.")
            started = False
    elif user_input == "HELP":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    else:
        print("I dont understand that")
