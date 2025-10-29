#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, sys
from pathlib import Path
from urllib.parse import quote
import requests, msal

TENANT_ID  = "ccb6deed-bd29-4b38-8979-d72780f62d3b"
CLIENT_ID  = "c69f7fe6-49f8-4f27-95f3-d0466fe2309b"
AUTHORITY  = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES     = ["Files.ReadWrite"]
CACHE_PATH = Path.home() / ".msal_token_cache.bin"

DOCS_ROOT  = Path.home() / "Documents"   # Detects your RFID data automatically

def build_app():
    cache = msal.SerializableTokenCache()
    if CACHE_PATH.exists():
        try: cache.deserialize(CACHE_PATH.read_text())
        except: pass
    return msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache), cache

def save_cache(cache):
    if cache.has_state_changed:
        CACHE_PATH.write_text(cache.serialize())

def get_token(app, cache):
    accts = app.get_accounts()
    if accts:
        res = app.acquire_token_silent(SCOPES, accts[0])
        if res and "access_token" in res:
            save_cache(cache)
            return res["access_token"]
    flow = app.initiate_device_flow(scopes=SCOPES)
    print("Go to:", flow["verification_uri"]); print("Enter code:", flow["user_code"])
    res = app.acquire_token_by_device_flow(flow)
    if "access_token" not in res:
        print("Auth failed"); sys.exit(1)
    save_cache(cache)
    return res["access_token"]

def ensure_remote_folder(token, relpath):
    url = f"https://graph.microsoft.com/v1.0/me/drive/root:/{quote(relpath)}"
    r = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    if r.status_code == 200: return
    parent = relpath.rsplit("/",1)[0] if "/" in relpath else ""
    parent_url = f"https://graph.microsoft.com/v1.0/me/drive/root:/{quote(parent)}:/children" if parent else \
                 "https://graph.microsoft.com/v1.0/me/drive/root/children"
    requests.post(parent_url, headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"},
                  json={"name": relpath.split("/")[-1], "folder": {}, "@microsoft.graph.conflictBehavior": "replace"}).raise_for_status()

def upload_file(token, local_path: Path, remote_relpath: str):
    url = f"https://graph.microsoft.com/v1.0/me/drive/root:/{quote(remote_relpath)}:/content"
    with local_path.open("rb") as f:
        requests.put(url, headers={"Authorization": f"Bearer {token}"}, data=f).raise_for_status()
    print(f"✔ Uploaded: {remote_relpath}")

def main():
    app, cache = build_app()
    token = get_token(app, cache)

    for data_dir in DOCS_ROOT.glob("data_20*"):
        if not data_dir.is_dir(): continue
        remote_base = f"RFID_Data/{data_dir.name}"   # <—— Remote root folder
        ensure_remote_folder(token, remote_base)

        for csv in data_dir.rglob("*.csv"):
            rel = csv.relative_to(DOCS_ROOT).as_posix()
            remote_relpath = f"RFID_Data/{rel}"
            ensure_remote_folder(token, os.path.dirname(remote_relpath))
            upload_file(token, csv, remote_relpath)

if __name__ == "__main__":
    main()
