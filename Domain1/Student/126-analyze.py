quote = "The quick brown fox jumped over the lazy dog."
print(quote[4:9])

coins = ('Platinum','Gold','Silver') #What type of data structure is this?
#Can we change Platinum to Bronze?

#New Code
quote = "The quick brown fox jumped over the lazy dog."
print(quote[4:9])

coins = ('Platinum','Gold','Silver') #What type of data structure is this?
#Can we change Platinum to Bronze?
coins_list = list(coins)
coins_list[0] = "Bronze" 
coins2 = tuple(coins_list)
print(coins2)
