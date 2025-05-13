# rating is supposed to be a whole number
rating = (input("Enter a rating between 1 and 5"))
points = (rating) * 100
print("You have " + (points) + " to start.")


#new code
# rating is supposed to be a whole number
rating = float(input("Enter a rating between 1 and 5"))
points = int(rating) * 100
print("You have " + str(points) + " to start.")
