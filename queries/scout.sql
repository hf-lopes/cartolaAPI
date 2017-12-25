SELECT match_week, scout.player_id as player_id, scout.team_id as team_id, delta_price, player.position_id as position_id, scout.id FROM scout
LEFT JOIN player ON scout.player_id = player.player_id AND scout.year = player.year
WHERE scout.id = {}