# Access URL and Download csv data from URL and save it to specific location or database
import requests
import re
import urllib3
import csv
import os
import io
import time
from datamidware.pydm import csv2mysql


def get_csv(url, filepath=None, save2db={}):
    """Access URL and Download csv data from URL and save it to specific location.
    :param url: URL from where csv data is to be downloaded
    :param filename: file name and path to save csv data
    :param save2db: dictionary; if given csv data is loaded into database.
           save2db=dict(host="host", user="user", password="password", db_type="db_type", "db_name="db_name", tb_name="tb_name")
           (db_type: mysql, nosql)
    """
    try:
        # send a HTTP request to the server and save
        # the HTTP response in a response object called r
        r = requests.get(url, stream=True, headers={'Accept-Encoding': None}, allow_redirects=True, timeout=3)   # create HTTP response object
        print("HTTP request sent, awaiting response...")
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Oops, something broke: {}".format(e.response.status_code))
    except requests.exceptions.ConnectionError:
        print("Connection Error occurred!")
    except requests.exceptions.Timeout:
        print("Timeout Error occurred!")
    except urllib3.exceptions.NewConnectionError:
        print("Failed to establish a new connection!")
    except urllib3.exceptions.MaxRetryError:
        print("Failed to establish a new connection!")
    except requests.exceptions.RequestException:
        print("Oops: Something Else!")
    except KeyboardInterrupt:
        print("Keyboard Interruption!")
    else:
        # get url data info- content type, length, size
        print("Status: {}.. OK".format(r.status_code))
        s = r.content
        # print(r.headers)
        print("Content type: {}".format(r.headers.get('Content-Type')))
        if r.headers.get("Content-Length"):
            print("Length: {}".format(r.headers.get("Content-Length")))
            print("Size: {} Kb".format(int(r.headers.get("Content-Length"))//1024))
        print("Encoding: {}".format(r.encoding))

        # get the filename from content-disposition
        filename = get_filename_from_cd(r.headers.get('content-disposition'))
        if not filename:
            # get the file name from url string
            parts = url.split('/')
            filename = parts[-1]
            # print(filename)

        encoding = r.encoding
        try:
            # right to csv
            if filepath:
                if os.path.exists('{}{}'.format(filepath, filename)):
                    old_file_name = '{}{}'.format(filepath, filename)
                    # split_path = os.path.split(filepath)
                    new_file_name = '{}old_{}'.format(filepath, filename)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file2save = str(filepath) + str(filename)
                print("Saving to: '{}'".format(file2save))
                with open(file2save, 'w') as f:
                    start = time.time()
                    writer = csv.writer(f)
                    for line in r.iter_lines():
                        if encoding == "utf-8":
                            writer.writerow(line.decode('utf-8', errors='ignore').split(','))
                        else:
                            writer.writerow(line.decode(encoding).split(','))
                            # writer.writerow(line.decode('ISO-8859-1').split(','))

                # Print output description in the console
                print("")
                if r.headers.get("Content-Length"):
                    print("Download complete... {:.2f}Kb/s".format((int(r.headers.get("Content-Length"))//1024)/float((time.time() - start))))
                else:
                    print("Download complete")
                print('{} - "{}" saved in {:.5f}s'.format(r.headers.get("Date"), file2save, time.time() - start))

            if save2db:
                print("Start loading into database")
                # s = r.content
                try:
                    if save2db["db_type"] == "mysql":
                        if save2db["tb_name"]:
                            csv2mysql.csv2mysql(save2db["host"], save2db["user"], save2db["password"], io.StringIO(s.decode(encoding)), save2db["db_name"], save2db["tb_name"])
                            print("Table '{}' created successfully".format(save2db["tb_name"]))
                        else:
                            # get table name
                            if len(filename) > 64:
                                filename.replace(r"[^a-zA-Z\d\_]+", "_")
                                tb_name = filename.split('_')[0]
                            else:
                                tb_name = filename.split('.')[0]
                            print(tb_name)
                            csv2mysql.csv2mysql(save2db["host"], save2db["user"], save2db["password"], io.StringIO(s.decode(encoding)), save2db["db_name"], tb_name)
                            print("Table '{}' created successfully".format(tb_name))

                except Exception as e:
                    print('Error: {}'.format(str(e)))
        except Exception as e:
            print('Error: {}'.format(str(e)))


# Get filename from content-disposition
def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    f_name = re.findall('filename=(.+)', cd)

    if len(f_name) == 0:
        return None
    return f_name[0]
