SELECT CAST(SUM(scout.plays[{}]) AS FLOAT) / {}  as {}, player.name
FROM (SELECT player.player_id as id, player.name as name, scout.match_week as s_rodada, scout.year as s_year FROM scout
LEFT JOIN player ON scout.player_id = player.player_id AND scout.year = player.year
WHERE scout.id = {}) s1, player
LEFT JOIN scout ON player.player_id = scout.player_id AND player.year = scout.year
WHERE player.player_id = s1.id AND player.year = s1.s_year
      AND scout.match_week >= s1.s_rodada - {}  AND scout.match_week < s1.s_rodada
  GROUP BY player.name;