#!/usr/bin/env python3

import base64
import http.client
import json
import os
import ssl
import urllib.request

WEBSITE_REPO = "milanaleksic/man-website"
CV_LOCATION_IN_WEBSITE = "static/public/cv.html"
GITHUB_API = "api.github.com"
CV_API_URL = f"/repos/{WEBSITE_REPO}/contents/{CV_LOCATION_IN_WEBSITE}"
CV_CRUD_URL = f"https://{GITHUB_API}{CV_API_URL}"


class UploadCv:
    def __init__(self):
        self.ctx = self._create_non_verifying_context()

    @staticmethod
    def _create_non_verifying_context() -> ssl.SSLContext:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context

    def get_previous_sha(self) -> str:
        with urllib.request.urlopen(CV_CRUD_URL, context=self.ctx) as url:
            data = json.loads(url.read().decode())
            return data['sha']

    def upload_new_cv(self, cv, sha: str):
        http.client.HTTPConnection.debuglevel = 1
        conn = http.client.HTTPSConnection(GITHUB_API, context=self.ctx)
        credentials_raw = bytes('milanaleksic:' + os.environ['GITHUB_TOKEN'], "utf-8")
        credentials = base64.b64encode(credentials_raw).decode("utf-8")
        headers = {
            'Authorization': f'Basic {credentials}',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'User-Agent': 'GithubActions',
        }
        payload = {
            'message': 'Update the CV from the upstream CV project',
            'content': cv.decode("utf-8"),
            'sha': sha
        }
        json_data = json.dumps(payload)
        conn.request("PUT", CV_API_URL, json_data, headers=headers)
        response = conn.getresponse()
        print(response.status, response.reason)


def get_cv_as_base64() -> str:
    cv_location = os.path.join(os.path.dirname(__file__), '../../cv.html')
    with open(cv_location, "rb") as cv:
        return base64.b64encode(cv.read())


if __name__ == '__main__':
    upload_cv = UploadCv()
    sha = upload_cv.get_previous_sha()
    print(f"Previous SHA was: {sha}")
    cv = get_cv_as_base64()
    upload_cv.upload_new_cv(cv, sha)