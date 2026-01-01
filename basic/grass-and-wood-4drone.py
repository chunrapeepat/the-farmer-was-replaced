import utils
change_hat(Hats.Tree_Hat)
harvest()

size = get_world_size()

utils.goto(0, 0)
# utils.clean_the_land()

# set the last row to grassland
utils.goto(size-1, 0)
for gi in range(size):
    if get_ground_type() != Grounds.Grassland:
        till()
    move(North)
utils.goto(0, 0)

# deploy drone to collect grass
def collect_grass():
    utils.goto(size-1, 0)
    while True:
        harvest()
        move(North)
spawn_drone(collect_grass)
do_a_flip()
spawn_drone(collect_grass)

# collect tree
def another_drone():
    utils.goto(0, 0)
    x = 0
    y = 0
    while True:
        row = x % size
        col = y % size
        
        # reserve last row for grass generation
        if row == size - 1:
            x = 0
            y = 0
            move(East)
            continue
        else:
            harvest()
            plant(Entities.Tree)
            use_item(Items.Water, 5)
        y += 1
        move(North)
        if y % size == 0:
            x += 1
            y = 0
            move(East)

i = 0
j = 0
is_another_drone_swap = False
while True:
    row = i % size
    col = j % size

    if row == size // 2 and not is_another_drone_swap:
        spawn_drone(another_drone)
        is_another_drone_swap = True
    
    # reserve last row for grass generation
    if row == size - 1:
        i = 0
        j = 0
        move(East)
        continue
    else:
        harvest()
        plant(Entities.Tree)
        use_item(Items.Water, 5)
    j += 1
    move(North)
    if j % size == 0:
        i += 1
        j = 0
        move(East)
