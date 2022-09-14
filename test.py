import json
import random
import re
import json
import sys
import time
import os
from urllib.parse import quote

import requests

proxies = {
  'http': 'http://10.10.90.55:7890',
  'https': 'http://10.10.90.55:7890',
}

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; MI 6 MIUI/20.6.18)'
}


def get_code(location):
    code_pattern = re.compile("(?<=access=).*?(?=&)")
    code = code_pattern.findall(location)[0]
    return code


def login(_user, password):
    url1 = "https://api-user.huami.com/registrations/+86" + _user + "/tokens"
    _headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": "MiFit/4.6.0 (iPhone; iOS 14.0.1; Scale/2.00)"
    }
    data1 = {
        "client_id": "HuaMi",
        "password": f"{password}",
        "redirect_uri": "https://s3-us-west-2.amazonaws.com/hm-registration/successsignin.html",
        "token": "access"
    }
    r1 = requests.post(url1, data=data1, headers=_headers, allow_redirects=False, proxies = proxies)
    try:
        location = r1.headers["Location"]
        code = get_code(location)
    except:
        return 0, 0

    url2 = "https://account.huami.com/v2/client/login"
    data2 = {
        "app_name": "com.xiaomi.hm.health",
        "app_version": "4.6.0",
        "code": f"{code}",
        "country_code": "CN",
        "device_id": "2C8B4939-0CCD-4E94-8CBA-CB8EA6E613A1",
        "device_model": "phone",
        "grant_type": "access_token",
        "third_name": "huami_phone",
    }
    r2 = requests.post(url2, data=data2, headers=_headers, proxies = proxies).json()
    login_token = r2["token_info"]["login_token"]
    # print(login_token)
    userid = r2["token_info"]["user_id"]
    # print(userid)

    return login_token, userid


