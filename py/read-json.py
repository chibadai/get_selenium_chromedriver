# Chrome Versionを取得しておく
# ChromeDriverのバージョンを取得する
with open("./data/chrome_version.txt", "r") as f:
    chrome_version = f.read()
print(chrome_version)
# chrome_version は最終行ので取得する
now_chrome_version = chrome_version.split("\n")[-2]
print(now_chrome_version)
split_now_chrome_version = [int(x) for x in now_chrome_version.split(".")]

## 保存したファイルを読み込み利用可能な状態にする
json_name = "known-good-versions-with-downloads.json"
# print(json_name)

json_dir_file_path = "./data/json"

# jsonファイル一覧を取得し、最新のjsonファイルを取得する
import glob
import os

json_files = glob.glob(f"{json_dir_file_path}/*.json")
latest_json_file_path = max(json_files, key=os.path.getctime)
print(latest_json_file_path)

# このデータを利用する
import json

with open(latest_json_file_path, "r") as f:
    json_data = json.load(f)
# print(json_data)
# print(type(json_data))
for first_key, value in json_data.items():
    # print(first_key, value)
    print(first_key)

key_timestamp = "timestamp"
# print(json_data[key_timestamp])
key_versions = "versions"
key_version = "version"
# print(json_data[key_versions])
# print(type(json_data[key_versions]))
json_data_versions = json_data[key_versions]
chrome_driver_version_dict = {}
for json_data_idx in range(0, len(json_data_versions)):
    json_data_version = json_data_versions[json_data_idx]
    chrome_driver_version_dict[json_data_idx] = {}
    # print(json_data_version)
    # print(type(json_data_version))
    """json_data_version layout
    version 113.0.5672.0
    revision 1121455
    downloads {'chrome': [{'platform': 'linux64', 'url': 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/113.0.5672.0/linux64/chrome-linux64.zip'}, {'platform': 'mac-arm64', 'url': 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/113.0.5672.0/mac-arm64/chrome-mac-arm64.zip'}, {'platform': 'mac-x64', 'url': 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/113.0.5672.0/mac-x64/chrome-mac-x64.zip'}, {'platform': 'win32', 'url': 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/113.0.5672.0/win32/chrome-win32.zip'}, {'platform': 'win64', 'url': 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/113.0.5672.0/win64/chrome-win64.zip'}]}
    """
    # for key_seconds, value in json_data_version.items():
    #     print(key_seconds, value)
    # key_version = "version"
    key_revision = "revision"
    key_downloads = "downloads"
    json_data_version_version = json_data_version[key_version]
    # print(json_data_version_version)
    json_data_version_revision = json_data_version[key_revision]
    # print(json_data_version_revision)
    json_data_version_downloads = json_data_version[key_downloads]
    # print(json_data_version_downloads)
    json_data_version_downloads_chrome = json_data_version_downloads["chrome"]
    # print(type(json_data_version_downloads_chrome))
    # print(json_data_version_downloads_chrome)
    target_os_type = "win64"
    key_platform = "platform"
    for dl_chrome_idx in range(0, len(json_data_version_downloads_chrome)):
        json_data_version_downloads_chrome_dict = json_data_version_downloads_chrome[
            dl_chrome_idx
        ]
        # print(json_data_version_downloads_chrome_dict)
        if json_data_version_downloads_chrome_dict[key_platform] == target_os_type:
            # print(json_data_version_downloads_chrome_dict)
            break
    # break

    chrome_driver_version_dict[json_data_idx][key_version] = json_data_version_version
    chrome_driver_version_dict[json_data_idx][key_revision] = json_data_version_revision
    # chrome_driver_version_dict[json_data_idx][key_downloads] = json_data_version_downloads
    chrome_driver_version_dict[json_data_idx][
        key_platform
    ] = json_data_version_downloads_chrome_dict["url"]
# print(chrome_driver_version_dict)
for json_data_idx in chrome_driver_version_dict.keys():
    # print(json_data_idx, chrome_driver_version_dict[json_data_idx])
    version = chrome_driver_version_dict[json_data_idx][key_version]
    split_version = [int(x) for x in version.split(".")]
    # print(split_version, split_now_chrome_version)
    if split_version[0] == split_now_chrome_version[0]:
        # print(split_version, split_now_chrome_version)
        if split_version[1] == split_now_chrome_version[1]:
            # print(split_version, split_now_chrome_version)
            if split_version[2] == split_now_chrome_version[2]:
                print(split_version, split_now_chrome_version)
                if split_version[3] >= split_now_chrome_version[3]:
                    print(split_version[3], split_now_chrome_version[3])
                    print("OK")
                    break
    if split_version[0] > split_now_chrome_version[0]:
        break
    # if version == now_chrome_version:
    #     print("OK")
    #     break

# print(chrome_driver_version_dict[json_data_idx][key_version])
print(chrome_driver_version_dict[json_data_idx - 1][key_version])
print(chrome_driver_version_dict[json_data_idx - 1])
# 上記のデータをダウンロードする
