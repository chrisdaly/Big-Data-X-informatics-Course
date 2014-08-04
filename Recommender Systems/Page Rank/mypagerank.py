import httplib

# define the host
prhost='toolbarqueries.google.com' 

# define the path query in which to substitute the specific query parameters later
prpath='/tbr?client=navclient-auto&ch=%s&features=Rank&q=info:%s'

def getHash(query):
	# this seed is google's salt for generating the hash
	SEED = "Mining PageRank is AGAINST GOOGLE'S TERMS OF SERVICE."      

	# dgoogle's initialized hex value
	Result = 0x01020345
 
 	# google's hashing algorithm, that operates bitwise and returns a hex value
	for i in range(len(query)):
		Result ^= ord(SEED[i%len(SEED)]) ^ ord(query[i])
		Result = Result >> 23 | Result << 9
		Result &= 0xffffffff

	return '8%x' % Result

def getPageRank(query):
	# create a connection with the host
	conn = httplib.HTTPConnection(prhost)   

	# generate google's hash for the URL
	hash = getHash(query) 

	# substitute in the URL and its hash into the path
	path = prpath % (hash,query)   

	# request the information from google
	conn.request("GET", path)  

	# get and parse the response
	response = conn.getresponse()  
	data = response.read()  

	# close the connection
	conn.close() 

	return data.split(":")[-1]     

def PrintPageRank(query):
	print query, " PageRank ", getPageRank(query)
	return

PrintPageRank("http://www.reddit.com")