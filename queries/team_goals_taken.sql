SELECT CAST(SUM(
          CASE WHEN team.id = match.home_team_id
          THEN match.visiting_score
          ELSE match.home_score END) AS FLOAT) / {} as {}, team.name, team.id, s1.scout_id as scout_id
        FROM
            (SELECT  scout.id as scout_id, team.id as t_id, scout.year as s_year, scout.match_week as s_rodada
             FROM scout
            LEFT JOIN player ON scout.player_id = player.player_id AND scout.year = player.year
            LEFT JOIN team ON player.team_id = team.id
            WHERE scout.id IN {}) s1, team
      LEFT JOIN match ON team.id = match.home_team_id OR team.id = match.visiting_team_id
      WHERE team.id = s1.t_id AND match.year = s1.s_year
            AND match.match_week >= s1.s_rodada - {}  AND match.match_week < s1.s_rodada
      GROUP BY team.name, team.id, s1.scout_id
ORDER BY s1.scout_id;