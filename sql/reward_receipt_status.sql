SELECT
	rewardsReceiptStatus,
	sum(purchasedItemCount) AS total_items_purchased,
	round(avg(totalSpent)) AS average_amount
FROM
	receipts
GROUP BY
	rewardsReceiptStatus
ORDER BY
	3 DESC;

-- output 

-- rewardsReceiptStatus,total_items_purchased,average_amount
-- FLAGGED,1014,180.0
-- FINISHED,8184,81.0
-- PENDING,0,27.0
-- REJECTED,173,23.0
-- SUBMITTED,0,0.0


-- accepted>rejected - amount
-- accepted > rejected - count purchased