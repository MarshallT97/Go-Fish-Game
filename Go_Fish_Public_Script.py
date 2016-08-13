import random
const_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]  #Avaliable numbers the player can chose
deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
player_deck = []
computer_deck = []
player_score = 0
computer_score = 0
count = 0  
game_turn = True  #Tigger for whether or not the game is over
dealer = 5
rounds = 1

def Player_Drawer():
    '''Takes out 5 cards from deck and place them in the players deck'''
    global dealer
    if len(deck) <= 5:  
        dealer = len(deck)
    for x in range(dealer):
        randP_card = random.choice(deck)
        if randP_card in deck:  
             deck.remove(randP_card)
        player_deck.append(randP_card)
    print(("Player Hand:", player_deck))
    
def Computer_Drawer():
    '''Takes out 5 cards from deck and place them in the computer deck'''
    global dealer
    if len(deck) <= 5:  
        dealer = len(deck)
    for y in range(dealer):
        randC_card = random.choice(deck)
        if randC_card in deck:  
            deck.remove(randC_card)
        computer_deck.append(randC_card)

def hand_checker(hand):
    '''Checks each hand if they have 4 of a kind'''
    global count
    if len(hand) == 0:  
        return False
    for x in hand:  
        if hand.count(x) == 4:
            while x in hand:
                hand.remove(x)
            count += 1  #For every set of 4 of one card in their hand they will gain a point
    return True

def score_giver():
    '''Gives the right number of points to the side that earn it'''
    global player_deck, computer_deck, player_score, computer_score, count
    print('~~~~~~~~~~~~~~')
    print('Current Score:')
    if hand_checker(player_deck):
        player_score += count
        print()
        print(('Player Hand:' , filler(player_deck)))
        print(('Player score:' , player_score))
        count = 0
    else:
        print()
        print(('Player Hand:' , filler(player_deck)))
        print(('Player score:' , player_score))
        count = 0
        
    if hand_checker(computer_deck):
        computer_score += count
        print()
        print(('Computer score:' , computer_score))
        count = 0
    else:
        print()
        print(('Computer score:' , computer_score))
        count = 0
    print(('Cards in deck left:' , len(deck)))
    print('~~~~~~~~~~~~~~')

def dealer_check():
    ''' Checks the both the computer deck and player deck to see if they have any cards
        and will give them 5 or less depending on the remain cards in main deck '''
    if len(computer_deck) == 0:
        if len(deck) == 0:
            print('Computer: Go fish...\nHowever there no more cards to draw so let keep going.')
        else:
            print('Computer: Im out of cards so just let me grab some more')
            Computer_Drawer()
    if len(player_deck) == 0:
        if len(deck) == 0:
            print('Player: Nope, Go Fish...\nHowever there no more cards to draw so let keep going.')
        else:
            print('Player: Hold on im out of cards, need to get more')
            Player_Drawer()
            
def filler(hand):
    ''' Checks the given hand to see if they have cards or not '''
    if len(hand) == 0:
        return 'Empty'
    else:
        return hand
        
def player_turn():
    ''' Controller for the player turn '''
    retry = True
    while retry:
        my_turn = False  #Trigger to see if the player can get another turn
        dealer_check()
        user_input = eval(input("Ask the computer for one type of card:"))

        try:  #Checks if the user input a non number
            int(user_input) + 1
        except:
            user_input = -1
            
        #Checks to make sure the player has atleast one of the same card in his deck before asking if the computer has it
        #Also checks if the asked card is a optional card in the 52 deck of cards
        if int(user_input) not in const_cards or int(user_input) not in player_deck:
            print("GM: That is not a vailded card choice.")
            print("GM: Try again")
        else:
            #If the player asked card is in the computer deck then the player takes it and removes it from the computer deck
            if int(user_input) in computer_deck:
                print(("Computer: Yes i do have a " + str(user_input) + ' in my hand.'))
                while int(user_input) in computer_deck:
                    computer_deck.remove(int(user_input))
                    player_deck.append(int(user_input))
                print(('The Computer gave you his ', user_input))
                
            #If the player asked card is not in the computer deck then the player 'Goes Fish' and takes a card from the deck
            else:
                if len(deck) == 0:
                    print('Computer: Go fish...\nHowever there no more cards to draw so let keep going.')
                else:
                    print("Computer: Go fish")
                    card = random.choice(deck)
                    player_deck.append(card)
                    if card == int(user_input):  #checks to see if player draw a card that match in his hand for another turn
                        my_turn = True
                    deck.remove(card)
                print(('You drew a ' + str(card)))
            dealer_check()
            
            if my_turn:
                score_giver()
                print(('Player: Well look at that... i just pull out a ' + str(user_input) + '.'))
                print('Player: So i get another turn.')
                retry = True
            else:
                retry = False
            
def computer_turn():
    ''' Controller for the computer turn '''
    retry = True
    print()
    while retry:
        my_turn = False  #Trigger to see if the player can get another turn
        dealer_check()
        computer_input = random.choice(computer_deck)
        print(('Computer: Im looking for a ' + str(computer_input) + '...\nDo you have one?'))
        
        #If the computer asked card is in the player deck then the computer takes it and removes it from the player deck
        if computer_input in player_deck:
            print(('Player: Lucky for you i do have a ' + str(computer_input) + ' in my hand.'))
            while computer_input in player_deck:
                player_deck.remove(computer_input)
                computer_deck.append(computer_input)
            print(('You have given your ' + str(computer_input) + ' to the Computer'))
        else:
            if len(deck) == 0:
                print('Player: Nope, Go Fish...\nHowever there no more cards to draw so let keep going.')
            else:
                print('Player: Nope, Go Fish.')
                card = random.choice(deck)
                computer_deck.append(card)
                if card == computer_input:
                    my_turn = True  #checks to see if player draw a card that match in his hand for another turn
                deck.remove(card)
        dealer_check()
        if my_turn:
            score_giver()
            print(('Computer: Oh here the ' + str(computer_input) + ' i needed.'))
            print('Computer: This means i get another turn.') 
            retry = True
            not_again = computer_input
        else:
            retry = False

Player_Drawer()
Computer_Drawer()

while game_turn:
    ''' Game Looper '''
    print()
    print(('Turn ' + str(rounds) + '                                              <------'))
    print()
    
    player_turn()
    score_giver()
    
    if len(deck) == 0 and len(computer_deck) == 0:  #the will end the game if the computer handa is empty
        game_turn = False
    
    if game_turn:  #switches to the computer turn
        computer_turn()
        score_giver()
        if len(deck) == 0 and (len(player_deck) == 0 and len(computer_deck) == 0):  #This will end the game if both players hands are empty
            game_turn = False
        else:
            game_turn = True
            
    rounds += 1  #incerment the number of the round after both players had a turn
    
if player_score > computer_score:
    print('You win!')
elif player_score == computer_score:
    print('It a tie!')
else:
    print('You lose!')

