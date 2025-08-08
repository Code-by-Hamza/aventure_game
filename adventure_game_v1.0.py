import random
import time

# Locations
locations = (
    "Hunted Forest", "Crystal Cave",
    "Abandoned Village", "Ancient Ruins", "River Bank",
    "Hidden Shrine", "Volcanic Caves", "Desert", "Mountain Pass"
)

# Events
event = {
    "treasure": "💎 You found an awesome Treasure",
    "enemy": "⚔️ A rogue shinobi challenges you to a duel!",
    "healer": "🌸 A kind healer restores some of your health.",
    "trap": "💥 You stepped into a trap!",
    "nothing": "🌫️ The area is quiet… nothing happens.",
    "legendary_item": "🏆 You found a Legendary Exiler!",
    "ally": "🫂 An old ally joins your journey and gives you supplies."
}

# Treasure items
treasure = ("Sword", "Bow", "Diamonds", "Gold", "Boots")

# Player setup
player = {
    "name": input("   Enter Hero Name: "),
    "health": 100,
    "inventory": set(),
    "score": 0
}

time.sleep(0.8)
print(f"              Welcome {player['name'].title()}\n     Your Journey begins here...\n")
time.sleep(1)

# Game loop
while player["health"] > 0:
    time.sleep(3)
    print(f"\n   Hero Name: {player['name'].title()} | Health: {player['health']}♥️ |")
    print(f"\n   Score: {player['score']}")
    print(f"   Items: {', '.join(player['inventory']) or 'None'}\n")

    move = input(f"    where to move {player["name"]} ?(N/S/E/W):  ").strip().lower()
    random_location = random.choice(locations)
    if player["score"] >= 100:
        print("     You have won!🔥")
        break
        
    if move in ("n", "s", "e", "w"):
        print(f"    You have now reached: {random_location}")
        time.sleep(1)
        
        random_event = random.choice(list(event.keys()))

        if random_event == "treasure":
            print(event["treasure"])
            new_item = random.choice(treasure)
            player["inventory"].add(new_item)
            time.sleep(0.8)
            print(f"   {new_item} has been added to your items")
            time.sleep(0.5)
            player["score"] += 20
            print("   Score +20")

        elif random_event == "enemy":
            print(event["enemy"])
            if "Sword" in player["inventory"]:
                print("   You have defeated the enemy with your sword 🗡️")
                time.sleep(0.5)
                player["score"] += 10
                print("   Score +10")
            else:
                injury = random.randint(10,40)
                player["health"] = max(player["health"] - injury, 0)
                print(f"   You have suffered an injury \n   Health: -{injury}♥️")
                time.sleep(0.5)
                player["score"] -= 20
                print("   Score -20")

        elif random_event == "healer":
            print(event["healer"])
            time.sleep(0.8)
            heal = random.randint(10,30)
            player["health"] = min(player["health"] + heal, 100)
            print(f"   Health: +{heal} (Now {player['health']}♥️)")

        elif random_event == "trap":
            print(event["trap"])
            time.sleep(0.8)
            print("   Looks like your leg is broken! 🦴")
            player["health"] = max(player["health"] - 30, 0)
            player["score"] -= 20
            print("   Health: -30   Score: -20")

        elif random_event == "nothing":
            print(event["nothing"])

        elif random_event == "legendary_item":
            print("   ",event["legendary_item"])
            time.sleep(0.8)
            player["score"] += 50
            print("   Score: +50")
        
        elif random_event == "ally":
            print("   ",event["ally"])
            new_item = random.choice(treasure)
            player["inventory"].add(new_item)
            time.sleep(0.8)
            print(f"You ally has given you {new_item}")  
            
               
    else:
            print("   Invalid Direction..\n   Buddy where are you going🧐")                              
    
                                                         
else:
    print("You have died!💀")                                                                                                                                                                   