#This program operates as a simple vehicle inventory for a small car dealership
print('Automotive Inventory')
class Automobile:
    
    def __init__(self):
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._mileage = 0
    def addVehicle(self):
        try:
            self._make = input('Enter make: ')
            self._model = input('Enter model: ')
            self._year = int(input('Enter year: '))
            self._color = input('Enter color: ')
            self._mileage = int(input('Enter mileage: '))
            return True
        except ValueError:
            print('Please try again using only whole numbers for mileage and year')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self._make, self._model, self._year, self._color, self._mileage])

class Inventory:
    def __init__(self):
        self.vehicles = []
    def addVehicle(self):
        vehicle = Automobile()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            print ()
            print('Vehicle added, Thank you')
    def viewInventory(self):
        print('\t'.join(['','Make', 'Model','Year', 'Color', 'Mileage']))
        for idx, vehicle in enumerate(self.vehicles) :
            print(idx + 1, end='\t')
            print(vehicle)

inventory = Inventory()
while True:

    print ('''
    1.Add a Vehicle
    2.Delete a Vehicle
    3.View Inventory
    4.Update Inventory
    5.Export Inventory
    6.Quit
    ''')
    userInput=input('Please choose one of the above options: ') 
    if userInput=="1": 
        #add a vehicle
        inventory.addVehicle()
    elif userInput=='2':
        #delete a vehicle
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles in inventory')
            continue
        inventory.viewInventory()
        item = int(input('Enter the number associated with the vehicle to remove: '))
        if item - 1  > len(inventory.vehicles):
            print('Invalid number')
        else:
            inventory.vehicles.remove(inventory.vehicles[item - 1])
            print ()
            print('Vehicle has been removed')
    elif userInput == '3':
        #list all the vehicles
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles in inventory')
            continue
        inventory.viewInventory()
    elif userInput == '4':
        #edit vehicle 
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles in inventory')
            continue
        inventory.viewInventory()
        item = int(input('Enter the number associated with the vehicle to update: '))
        if item - 1  > len(inventory.vehicles):
            print('Invalid number')
        else:
            automobile = Automobile()
            if automobile.addVehicle() == True :
                inventory.vehicles.remove(inventory.vehicles[item - 1])
                inventory.vehicles.insert(item - 1, automobile)
                print ()
                print('Vehicle has been updated')
    elif userInput == '5':
        #export inventory to file
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles in inventory')
            continue
        f = open('vehicle_inventory.txt', 'w')
        f.write('\t'.join(['Make', 'Model','Year', 'Color', 'Mileage']))
        f.write('\n')
        for vechicle in inventory.vehicles:
            f.write('%s\n' %vechicle)
        f.close()
        print('Vehicle inventory has been exported to file')
    elif userInput == '6':
        #exit the loop
        print('Good Bye')
        break
    else:
        #invalid user input
        print('Invalid input, please try again')
