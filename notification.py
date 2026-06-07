import requests

url = "http://4.224.186.213/evaluation-service/notifications"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJzcnVwYW5hZzJAZ2l0YW0uaW4iLCJleHAiOjE3ODA4MTU0NDEsImlhdCI6MTc4MDgxNDU0MSwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6ImJhMGEzN2FiLTNlY2YtNDQ5NC04YmVjLWQwZTZkMmUxZjg3NyIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6InNhaSBha3NoYXlhIiwic3ViIjoiMjFlZThhNmYtNWRmNC00NGEyLWI1MmUtOTEzMTdiMmQ1NGM5In0sImVtYWlsIjoic3J1cGFuYWcyQGdpdGFtLmluIiwibmFtZSI6InNhaSBha3NoYXlhIiwicm9sbE5vIjoiMjAyMzAwNTE5MiIsImFjY2Vzc0NvZGUiOiJ3Z0t0Z1oiLCJjbGllbnRJRCI6IjIxZWU4YTZmLTVkZjQtNDRhMi1iNTJlLTkxMzE3YjJkNTRjOSIsImNsaWVudFNlY3JldCI6IkZOWnVndnZ6Qm1oeU5wc3UifQ.giSq8NHlv5D-_Pzq7HTB841BmCIkrIkt-72apW4rQeI"
}

response = requests.get(url, headers=headers)

data = response.json()

weights = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

notifications = data["notifications"]

notifications.sort(
    key=lambda x: (weights[x["Type"]], x["Timestamp"]),
    reverse=True
)

top10 = notifications[:10]

for n in top10:
    print(n["Type"], "-", n["Message"], "-", n["Timestamp"])