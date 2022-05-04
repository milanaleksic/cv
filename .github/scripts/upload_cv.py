#!/usr/bin/env python3

import base64
import http.client
import json
import logging
import os
import ssl
import time
import urllib.request
from urllib.error import HTTPError

WEBSITE_REPO = "milanaleksic/aleksic.dev"
CV_LOCATION_IN_WEBSITE = "static/public/"
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

    def _get_previous_sha(self, file: str) -> str:
        try:
            with urllib.request.urlopen(CV_CRUD_URL + file, context=self.ctx) as url:
                data = json.loads(url.read().decode())
                return data['sha']
        except HTTPError as e:
            return ""

    def upload_file(self, file: str):
        sha = self._get_previous_sha(file)
        data = self._get_cv_as_base64(file)
        http.client.HTTPConnection.debuglevel = 1
        conn = http.client.HTTPSConnection(GITHUB_API, context=self.ctx)
        credentials_raw = bytes('milanaleksic:' + os.environ['TOKEN_TO_UPLOAD'], "utf-8")
        credentials = base64.b64encode(credentials_raw).decode("utf-8")
        headers = {
            'Authorization': f'Basic {credentials}',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'User-Agent': 'GithubActions',
        }
        payload = {
            'message': f'Update the CV from the upstream CV project (file {file})',
            'content': data.decode("utf-8"),
            'sha': sha
        }
        json_data = json.dumps(payload)
        conn.request("PUT", CV_API_URL + file, json_data, headers=headers)
        response = conn.getresponse()
        logging.info("Put command response: ", response.status)

    @staticmethod
    def _get_cv_as_base64(file) -> bytes:
        cv_location = os.path.join(os.path.dirname(__file__), '../../', file)
        with open(cv_location, "rb") as cv:
            return base64.b64encode(cv.read())


if __name__ == '__main__':
    upload_cv = UploadCv()
    upload_cv.upload_file('cv.html')
    # FIXME: Cloudflare Pages builder doesn't let last commit win, so we need to let it rest between commits, unfortunately
    # Proper fix would pobably be to open a PR, then push changes on these 2 files and then merge it
    time.sleep(60)
    upload_cv.upload_file('cv.pdf')
