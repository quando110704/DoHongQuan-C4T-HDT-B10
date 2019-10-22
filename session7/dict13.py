POKEMON = {
    "raichu" : "raichu has a regional variant that is Electric/Psychic. It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will evolve into this form regardless of their origin.",
    "onix" : "Onix resembles a giant chain of gray boulders that become smaller towards the tail. It has a rocky spine on its head and a pair of black eyes right beneath it. This Pokémon has a magnet in its brain that serves as an internal compass. Its body absorbs many hard objects, making its body very solid. As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds.",
    "blue" : "BLue is pushy and competitive, but is generally a good Pokémon Trainer. He is the grandson of Professor Oak and the player's childhood friend. After that he became the champion waiting for player to challenge. Blue is the basis for Gary Oak in the anime. IGN listed Blue as the 98th best villain in video games, though they stressed that it was difficult to view him as a villain. However, they did say that he was kind of a douche, citing his attempt to prevent the player character from getting a map. Three years later in Pokémon Gold, Silver and Crystal, and their remakes, Pokémon HeartGold and SoulSilver, he becomes a Gym Leader for Viridian City."
}
i = input("what pokemon you want to see ? ").lower()
u = input("what more ? ").lower()
print(POKEMON[i])
print("and:")
print(POKEMON[u])