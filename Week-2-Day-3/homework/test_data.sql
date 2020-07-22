-- 需要提前插入的测试数据
insert into product (name, price, category, num)
values ('iPhoneXX',9999.00,'手机',99),
('大辣条',19.00,'零食',99),
('大猪蹄子',29.00,'熟食',99),
('棒棒糖',9.00,'零食',99),
('如何交女朋友',39.00,'书籍',99);


insert into user (username, password, role)
values ('admin', '123456', 'admin'),
('robin', '123456', 'user'),
('david', '123456', 'user'),
('pony', '123456', 'user'),
('jack', '123456', 'user');

insert into user_order (user_id, product_id)
values (1,2),(2,3),(1,3),(1,4),(1,5),(2,3);

