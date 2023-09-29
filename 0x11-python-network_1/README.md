# alx-higher_level_programming

This repository contains Python scripts that demonstrate various network-related tasks, including making HTTP requests, handling response data, and interacting with the GitHub API.

## Table of Contents

- [What's my status? #0](#whats-my-status-0)
- [Response header value #0](#response-header-value-0)
- [POST an email #0](#post-an-email-0)
- [Error code #0](#error-code-0)
- [What's my status? #1](#whats-my-status-1)
- [Response header value #1](#response-header-value-1)
- [POST an email #1](#post-an-email-1)
- [Error code #1](#error-code-1)
- [Search API](#search-api)
- [My GitHub!](#my-github)
- [Time for an interview!](#time-for-an-interview)

## What's my status? #0

**Task Description:**
Write a Python script that fetches https://alx-intranet.hbtn.io/status using the `urllib` package. Display information about the response, including the type of content and its content.

**Script File:** [0-hbtn_status.py](0x11-python-network_1/0-hbtn_status.py)

## Response header value #0

**Task Description:**
Write a Python script that takes a URL as input, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the response header. Use `urllib` and `sys` packages for this task.

**Script File:** [1-hbtn_header.py](0x11-python-network_1/1-hbtn_header.py)

## POST an email #0

**Task Description:**
Write a Python script that takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response (decoded in utf-8). Use `urllib` and `sys` packages.

**Script File:** [2-post_email.py](0x11-python-network_1/2-post_email.py)

## Error code #0

**Task Description:**
Write a Python script that takes a URL as input, sends a request to the URL, and displays the body of the response (decoded in utf-8). If the HTTP status code is an error (>= 400), print "Error code:" followed by the HTTP status code. Use `urllib` and `sys` packages for this task.

**Script File:** [3-error_code.py](0x11-python-network_1/3-error_code.py)

## What's my status? #1

**Task Description:**
Write a Python script that fetches https://alx-intranet.hbtn.io/status using the `requests` package. Display information about the response, including the type of content.

**Script File:** [4-hbtn_status.py](0x11-python-network_1/4-hbtn_status.py)

## Response header value #1

**Task Description:**
Write a Python script that takes a URL as input, sends a request to the URL, and displays the value of the `X-Request-Id` variable in the response header. Use the `requests` package and `sys` package for this task.

**Script File:** [5-hbtn_header.py](0x11-python-network_1/5-hbtn_header.py)

## POST an email #1

**Task Description:**
Write a Python script that takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response. Use the `requests` package and `sys` package.

**Script File:** [6-post_email.py](0x11-python-network_1/6-post_email.py)

## Error code #1

**Task Description:**
Write a Python script that takes a URL as input, sends a request to the URL, and displays the body of the response. If the HTTP status code is an error (>= 400), print "Error code:" followed by the HTTP status code. Use the `requests` package and `sys` package for this task.

**Script File:** [7-error_code.py](0x11-python-network_1/7-error_code.py)

## Search API

**Task Description:**
Write a Python script that takes a letter as input, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter, and displays the response. If the response is properly formatted JSON and not empty, display the id and name. Otherwise, display "Not a valid JSON" or "No result" accordingly.

**Script File:** [8-json_api.py](0x11-python-network_1/8-json_api.py)

## My GitHub!

**Task Description:**
Write a Python script that takes GitHub credentials (username and personal access token) as input and uses the GitHub API to display the user's ID. Basic Authentication is used with the personal access token as the password.

**Script File:** [10-my_github.py](0x11-python-network_1/10-my_github.py)

## Time for an interview!

**Task Description:**
Write a Python script that retrieves and lists 10 commits (from most recent to oldest) of a specified repository by a given user on GitHub. Print each commit as `<sha>: <author name>`. Use the GitHub API.

**Script File:** [100-github_commits.py](0x11-python-network_1/100-github_commits.py)

_Note: Be aware of rate limiting (only 60 requests per hour per IP for unauthenticated requests) when using the GitHub API._

Feel free to explore each script for detailed implementation. Good luck with your network-related tasks!
