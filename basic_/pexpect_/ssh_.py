import signal

import pexpect


def sigterm(signum, frame):
    if signum == signal.SIGTERM or signum == signal.SIGINT:
        print('*** SIGTERM/SIGINT received, exiting...')
        exit(0)


def send_cmd(child: pexpect.spawn, cmd):
    prompt = ['# ', '>>> ', '> ', '\$ ']
    child.sendline(cmd)
    child.expect(prompt)
    print(child.before.decode())


def wait_for(child: pexpect.spawn, pattern: str, answer: str):
    countdown = 1024
    while True:
        hit = child.expect([pattern, pexpect.TIMEOUT, pexpect.EOF], timeout=15)
        if hit == 0:
            if answer and len(answer):
                child.sendline(answer)
            return 0
        if hit == 1:
            print('timeout on pattern : ', pattern)
            sigterm(signal.SIGTERM, None)
            return 1
        if hit == 2:
            countdown -= 1
            if countdown == 0:
                print('too much EOF on pattern : ', pattern)
                return 2


def connect(host, user, password):
    expect_newssh = "Are you sure you want to continue connecting"
    expect_password = "[p|P]assword:"
    cmd = f"ssh {user}@{host}"
    child = pexpect.spawn(cmd)

    err = wait_for(child, expect_password, password)
    if err == 1:
        wait_for(child, expect_newssh, 'yes')
        wait_for(child, expect_password, password)
    elif err == 2:
        pass

    return child


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, sigterm)
    signal.signal(signal.SIGINT, sigterm)
    child = connect('192.168.6.102', 'scott', 'scott123')
    send_cmd(child, 'ls -ltr')
