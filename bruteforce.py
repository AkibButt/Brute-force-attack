import requests
target_url="https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjEyNzcyOTI3LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D"
data_dic={"email":"youremail@gmail.com","pass":"yourpass","login":"submit"}
res=requests.post(target_url,data=data_dic)
print(res.content)
