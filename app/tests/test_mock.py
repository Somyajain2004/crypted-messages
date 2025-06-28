import requests

LOCAL_URL = "http://localhost:5000" 

def test_data():
    payload = {"data": "a"}
    res = requests.post(f"{LOCAL_URL}/data", json=payload)
    print("/data =>", res.json())

def test_time():
    res = requests.get(f"{LOCAL_URL}/time")
    print("/time =>", res.json())

def test_fizzbuzz():
    payload = {"data": "anything"}
    res = requests.post(f"{LOCAL_URL}/fizzbuzz", json=payload)
    print("/fizzbuzz =>", res.json())

def test_zap():
    payload = {"data": "a1b2c3 d4e5"}
    res = requests.post(f"{LOCAL_URL}/zap", json=payload)
    print("/zap =>", res.json())

def test_alpha():
    tests = ["a1!", "Z9", "1first", "_underscore"]
    for t in tests:
        res = requests.post(f"{LOCAL_URL}/alpha", json={"data": t})
        print(f"/alpha ({t}) =>", res.json())

def test_glitch():
    tests = ["abcdef", "abcde", "1234", "oddone"]
    for t in tests:
        res = requests.post(f"{LOCAL_URL}/glitch", json={"data": t})
        print(f"/glitch ({t}) =>", res.json())

if __name__ == "__main__":
    print("=== Testing Local Mock API ===")
    test_data()
    test_time()
    test_fizzbuzz()
    test_zap()
    test_alpha()
    test_glitch()
