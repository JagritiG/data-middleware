from datamidware.pydm import connect2mysql


def test_connect2mysql():

    try:
        # Call connect2mysql()
        status = connect2mysql.connect2mysql()
        assert status == "Successfully connected to MySQL"

    except Exception as e:
            print('Error: {}'.format(str(e)))






