import urllib.request
import os


path= './http_access_log.txt'

exists = os.path.exists(path)

#print(exists)
if exists == False:

    print('Seems you are missing some important files...lets get them for you.....')

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url,'./http_access_log.txt')


    file = open("http_access_log.txt")
    data = file.read()

    J1 = data.count("01/Jan" and "02/Jan" and "03/Jan" and "04/Jan" and "05/Jan" and "06/Jan" and "07/Jan")
    J2 = data.count("08/Jan" and "09/Jan" and "10/Jan" and "11/Jan" and "12/Jan" and "13/Jan" and "14/Jan")
    J3 = data.count("15/Jan" and "16/Jan" and "17/Jan" and "18/Jan" and "19/Jan" and "20/Jan" and "21/Jan")
    J4 = data.count("22/Jan" and "23/Jan" and "24/Jan" and "25/Jan" and "26/Jan" and "27/Jan" and "28/Jan")
    J5 = data.count("29/Jan" and "30/Jan" and "31/Jan")

    F1 = data.count("01/Feb" and "02/Feb" and "03/Feb" and "04/Feb" and "05/Feb" and "06/Feb" and "07/Feb")
    F2 = data.count("08/Feb" and "09/Feb" and "10/Feb" and "11/Feb" and "12/Feb" and "13/Feb" and "14/Feb")
    F3 = data.count("15/Feb" and "16/Feb" and "17/Feb" and "18/Feb" and "19/Feb" and "20/Feb" and "21/Feb")
    F4 = data.count("22/Feb" and "23/Feb" and "24/Feb" and "25/Feb" and "26/Feb" and "27/Feb" and "28/Feb")
    F5 = data.count("29/Feb" and "30/Feb" and "31/Feb")

    M1 = data.count("01/Mar" and "02/Mar" and "03/Mar" and "04/Mar" and "05/Mar" and "06/Mar" and "07/Mar")
    M2 = data.count("08/Mar" and "09/Mar" and "10/Mar" and "11/Mar" and "12/Mar" and "13/Mar" and "14/Mar")
    M3 = data.count("15/Mar" and "16/Mar" and "17/Mar" and "18/Mar" and "19/Mar" and "20/Mar" and "21/Mar")
    M4 = data.count("22/Mar" and "23/Mar" and "24/Mar" and "25/Mar" and "26/Mar" and "27/Mar" and "28/Mar")
    M5 = data.count("29/Mar" and "30/Mar" and "31/Mar")

    A1 = data.count("01/Apr" and "02/Apr" and "03/Apr" and "04/Apr" and "05/Apr" and "06/Apr" and "07/Apr")
    A2 = data.count("08/Apr" and "09/Apr" and "10/Apr" and "11/Apr" and "12/Apr" and "13/Apr" and "14/Apr")
    A3 = data.count("15/Apr" and "16/Apr" and "17/Apr" and "18/Apr" and "19/Apr" and "20/Apr" and "21/Apr")
    A4 = data.count("22/Apr" and "23/Apr" and "24/Apr" and "25/Apr" and "26/Apr" and "27/Apr" and "28/Apr")
    A5 = data.count("29/Apr" and "30/Apr" and "31/Apr")

    MA1 = data.count("01/May" and "02/May" and "03/May" and "04/May" and "05/May" and "06/May" and "07/May")
    MA2 = data.count("08/May" and "09/May" and "10/May" and "11/May" and "12/May" and "13/May" and "14/May")
    MA3 = data.count("15/May" and "16/May" and "17/May" and "18/May" and "19/May" and "20/May" and "21/May")
    MA4 = data.count("22/May" and "23/May" and "24/May" and "25/May" and "26/May" and "27/May" and "28/May")
    MA5 = data.count("29/May" and "30/May" and "31/May")

    JU1 = data.count("01/Jun" and "02/Jun" and "03/Jun" and "04/Jun" and "05/Jun" and "06/Jun" and "07/Jun")
    JU2 = data.count("08/Jun" and "09/Jun" and "10/Jun" and "11/Jun" and "12/Jun" and "13/Jun" and "14/Jun")
    JU3 = data.count("15/Jun" and "16/Jun" and "17/Jun" and "18/Jun" and "19/Jun" and "20/Jun" and "21/Jun")
    JU4 = data.count("22/Jun" and "23/Jun" and "24/Jun" and "25/Jun" and "26/Jun" and "27/Jun" and "28/Jun")
    JU5 = data.count("29/" and "30/" and "31/")

    JL1 = data.count("01/Jul" and "02/Jul" and "03/Jul" and "04/Jul" and "05/Jul" and "06/Jul" and "07/Jul")
    JL2 = data.count("08/Jul" and "09/Jul" and "10/Jul" and "11/Jul" and "12/Jul" and "13/Jul" and "14/Jul")
    JL3 = data.count("15/Jul" and "16/Jul" and "17/Jul" and "18/Jul" and "19/Jul" and "20/Jul" and "21/Jul")
    JL4 = data.count("22/Jul" and "23/Jul" and "24/Jul" and "25/Jul" and "26/Jul" and "27/Jul" and "28/Jul")
    JL5 = data.count("29/Jul" and "30/Jul" and "31/Jul")

    Aug1 = data.count("01/Aug" and "02/Aug" and "03/Aug" and "04/Aug" and "05/Aug" and "06/Aug" and "07/Aug")
    Aug2 = data.count("08/Aug" and "09/Aug" and "10/Aug" and "11/Aug" and "12/Aug" and "13/Aug" and "14/Aug")
    Aug3 = data.count("15/Aug" and "16/Aug" and "17/Aug" and "18/Aug" and "19/Aug" and "20/Aug" and "21/Aug")
    Aug4 = data.count("22/Aug" and "23/Aug" and "24/Aug" and "25/Aug" and "26/Aug" and "27/Aug" and "28/Aug")
    Aug5 = data.count("29/Aug" and "30/Aug" and "31/Aug")

    S1 = data.count("01/Sep" and "02/Sep" and "03/Sep" and "04/Sep" and "05/Sep" and "06/Sep" and "07/Sep")
    S2 = data.count("08/Sep" and "09/Sep" and "10/Sep" and "11/Sep" and "12/Sep" and "13/Sep" and "14/Sep")
    S3 = data.count("15/Sep" and "16/Sep" and "17/Sep" and "18/Sep" and "19/Sep" and "20/Sep" and "21/Sep")
    S4 = data.count("22/Sep" and "23/Sep" and "24/Sep" and "25/Sep" and "26/Sep" and "27/Sep" and "28/Sep")
    S5 = data.count("29/Sep" and "30/Sep" and "31/Sep")

    O1 = data.count("01/Oct" and "02/Oct" and "03/Oct" and "04/Oct" and "05/Oct" and "06/Oct" and "07/Oct")
    O2 = data.count("08/Oct" and "09/Oct" and "10/Oct" and "11/Oct" and "12/Oct" and "13/Oct" and "14/Oct")
    O3 = data.count("15/Oct" and "16/Oct" and "17/Oct" and "18/Oct" and "19/Oct" and "20/Oct" and "21/Oct")
    O4 = data.count("22/Oct" and "23/Oct" and "24/Oct" and "25/Oct" and "26/Oct" and "27/Oct" and "28/Oct")
    O5 = data.count("29/Oct" and "30/Oct" and "31/Oct")

    N1 = data.count("01/Nov" and "02/Nov" and "03/Nov" and "04/Nov" and "05/Nov" and "06/Nov" and "07/Nov")
    N2 = data.count("08/Nov" and "09/Nov" and "10/Nov" and "11/Nov" and "12/Nov" and "13/Nov" and "14/Nov")
    N3 = data.count("15/Nov" and "16/Nov" and "17/Nov" and "18/Nov" and "19/Nov" and "20/Nov" and "21/Nov")
    N4 = data.count("22/Nov" and "23/Nov" and "24/Nov" and "25/Nov" and "26/Nov" and "27/Nov" and "28/Nov")
    N5 = data.count("29/Nov" and "30/Nov" and "31/Nov")

    D1 = data.count("01/Dec" and "02/Dec" and "03/Dec" and "04/Dec" and "05/Dec" and "06/Dec" and "07/Dec")
    D2 = data.count("08/Dec" and "09/Dec" and "10/Dec" and "11/Dec" and "12/Dec" and "13/Dec" and "14/Dec")
    D3 = data.count("15/Dec" and "16/Dec" and "17/Dec" and "18/Dec" and "19/Dec" and "20/Dec" and "21/Dec")
    D4 = data.count("22/Dec" and "23/Dec" and "24/Dec" and "25/Dec" and "26/Dec" and "27/Dec" and "28/Dec")
    D5 = data.count("29/Dec" and "30/Dec" and "31/Dec")

    print(f'Data was asked for in January of each year by week {J1, J2, J3, J4, J5} times respectively')
    print(f'Data was asked for in February of each year by week {F1, F2, F3, F4, F5} times respectively')
    print(f'Data was asked for in March of each year by week {M1, M2, M3, M4, M5} times respectively')
    print(f'Data was asked for in April of each year by week {A1, A2, A3, A4, A5} times respectively')
    print(f'Data was asked for in May of each year by week {MA1, MA2, MA3, MA4, MA5} times respectively')
    print(f'Data was asked for in June of each year by week {JU1, JU2, JU3, JU4, JU5} times respectively')
    print(f'Data was asked for in July of each year by week {JL1, JL2, JL3, JL4, JL5} times respectively')
    print(f'Data was asked for in August of each year by week {Aug1, Aug2, Aug3, Aug4, Aug5} times respectively')
    print(f'Data was asked for in September of each year by week {S1, S2, S3, S4, S5} times respectively')
    print(f'Data was asked for in October of each year by week {O1, O2, O3, O4, O5} times respectively')
    print(f'Data was asked for in November of each year by week {N1, N2, N3, N4, N5} times respectively')
    print(f'Data was asked for in December of each year by week {D1, D2, D3, D4, D5} times respectively')



