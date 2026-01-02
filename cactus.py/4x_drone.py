import utils
change_hat(Hats.Cactus_Hat)

total_drone=4
size = get_world_size()
utils.goto(0, 0)
utils.clean_the_land(entity=Entities.Cactus)

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