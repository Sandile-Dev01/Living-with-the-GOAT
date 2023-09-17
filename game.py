print("Welcome to Living with the GOAT!")

your_name = input("What is your name ?: ")

#
while True:

    your_networth = 0
    your_goat = input("Who is your GOAT? (Ronaldo / Messi): ")
    ronaldo = "ronaldo"
    messi = "messi"

    # An adventure with C.Ronaldo

    if your_goat.upper() == ronaldo.upper():

        # Some constant variables throughout your game with Ronaldo
        your_place = "Saudi Arabia"
        your_goat_current_team = "Al Nassr"
        your_goat_last_team = "Man United FC"
        your_goat_best_team = "Real Madrid"
        your_goat_friend_1 = "Marcelo"
        your_goat_friend_2 = "Ramos"

        answer = input(
            "Well CR7 is happy you chose him and ready to engage in a journey with you. (continue/ quit): ").lower()
        if answer == "continue":
            answer = input(
                """Ronaldo just fell off the stair-cases trying to fetch you. 
                    What do you do? (call ambulance or laugh at him): """).lower()
            if answer == "call ambulance":
                answer = input(
                    """The Doctors said he will be fine in a weeks time.  
What do you do? (wait for him / leave him): """).lower()
                if answer == "wait for him":
                    answer = input(
                        """The GOAT was so grateful for your company and he offered you $2 000. 
Do you take it? (Yes / No): """).lower()
                    if answer == "yes":
                        your_networth += 2000
                        answer = input(f"""In a weeks time {your_goat_current_team} will play PSG for a friendly 
match & Ronaldo wants to force himself to play in what looks like the last battle of the 
goats. He needs your advice ( play the game  / wait till you're recovered): """).lower()
                        if answer == "play the game":
                            answer = input("""Luckily Ronaldo does get some minutes on this game and he scores a brace, 
he is excited about his performance even though they lost the game by a margin of 2. 
He than gifts you with a $5 000 gift card for your advice. 
What do you do with it (give it away / save it as cash) """).lower()
                            if answer == "give it away":
                                print("Gift successfully given away")
                            elif answer == "save it as cash":
                                your_networth += 5000

                            else:
                                print(
                                    "Next time, choose one of the answers in the brackets!")

                        elif answer == "wait till you're recovered":
                            answer = input("""The Goat is sad for your advice and double sad
because they lost the game by a margin of 2. What do you say to him ( sorry / nothing) :""").lower()
                            if answer == "Sorry":
                                print("The goat is stroke by how humble you are and offered you $2 000")
                            answer = input("""The goat is stroke by how humble you are and offered you $2 000."
What do you do ? take it / leave it""").lower()
                            if answer == "Take it":
                                your_networth += 2000
                                break
                            elif answer == "leave it":
                                break

                        else:
                            print(
                                "Next time, choose one of the answers in the brackets!")
                        break
                    elif answer == "no":
                        answer = input(f"""Ronaldo feels cool about it. A week past and he is now fully recovered and 
                        back to training with {your_goat_current_team}, in the mean-time he asks if you want to join 
                        the youth team (yes / no) :""").lower()
                        if answer == "yes":
                            var = answer == input("""Before you sign the contract you're bound to do some trainings.
You will play penalties is that ok ? (yes / no): """).lower()
                            while answer == "yes":
                                print("okay than let's go!")
                                break
                            else:
                                break

                        elif answer == "no":
                            var = answer == input("""Ronaldo is not happy with your decision though.
For the time being you will spectate Ronaldo's game and make some bets in his games. 
                                        Is that right by you? ( yes / no ): """).lower()
                            if answer == "yes":

                                while True:
                                    print("Okay bet")
                                    break

                            elif answer == "no":
                                print(
                                    "Okay than Ronaldo has decided to continue with his football and let you be")
                                break
                            else:
                                print(
                                    "Next time, choose one of the answers in the brackets!")
                                break

                        else:
                            print(
                                "Next time, choose one of the answers in the brackets!")
                        break

                    else:
                        print("Next time, choose one of the answers in the brackets!")
                        break
                elif answer == "leave him":
                    answer = input(
                        """Ronaldo heard about that and wasn't pleased. 2 weeks later he got discharged
and they found that he had a minor ankle injury. Can you be able to be his helper
till he fully recovers? (yes/ no): """).lower()
                else:
                    print("Next time, choose one of the answers in the brackets!")
                    break

            elif answer == "laugh at him":
                print(
                    "Ronaldo felt offended and asked the security guard to escourt you out of his estate")
                break
            else:
                print("Next time, choose one of the answers in the brackets!")
                break

        elif answer == "quit":
            print(":)")
        break

    # Some constant throughout your adventure with Messi
    elif your_goat.upper() == messi.upper():
        your_place = "USA (Miami)"
        your_goat_current_team = "Inter Miami FC"
        your_goat_last_team = "PSG"
        your_goat_best_team = "Barcelona"
        your_goat_friend_1 = "Neymar Jr"
        your_goat_friend_2 = "Luis Suarez"

        print("Messi is a goat")
        answer = input(
                "Well Messi is more excited about the adventure you will have together. (continue/ quit): ").lower()

        if answer == "continue":
            answer = input(
                "Well as you know Messi he is a soccer fanatic himself, so he just made you a FIFA challenge. (accept "
                "/ decline ): ").lower()

            if answer == "accept":
                "You got lucky and won with a margin of 1 - 0, Messi just gave you $ 300 for accepting the challenge"
                "/ and $ 750 for winning!"
                your_networth += 1050

        elif answer == "quit":
            break


# If invalid input is selected
    else:
        print("Invalid input, try again")
        continue
    break

# When game is quit, putting your networth in the picture

if your_networth >= 1:

    converted_worth = your_networth * 17
    print(
        f"""{your_name} you really made bank on your adventure with {your_goat}, 
you now have a networth of ${your_networth}.
That is close to {converted_worth} in Rands...sheesh! You should visit {your_place} again!""")

if your_networth >= 60000:
    converted_worth = your_networth * 17
    print(
        f"""{your_name} you really made bank on your adventure with {your_goat}, 
    you now have a networth of ${your_networth}.
    
    That is more than {converted_worth} in Rands... wow you're in the Millionaire's bracket now!
    You should definitely visit {your_goat} again!
""")

else:
    print(
        f"""{your_name} it looks like you had a good adventure with {your_goat}, you made ${your_networth} though.
    I guess {your_place} wasn't that profitable to you, till next time!""")
