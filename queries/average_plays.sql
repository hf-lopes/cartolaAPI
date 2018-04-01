SELECT CAST(SUM(scout.plays[{}]) AS FLOAT) / {}  as {}, player.name, s1.scout_id as scout_id
FROM (SELECT scout.id as scout_id, player.player_id as id, player.name as name, scout.match_week as s_rodada,
        scout.year as s_year FROM scout
LEFT JOIN player ON scout.player_id = player.player_id AND scout.year = player.year
WHERE scout.id IN {}) s1, player
LEFT JOIN scout ON player.player_id = scout.player_id
WHERE player.player_id = s1.id AND player.year = s1.s_year
      AND ((scout.year = player.year AND scout.match_week >= s1.s_rodada - {}  AND scout.match_week < s1.s_rodada)
      OR (scout.year = player.year - 1 AND scout.match_week <= 38 AND scout.match_week > 38 - {} + s1.s_rodada))
  GROUP BY player.name, s1.scout_id
ORDER BY s1.scout_id;