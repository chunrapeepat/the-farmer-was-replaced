def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
		
def goto(i, j):
	x = get_pos_x()
	y = get_pos_y()
	diff_x = x - i
	diff_y = y - j
	if diff_x > 0:
		move_n_dir(diff_x, West)
	else:
		move_n_dir(-diff_x, East)
	if diff_y > 0:
		move_n_dir(diff_y, South)
	else:
		move_n_dir(-diff_y, North)

def clean_the_land(ground = Grounds.Soil, total_drone = 4, entity = None):
	size = get_world_size()

	start_i = 0
	end_i = 0
	def clean_area():
		i = start_i
		j = 0
		goto(i, j)
		while i <= end_i and j < size:
			if can_harvest():
				harvest()
			else:
				till()
			if get_ground_type() != ground:
				till()
			if entity != None:
				plant(entity)
			j += 1
			move(North)
			if j % size == 0:
				i += 1
				j = 0
				move(East)
		return True

	for i in range(total_drone):
		start_i = i * (size // total_drone)
		end_i = start_i + (size // total_drone - 1)
		if i == total_drone - 1:
			end_i = size - 1
			clean_area()
		else:
			spawn_drone(clean_area)