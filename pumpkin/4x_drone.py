import utils
change_hat(Hats.Pumpkin_Hat)

# Init
size = get_world_size()
utils.goto(0, 0)
utils.clean_the_land()

drone_tasks = []
total_drone = 4

global plant_start_i
global plant_end_i
def plant():
	i = plant_start_i
	j = 0
	utils.goto(i, j)
	while i <= plant_end_i and j < size:
		plant(Entities.Pumpkin)
		use_item(Items.Water)
		i += 1
		move(North)

		if i % size == 0:
			j += 1
			i = 0
			move(East)
	return True

global fix_start_i
global fix_end_i
def fix_bad_yield():
	i = fix_start_i
	j = 0
	utils.goto(i, j)
	while i <= fix_end_i:
		if not can_harvest() and get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
			use_item(Items.Water)
			continue
		if can_harvest() and get_entity_type() == Entities.Pumpkin:
			j += 1
			move(North)
			if j % size == 0:
				i += 1
				j = 0
				move(East)
	return True

while True:
	# plant
	plant_start_i = 0
	plant_end_i = size // 2
	spawn_drone(plant)
	plant_start_i += 1
	plant_end_i = size - 1
	spawn_drone(plant)

	# fix bad yield
	fix_start_i = 0
	fix_end_i = size // 2
	spawn_drone(fix_bad_yield)

	fix_start_i += 1
	fix_end_i = size - 1
	fix_bad_yield()
	
	harvest()