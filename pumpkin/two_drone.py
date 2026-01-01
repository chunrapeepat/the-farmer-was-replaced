import utils
change_hat(Hats.Pumpkin_Hat)

i = 0
j = 0
size = get_world_size()
utils.goto(0, 0)
utils.clean_the_land()

drone2_dead = []

def drone2():
	dead1 = drone2_dead
	while len(dead1) > 0:
		removed = []
		for index in range(len(dead1)):
			d = dead1[index]
			utils.goto(d[0], d[1])
			if not can_harvest() and get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
				use_item(Items.Water)
				continue
			if can_harvest():
				removed.append(d)
		for index in range(len(removed)):
			dead1.remove(removed[index])
	return True

while True:
	# plant
	while i < size  and j < size:
		plant(Entities.Pumpkin)
		
		i += 1
		move(North)
		if i % size == 0:
			j += 1
			i = 0
			move(East)
	
	dead = []
	i = 0
	j = 0
	while i < size and j < size:
		if not can_harvest() and get_entity_type() == Entities.Dead_Pumpkin:
			dead.append([i, j])
			plant(Entities.Pumpkin)
			use_item(Items.Water)
		j += 1
		move(North)
		if j % size == 0:
			i += 1
			j = 0
			move(East)
	
	dead1 = []
	dead2 = []
	for di in range(len(dead)):
		if (di <= len(dead) // 2):
			dead1.append(dead[di])
		else:
			dead2.append(dead[di])
	
	drone2_dead = dead2
	drone2_task = spawn_drone(drone2)
			
	while len(dead1) > 0:
		removed = []
		for index in range(len(dead1)):
			d = dead1[index]
			utils.goto(d[0], d[1])
			if not can_harvest() and get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
				use_item(Items.Water)
				continue
			if can_harvest():
				removed.append(d)
		for index in range(len(removed)):
			dead1.remove(removed[index])
			
	wait_for(drone2_task)
	
	harvest()
	utils.goto(0, 0)
	i = 0
	j = 0