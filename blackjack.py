def deal_cards():
    import random
    suits = ["♠", "♥", "♣", "♦"]
    value = [i for i in range(1, 14)]
    points = [i if i < 11 else 10 for i in value]
    cards = [[str(i), j, points[value.index(i)]] for j in suits for i in value]
    random.shuffle(cards)
    return cards


def output_cards(shown_cards):
    faced = {
        '11': 'J',
        '12': 'Q',
        '13': 'K',
        '1': 'A',
        '#': '#'
    }
    facel = [i[0] if i[0] == "#" else i[0] if 1 < int(i[0]) < 11 else faced[i[0]] for i in shown_cards]
    suitl = [i[1] for i in shown_cards]

    number = len(shown_cards)

    print(" ___ " * number)
    print("".join([f"|{i} |" if i == "10" else f"|{i}  |" for i in facel]))
    print("".join([f"| {i} |" for i in suitl]))
    print("".join([f"|_{i}|" if i == "10" else f"|__{i}|" for i in facel]))


def get_best_value(cardlist):
    maxval = [11 if i[2] == 1 else i[2] for i in cardlist]

    while sum(maxval) > 21 and 11 in maxval:
        maxval[maxval.index(11)] = 1
    return sum(maxval)


def get_cards(cardlist):
    i = 2
    while get_best_value(cardlist[:i]) < 21:
        i += 1
    return cardlist[:i]


def player_plays(cards):
    all_player_cards = get_cards([cards[i] for i in range(0, 24, 2)])
    shown_player_cards = all_player_cards[:2]

    i = 2
    while shown_player_cards != all_player_cards:
        print("Your score is ", get_best_value(shown_player_cards), "with the cards")
        output_cards(shown_player_cards)
        print("(h)it or (s)tand")
        while True:
            choice = input("> ")
            if choice in "hs": break
        if choice == "s": break

        shown_player_cards.append(all_player_cards[i])
        i += 1
    return shown_player_cards


def dealer_plays(cards, player_score):
    i = 1
    all_dealer_cards = get_cards([cards[i] for i in range(1, 24, 2)])

    while get_best_value(all_dealer_cards[:i]) < player_score:
        i += 1
    return all_dealer_cards[:i]


def main():
    print("""Hello welcome to blackjack, this is the... 5th? version I'm making. Don't know how I keep fucking it up,
but there you go. Anyway, you start with 5000 mahoneys, and bet on rounds of blackjack. Get more than 21 and you lose.
Get 21 exactly and you win. Otherwise, you got to get more than the dealer to win""")

    money = 5000
    while money > 0:
        print(f"\nYou have {money} money. Do you want to play? (y/n)")
        if input("> ").lower().startswith("n"): break


        print("How much do you want to bet?")
        while True:
            bet = input("> ")
            try:
                if 0 < int(bet) <= money:
                    bet = int(bet)
                    break
            except:
                continue

        cards = deal_cards()

        print("Dealer has drawn this card:")
        output_cards([cards[1], ["#", "#", "#"]])

        shown_player_cards = player_plays(cards)
        player_score = get_best_value(shown_player_cards)

        if player_score > 21:
            output_cards(shown_player_cards)
            print(f"I'm sorry, you lost with a score of {player_score}")
            money -= bet
            continue

        elif player_score == 21:
            output_cards(shown_player_cards)
            print("Nice, you won")
            money += bet
            continue

        dealer_cards = dealer_plays(cards, player_score)
        dealer_score = get_best_value(dealer_cards)
        print("Dealer drew these cards, with the score ", dealer_score)
        output_cards(dealer_cards)

        if player_score <= dealer_score < 22:
            print("The dealer beat you this round, sorry about that")
            money -= bet
        else:
            print("You beat the dealer, not bad!")
            money += bet


main()
