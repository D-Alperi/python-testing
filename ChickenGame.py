import random
import time

try:
    # Get number of players
    while True:
        try:
            num_players = int(input("Hur många spelare vill spela? (2 eller fler): "))
            if num_players >= 2:
                break
            else:
                print("Ni måste vara minst 2 spelare.")
        except ValueError:
            print("Ange ett giltigt heltal.")

    # Get player names
    players = []
    for i in range(num_players):
        name = input(f"Ange namn för spelare {i+1}: ").strip()
        players.append(name)

    while True:
        while True:# Choose goal at the start of each game
            try:
                goal = int(input("Ange ett mål mellan 50 och 1000: "))
                if 50 <= goal <= 1000:
                    break
                else:
                    print("Målet måste vara mellan 50 och 1000.")
            except ValueError:
                print("Ange ett giltigt heltal.")

        # Calculate dice max between 75% and 110% of goal
        lower = max(1, int(goal * 0.75))
        upper = max(lower, int(goal * 1.10))
        dice_max = random.randint(lower, upper)
        print(f"\nMålet är att nå {goal} poäng utan att gå över")
        print(f"Tärningens maxvärde är slumpat till {dice_max}\n")
        scores = {player: 0 for player in players}
        stopped = {player: False for player in players}
        turn = 0  # Index for current player
        busted_players = []

        while True:
            current_player = players[turn % num_players]
            if stopped[current_player]: # Skip if player has quit
                turn += 1
                continue

            print(f"{current_player}s tur. Du har nu {scores[current_player]} poäng och målet är {goal}.")
            val = input("skriv '+' för att kasta på nytt eller '-' för att stanna: ").strip()
            if val == "+":
                num = random.randint(1, dice_max)  # Use new dice_max
                print(f"Du kastade {num} och har nu totalt {scores[current_player] + num} poäng\n")
                if scores[current_player] + num <= goal:
                    time.sleep(1)
                scores[current_player] += num
                if scores[current_player] > goal:
                    print(f"BUST! {current_player} har {scores[current_player]} vilket gick över \n")
                    scores[current_player] = 0
                    stopped[current_player] = True
                    busted_players.append(current_player)  # Mark as busted
                    time.sleep(1)
            elif val == "-":
                print(f"{current_player} har stannat på {scores[current_player]} poäng!\n")
                stopped[current_player] = True
                time.sleep(1)
            else:
                print("\nOgiltigt val, försök igen \n")
                continue

            # Check if all players have stopped
            if all(stopped.values()):
                # Determine winner(s)
                diffs = {player: (goal - score if score <= goal else float('inf')) for player, score in scores.items()}
                min_diff = min(diffs.values())
                winners = [player for player, diff in diffs.items() if diff == min_diff]
                # Only show difference if no one busted
                if not busted_players:
                    highest = max(scores.values())
                    lowest = min(scores.values())
                    diff = highest - lowest
                    highest_players = [player for player, score in scores.items() if score == highest]
                    lowest_players = [player for player, score in scores.items() if score == lowest]

                    if len(winners) == 1:
                        print(f"\n{winners[0]} vinner med {scores[winners[0]]} poäng, närmast målet {goal}!\n")
                        print(f"Skillnaden mellan {', '.join(highest_players)} och {', '.join(lowest_players)} är {diff} poäng.\n")
                    else:
                        print(f"\nOavgjort! Följande spelare är lika nära målet {goal}: {', '.join(winners)}\n")
                else:
                    if len(winners) == 1:
                        print(f"\n{winners[0]} vinner med {scores[winners[0]]} poäng, närmast målet {goal}!")
                        print(f"BUSTED och förlorade: {', '.join(busted_players)}\n")
                    else:
                        print(f"\nOavgjort! Följande spelare är lika nära målet {goal}: {', '.join(winners)}")
                        print(f"BUSTED och förlorade: {', '.join(busted_players)}\n")
                break

            turn += 1  # Next player's turn

        play_again = input("Vill ni spela igen? (j/n): ")
        if play_again.lower() != 'j':
            print("Tack för att ni spelade!")
            break
except KeyboardInterrupt:
    print("\nSpelet avslutat. Tack för att ni spelade!")