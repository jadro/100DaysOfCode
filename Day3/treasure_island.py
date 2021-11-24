print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'

""")
print("Welcome to treasure island.\nYour mission is to find the treasure")
direction = input("You're at crossroad, where you would like to go? Type 'left' or 'right'").lower()

if 'left' in direction:
    activity = input("You have came to lake. There is a island in the middle of the lake. What you will do. \
Type 'wait' to wait for a boat or type 'swim' to swim across lake. ").lower()
    if 'wait' in activity:
        color = input("You arrive to island. There is a house with three doors. One 'white', second 'red' and last 'yellow'. \
Which doors you will choose? ").lower()
        if 'yellow' in color:
            print("You found the treasure. You won.")
        elif 'red' in color:
            print("You entered room full of fire. Game over")
        elif 'white' in color:
            print("You entered room full of beasts. Game over.")
        else:
            print("You choosed not existing doors. Game over.")
    else:
        print("You have not enough energy to swim to island. Game over.")
else:
    print("You fall to big hole. Game over.")
