1.The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
2.The domain must be exactly '@leetcode.com' in lowercase.
# Write your MySQL query statement below
select * from users where mail regexp '^[A-Za-z][A-Za-z0-9_.-]*@leetcode.com' ;
