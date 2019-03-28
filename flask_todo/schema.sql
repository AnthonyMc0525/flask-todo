DROP TABLE IF EXISTS items;

CREATE TABLE ITEMS (
  id bigserial,
  name varchar(100),
  complete varchar(20),
  date_added varchar(100)
);
