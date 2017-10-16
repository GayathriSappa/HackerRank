SELECT N.hacker_id, H.name
FROM (SELECT M.submission_id, M.hacker_id, M.challenge_id, M.difficulty_level, M.score 
FROM (SELECT S.submission_id, S.hacker_id, S.challenge_id, S.score, C.difficulty_level 
    FROM Submissions S JOIN Challenges C ON S.challenge_id = C.challenge_id) as M 
    JOIN Difficulty D ON M.difficulty_level = D.difficulty_level WHERE M.score = D.score) as N 
JOIN Hackers H ON N.hacker_id = H.hacker_id 
GROUP BY name, hacker_id HAVING COUNT(name) > 1 
ORDER BY COUNT(name) DESC, hacker_id ASC;
