import os
import math
import requests
import json

SITE_URL = "https://vmestecdn.site"
UPLOAD_URL = SITE_URL + "/api/upload/"
INFO_URL = SITE_URL + "/api/info/" 
DELETE_URL = SITE_URL + "/api/delete/"

class VmestecdnUpload(object):
    def __init__(self, upload_uuid):
        self.upload_uuid = upload_uuid

    def upload_chunk(self, name, chunks_count, current_chunk, data):        
        print(name, chunks_count, current_chunk, len(data))
        r = requests.post(UPLOAD_URL, {"name": name, "uuid": self.upload_uuid, "chunk": current_chunk, "chunks": chunks_count}, files={"file": data})
        print(r.content)
        if current_chunk+1==chunks_count:
            return r.content.decode('utf-8')
        if r.content != b'ok':
            raise Exception(r.content)


    def upload_file(self, fpath):
        if not os.path.exists(fpath):
            raise Exception("Upload file not exists "+fpath)

        chunk_size = 1024*1024
        chunks_count = math.ceil(os.stat(fpath).st_size / chunk_size)
        current_chunk = 0
        name = fpath.replace("\\", "/").split("/")[-1]
        file_uuid = ''
        with open(fpath, "rb") as f:
            chunk = f.read(chunk_size)
            while chunk:
                file_uuid = self.upload_chunk(name, chunks_count, current_chunk, chunk)
                chunk = f.read(chunk_size)
                current_chunk += 1
        return file_uuid

    def info(self, uuid):
        r = requests.get(INFO_URL+uuid)
        return json.loads(r.content.decode("utf-8"))

    def delete(self, uuid):
        r = requests.get(DELETE_URL+self.upload_uuid+"/"+uuid)
        return json.loads(r.content.decode("utf-8"))


if __name__=="__main__":
    vcu = VmestecdnUpload("558bec05d73142c5a0d727482e0190f4") # lin
    #files = [
    #    "/opt/lapon/media/2022/3/user_5/video/video4.mp4",
    #    "/home/mixolap/temp/in.mp4",
    #]

    

    print(vcu.info("098bec05d73842c5a0d727482e0190f4"))
    #print(vcu.delete("098bec05d73842c5a0d727482e0190f4"))
    # for f in files:
    #     if os.path.exists(f):
    #         print(vcu.upload_file(f))
