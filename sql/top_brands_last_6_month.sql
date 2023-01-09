WITH amount_spent AS (
	SELECT
		brandCode,
		userId AS user_id,
		sum(finalPrice) AS amount
	FROM
		receipts
	WHERE
		brandCode NOT NULL
	GROUP BY
		brandCode
	ORDER BY
		2 DESC
),
recent_users AS (
	SELECT
		id AS user_id,
		datetime (createdDate / 1000,
			'unixepoch',
			'localtime') AS created_date
	FROM
		users
	WHERE
		datetime (createdDate / 1000,
			'unixepoch',
			'localtime') >= (
			SELECT
				datetime ((
						SELECT
							max(datetime (createdDate / 1000,
									'unixepoch',
									'localtime'))
						FROM
							users),
						'-6 month'))
),
final AS (
	SELECT
		ru.user_id,
		ru.created_date,
		amt.brandCode,
		amt.amount
	FROM
		recent_users ru
		JOIN amount_spent amt ON ru.user_id = amt.user_id
)
SELECT
	brandCode,
	count(*) as no_of_transaction,
	sum(amount) as total_amount_spent
FROM
	final
GROUP BY
	brandCode
ORDER BY
	3 DESC;



-- output 

-- brandCode,no_of_transaction,total_amount_spent

-- BRAND,11,2420.0
-- MISSION,11,171.71
-- WONDERFUL,6,53.94
-- HY-VEE,6,29.94
-- ORAL-B GLIDE,6,23.94
-- BORDEN,1,20.41
-- KLEENEX,1,18.91
-- PEPSI,3,6.48
-- GERM-X,2,4.58
-- CHEERIOS,1,3.49
-- AMERICAN BEAUTY,1,0.89
