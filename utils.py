def clean_the_land(ground = Grounds.Soil, total_drone = 4):
	i = 0
	j = 0
	size = get_world_size()
	
	while i < size and j < size:
		if can_harvest():
			harvest()
		else:
			till()
		if get_ground_type() != ground:
			till()
		
		i += 1
		move(North)
		if i % size == 0:
			j += 1
			i = 0
			move(East)
			
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