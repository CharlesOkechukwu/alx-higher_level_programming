-- count number of score records with the same score
-- organize in descending order
SELECT score, COUNT(`score`) as number FROM second_table GROUP BY score ORDER BY score Desc;
