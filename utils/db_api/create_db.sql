CREATE TABLE restaurants
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    status INTEGER NOT NULL,
    positions VARCHAR(280) NOT NULL,
    image_link VARCHAR(200),
    link VARCHAR(100),
    address VARCHAR(100) NOT NULL,
    coords VARCHAR(30)
);

alter table restaurants
    owner to postgres;

create unique index restaurants_id_uindex
    on restaurants (id);