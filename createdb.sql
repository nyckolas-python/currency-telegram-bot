create table currency(
	iso_4217_code smallint primary key,
	name varchar(255),
	long_name varchar(255)

);

create table users_currency();

create table users(
    user_id integer primary key unique,
	currency_codename smallint,
	shedule_time time,
	created datetime,
	FOREIGN KEY(currency_iso_4217_code) REFERENCES currency(iso_4217_code)
);

exchange_rate_archive();