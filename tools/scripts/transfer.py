import sys
import json
import requests

from datetime import datetime, timedelta
from common.api import Api
from common.params import Params
from tools.lib.api import CommaApi as ToolsApi
from tools.lib.retry import retry
from urllib.parse import urlparse

FILE_TRANSFER_ORDER = ["qlogs", "logs", "cameras", "dcameras", "qcameras"]


@retry(tries=5, delay=60)
def put_url(url, **kwargs):
    print("Sending PUT request")
    return requests.put(url, **kwargs)

@retry(tries=5, delay=60)
def get_upload_url(api, dongle_id, segment_file):
    print(f"Getting upload URL for: {segment_file}")
    return api.get("v1.3/" + dongle_id + "/upload_url/", timeout=10, path=segment_file, access_token=api.get_token())

@retry(tries=5, delay=60)
def get_url(url):
    print("Sending GET request")
    return requests.get(url, timeout=10)

@retry(tries=5, delay=60)
def get_files(route, tools_api):
    print(f"Getting files for {route}")
    return tools_api.get('v1/route/' + route + '/files', timeout=10)

def transfer_route(route, tools_api, api, dongle_id):
    print("Begin transfer of route: " + route)

    files = get_files(route, tools_api)

    for key in FILE_TRANSFER_ORDER:
        for url in files[key]:
            url_file = get_url(url)
            dat = url_file.content

            print(f"Done downloading {route}. Prepairing upload...")

            _, _, time_str, segment_num, fn = urlparse(url).path.rsplit('/', maxsplit=4)
            segment_file = f'{time_str}--{segment_num}/{fn}'
            
            url_resp = get_upload_url(api, dongle_id, segment_file)
            url_resp_json = json.loads(url_resp.text)
            upload_url = url_resp_json['url']
            headers = url_resp_json['headers']

            print(f"Uploading: {segment_file}")
            upload_resp = put_url(upload_url, data=dat, headers=headers, timeout=10)

            if upload_resp is not None and upload_resp.status_code in (200, 201):
                print(f"Finished uploading: {segment_file}\n\n")


def get_uploaded_routes(dongle_id, tools_api):
    print(f"Getting uploaded segments for {dongle_id}")
    start_time = (datetime.today() + timedelta(days=-365)).timestamp() * 1000
    seg_resp = tools_api.get(f"v1/devices/{dongle_id}/segments?from={start_time}")

    segs = dict()

    for seg_json in seg_resp:
        segs[seg_json["canonical_route_name"].split("|")[1]] = None

    print("Finished getting segments\n\n")

    return segs.keys()
            

def main(args):
    old_dongle_id = args[0]
    token = args[1]

    assert old_dongle_id, "Old device's dongle ID is required"
    assert token, "Comma API token is required"

    route = None

    if len(args) == 3:
        route = f"{old_dongle_id}|{args[2]}"

    tools_api = ToolsApi(token=token)

    params = Params()
    dongle_id = params.get("DongleId").decode('utf8')

    api = Api(dongle_id)

    if route:
        transfer_route(route, tools_api, api, dongle_id)
    else:
        old_segs = get_uploaded_routes(old_dongle_id, tools_api)
        new_segs = get_uploaded_routes(dongle_id, tools_api)

        for seg in old_segs:
            route = f"{old_dongle_id}|{seg}"

            if not seg or seg in new_segs:
                print(f"Skipping {route} because a route already exists on new dongle.\n\n")
                continue

            transfer_route(route, tools_api, api, dongle_id)

            print(f"\n\nFinish transfering {route}\n\n")
    
        

if __name__ == "__main__":
    main(sys.argv[1:])