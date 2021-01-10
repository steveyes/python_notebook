use chekawa;


-- test_user
drop table if exists crypto_user;
create table if not exists crypto_user (
  uid int unsigned primary key not null,
	user char(32),
  role enum ('User','Adversary','ISP','Justice', 'Prover', 'Verifier','Arbitrator','Warden')
);
SELECT * from crypto_user;