with current_month as (
SELECT
	brandCode,
	count(*) AS no_of_receipts_scanned,
	strftime('%m', max(datetime (dateScanned / 1000, 'unixepoch', 'localtime'))) as mnth
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
			brandCode
			ORDER by 2 desc
			limit 5
),
previous_month as(
SELECT
	brandCode,
	count(*) AS no_of_receipts_scanned,
	strftime('%m', max(datetime (dateScanned / 1000, 'unixepoch', 'localtime'))) as mnth
	
FROM
	receipts
WHERE
	datetime (dateScanned / 1000, 'unixepoch', 'localtime') between (
		SELECT
			datetime ((SELECT
						max(datetime (dateScanned / 1000, 'unixepoch', 'localtime'))
					FROM
						receipts),
					'-2 month')) AND
		(
		SELECT
			datetime ((SELECT
						max(datetime (dateScanned / 1000, 'unixepoch', 'localtime'))
					FROM
						receipts),
					'-1 month')) 
		
			AND brandCode IS NOT NULL
		GROUP BY
			brandCode
		ORDER by 2 desc
			limit 5

)
SELECT * 
from current_month 
UNION all
select * from previous_month


-- output

-- brandCode,no_of_receipts_scanned,mnth
-- BRAND,3,02
-- MISSION,2,02
-- VIVA,1,02
-- BRAND,19,01
-- WINGSTOP,7,01
-- MISSION,5,01
-- KLEENEX,4,01
-- BORDEN,4,01


