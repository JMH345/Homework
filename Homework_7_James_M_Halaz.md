# Homework 7
### James M. Halaz
____
# Section 7.1

## Question 1
```SQL
SELECT ModelYear, Make, Model
FROM EVRegistry;
```

## Question 2
```SQL
SELECT DISTINCT ElectricVehicleType
FROM EVRegistry;
```

## Question 3
```SQL
SELECT *
FROM EVRegistry
WHERE ElectricVehicleType = "Battery Electric Vehicle (BEV)";
```

## Question 4
```SQL
SELECT Make, Model
FROM EVRegistry
WHERE BaseMSRP BETWEEN 20000 AND 35000;
```

# Section 7.2

## Question 1
```SQL
SELECT *
FROM EVRegistry
WHERE City IS NULL;
```

## Question 2
```SQL
SELECT Make, Model, ElectricVehicleType
FROM EVRegistry
WHERE VIN LIKE "%3E1EA1J";
```

## Question 3
```SQL
SELECT ModelYear, Make, Model, ElectricVehicleType, "Range"
FROM EVRegistry
WHERE Make = "TESLA" OR Make = "CHEVROLET"
ORDER BY Make, ModelYear DESC;
```

## Question 4
```SQL
SELECT stationId, COUNT(sessionId) as stationUSE
FROM EVCharging
GROUP BY stationId
ORDER BY stationUSE DESC
LIMIT 5;
```

## Question 5
```SQL
SELECT userId, MIN(chargeTimeHrs) as minTime, MAX(chargeTimeHrs) as maxTime
FROM EVCharging
GROUP BY userId
HAVING chargeTimeHrs > 0.5
ORDER BY minTime ASC, maxTime DESC
```

# Section 7.3

## Question 1
```SQL
SELECT weekday, ROUND(AVG(chargeTimeHrs),2) as chargeHrsAvg
FROM EVCharging
GROUP BY weekday
ORDER BY chargeHrsAvg DESC
LIMIT 1;
```

## Question 2
```SQL
SELECT userId, ROUND(SUM(kwhTotal),2) as totalPower
FROM EVCharging
GROUP BY userId
ORDER BY totalPower DESC
LIMIT 15;
```

## Question 3
```SQL
SELECT df.typeFacility, COUNT(DISTINCT fc.stationID) as numStation
FROM factCharge fc
INNER JOIN dimFacility df
ON fc.facilityID = df.FacilityKey
GROUP BY df.typeFacility
ORDER BY numStation DESC
```

## Question 4

* The primary key is the main index of the table you obtain your data from in the `FROM` clause. It has to have unique values and be void of NULL values. The foreign is the main index of the table you connect with you `JOIN` clause. It also must have unique values. The primary purpose is to have two matching or close to matching columns of data in order to merge two tables.

## Question 5
```SQL
SELECT userId, MIN(chargeTimeHrs) as minTime, MAX(chargeTimeHrs) as maxTime
FROM EVCharging
GROUP BY userId
HAVING chargeTimeHrs > 1
ORDER BY minTime ASC, maxTime DESC