def rental_car_cost(d):
    carRent = d * 40
    if d >=7:
        carRent = carRent - 50
    elif d >= 3:
        carRent = carRent - 20
    
    return carRent
    f"The total cost for your rental car is {carRent}"