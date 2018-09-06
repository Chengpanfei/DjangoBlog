import os
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import time
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

def save_img_to_cos(request_file,uid):

	fobj = open('/tmp/cos_temp','wb')
	for chrunk in request_file.chunks():
		fobj.write(chrunk)
	fobj.close()

	secret_id = os.environ['COS_ID']     
	secret_key = os.environ['COS_KEY']      
	region = 'ap-chengdu'     
	token = ''                  
	scheme = 'http'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
	config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
	# 2. 获取客户端对象
	client = CosS3Client(config)

	#云端存储的文件名由当前时间和用户id组成
	filename = str(int(time.time())) + '-' + str(uid) + '.png'
	with open('/tmp/cos_temp','rb') as fb:
		response = client.put_object(
		Bucket='panfei-1257264121',
		Body = fb,
		Key = filename,
		StorageClass = 'STANDARD',
		ContentType = 'image/png'
		)
	return 'https://panfei-1257264121.cos.ap-chengdu.myqcloud.com/' + filename