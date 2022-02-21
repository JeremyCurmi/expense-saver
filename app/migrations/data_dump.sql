insert into products (name, description, updated_at)
values ('eggs', 'corn fed', now()),
    ('apples', 'green', now());
insert into shops (name)
values ('pama'),
    ('chains');
insert into product_shops (product_id, shop_id, price)
values (1, 1, 2.0),
    (1, 2, 2.1),
    (2, 1, 1.0);
insert into categories (name)
values ('food'),
    ('drink');
insert into product_categories (product_id, category_id)
values (1, 1),
    (2, 1);