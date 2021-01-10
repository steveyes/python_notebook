from Database import database

database.execute('''\
CREATE TABLE sniff_tcp(
    id SERIAL PRIMARY KEY,
    ip_src varchar(15),
    tcp_sport varchar(5),
    ip_dst varchar(15),
    tcp_dport varchar(5),
    tcp_flags varchar(6),
    tcp_seq varchar(32),
    tcp_ack varchar(32),
    ip_len varchar(6),
    ip_ihl varchar(2),
    tcp_dataofs varchar(2)
);''', fetch_one=False, auto_commit=True)
