#!/usr/bin/python

# 2021
# Tore Fredriksen, torefr@gmail.com



# Kazaross-XG2 Match Equity Table
# https://bkgm.com/articles/Keith/KazarossXG2MET/index.html
# Higher precision
met = [[0, 0, 0], \
[0, 50.000, 67.736, 75.076, 81.436, 84.179, 88.731, 90.724], \
[0, 32.264, 50.000, 59.947, 66.870, 74.359, 79.940, 84.225], \
[0, 24.924, 40.053, 50.000, 57.150, 64.795, 71.123, 76.209], \
[0, 18.564, 33.130, 42.850, 50.000, 57.732, 64.285, 69.924], \
[0, 15.821, 25.641, 35.205, 42.268, 50.000, 56.635, 62.638], \
[0, 11.269, 20.060, 28.877, 35.715, 43.365, 50.000, 56.261], \
[0, 9.276,  15.775, 23.791, 30.076, 37.362, 43.739, 50.000]]


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
print (cubelesstakepoint(4,6))

