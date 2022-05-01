#modified for pokémon

pokemon = ('Talonflame', 'Kyurem', 'Bruxish', 'Missingno', 'Metang',
          'Mega Mawile', 'Arceus', 'Bewear', 'Rayquaza', 'Espurr',
          'Buzzwole', 'Mewtwo', 'Primal Groudon', 'Tapu Lele', 'Mega Kangaskhan',
           'Kartana', 'Volcarona', 'Vaporeon', 'Machamp', 'Oricorio Sensu')

print("Top 5: {}".format(pokemon[:5]))

print("\nLast 4: {}".format(pokemon[-4:]))

print("\nAlphabetical order: {}".format(sorted(pokemon)))

print("\nMewtwo position in the list is: {}th position".format(pokemon.index('Mewtwo')))
