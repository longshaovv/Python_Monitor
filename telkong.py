#! /usr/bin/env python3
#_*_ coding:utf-8 _*_
def do_telnet(Host,username,password,finish,commands):
	import telnetlib
	import time
	import re
	import pymysql
	buff = '0'
	info = ' '
	flag = 0
	
	#连接服务器
	tn = telnetlib.Telnet(Host,port = 23,timeout = 20)
#	tn.set_debuglevel(2)
	#输入登录名
	tn.read_until(b'login:')
	tn.write((username + '\r\n').encode())
	#输入密码	
	tn.read_until(b'password:')
	tn.write((password + '\r\n').encode())
	#登陆后执行命令
	tn.read_until(finish)
	print('loging success!')
	'''for command in commands:
		tn.write(('%s'%command +'\r\n').encode())
		time.sleep(5)
		buff =tn.read_very_eager()
		bufff=str(buff)
		a = 'Print Spooler'
		pattern = re.compile(a)
		match = pattern.search(bufff)
		if match:
			print('%s服务已经开启'%a)
		else:
			print('%s服务未开启'%a)'''
	while True:
		#读取服务器服务信息
		for command in commands:
			tn.write(('%s'%command +'\r\n').encode())
			time.sleep(5)
			buff = tn.read_very_eager()
			info = str(buff)
	#连接数据库
		conn = pymysql.connect(host='localhost',user='root',passwd='zz123456',db='jiankong')
		cur = conn.cursor()
		cur.execute('select * from test1_fuwu')
		data = cur.fetchall()
		for d in data :
			i=0;
			a = (d[1])
			b = d[0]
			pattern =re.compile(a)
			match = pattern.search(info)
			if match:
				cur.execute('update test1_fuwu set flag = 1 where id = %d'%b)
				print('服务已经开启')
				conn.commit()
			else :
				cur.execute('update test1_fuwu set flag = 0 where id =%d' %b)			
				print('服务未开启')
				conn.commit()
		cur.close()
		cur = conn.cursor()
		cur.execute('select *from test1_fuwu')
		data1 = cur.fetchall()
		for d in data1 :
			opcom = ''
			docom = ''
			b = d[0]
			if(d[4]==1):
				opcom =d[6]
				tn.write((opcom +'\r\n').encode())
				cur.execute('update test1_fuwu set openflag = 0 where id =%d'%b)			
				print('服务正在开启')
				conn.commit()

			if(d[5]==1):
				docom = d[5]
				tn.write((docom +'\r\n').encode())
				cur.execute('update test1_fuwu set openflag = 0 where id =%d'%b)
				print('服务正在关闭')
				conn.commit()
		cur.close()
		time.sleep(20)
				  
	'''while  True:
		tn.write(b'net start \r\n')
		time.sleep(10)
		print(tn.read_very_eager())'''
	tn.close()

if __name__ =='__main__':
	#配置选项
	Host = '172.16.64.152'
	username = 'Administrator'
	password = 'z992924293'
	finish = b'>'
	commands = ['net start']
	do_telnet(Host,username,password,finish,commands)