else:
        file= open ("http_access_log.txt")
        data = file.read()

        J1 = data.count("01/Jan" and "02/Jan" and "03/Jan" and "04/Jan" and "05/Jan" and "06/Jan" and "07/Jan")
        J2 = data.count("08/Jan" and "09/Jan" and "10/Jan" and "11/Jan" and "12/Jan" and "13/Jan" and "14/Jan")
        J3 = data.count("15/Jan" and "16/Jan" and "17/Jan" and "18/Jan" and "19/Jan" and "20/Jan" and "21/Jan")
        J4 = data.count("22/Jan" and "23/Jan" and "24/Jan" and "25/Jan" and "26/Jan" and "27/Jan" and "28/Jan")
        J5 = data.count("29/Jan" and "30/Jan" and "31/Jan")

        F1 = data.count("01/Feb" and "02/Feb" and "03/Feb" and "04/Feb" and "05/Feb" and "06/Feb" and "07/Feb")
        F2 = data.count("08/Feb" and "09/Feb" and "10/Feb" and "11/Feb" and "12/Feb" and "13/Feb" and "14/Feb")
        F3 = data.count("15/Feb" and "16/Feb" and "17/Feb" and "18/Feb" and "19/Feb" and "20/Feb" and "21/Feb")
        F4 = data.count("22/Feb" and "23/Feb" and "24/Feb" and "25/Feb" and "26/Feb" and "27/Feb" and "28/Feb")
        F5 = data.count("29/Feb" and "30/Feb" and "31/Feb")

        M1 = data.count("01/Mar" and "02/Mar" and "03/Mar" and "04/Mar" and "05/Mar" and "06/Mar" and "07/Mar")
        M2 = data.count("08/Mar" and "09/Mar" and "10/Mar" and "11/Mar" and "12/Mar" and "13/Mar" and "14/Mar")
        M3 = data.count("15/Mar" and "16/Mar" and "17/Mar" and "18/Mar" and "19/Mar" and "20/Mar" and "21/Mar")
        M4 = data.count("22/Mar" and "23/Mar" and "24/Mar" and "25/Mar" and "26/Mar" and "27/Mar" and "28/Mar")
        M5 = data.count("29/Mar" and "30/Mar" and "31/Mar")

        A1 = data.count("01/Apr" and "02/Apr" and "03/Apr" and "04/Apr" and "05/Apr" and "06/Apr" and "07/Apr")
        A2 = data.count("08/Apr" and "09/Apr" and "10/Apr" and "11/Apr" and "12/Apr" and "13/Apr" and "14/Apr")
        A3 = data.count("15/Apr" and "16/Apr" and "17/Apr" and "18/Apr" and "19/Apr" and "20/Apr" and "21/Apr")
        A4 = data.count("22/Apr" and "23/Apr" and "24/Apr" and "25/Apr" and "26/Apr" and "27/Apr" and "28/Apr")
        A5 = data.count("29/Apr" and "30/Apr" and "31/Apr")

        MA1 = data.count("01/May" and "02/May" and "03/May" and "04/May" and "05/May" and "06/May" and "07/May")
        MA2 = data.count("08/May" and "09/May" and "10/May" and "11/May" and "12/May" and "13/May" and "14/May")
        MA3 = data.count("15/May" and "16/May" and "17/May" and "18/May" and "19/May" and "20/May" and "21/May")
        MA4 = data.count("22/May" and "23/May" and "24/May" and "25/May" and "26/May" and "27/May" and "28/May")
        MA5 = data.count("29/May" and "30/May" and "31/May")

        JU1 = data.count("01/Jun" and "02/Jun" and "03/Jun" and "04/Jun" and "05/Jun" and "06/Jun" and "07/Jun")
        JU2 = data.count("08/Jun" and "09/Jun" and "10/Jun" and "11/Jun" and "12/Jun" and "13/Jun" and "14/Jun")
        JU3 = data.count("15/Jun" and "16/Jun" and "17/Jun" and "18/Jun" and "19/Jun" and "20/Jun" and "21/Jun")
        JU4 = data.count("22/Jun" and "23/Jun" and "24/Jun" and "25/Jun" and "26/Jun" and "27/Jun" and "28/Jun")
        JU5 = data.count("29/" and "30/" and "31/")

        JL1 = data.count("01/Jul" and "02/Jul" and "03/Jul" and "04/Jul" and "05/Jul" and "06/Jul" and "07/Jul")
        JL2 = data.count("08/Jul" and "09/Jul" and "10/Jul" and "11/Jul" and "12/Jul" and "13/Jul" and "14/Jul")
        JL3 = data.count("15/Jul" and "16/Jul" and "17/Jul" and "18/Jul" and "19/Jul" and "20/Jul" and "21/Jul")
        JL4 = data.count("22/Jul" and "23/Jul" and "24/Jul" and "25/Jul" and "26/Jul" and "27/Jul" and "28/Jul")
        JL5 = data.count("29/Jul" and "30/Jul" and "31/Jul")

        Aug1 = data.count("01/Aug" and "02/Aug" and "03/Aug" and "04/Aug" and "05/Aug" and "06/Aug" and "07/Aug")
        Aug2 = data.count("08/Aug" and "09/Aug" and "10/Aug" and "11/Aug" and "12/Aug" and "13/Aug" and "14/Aug")
        Aug3 = data.count("15/Aug" and "16/Aug" and "17/Aug" and "18/Aug" and "19/Aug" and "20/Aug" and "21/Aug")
        Aug4 = data.count("22/Aug" and "23/Aug" and "24/Aug" and "25/Aug" and "26/Aug" and "27/Aug" and "28/Aug")
        Aug5 = data.count("29/Aug" and "30/Aug" and "31/Aug")

        S1 = data.count("01/Sep" and "02/Sep" and "03/Sep" and "04/Sep" and "05/Sep" and "06/Sep" and "07/Sep")
        S2 = data.count("08/Sep" and "09/Sep" and "10/Sep" and "11/Sep" and "12/Sep" and "13/Sep" and "14/Sep")
        S3 = data.count("15/Sep" and "16/Sep" and "17/Sep" and "18/Sep" and "19/Sep" and "20/Sep" and "21/Sep")
        S4 = data.count("22/Sep" and "23/Sep" and "24/Sep" and "25/Sep" and "26/Sep" and "27/Sep" and "28/Sep")
        S5 = data.count("29/Sep" and "30/Sep" and "31/Sep")

        O1 = data.count("01/Oct" and "02/Oct" and "03/Oct" and "04/Oct" and "05/Oct" and "06/Oct" and "07/Oct")
        O2 = data.count("08/Oct" and "09/Oct" and "10/Oct" and "11/Oct" and "12/Oct" and "13/Oct" and "14/Oct")
        O3 = data.count("15/Oct" and "16/Oct" and "17/Oct" and "18/Oct" and "19/Oct" and "20/Oct" and "21/Oct")
        O4 = data.count("22/Oct" and "23/Oct" and "24/Oct" and "25/Oct" and "26/Oct" and "27/Oct" and "28/Oct")
        O5 = data.count("29/Oct" and "30/Oct" and "31/Oct")

        N1 = data.count("01/Nov" and "02/Nov" and "03/Nov" and "04/Nov" and "05/Nov" and "06/Nov" and "07/Nov")
        N2 = data.count("08/Nov" and "09/Nov" and "10/Nov" and "11/Nov" and "12/Nov" and "13/Nov" and "14/Nov")
        N3 = data.count("15/Nov" and "16/Nov" and "17/Nov" and "18/Nov" and "19/Nov" and "20/Nov" and "21/Nov")
        N4 = data.count("22/Nov" and "23/Nov" and "24/Nov" and "25/Nov" and "26/Nov" and "27/Nov" and "28/Nov")
        N5 = data.count("29/Nov" and "30/Nov" and "31/Nov")

        D1 = data.count("01/Dec" and "02/Dec" and "03/Dec" and "04/Dec" and "05/Dec" and "06/Dec" and "07/Dec")
        D2 = data.count("08/Dec" and "09/Dec" and "10/Dec" and "11/Dec" and "12/Dec" and "13/Dec" and "14/Dec")
        D3 = data.count("15/Dec" and "16/Dec" and "17/Dec" and "18/Dec" and "19/Dec" and "20/Dec" and "21/Dec")
        D4 = data.count("22/Dec" and "23/Dec" and "24/Dec" and "25/Dec" and "26/Dec" and "27/Dec" and "28/Dec")
        D5 = data.count("29/Dec" and "30/Dec" and "31/Dec")



        print(f'Data was asked for in January of each year by week {J1, J2 , J3, J4 ,J5} times respectively')
        print(f'Data was asked for in February of each year by week {F1, F2, F3, F4, F5} times respectively')
        print(f'Data was asked for in March of each year by week {M1, M2, M3, M4, M5} times respectively')
        print(f'Data was asked for in April of each year by week {A1, A2, A3, A4, A5} times respectively')
        print(f'Data was asked for in May of each year by week {MA1, MA2, MA3, MA4, MA5} times respectively')
        print(f'Data was asked for in June of each year by week {JU1, JU2, JU3, JU4, JU5} times respectively')
        print(f'Data was asked for in July of each year by week {JL1, JL2, JL3, JL4, JL5} times respectively')
        print(f'Data was asked for in August of each year by week {Aug1, Aug2, Aug3, Aug4, Aug5} times respectively')
        print(f'Data was asked for in September of each year by week {S1, S2, S3, S4, S5} times respectively')
        print(f'Data was asked for in October of each year by week {O1, O2, O3, O4, O5} times respectively')
        print(f'Data was asked for in November of each year by week {N1, N2, N3, N4, N5} times respectively')
        print(f'Data was asked for in December of each year by week {D1, D2, D3, D4, D5} times respectively')









