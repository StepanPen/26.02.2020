def season(month):
    if month < 3 or month  == 12:
        return "Winter"
    if 3 <= month < 6:
        return "Spring"
    if 6 <= month < 9:
        return "Summer"
    if 9 <= month < 12:
        return "Autumn"
b = 1
while b<13:
    print(b)
    print(season (b))
    b+=1