def main(_user, _passwd, _step):
    _user = str(_user)
    password = str(_passwd)
    _step = str(_step)
    if _user == '' or password == '':
        print("username and password no null!")
        return "user and passwd not empty!"

    if _step == '':
        print("random(10000-19999)")
        _step = str(random.randint(10000, 19999))
    login_token, userid = login(_user, password)
    if login_token == 0:
        print("login fail")
        return "login fail!"

    t = get_time()

    app_token = get_app_token(login_token)

    today = time.strftime("%F")

    summary = {
        "v": 6,
        "slp": {
            "st": int(time.time()),
            "ed": int(time.time()),
            "dp": 0,
            "lt": 0,
            "wk": 0,
            "usrSt": -1440,
            "usrEd": -1440,
            "wc": 0,
            "is": 0,
            "lb": 0,
            "to": 0,
            "dt": 0,
            "rhr": 0,
            "ss": 0
        },
        "stp": {
            "ttl": _step,
            "dis": 10627,
            "cal": 510,
            "wk": 41,
            "rn": 50,
            "runDist": 7654,
            "runCal": 397,
            "stage": [
                {
                    "start": 327,
                    "stop": 341,
                    "mode": 1,
                    "dis": 481,
                    "cal": 13,
                    "step": 680
                },
                {
                    "start": 342,
                    "stop": 367,
                    "mode": 3,
                    "dis": 2295,
                    "cal": 95,
                    "step": 2874
                },
                {
                    "start": 368,
                    "stop": 377,
                    "mode": 4,
                    "dis": 1592,
                    "cal": 88,
                    "step": 1664
                },
                {
                    "start": 378,
                    "stop": 386,
                    "mode": 3,
                    "dis": 1072,
                    "cal": 51,
                    "step": 1245
                },
                {
                    "start": 387,
                    "stop": 393,
                    "mode": 4,
                    "dis": 1036,
                    "cal": 57,
                    "step": 1124
                },
                {
                    "start": 394,
                    "stop": 398,
                    "mode": 3,
                    "dis": 488,
                    "cal": 19,
                    "step": 607
                },
                {
                    "start": 399,
                    "stop": 414,
                    "mode": 4,
                    "dis": 2220,
                    "cal": 120,
                    "step": 2371
                },
                {
                    "start": 415,
                    "stop": 427,
                    "mode": 3,
                    "dis": 1268,
                    "cal": 59,
                    "step": 1489
                },
                {
                    "start": 428,
                    "stop": 433,
                    "mode": 1,
                    "dis": 152,
                    "cal": 4,
                    "step": 238
                },
                {
                    "start": 434,
                    "stop": 444,
                    "mode": 3,
                    "dis": 2295,
                    "cal": 95,
                    "step": 2874
                },
                {
                    "start": 445,
                    "stop": 455,
                    "mode": 4,
                    "dis": 1592,
                    "cal": 88,
                    "step": 1664
                },
                {
                    "start": 456,
                    "stop": 466,
                    "mode": 3,
                    "dis": 1072,
                    "cal": 51,
                    "step": 1245
                },
                {
                    "start": 467,
                    "stop": 477,
                    "mode": 4,
                    "dis": 1036,
                    "cal": 57,
                    "step": 1124
                },
                {
                    "start": 478,
                    "stop": 488,
                    "mode": 3,
                    "dis": 488,
                    "cal": 19,
                    "step": 607
                },
                {
                    "start": 489,
                    "stop": 499,
                    "mode": 4,
                    "dis": 2220,
                    "cal": 120,
                    "step": 2371
                },
                {
                    "start": 500,
                    "stop": 511,
                    "mode": 3,
                    "dis": 1268,
                    "cal": 59,
                    "step": 1489
                },
                {
                    "start": 512,
                    "stop": 522,
                    "mode": 1,
                    "dis": 152,
                    "cal": 4,
                    "step": 238
                }
            ]
        },
        "goal": 8000,
        "tz": "28800"
    }

    data_json = [
        {
            "data_hr": "//////9L////////////Vv///////////0v///////////9e/////0n/a///S////////////0b//////////1FK////////////R/////////////////9PTFFpaf9L////////////R////////////0j///////////9K////////////Ov///////////zf///86/zr/Ov88/zf/Pf///0v/S/8/////////////Sf///////////z3//////0r/Ov//////S/9L/zb/Sf9K/0v/Rf9H/zj/Sf9K/0//N////0D/Sf83/zr/Pf9M/0v/Ov9e////////////S////////////zv//z7/O/83/zv/N/83/zr/N/86/z//Nv83/zn/Xv84/zr/PP84/zj/N/9e/zr/N/89/03/P/89/z3/Q/9N/0v/Tv9C/0H/Of9D/zz/Of88/z//PP9A/zr/N/86/zz/Nv87/0D/Ov84/0v/O/84/zf/MP83/zH/Nv83/zf/N/84/zf/Of82/zf/OP83/zb/Mv81/zX/R/9L/0v/O/9I/0T/S/9A/zn/Pf89/zn/Nf9K/07/N/83/zn/Nv83/zv/O/9A/0H/Of8//zj/PP83/zj/S/87/zj/Nv84/zf/Of83/zf/Of83/zb/Nv9L/zj/Nv82/zb/N/85/zf/N/9J/zf/Nv83/zj/Nv84/0r/Sv83/zf/MP///zb/Mv82/zb/Of85/z7/Nv8//0r/S/85/0H/QP9B/0D/Nf89/zj/Ov83/zv/Nv8//0f/Sv9O/0ZeXv///////////1X///////////9B////////////TP///1b//////0////////////9N/////////v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+",
            "date": today,
            "data": [
                {
                    "start": 0,
                    "stop": 1439,
                    "value": "UA8AUBQAUAwAUBoAUAEAYCcAUBkAUB4AUBgAUCAAUAEAUBkAUAwAYAsAYB8AYB0AYBgAYCoAYBgAYB4AUCcAUBsAUB8AUBwAUBIAYBkAYB8AUBoAUBMAUCEAUCIAYBYAUBwAUCAAUBgAUCAAUBcAYBsAYCUAATIPYD0KECQAYDMAYB0AYAsAYCAAYDwAYCIAYB0AYBcAYCQAYB0AYBAAYCMAYAoAYCIAYCEAYCYAYBsAYBUAYAYAYCIAYCMAUB0AUCAAUBYAUCoAUBEAUC8AUB0AUBYAUDMAUDoAUBkAUC0AUBQAUBwAUA0AUBsAUAoAUCEAUBYAUAwAUB4AUAwAUCcAUCYAUCwKYDUAAUUlEC8IYEMAYEgAYDoAYBAAUAMAUBkAWgAAWgAAWgAAWgAAWgAAUAgAWgAAUBAAUAQAUA4AUA8AUAkAUAIAUAYAUAcAUAIAWgAAUAQAUAkAUAEAUBkAUCUAWgAAUAYAUBEAWgAAUBYAWgAAUAYAWgAAWgAAWgAAWgAAUBcAUAcAWgAAUBUAUAoAUAIAWgAAUAQAUAYAUCgAWgAAUAgAWgAAWgAAUAwAWwAAXCMAUBQAWwAAUAIAWgAAWgAAWgAAWgAAWgAAWgAAWgAAWgAAWREAWQIAUAMAWSEAUDoAUDIAUB8AUCEAUC4AXB4AUA4AWgAAUBIAUA8AUBAAUCUAUCIAUAMAUAEAUAsAUAMAUCwAUBYAWgAAWgAAWgAAWgAAWgAAWgAAUAYAWgAAWgAAWgAAUAYAWwAAWgAAUAYAXAQAUAMAUBsAUBcAUCAAWwAAWgAAWgAAWgAAWgAAUBgAUB4AWgAAUAcAUAwAWQIAWQkAUAEAUAIAWgAAUAoAWgAAUAYAUB0AWgAAWgAAUAkAWgAAWSwAUBIAWgAAUC4AWSYAWgAAUAYAUAoAUAkAUAIAUAcAWgAAUAEAUBEAUBgAUBcAWRYAUA0AWSgAUB4AUDQAUBoAXA4AUA8AUBwAUA8AUA4AUA4AWgAAUAIAUCMAWgAAUCwAUBgAUAYAUAAAUAAAUAAAUAAAUAAAUAAAUAAAUAAAUAAAWwAAUAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAeSEAeQ8AcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBcAcAAAcAAAcCYOcBUAUAAAUAAAUAAAUAAAUAUAUAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcCgAeQAAcAAAcAAAcAAAcAAAcAAAcAYAcAAAcBgAeQAAcAAAcAAAegAAegAAcAAAcAcAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcCkAeQAAcAcAcAAAcAAAcAwAcAAAcAAAcAIAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcCIAeQAAcAAAcAAAcAAAcAAAcAAAeRwAeQAAWgAAUAAAUAAAUAAAUAAAUAAAcAAAcAAAcBoAeScAeQAAegAAcBkAeQAAUAAAUAAAUAAAUAAAUAAAUAAAcAAAcAAAcAAAcAAAcAAAcAAAegAAegAAcAAAcAAAcBgAeQAAcAAAcAAAcAAAcAAAcAAAcAkAegAAegAAcAcAcAAAcAcAcAAAcAAAcAAAcAAAcA8AeQAAcAAAcAAAeRQAcAwAUAAAUAAAUAAAUAAAUAAAUAAAcAAAcBEAcA0AcAAAWQsAUAAAUAAAUAAAUAAAUAAAcAAAcAoAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAYAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBYAegAAcAAAcAAAegAAcAcAcAAAcAAAcAAAcAAAcAAAeRkAegAAegAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAEAcAAAcAAAcAAAcAUAcAQAcAAAcBIAeQAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBsAcAAAcAAAcBcAeQAAUAAAUAAAUAAAUAAAUAAAUBQAcBYAUAAAUAAAUAoAWRYAWTQAWQAAUAAAUAAAUAAAcAAAcAAAcAAAcAAAcAAAcAMAcAAAcAQAcAAAcAAAcAAAcDMAeSIAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBQAeQwAcAAAcAAAcAAAcAMAcAAAeSoAcA8AcDMAcAYAeQoAcAwAcFQAcEMAeVIAaTYAbBcNYAsAYBIAYAIAYAIAYBUAYCwAYBMAYDYAYCkAYDcAUCoAUCcAUAUAUBAAWgAAYBoAYBcAYCgAUAMAUAYAUBYAUA4AUBgAUAgAUAgAUAsAUAsAUA4AUAMAUAYAUAQAUBIAASsSUDAAUDAAUBAAYAYAUBAAUAUAUCAAUBoAUCAAUBAAUAoAYAIAUAQAUAgAUCcAUAsAUCIAUCUAUAoAUA4AUB8AUBkAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAA",
                    "tz": 32,
                    "did": "DA932FFFFE8816E7",
                    "src": 24
                }
            ],
            "summary": json.dumps(summary),
            "source": 24,
            "type": 0
        }
    ]

    url = f'https://api-mifit-cn.huami.com/v1/data/band_data.json?&t={t}'
    head = {
        "apptoken": app_token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = f'userid={userid}&last_sync_data_time=1597306380&device_type=0&last_deviceid=DA932FFFFE8816E7&data_json={quote(json.dumps(data_json))}'

    response = requests.post(url, data=data, headers=head, proxies = proxies).json()
    # print(response)
    result = f"{_user[:4]}****{_user[-4:]}: [{now}] modify step({_step})" + response['message']
    print(result)
    return result


def get_time():
    url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
    response = requests.get(url, headers=headers, proxies = proxies).json()
    t = response['data']['t']
    return t


def get_app_token(login_token):
    url = f"https://account-cn.huami.com/v1/client/app_tokens" \
          f"?app_name=com.xiaomi.hm.health&dn=api-user.huami.com%2Capi-mifit.huami.com%2Capp-analytics.huami.com" \
          f"&login_token={login_token}"
    response = requests.get(url, headers=headers, proxies = proxies).json()
    app_token = response['token_info']['app_token']
    return app_token


def push_wx(_sckey, desp=""):
    if _sckey == '':
        print("no key no push")
    else:
        server_url = f"https://sc.ftqq.com/{_sckey}.send"
        params = {
            "text": 'mi sport',
            "desp": desp
        }

        response = requests.get(server_url, params=params, proxies = proxies)
        json_data = response.json()

        if json_data['errno'] == 0:
            print(f"[{now}] success")
        else:
            print(f"[{now}] fail {json_data['errno']}({json_data['errmsg']})")


def push_server(_sckey, desp=""):
    if _sckey == '':
        print("no key no wechat")
    else:
        server_url = f"https://sctapi.ftqq.com/{_sckey}.send"
        params = {
            "title": 'mi sport modify',
            "desp": desp
        }

        response = requests.get(server_url, params=params, proxies = proxies)
        json_data = response.json()

        if json_data['code'] == 0:
            print(f"[{now}] push success")
        else:
            print(f"[{now}] push fail {json_data['code']}({json_data['message']})")


def push_pushplus(token, content=""):
    if token == '':
        print("no token no push")
    else:
        server_url = "http://www.pushplus.plus/send"
        params = {
            "token": token,
            "title": 'mi sport',
            "content": content
        }

        response = requests.get(server_url, params=params, proxies = proxies)
        json_data = response.json()

        if json_data['code'] == 200:
            print(f"[{now}] success")
        else:
            print(f"[{now}] fail {json_data['code']}({json_data['message']})")


def push_tg(token, chat_id, desp=""):
    if token == '':
        print("no tg")
    elif chat_id == '':
        print("no tg")
    else:
        server_url = f"https://api.telegram.org/bot{token}/sendmessage"
        params = {
            "text": 'mi sport modify \n\n' + desp,
            "chat_id": chat_id
        }

        response = requests.get(server_url, params=params, proxies = proxies)
        json_data = response.json()

        if json_data['ok']:
            print(f"[{now}] success")
        else:
            print(f"[{now}] fail {json_data['error_code']}({json_data['description']})")


def wxpush(msg, usr, corpid, corpsecret, agentid=1000002):
    base_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
    req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
    corpid = corpid
    corpsecret = corpsecret
    agentid = agentid

    if agentid == 0:
        agentid = 1000002

    def get_access_token(_base_url, _corpid, _corpsecret):
        urls = _base_url + 'corpid=' + _corpid + '&corpsecret=' + _corpsecret
        resp = requests.get(urls, proxies = proxies).json()
        access_token = resp['access_token']
        return access_token

    def send_message(_msg, _usr):
        data = get_message(_msg, _usr)
        req_urls = req_url + get_access_token(base_url, corpid, corpsecret)
        res = requests.post(url=req_urls, data=data, proxies = proxies)
        ret = res.json()
        if ret["errcode"] == 0:
            print(f"[{now}] success")
        else:
            print(f"[{now}] fail {ret['errcode']} err msg {ret['errmsg']}")

    def get_message(_msg, _usr):
        data = {
            "touser": _usr,
            "toparty": "@all",
            "totag": "@all",
            "msgtype": "text",
            "agentid": agentid,
            "text": {
                "content": _msg
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        data = json.dumps(data)
        return data

    msg = msg
    usr = usr
    if corpid == '':
        print("no wechat")
    elif corpsecret == '':
        print("no wechat")
    else:
        send_message(msg, usr)


class ToPush:
    push_msg: str

    def __init__(self, _pkey):
        self.pkey = _pkey

    def to_push_wx(self):
        if str(self.pkey) == '0':
            self.pkey = ''
        push_wx(self.pkey, self.push_msg)

    def to_push_server(self):
        if str(self.pkey) == '0':
            self.pkey = ''
        push_server(self.pkey, self.push_msg)

    def to_push_tg(self):
        try:
            token, chat_id = self.pkey.split('@')
            push_tg(token, chat_id, self.push_msg)
        except ValueError:
            print('tg error')

    def to_wxpush(self):
        try:
            usr, corpid, corpsecret, *agentid = self.pkey.split('-')
            if agentid:
                wxpush(self.push_msg, usr, corpid, corpsecret, int(agentid[0]))
            else:
                wxpush(self.push_msg, usr, corpid, corpsecret)
        except ValueError:
            print('wechat error')

    def to_push_pushplus(self):
        if self.pkey == '':
            print('pushplus token error')
        else:
            push_pushplus(self.pkey, self.push_msg)

    @staticmethod
    def no_push():
        print(f"[{now}] run success")


if __name__ == "__main__":
    try:
        Pm = "off"
        pkey = "off"

        to_push = ToPush(pkey)
        user = os.getenv('user')
        passwd = os.getenv('passwd')
        step = "28000-36000"
    except IndexError as e:
        print("param error : " + str(e))
        exit(1)

    try:
        user_list = user.split('#')
        passwd_list = passwd.split('#')
        step_array = step.split('-')

        if len(user_list) == len(passwd_list):
            to_push.push_msg = ''
            for user, passwd in zip(user_list, passwd_list):
                if len(step_array) == 2:
                    step = str(random.randint(int(step_array[0]), int(step_array[1])))
                elif str(step) == '0':
                    step = ''
                to_push.push_msg += main(user, passwd, step) + '\n'

            push = {
                'wx': to_push.to_push_wx,
                'nwx': to_push.to_push_server,
                'tg': to_push.to_push_tg,
                'qwx': to_push.to_wxpush,
                'pp': to_push.to_push_pushplus,
                'off': to_push.no_push
            }
            try:
                push[Pm]()
            except KeyError:
                print('push error')
                exit(0)
        else:
            print('count error')
    except:
         print(os.environ)
