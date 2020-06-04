#5.6 好玩游戏的物品清单

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    for i ,j in inventory.items():
        print(j," ",i)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
#print(inv)