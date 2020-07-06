from game import person,bcolors
from inventory import item
from magic import spell

#black magic
fire = spell("Fire", 10, 100, "black")
thunder = spell("Thunder", 10, 100, "black")
blizzard = spell("Blizzard", 10, 100, "black")
meteor = spell("Meteor", 20, 200, "black")
quake = spell("Quake", 14, 140, "black")

#white magic
cure = spell("Cure", 12, 120, "white")
cura = spell("Cura", 18, 200, "white")

#adding items
potion = item("potion", "potion", "heals 50 hp", 50, 1)
hipotion = item("hipotion", "potion", "heals 100 hp", 100, 1)
superpotion = item("super potion", "potion", "Heals 500 hp", 500, 1)
elixer = item("elixer", "elixer", "Fully restores HP/MP ", 9999, 3)
hielixer = item("hielixer", "elixer", "Fully restores HP/MP", 9999, 3)

grenade = item("Grenade", "attack", "Deals 500 damage", 500, 4)


player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade]

#initilazing people
player = person(460, 65, 60, 34, player_spells, player_items)
enemy = person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "BATTLE START >> ATTACK! " + bcolors.ENDC)
print(bcolors.FAIL + bcolors.BOLD + "magic points(MP) = 65/65 use magic_points for 2.Magic_power" + bcolors.ENDC)
print(bcolors.FAIL + bcolors.BOLD + "5 special_coins available for using 3.Items" + bcolors.ENDC)
current_scoins = 5

while running:
    print("==========================")
    player.choose_action()
    choice = input("choose an action : ")
    index = int(choice) - 1


    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.OKBLUE + bcolors.BOLD + "YOU ATTACK FOR ", dmg, "POINTS OF DAMAGE" + bcolors.ENDC)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("choose magic : "))-1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_spell_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD + "\n NOT ENOUGH MP" + bcolors.ENDC)
            if current_mp > 0:
                print(bcolors.FAIL + bcolors.BOLD + " REMAINING MP :" + str(current_mp) + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == 'white':
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + bcolors.BOLD + "\n" + spell.name + "HEALS FOR ", str(magic_dmg), "HP" + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + bcolors.BOLD + "\n" + spell.name.upper() + " DEALS " + str(magic_dmg) + " POINTS OF DAMAGE  " + bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("choose item : ")) - 1

        if item_choice == -1:
            continue

        item = player_items[item_choice]
        if item.type == "potion":
            if current_scoins >= 1:
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
                current_scoins -= 1
            else:
                print(bcolors.FAIL +"special_coins are not enough left only", str(current_scoins) +  bcolors.ENDC)
                continue
        elif item.type == "elixer":
            if current_scoins >= 3:
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP " + bcolors.ENDC)
                current_scoins -= 3
            else:
                print(bcolors.FAIL +"special_coins are not enough left only", str(current_scoins) +  bcolors.ENDC)
                continue
        elif item.type == 'attack':
            if current_scoins >= 4:
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)
                current_scoins -= 4
            else:
                print(bcolors.FAIL +"special_coins are not enough left only", str(current_scoins) +  bcolors.ENDC)
                continue

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + "ENEMY ATTACK FOR ", enemy_dmg, "POINTS OF DAMAGE" + bcolors.ENDC)

    print("========================================")

    print("ENEMY HP : " + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

    print("YOUR HP : " + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("YOUR MP : " + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    print("========================================")


    if player.get_hp() == 0 or enemy.get_hp() == 0:
        if player.get_hp() == 0:
            print(bcolors.FAIL + bcolors.BOLD + "ENEMY WON THE MATCH" + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + bcolors.BOLD + "YOU WON THE MATCH" + bcolors.ENDC)
        if input("enter 'exit' to quit or any key to play again : ") == "exit":
            running = False
