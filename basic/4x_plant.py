import utils
change_hat(Hats.Tree_Hat)
harvest()

total_drone = 4
ground = Grounds.Soil
entity = Entities.Tree
water = 6
delay = 10

size = get_world_size()
utils.goto(0, 0)
utils.clean_the_land(ground)

def harvest_and_plant():
	utils.goto(0, 0)
	i = 0
	j = 0
	while True:
		harvest()
		plant(entity)
		use_item(Items.Water, water)		
		j += 1
		move(North)
		if j % size == 0:
			i += 1
			j = 0
			move(East)

for i in range(total_drone - 1):
	spawn_drone(harvest_and_plant)
	for i in range(delay):
		do_a_flip()

harvest_and_plant()