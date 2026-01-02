import utils
change_hat(Hats.Cactus_Hat)

total_drone=4
size = get_world_size()
utils.goto(0, 0)
utils.clean_the_land(entity=Entities.Cactus)

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

    bubble_sort()
    break
