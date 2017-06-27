/*
Enter your query here.
*/
SELECT S.hacker_id, name, Sum 
FROM (SELECT hacker_id, SUM(Max) Sum FROM (SELECT hacker_id, MAX(score) Max 
    FROM Submissions GROUP BY hacker_id, challenge_id) as M  
    GROUP BY hacker_id) as S JOIN Hackers H 
WHERE S.hacker_id = H.hacker_id AND Sum > 0 ORDER BY Sum DESC, S.hacker_id;
