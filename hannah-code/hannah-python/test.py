print('hello,world!')
print('go away')

# make the function
def philDoesThis():
    print('hey phil does this')


# call the function
philDoesThis()

#get inside code
import requests

r = requests.get('https://www.bbc.co.uk/')
print (r)
print (r.headers)
print (r.text)

r = requests.get('https://www.philanderson.co.uk/hannah/index.html')
print (r)
print (r.headers)
print (r.text)