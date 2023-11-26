# run outside of venv to avoid SSL error


import requests
response = requests.get('https://www.gutenberg.org/files/1342/1342-0.txt') 

with open('pride_and_prejudice.txt', 'w') as f:
    f.write(response.text)

print('move data to data folder')


# context for error in venv 
#  
# install certifi?
# URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1000)>
# https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
# The workaround works in venv but not here.

# import dask 
# dask.config.set({"distributed.scheduler.http.request_kwargs": {"verify": False}}) # tried. didn't work

# pem_path = "/etc/ssl/cert.pem"
# dask.config.set({"distributed.scheduler.http.request_kwargs": {"verify": "/etc/ssl/cert.pem"}}) 


# does not work in venv. same error
# import requests
# response = requests.get('https://www.gutenberg.org/files/1342/1342-0.txt') 