flight_response = input("Would you like to fly? (Y|N)")
match flight_response:
    case "Y":
        flight_willing = True
    case "N":
        flight_willing = False
    case _:
        flight_willing = Maybe # Refer to https://github.com/TodePond/GulfOfMexico/?tab=readme-ov-file#booleans

if not flight_willing:
    print("That's not very nice.")

if flight_willing:
    print("sorry, this course is booked out")

if flight_willing == Maybe:
    print("good job please refer to the Hitchhiker's guide to the galaxy for more information")