import utils
change_hat(Hats.Cactus_Hat)

total_drone=3
size = get_world_size()
utils.goto(0, 0)
utils.clean_the_land(Grounds.Soil, 4, Entities.Cactus)

while True:
	row = 0
	def bubble_sort():
		arr = []
		j = 0
		utils.goto(row, 0)
		while j < size:
			arr.append(measure())
			move(North)
			j += 1
		# now you're at the start of the row
		j = 0
		while j < size - 1:
			if arr[j] > arr[j+1]:
				swap(North)
				# swap actual arr
				tmp = arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = tmp
				# move back 1 step
				if j == 0:
					move(North)
					j += 1
					continue
				else:
					j -= 1
					move(South)
			else:
				move(North)
				j += 1

	# sort vertically
	drone_used = 0
	tasks = []
	for r in range(size):
		row = r
		t = spawn_drone(bubble_sort)
		tasks.append(t)
		drone_used += 1

		if (drone_used == total_drone):
			while len(tasks) > 0:
				t = tasks.pop()
				drone_used -= 1
				if t == None:
					continue
				wait_for(t)
		
	for drone in tasks:
		if drone != None:
			wait_for(drone)

	col = 0
	def bubble_sort_horizontally():
		arr = []
		j = 0
		utils.goto(0, col)
		while j < size:
			arr.append(measure())
			move(East)
			j += 1
		# now you're at the start of the col
		j = 0
		while j < size - 1:
			if arr[j] > arr[j+1]:
				swap(East)
				# swap actual arr
				tmp = arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = tmp
				# move back 1 step
				if j == 0:
					move(East)
					j += 1
					continue
				else:
					j -= 1
					move(West)
			else:
				move(East)
				j += 1
	
	drone_used = 0
	tasks = []
	for c in range(size):
		col = c
		t = spawn_drone(bubble_sort_horizontally)
		tasks.append(t)
		drone_used += 1

		if (drone_used == total_drone):
			while len(tasks) > 0:
				t = tasks.pop()
				drone_used -= 1
				if t == None:
					continue
				wait_for(t)

	harvest()
	utils.clean_the_land(Grounds.Soil, 4, Entities.Cactus)
