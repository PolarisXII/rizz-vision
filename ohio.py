from pprint import pp

from httpx import post, get, Response


url = "http://0.0.0.0:8000"


def report(re: Response):
    print(re)
    pp(re.json())
    print()
    return re.json()


ucount = report(get(url + "/users"))

id = report(
    post(
        url + "/self",
        json={"name": "Ohio Rizzler", "password": "plaintext~<3"},
    )
)


report(post(url + f"/upimage/{id}", json={"image": "asd"}))
