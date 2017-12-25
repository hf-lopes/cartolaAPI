SELECT
  CASE WHEN (match.home_team_id = s1.t_id) THEN 1 ELSE 0 END as {} FROM
(SELECT team.id as t_id, scout.year as s_year, scout.match_week as s_rodada
             FROM scout
            LEFT JOIN player ON scout.player_id = player.player_id AND scout.year = player.year
            LEFT JOIN team ON player.team_id = team.id
            WHERE scout.id = {}) as s1, team
      LEFT JOIN match ON team.id = match.home_team_id OR team.id = match.visiting_team_id
      WHERE team.id = s1.t_id AND match.year = s1.s_year AND match.match_week = s1.s_rodada;