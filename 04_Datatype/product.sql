-- create the Product table and load data into it.

DROP TABLE product;
CREATE TABLE product
( 
    product_category varchar(255),
    brand varchar(255),
    product_name varchar(255),
    price int,
    realse_date date,
    sales int8
);

-- add the column with in alter command

alter table product  add column sales int8;


INSERT INTO product VALUES
('Phone', 'Apple', 'iPhone 12 Pro Max', 1300,'12-02-2001',1200),
('Phone', 'Apple', 'iPhone 12 Pro', 1100,'12-02-1989',1233),
('Phone', 'Apple', 'iPhone 12', 1000,'11-01-2001',2333),
('Phone', 'Samsung', 'Galaxy Z Fold 3', 1800,'11-01-1980',2673),
('Phone', 'Samsung', 'Galaxy Z Flip 3', 1000,'11-01-2001',2653),
('Phone', 'Samsung', 'Galaxy Note 20', 1200,'11-01-1991',2387),
('Phone', 'Samsung', 'Galaxy S21', 1000,'11-01-2007',2303),
('Phone', 'OnePlus', 'OnePlus Nord', 300,'11-02-2001',2389),
('Phone', 'OnePlus', 'OnePlus 9', 800,'01-01-2000',2363),
('Phone', 'Google', 'Pixel 5', 600,'11-01-1991',2383),
('Laptop', 'Apple', 'MacBook Pro 13', 2000,'11-01-1981',2373),
('Laptop', 'Apple', 'MacBook Air', 1200,'11-01-1981',2763),
('Laptop', 'Microsoft', 'Surface Laptop 4', 2100,'11-01-1988',2333),
('Laptop', 'Dell', 'XPS 13', 2000,'11-01-2012',2333),
('Laptop', 'Dell', 'XPS 15', 2300,'11-01-2001',2333),
('Laptop', 'Dell', 'XPS 17', 2500,'11-01-2001',2333),
('Earphone', 'Apple', 'AirPods Pro', 280,'11-01-2001',2333),
('Earphone', 'Samsung', 'Galaxy Buds Pro', 220,'11-01-2001',233),
('Earphone', 'Samsung', 'Galaxy Buds Live', 170,'11-01-2001',233),
('Earphone', 'Sony', 'WF-1000XM4', 250,'11-01-2001',273),
('Headphone', 'Sony', 'WH-1000XM4', 400,'11-01-2002',2563),
('Headphone', 'Apple', 'AirPods Max', 550,'11-01-2001',2312),
('Headphone', 'Microsoft', 'Surface Headphones 2', 250,'11-01-2011',2113),
('Smartwatch', 'Apple', 'Apple Watch Series 6', 1000,'11-01-2001',2312),
('Smartwatch', 'Apple', 'Apple Watch SE', 400,'11-01-2001',2312),
('Smartwatch', 'Samsung', 'Galaxy Watch 4', 600,'11-01-2001',2312),
('Smartwatch', 'OnePlus', 'OnePlus Watch', 220,'11-01-2001',2333);
COMMIT;



select * from product;

-- Write query to display the most expensive product under each category (corresponding to each record)

select *, first_value(product_name) over(partition by product_category order by price desc) as most_expensive_product from product;



-- Write query to display the least expensive product under each category (corresponding to each record)

select *, first_value(product_name)  over(partition by product_category order by price desc) as most_exp_product,
last_value(product_name) 
    over(partition by product_category order by price desc
        range between unbounded preceding and unbounded following) 
    as least_exp_product    
from product WHERE product_category ='Phone';



-- Alternate way to write SQL query using Window functions
select *,
first_value(product_name) over w as most_exp_product,
last_value(product_name) over w as least_exp_product    
from product
WHERE product_category ='Phone'
window w as (partition by product_category order by price desc
            range between unbounded preceding and unbounded following);
            

            
-- NTH_VALUE 
-- Write query to display the Second most expensive product under each category.
select *,
first_value(product_name) over w as most_exp_product,
last_value(product_name) over w as least_exp_product,
nth_value(product_name, 5) over w as second_most_exp_product
from product
window w as (partition by product_category order by price desc
            range between unbounded preceding and unbounded following);



-- NTILE
-- Write a query to segregate all the expensive phones, mid range phones and the cheaper phones.
select x.product_name, 
case when x.buckets = 1 then 'Expensive Phones'
     when x.buckets = 2 then 'Mid Range Phones'
     when x.buckets = 3 then 'Cheaper Phones' END as Phone_Category
from (
    select *,
    ntile(3) over (order by price desc) as buckets
    from product
    where product_category = 'Phone') x;




-- CUME_DIST (cumulative distribution) ; 
/*  Formula = Current Row no (or Row No with value same as current row) / Total no of rows */

-- Query to fetch all products which are constituting the first 30% 
-- of the data in products table based on price.
select product_name, cume_dist_percetage
from (
    select *,
    cume_dist() over (order by price desc) as cume_distribution,
    round(cume_dist() over (order by price desc)::numeric * 100,2)||'%' as cume_dist_percetage
    from product) x
where x.cume_distribution <= 0.3;




-- PERCENT_RANK (relative rank of the current row / Percentage Ranking)
/* Formula = Current Row No - 1 / Total no of rows - 1 */

-- Query to identify how much percentage more expensive is "Galaxy Z Fold 3" when compared to all products.
select product_name, per
from (
    select *,
    percent_rank() over(order by price) ,
    round(percent_rank() over(order by price)::numeric * 100, 2) as per
    from product) x
where x.product_name='Galaxy Z Fold 3';

