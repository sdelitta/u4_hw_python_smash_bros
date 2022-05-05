import random
import json

from smash import Battle, Character
characters = []
game_over = False
player_one = {}
player_two = {}

with open('characters.json') as json_file:
    characters = json.load(json_file)

def game():
    print("This... is..... SMASH BROS! \n Type (list) for a list of characters or enter your character name NOW")
    
    global game_over
    global player_one
    global player_two
    gameover = False

    while (player_one == {}):

        res = input("Choose your character: ")

        if res == "list":
            print("Character List... ")
            for char in characters:
                print(char["name"])
        elif res == "":
            player_one = random.choice(characters)

        for char in characters:
            if res.lower() == char["name"].lower():
                player_one = char

    print("You've selected " + player_one["name"])

    player_two = random.choice(characters)

    player_one = Character(player_one["name"], player_one["attacks"])
    player_two = Character(player_two["name"], player_two["attacks"])

    print("Player Two chose " + player_two.name)

    battle = Battle(player_one, player_two)
    
    while (not gameover):
        res = input("Choose your attack: ")

        for attack in player_one.attacks:
            if res.lower() == attack["name"].lower():
                battle.npc.damage(attack["damage"])
        print("Player Two has " + str(battle.npc.health) + " hp." )

        npc_attack = random.choice(player_two.attacks)
        battle.player.damage(npc_attack["damage"]) 
        print("Player One has " + str(battle.player.health) + " hp. \n Player Two used " + npc_attack["name"])


        if (battle.player.health <= 0 or battle.npc.health <= 0):
            gameover = True
            if (battle.player.health > battle.npc.health):
                print("Player One Wins!")
            else: 
                print("Player Two Wins. You're bad")  

    restart = input("Would you like to play again? (y/n) ")
    if restart == "y":
        player_one = {}
        game_over = False
    else: 
        player_one = {}
        game_over = True

while (not game_over):
    game()
