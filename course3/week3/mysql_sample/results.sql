use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select name from store;

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct store.store_id from store join sale on store.store_id = sale.store_id where sale.quantity >= 1;

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select distinct store.store_id from store left join sale on store.store_id = sale.store_id where quantity is null;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select product.name, avg(sale.total/sale.quantity) from product join sale on product.product_id = sale.product_id group by product.name;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select product.name from product join sale on product.product_id = sale.product_id group by sale.product_id having count(distinct sale.store_id) = 1;

-- 8. Получить названия всех складов, с которых продавался только один продукт
select store.name from store join sale on store.store_id = sale.store_id group by sale.store_id having count(distinct sale.product_id)=1;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale where sale.total = (select total from sale order by total desc limit 1 );

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from sale order by date, total desc limit 1;
