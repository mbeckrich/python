# Be careful about uppercase/lowercase answers
print(
    """
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\\.
        .   . :: +. :.:/: .   .    .        . . .:\\
 .  :    .     . _ :::/:               .  ^ .  . .:\\
  .. . .   . - : :.:./.                        .  .:\\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\\ ########          :######## :/
  .        .+ :: : -.:\\ ########       . ########.:/
    .  .+   . . . . :.:\\. #######       #######..:/
      :: . . . . ::.:..:.\\           .   .   ..:/
   .   .   .  .. :  -::::.\\.       | |     . .:/
      .  :  .  .  .-:.":.::.\\             ..:/
 .      -.   . . . .: .:::.:.\\.           .:/
.   .   .  :      : ....::_:..:\\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\\       :/
     +   .   .   : . ::. :.:. .:.|\\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\
"""
)
print("You awake to an alien standing over you in your sleep.")
print(
    """This happens a lot. Normally, you would be paralyzed, but this time you can move. Escape the alien!
    """
)

escape_method = input(
    "You can dodge to the alien's left and dive out the window or"
    " move around his right for the door. Do you go left or right?\n"
).lower()

if escape_method == "left":
    print("You crash through the window and hit the ground on your feet.")
    escape_method_2 = input(
        "Do you run to the car or duck behind the house? Answer with 'car' or"
        " 'house.'\n"
    ).lower()
    if escape_method_2 == "house":
        print(
            "You round the corner are greeted by the Mothership. Dozens of"
            " aliens pour out. RIP, and game over."
        )
        exit()
    elif escape_method_2 == "car":
        print("You race to the car burn rubber out of the driveway.")
        escape_method_3 = input(
            "You make it out of your neighborhood and onto the highway. The"
            " sun is coming up and your city is returning to life. Do you go"
            " see your therapist, splash some water from yesterday's bottle on"
            " your face, or high tail it to the nearest army recruitment"
            " center to sign up to defend your home planet from the alien"
            " invasion? Answer with 'therapist', 'water', or 'army.'\n"
        ).lower()
        if escape_method_3 == "therapist":
            print(
                "You make for your therapist's office. You exit the car and"
                " run inside. He greets you with concern and you begin to"
                " explain what's happened. He smiles and his human face falls"
                " off. You are frozen in place and eaten alive. Game over."
            )
            exit()
        elif escape_method_3 == "water":
            print(
                "This must all be a bad dream. You splash some lukewarm water"
                " from yesterday's bottle on your face. Nothing happens... you"
                " panic, and pour the remnants of the bottle over your face."
                " You feel your foot kick and begin to wake up in your bed, no"
                " alien in sight. Everything is okay!"
            )
            exit()
        elif escape_method_3 == "army":
            print(
                "You pull up or you maps app and look for the nearest Army"
                " recruiter. You're ready to enlist and fight off the alien"
                " menace. Waze says the drive will take about 5 minutes. When"
                " you arrive, the recruiter eyes you greedily as you explain"
                " everything you've seen. He hands you the paperwork, which"
                " you immediately sign. The next day, you meet your unit. They"
                " have no idea what you mean by all this alien stuff. You"
                " spend the next year in Iraq. Game over."
            )
            exit()

else:
    print(
        "You move for the door, open it, and are eaten by an"
        " alien-grue on the other side. Game over."
    )
    exit()

# Differences with her code
# 1) She prompts user to use "left" or "right" with first input.
# This requires something like use of an escape character (\) in quotation
# marks.
