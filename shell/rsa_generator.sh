function ken_gen() {
    local country='CN'
    local province='Shanghai'
    local city='Shanghai'
    local OrganizationName='chekawa'
    local OrganizationUnitName='IT Dept'
    local CommonName='www.chekawa.com'

    sudo openssl req \
        -x509 \
        -nodes \
        -days 3650 \
        -newkey rsa:2048 \
        -keyout ${chekawa_cert_key} \
        -out ${chekawa_cert} \
        -subj "/C=${country}/ST=${province}/L=${city}/O=${OrganizationName}/OU=${OrganizationUnitName}/CN=${CommonName}"
    # -x509: This further modifies the previous subcommand by telling the utility that we want to make a self-signed certificate instead of generating a certificate signing request, as would normally happen.
    # -nodes: This tells OpenSSL to skip the option to secure our certificate with a passphrase. We need Nginx to be able to read the file, without user intervention, when the server starts up. A passphrase would prevent this from happening because we would have to enter it after every restart.
    # -days 3650: This option sets the length of time that the certificate will be considered valid. We set it for ten years here.
    # -newkey rsa:2048: This specifies that we want to generate a new certificate and a new key at the same time. We did not create the key that is required to sign the certificate in a previous step, so we need to create it along with the certificate. The rsa:2048 portion tells it to make an RSA key that is 2048 bits long.
    # -keyout: This line tells OpenSSL where to place the generated private key file that we are creating.
    # -out: This tells OpenSSL where to place the certificate that we are creating.