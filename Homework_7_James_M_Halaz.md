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