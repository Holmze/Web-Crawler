
create table books
(
bTitle varchar(512) primary key,
bAuthor varchar(256),
bPublisher varchar(256),
bDate varchar(32),
bPrice varchar(16),
bDetail text,
);
select * from books
drop table books
--exec sys.sp_readerrorlog 0, 1, 'listening'