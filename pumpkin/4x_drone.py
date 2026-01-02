import utils
change_hat(Hats.Pumpkin_Hat)

# Init
size = get_world_size()
utils.goto(0, 0)
# utils.clean_the_land()

while True:
	plant_start_i = 0
	plant_end_i = 0

	def plant_the_pumpkin():
		i = plant_start_i
		j = 0
		utils.goto(i, j)
		while i <= plant_end_i and j < size:
			plant(Entities.Pumpkin)
			use_item(Items.Water)

			j += 1
			move(North)
			if j % size == 0:
				i += 1
				j = 0
				move(East)
		return True

	def fix_bad_yield():
		i = plant_start_i
		j = 0
		utils.goto(i, j)
		while i <= plant_end_i:
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

	# first half
	plant_start_i = 0
	plant_end_i = size // 2
	a = spawn_drone(plant_the_pumpkin)
	do_a_flip()
	b = spawn_drone(fix_bad_yield)

	# second half
	plant_start_i = size // 2 + 1
	plant_end_i = size - 1
	c = spawn_drone(plant_the_pumpkin)
	do_a_flip()
	fix_bad_yield()
	wait_for(a)
	wait_for(b)
	wait_for(c)
	
	harvest()