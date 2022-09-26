import requests


def api_call_request(URL):
    r = requests.get(url=URL, params={'': ''})
    data = r.json()
    return data


def make_api_search_request(search_query, page):
    URL = f"https://api.github.com/search/users?q={search_query}&page={page}&per_page=5"
    return api_call_request(URL)


def get_user(username):
    URL = "https://api.github.com/users/" + username
    return api_call_request(URL)


def get_user_repos(username):
    URL = "https://api.github.com/users/" + username + "/repos"
    return api_call_request(URL)


# def count_user_stars(username):
#     repos = get_user_repos(username)
#     total_stars = 0
#     for i in repos:
#         # print(i['full_name'], i['stargazers_count'])
#         total_stars += i['stargazers_count']
#     return total_stars
