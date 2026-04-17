fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

print()
count = 0

while count < len(fish_list):
    fish = fish_list[count]
    print(fish)
    if fish == 'Nemo':
        break
    count += 1


    