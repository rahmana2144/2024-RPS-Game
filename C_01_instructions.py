# Displays instructions
def instructions():
    print('''

**** Instructions ****

To begin, choose the number of rounds (or [press <enter> for 
infinite mode).

Then play against the computer. You need to choose R (rock),
P (paper) or @ (scissors).

The rules are as follows:
- rock beats scissors
- scissors beats paper
- paper beats rock

    Good luck!
    ''')


# Main routine

print()
print("💎📰✂ Rock / Paper / Scissors Game ✂📰💎")
print()

# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")
