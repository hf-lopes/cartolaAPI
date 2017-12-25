SELECT s1.scout_id as scout_id, scout.points as {} FROM
      (SELECT scout.id as scout_id,player.player_id as p_id, player.name as p_name, player.year as p_year,
      scout.match_week as s_round FROM scout
      LEFT JOIN player ON scout.player_id = player.player_id AND scout.year = player.year
      WHERE scout.id IN {}) s1, scout
      WHERE scout.match_week = s1.s_round + 1 AND s1.p_id = scout.player_id AND s1.p_year = scout.year
    ORDER BY scout_id;