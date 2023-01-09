SELECT
	brandCode,
	count(*) AS no_of_receipts_scanned
FROM
	receipts
WHERE
	datetime (dateScanned / 1000, 'unixepoch', 'localtime') >= (
		SELECT
			datetime ((
					SELECT
						max(datetime (dateScanned / 1000, 'unixepoch', 'localtime'))
					FROM
						receipts),
					'-1 month'))
			AND brandCode IS NOT NULL
		GROUP BY
			brandCode;

-- output

-- brandCode,no_of_receipts_scanned
-- BRAND,3
-- MISSION,2
-- VIVA,1
