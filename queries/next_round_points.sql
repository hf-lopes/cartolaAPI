SELECT scout.id as scout_id,scout.points as {} FROM scout
      LEFT JOIN player ON scout.player_id = player.player_id AND scout.year = player.year
      WHERE scout.id IN {}