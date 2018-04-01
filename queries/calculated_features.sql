SELECT scout_id, feature_array, points FROM descriptors
LEFT JOIN scout ON descriptors.scout_id = scout.id
WHERE hash = CAST({} AS VARCHAR(50)) AND has_played = TRUE