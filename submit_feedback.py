# Python script to store feedback in a text file

feedback = input("Enter your feedback: ")

with open("feedback.txt", "a") as file:
    file.write(feedback + "\n")

print("Thank you for your feedback!")
