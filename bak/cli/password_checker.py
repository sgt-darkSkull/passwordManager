import requests
import hashlib


# Check password
def request_api_data(pass_hash):
    url = 'https://api.pwnedpasswords.com/range/' + pass_hash
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(
            f'Internal error occured, Please check Your Internet connection!\nServer response {response.status_code}')
    else:
        return response


def read_response(passwords, hash):
    hash_tuple = (hashes.split(':') for hashes in passwords.text.splitlines())

    record = sorted(hash_tuple, key=lambda rec: rec[0])

    def search(record, hash):
        if len(record) < 1:
            return 0
        else:

            m = len(record) // 2
            if record[m][0] == hash:
                return record[m][1]
            elif record[m][0] > hash:
                return search(record[:m], hash)
            else:
                return search(record[m + 1:], hash)

    return search(record, hash)


def check_password_api(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    first_char, rem_char = sha1password[:5], sha1password[5:]
    response = request_api_data(first_char)

    return read_response(response, rem_char)


def main():
    try:

        print('Enter password', end=' : ')
        passwd = input()

        count = check_password_api(passwd)

        if count:
            print(f'Your password was found in {count} data breaches')
        else:
            print('Password is good to Go, Safe and Secure!')
    except:
        raise RuntimeError(f'An error occurred, check your internet connection')
