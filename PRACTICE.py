print("Welcome to the NEED FOR SPEED contest")
car_number = int(input("Enter the car's number  : "))
Position_1 = int(input(f"Enter the position of the car from the starting line : "))
Speed_1    = int(input("Enter the speed of the car at the starting line : "))
car_number2 = int(input("Enter the car's number  : "))
Position_2 = int(input(f"Enter the position of the car {car_number2} from the starting line : "))
Speed_2    = int(input("Enter the speed of the car at the starting line : "))
print(f"Car 1 starts at position {Position_1} meters and has a speed of {Speed_1} meters per time step.")
print(f"Car 2 starts at position {Position_2} meters and has a speed of {Speed_2} meters per time step.")
if Position_1<Position_2 :
    while Position_1 <= Position_2 and Position_2< 50 and Position_1<50:
        Position_1 = Position_1+Speed_1
        Position_2 = Position_2+Speed_2
        distance_1 = Position_1 * Speed_1
        distance_2 = Position_2 * Speed_2
        print(Position_1 , Position_2)
else :
    while Position_2 <= Position_1 and Position_1< 50 and Position_2<50:
        Position_1 = Position_1+Speed_1
        Position_2 = Position_2+Speed_2
        distance_1 = Position_1 * Speed_1
        distance_2 = Position_2 * Speed_2
        print(Position_1 , Position_2)
if Position_1 > Position_2 :
    print("Car 1 won the race !")
elif Position_1 > 50 :
    print("Car 1 won the race !")
elif Position_1 > Position_2 :
    print("Car 2 won the race !")
elif Position_2 >50 :
    print("Car 2 won the race !")



