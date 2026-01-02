import utils
change_hat(Hats.Pumpkin_Hat)

# Init
i = 0
j = 0
size = get_world_size()
utils.goto(0, 0)
utils.clean_the_land()

while True:
	# plant phase
	drone2_count_dead_init = None

	while i < size and j < size:
		plant(Entities.Pumpkin)
		
		if j == size // 3 + 1 and drone2_count_dead_init == None:
			def drone2_count_dead():
				dead = []
				x = 0
				y = 0
				utils.goto(0, 0)
				while x < size and y < size:
					if not can_harvest() and get_entity_type() == Entities.Dead_Pumpkin:
						dead.append([x, y])
						plant(Entities.Pumpkin)
						use_item(Items.Water)
					y += 1
					move(North)
					if y % size == 0:
						x += 1
						y = 0
						move(East)
				return dead
			drone2_count_dead_init = spawn_drone(drone2_count_dead)

		i += 1
		move(North)
		if i % size == 0:
			j += 1
			i = 0
			move(East)
	
	dead = wait_for(drone2_count_dead_init)
	
	dead1 = []
	dead2 = []
	for di in range(len(dead)):
		if (di <= len(dead) // 2):
			dead1.append(dead[di])
		else:
			dead2.append(dead[di])
	def sort_by_y(item):
		return item[1]
	
	def drone2():
		dead1 = dead2
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
	