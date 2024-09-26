integers=[1,2,3,8,22]

animals=["dog","cat","bird"]

names=["dania","PELON","sam"]

floats=[2.5,3.4,1.6,6.5]

#heterogenious list

numbers_animals=[2,"cat",33.5,"FORTNITE"]

list_of_lists=[[1,2,3],["cat","dog","spiderman"]]

#how to acces an element in 

print()

words=[
    "Apple", "Mountain", "Whisper", "Journey", "Galaxy", "Lantern", "Harmony", 
    "Dancer", "Puzzle", "Ocean", "Cloud", "Sunrise", "Forest", "Rhythm", 
    "Crystal", "Echo", "Dream", "Canvas", "Meadow", "Flame", "Shadow", 
    "Compass", "Velvet", "Tranquil", "Treasure", "Mosaic", "Galaxy", 
    "Twilight", "Fountain", "Whistle", "Blossom", "Squirrel", "Journey", 
    "Desert", "Lantern", "Cactus", "Cascade", "Breeze", "Whisper", 
    "Laughter", "Serene", "Puzzle", "Tapestry", "Nimbus", "Voyage", 
    "Ember", "Echo", "Petal", "Glimmer", "Enigma", "Feather", 
    "Labyrinth", "Radiance", "Whisper", "Crystal", "Horizon", "Twilight", 
    "Cuddle", "Melody", "Wander", "Summit", "Driftwood", "Kaleidoscope", 
    "Dusk", "Quest", "Illusion", "Solstice", "Oasis", "Whirlwind", 
    "Petal", "Inkling", "Nebula", "Tidal", "Gossamer", "Harbor", 
    "Zephyr", "Tryst", "Epiphany", "Reverie", "Mosaic", "Bubbles", 
    "Silhouette", "Splendor", "Crescent", "Journey", "Echo", "Harmony", 
    "Prism", "Horizon", "Sanctuary", "Oasis", "Luminescence", "Tranquility", 
    "Chime", "Meadow", "Shimmer", "Nomad", "Fern", "Lullaby", 
    "Prism", "Ripple", "Cascade", "Starry", "Gale", "Haven", 
    "Solace", "Ember", "Whimsy", "Fable", "Glade", "Wanderlust", 
    "Zenith", "Echo", "Blush", "Foliage", "Quasar", "Ponder", 
    "Flicker", "Drift", "Tundra", "Meadow", "Aura", "Spellbound", 
    "Cascade", "Fractal", "Chandelier", "Puddle", "Glisten", 
    "Twilight", "Aether", "Echo", "Vale", "Cradle", "Paradox", 
    "Fable", "Trillium", "Meadow", "Mirage", "Whisper", "Horizon", 
    "Nimbus", "Lantern", "Fragrance", "Oasis", "Quiver", "Pebble", 
    "Journey", "Serenity", "Drift", "Vale", "Echo", "Journey", 
    "Wisp", "Sanctuary", "Dappled", "Amulet", "Chasm", "Glimmer", 
    "Silhouette", "Cascade", "Nova", "Bliss", "Driftwood", "Twilight", 
    "Radiant", "Haven", "Tranquil", "Ember", "Prism", "Wander", 
    "Whisper", "Labyrinth", "Kaleidoscope", "Gossamer", "Starlit", 
    "Echo", "Meadow", "Nimbus", "Mirage", "Echo", "Harmony", 
    "Tryst", "Whisper", "Mosaic", "Glade", "Reverie", "Elysium", 
    "Dreamscape", "Cascade", "Oasis", "Horizon", "Drift", "Wisp", 
    "Celestial", "Ember", "Tranquility", "Quicksilver", "Whimsy", 
    "Nebula", "Odyssey"
]

print(words[-1])


#list slicing

list1=[1,2,3,4,5]

print(list[1:3])

print(list[:])

print(list[2:-1])

list=[3,22,30,5.3,20]

#update a list

science=["art","chemistry","math"]

science[0] = "biology"
print(science)

science[2]="geology"
print(science)

integers = [2,5,9,28,27]

integers[-1] = 30.5

print(integers)

integers.remove(5)
print(integers)

integers.pop(2)
print(integers)

#list of fruits

list_of_fruit=["lemon","orange","melon"]

del list_of_fruit [0]

print(list_of_fruit)


listofnames=["dania","pelon","Sam"]

listofnames.append("GILBERT")

print(listofnames)