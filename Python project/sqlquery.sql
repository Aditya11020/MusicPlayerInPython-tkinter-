create table Users(U_id int IDENTITY(1,1) primary key , U_email varchar(30),U_name varchar(30) not null, U_ph numeric(10),U_pass varchar(15))
select * from Users