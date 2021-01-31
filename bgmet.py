#!/usr/bin/python

# 2021
# Tore Fredriksen, torefr@gmail.com

# Kazaross-XG2 Match Equity Table
# https://bkgm.com/articles/Keith/KazarossXG2MET/index.html
met = [[0, 0, 0], \
[0, 50.0, 67.7, 75.1, 81.4, 84.2, 88.7, 90.7], \
[0, 32.3, 50.0, 59.9, 66.9,	74.4, 79.9, 84.2], \
[0, 24.9, 40.1, 50.0, 57.6,	64.8, 71.1, 76.2], \
[0, 18.6, 33.1, 42.9, 50.0, 57.7, 64.3, 69.9], \
[0, 15.8, 25.6, 35.2, 42.3, 50.0, 56.6, 62.6], \
[0, 11.3, 20.1, 28.9, 35.7, 43.4, 50.0, 56.3], \
[0, 9.3, 15.8, 23.8, 30.1, 37.4, 43.7, 50.0]]


print (met)

# Match winning chances for a given score
def mwc (playeraway, opponentaway):
   return (met[playeraway][opponentaway])

# Cubeless takepoint for a given score
def cubelesstakepoint (playeraway, opponentaway):
   # cubelevel assumed to be on level 2 per default
   # cubeless takepoint = risk / risk + gain
   drop = mwc (playeraway, (opponentaway-1))
   takelose = mwc (playeraway, (opponentaway-2))
   takewin = mwc ((playeraway-2), opponentaway)

   risk = drop - takelose
   gain = takewin - drop
   
   takepoint = (risk / (risk + gain)*100)
   return takepoint

print (mwc(3,2))

# I get slightly different numbers than extreme gammon. Probably because they are using higher precision on the numbers in the met.
# But this should be investigated before I go further
print (cubelesstakepoint(7,4))
