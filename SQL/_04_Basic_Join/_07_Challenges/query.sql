/*
Enter your query here.
*/
SELECT M.hacker_id, M.name, M.cnt
FROM  (SELECT Hackers.hacker_id,
        Hackers.name,
        count(Hackers.hacker_id) as cnt,
        (SELECT count(hacker_id) as maximum
        FROM Challenges
        GROUP BY hacker_id
        ORDER BY maximum DESC
        LIMIT 1) as maximum2
    FROM Hackers
    JOIN Challenges ON Hackers.hacker_id = Challenges.hacker_id
    GROUP BY Hackers.hacker_id, Hackers.name) AS M
JOIN (SELECT cnt,
        count(cnt) as cnt2
      FROM (SELECT hacker_id,
              count(hacker_id) as cnt
          FROM Challenges
          GROUP BY hacker_id) AS Agg
      GROUP BY cnt) AS C ON M.cnt = C.cnt
WHERE cnt2 = 1 OR M.cnt = maximum2
ORDER BY M.cnt DESC, M.hacker_id ASC;
