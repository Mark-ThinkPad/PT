-- 建表
drop table if exists product;
create table product(
    id integer primary key autoincrement,
    name varchar(20) not null,
    price decimal(10,2) not null,
    category varchar(20) null,
    num integer not null default(0)
);

drop table if exists user;
create table user(
    id integer primary key autoincrement,
    username varchar(20) not null unique,
    password varchar(20) not null,
    role varchar(20) not null default('user'),
    created datetime default(datetime('now','localtime'))
);

drop table if exists user_order;
create table user_order(
    id integer primary key autoincrement,
    user_id integer not null,
    product_id integer not null,
    created datetime default(datetime('now', 'localtime')),
    foreign key(user_id) references user(id),
    foreign key(product_id) references product(id)
)
