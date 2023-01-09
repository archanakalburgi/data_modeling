## Question 1
What are the top 5 brands by receipts scanned for most recent month?

Top 5 brands by receipts scanned for most recent month are obtained using following queries 

```
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
						max(datetime (dateScanned / 1000, 'unixepoch','localtime'))
					FROM
						receipts),
					'-1 month'))
			AND brandCode IS NOT NULL
		GROUP BY
			brandCode
```

According to the query result, the top brands are `BRAND`, `MISSION`, and `VIVA`

## Question 2
How does the ranking of the top 5 brands by receipts scanned for the recent month compare to the ranking for the previous month?

```
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
SELECT * from previous_month
```

According the query results the ranking of top brands of the current month are 

| BrandCode | Rank |
|-----------|------|
| BRAND   |   1    |
| WINGSTOP  |  2  |
| MISSION  |   3  |
| KLEENEX  |   4  |
| BORDEN  |   5   |


where as the top 5 products of the previous month are
| Brandcode | Rank |
|-----------|------|
| BRAND | 1 |
| MISSION | 2 |
| VIVA | 3 |



## Question 3
When considering average spend from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?

This question can be answered using following query 
```
SELECT
	rewardsReceiptStatus,
	round(avg(totalSpent)) AS average_amount
FROM
	receipts
GROUP BY
	rewardsReceiptStatus
ORDER BY
	3 DESC
```

The average spend from receipts with rewardsReceiptStatus of Accepted is greater than the rewardsReceiptStatus of Rejected

**Assumptions made while making this calculations**
- One of the  data quality issues is that the rewardsReceiptStatus does not have Accepted status, to tackle the issue I have assumed Finished as the the Accepted

## Question 4
When considering total number of items purchased from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?

Following query was run against the dataset to answer the question 

```
SELECT
	rewardsReceiptStatus,
	round(avg(totalSpent)) AS average_amount
FROM
	receipts
GROUP BY
	rewardsReceiptStatus
ORDER BY
	3 DESC
```

The total number of items purchased from receipts with of Accepted is greater than the rewardsReceiptStatus of Rejected

**Assumptions made while making this calculations**
- One of the  data quality issues is that the rewardsReceiptStatus does not have Accepted status, to tackle the issue I have assumed Finished as the the Accepted


## Question 5
Which brand has the most spend among users who were created within the past 6 months?

This following query is run against the data to answer the question above

```
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
	3 DESC
```

The brand with most spend among users who were created within the past 6 months are 

| BrandCode | Amount |
|-----------|--------|
| BRAND | 2420.0 |
| MISSION | 171.71 |
| WONDERFUL | 53.94 |
| HY-VEE | 29.94 |
| ORAL-B GLIDE | 23.94 |
| BORDEN | 20.41 |
| KLEENEX | 18.91 |
| PEPSI | 6.48 |
| GERM-X | 4.58 |
| CHEERIOS | 3.49 |
| AMERICAN BEAUTY | 0.89 |


## Question 6
Which brand has the most transactions among users who were created within the past 6 months?

Using same query as the one used to answer Question 5 we can see these are the brand has the most transactions among users who were created within the past 6 months

| BrandCode| Transactions|
|-------|----|
| BRAND | 11 |
| MISSION | 11 |
| WONDERFUL | 6 |
| HY-VEE | 6 |
| ORAL-B GLIDE | 6 |
| BORDEN | 1 |
| KLEENEX | 1 |
| PEPSI | 3 |
| GERM-X | 2 |
| CHEERIOS | 1 |
| AMERICAN BEAUTY | 1 |
