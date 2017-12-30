SELECT match_week, scout.player_id as player_id, scout.team_id as team_id, delta_price, player.position_id as position_id,
 scout.id as scout_id, scout.year as year, player.name as name, scout.has_played, scout.points as score FROM scout
LEFT JOIN player ON scout.player_id = player.player_id AND scout.year = player.year
WHERE scout.id IN {}
GROUP BY match_week, scout.player_id, scout.team_id, delta_price, player.position_id, scout.id, scout.year, player.name
ORDER BY scout.id;