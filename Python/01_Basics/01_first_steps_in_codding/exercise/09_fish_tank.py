length = int(input())
width = int(input())
height = int(input())
percent = float(input())/100

tank_volume = length*width*height
litres = tank_volume/1000

total = litres-(litres*percent)

print(total)
