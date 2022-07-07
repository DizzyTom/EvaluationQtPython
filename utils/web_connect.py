class WebConnect:
    def __init__(self):
        self.IP = "10.181.7.56"
        self.PORT = "80"

    def getUrl(self, path=""):
        return "http://" + self.IP + ":" + self.PORT + "/" + path


webConnect = WebConnect()

# data = {}
# import requests

# ret = requests.post(
#     url=webConnect.getUrl("ScanTask/UploadFilm/"),
#     data=data,
#     files={
#         "img": (
#             "test.bmp",
#             open(r"A:\projects\Python\GrabCut\images\line.bmp", "rb"),
#             "image/bmp",
#         )
#     },
# ).json()
# print(ret)
