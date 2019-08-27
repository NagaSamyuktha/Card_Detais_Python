from http.server import HTTPServer, BaseHTTPRequestHandler
import json

#open json file and give it to data variable as a dictionary
with open("Database.json") as data_file:
	data = json.load(data_file)

#Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
	#sets basic headers for the server
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/json')
		#reads the length of the Headers
		length = int(self.headers['Content-Length'])
		#reads the contents of the request
		content = self.rfile.read(length)
		temp = str(content).strip('b\'')
		self.end_headers()
		return temp
	def _get_headers(self):
		# reads the length of the Headers
		length = self.headers['T_D']
		# reads the contents of the request
		#content = self.rfile.read(length)
		#temp= str(content)
		print(length)
		#return temp

    	######
	#LIST#
	######
	#GET Method Defination
	def do_GET(self):
		#defining all the headers
		#temp= self._get_headers()
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		Email_List=[]
		for key,value in data.items():
			# pass
			#print (value)
			if dict(value)['T_D'] ==self.headers['T_D'] and  dict(value)['E_D'] ==self.headers['E_D'] and dict(value)['S_D'] ==self.headers['S_D'] and dict(value)['E_D'] ==self.headers['E_D'] and  dict(value)['Card_type'] ==self.headers['Card_type']:
				Email_List.append(value['Email'])
				#self.wfile.write(json.dumps(value['Email']).encode())
		#prints all the keys and values of the json file
		Email_Dict={'Emails':Email_List}
		#print(Email_Dict)
		self.wfile.write(json.dumps(Email_Dict).encode())

    #######
    #CREATE#
    ########
    #POST method defination
	def do_POST(self):
		temp = self._set_headers()
		print (temp)
		temp_dict=json.loads(temp)
		key=0
		#getting key and value of the data dictionary
		for key,value in data.items():
			pass
		index = int(key)+1
		data[str(index)]=temp_dict
		#write the changes to the json file
		with open("Database.json",'w+') as file_data:
			json.dump(data,file_data)
		#self.wfile.write(json.dumps(data[str(index)]))

			
#Server Initialization
server = HTTPServer(('127.0.0.1',8080), ServiceHandler)
server.serve_forever()