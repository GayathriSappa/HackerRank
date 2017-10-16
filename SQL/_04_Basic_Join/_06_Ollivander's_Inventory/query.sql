/*
Enter your query here.
*/
SELECT Wands.id,
  Minimal.age,
  Minimal.coins_needed,
  Minimal.power
FROM
  (SELECT Wands.code,
     Wands_Property.age,
     min(coins_needed) as coins_needed,
     Wands.power
  FROM Wands
    LEFT JOIN Wands_Property ON Wands.code = Wands_Property.code
    WHERE is_evil != 1
    GROUP BY Wands.code, age, power) AS Minimal
LEFT JOIN Wands ON (Minimal.code, Minimal.power, Minimal.coins_needed) = (Wands.code, Wands.power, Wands.coins_needed)
ORDER BY Minimal.power DESC, Minimal.age DESC;
