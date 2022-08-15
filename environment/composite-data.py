import csv
import copy

myVehicle = {
    "vin": "",
    "make": "",
    "model": "",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

for key,value in myVehicle.items():
    print ("{} : {}".format(key,value))
    # print (f"{key} : {value}")
    

myInventoryList = []

with open('car_fleet.csv') as csvFile:
    # print (csvFile)
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    # print (csvReader)
    for row in csvReader:
        if lineCount == 0:
            print("Column names are {}" .format( ", ".join(row) ))
            lineCount += 1
            # lineCount = lineCOunt + 1
        else:
            print ("vin: {} make: {} model: {} year: {} range: {} topSpeed: {} zeroSixty: {} mileage: {}".format(row[0],row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            # print (f"vin: {row[0]} make: {row[1]} model: {row[2]} year: {row[3]} range: {row[4]} topSpeed: {row[5]} zeroSixty: {row[6]} mileage: {row[7]}")
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            
            myInventoryList.append(currentVehicle)
            lineCount += 1
            # lineCount = lineCount + 1
    print ("Processed {} lines".format(lineCount))

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print ("{}: {}".format(key, value))
    print ("-----------------")
        # print (f"{key} , {value}")

# print (myInventoryList)