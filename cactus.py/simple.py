import utils
change_hat(Hats.Cactus_Hat)
harvest()

i = 0
j = 0
size = get_world_size()

utils.goto(0, 0)
# utils.clean_the_land()

is_drone2_swap = False

def drone2():
	utils.goto(0, 0)
	i = 0
	j = 0
	while True:
		harvest()
		plant(Entities.Cactus)
		use_item(Items.Water, 3)		
		j += 1
		move(North)
		if j % size == 0:
			i += 1
			j = 0
			move(East)
	
while True:
	harvest()
	plant(Entities.Cactus)
	
	if i == 7 and not is_drone2_swap:
		spawn_drone(drone2)
	
	j += 1
	move(North)
	if j % size == 0:
		i += 1
		j = 0
		move(East)