from scapy.all import *
from basic_.psycopg2_.src_.Database import database

SQL_STMT = 'INSERT INTO sniff_tcp (ip_src, tcp_sport, ip_dst, tcp_dport, tcp_flags, tcp_seq, tcp_ack, ip_len, ip_ihl, tcp_dataofs) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'


def pkg_callback(pkg):
    out = pkg.sprintf(
        '%IP.src%:'
        '%r,TCP.sport%:'
        '%IP.dst%:'
        '%r,TCP.dport%:'
        '%TCP.flags%:'
        '%TCP.seq%:'
        '%TCP.ack%:'
        '%IP.len%:'
        '%IP.ihl%:'
        '%TCP.dataofs%:'
        # '%TCP.payload%'
    )

    pkgs = out.split(':', 10)[:10]
    while True:
        pkgss_len = 0
        pkgss = []
        while pkgss_len <= 99:
            pkgss.append(pkgs)
            pkgss_len += 1

        database.execute(sql_stmt=SQL_STMT, sql_data=pkgss, execute_many=True, auto_commit=True)


if __name__ == '__main__':
    sniff(filter='tcp', prn=pkg_callback)
