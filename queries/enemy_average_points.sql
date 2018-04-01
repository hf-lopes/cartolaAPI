SELECT CAST(SUM(scout.points) AS FLOAT) / {}  as {}, team.id as t_id, team.name, s2.scout_id
  FROM
(SELECT CASE WHEN (team.id = match.home_team_id)
      THEN match.visiting_team_id
  ELSE match.home_team_id END as enemy_team, s1.s_year as s_year, s1.s_rodada as s_rodada, s1.scout_id as scout_id
          FROM
            (SELECT scout.id as scout_id,team.id as t_id, scout.year as s_year, scout.match_week as s_rodada
             FROM scout
            LEFT JOIN player ON scout.player_id = player.player_id AND scout.year = player.year
            LEFT JOIN team ON player.team_id = team.id
            WHERE scout.id IN {}) s1, team
      LEFT JOIN match ON team.id = match.home_team_id OR team.id = match.visiting_team_id
      WHERE team.id = s1.t_id AND match.year = s1.s_year AND match.match_week = s1.s_rodada) s2, team
      LEFT JOIN match ON team.id = match.home_team_id OR team.id = match.visiting_team_id
      LEFT JOIN scout ON match.match_week = scout.match_week and match.year = scout.year and team.id = scout.team_id
      WHERE team.id = s2.enemy_team AND match.year = s2.s_year
      AND match.match_week >= s2.s_rodada - {}  AND match.match_week < s2.s_rodada
      GROUP BY team.name, team.id, s2.scout_id
      ORDER BY s2.scout_id;