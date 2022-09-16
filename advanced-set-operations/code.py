friends = {"Bob", "Rolf", "Anne"}
abroad_friends = {"Bob", "Rolf"}

local_friends = friends.difference(abroad_friends)

print(local_friends)

local = {"Anne"}
abroad = {"Bob", "Rolf"}

total_friends = local.union(abroad)

print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)

print(both)