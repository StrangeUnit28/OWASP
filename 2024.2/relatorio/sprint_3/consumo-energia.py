import requests

url = "http://localhost:8000/api/recommendation/"

cookies = {
    "csrftoken": "TUvoT4FdxdDjr2mZPIcKZ3Kde0w9nlK1",
    "next-auth.csrf-token": "a710d0e3c1ca1a14c2e53f146b34d8879a1f0bed91564bd098176ce54e7bf9f2%7Cbcc6aa8b4cacdbff4682828079dbf680b19ddf0111fc87136547552a0a45c067",
    "next-auth.session-token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..jVQahJ0p4x4a0gKL.nNyeQwNeRMZJ69lYDz76beg_VwoDo3vBJdoGsa8sgn-cq6j0KGAwu2LvxflaiAoJzMv13BDFNRu0rsrICKA5hehoFfW-Q9JtaryRQuaif9YyB1bzJw5DZ993giKM0iuT-mLJtbk5QktnvhZ0FpCScbdJomU0TXYEPFs7hXfRem398xdglX2uK6a_g5vZ-4h7YniPgauAsT5ZyiyGJITytynm7UEYtqX49GonyG6BZ5snN1OYXr35-5QsoSd8cShP-5r_WPsqYR1E0fM6HARgFZS1q4pP-fseRUeqJdIMzOFl1YUHOypGbfh6EmC74O66nyDcj0_UlN5gawV3tyLZ.r_2XvcMMqQi4pn0mb1pPBA",
    "sessionid": "3jcpi6c5x5pkzk8cf1jdsnj88pho3wl3"
}

with open('consumo-energia.txt', 'w') as file:
    for recommendation_id in range(1, 18):
        response = requests.get(f"{url}{recommendation_id}/", cookies=cookies)
        if response.status_code == 200:
            file.write(f"Dados para recommendation/{recommendation_id}:\n")
            file.write(str(response.json()) + "\n\n")
        else:
            file.write(f"Erro na requisição para recommendation/{recommendation_id}. Status: {response.status_code}\n\n")

print("Dados das requisições foram salvos em 'consumo-energia.txt'.")
