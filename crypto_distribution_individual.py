import os
import time
from datetime import datetime
import webbrowser
import subprocess


def getPrice():

    crypto_dict = {"DOGE": 0, "TEL": 0, "SHIB": 0}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    import urllib.request
    req = urllib.request.Request(
        url="https://www.coinspot.com.au/tradecoins", headers=headers)
    price = str(urllib.request.urlopen(req).read(), "utf-8")

################################################     D  O  G  E   ############################################

    span_start_doge = price.find("<span data-auddisplay='DOGE'>")
    if span_start_doge != -1:
        dollar_start_doge = price.find("$", span_start_doge)
        if dollar_start_doge != -1:
            span_end_doge = price.find("</span>", dollar_start_doge)
            doge_value = float(price[dollar_start_doge+1:span_end_doge])
            crypto_dict["DOGE"] = doge_value
        else:
            print("Website source code has changed")
    else:
        print("Website source code has changed")

###################################################   T   E   L   ############################################

    span_start_tel = price.find("<span data-auddisplay='TEL'>")
    if span_start_tel != -1:
        dollar_start_tel = price.find("$", span_start_tel)
        if dollar_start_tel != -1:
            span_end_tel = price.find("</span>", dollar_start_tel)
            tel_value = float(price[dollar_start_tel+1:span_end_tel])
            crypto_dict["TEL"] = tel_value
        else:
            print("Website source code has changed")
    else:
        print("Website source code has changed")

################################################## S  H  I  B  ###############################################

    span_start_shib = price.find("<span data-auddisplay='SHIB'>")
    if span_start_shib != -1:
        dollar_start_shib = price.find("$", span_start_shib)
        if dollar_start_tel != -1:
            span_end_shib = price.find("</span>", dollar_start_shib)
            shib_value = float(price[dollar_start_shib+1:span_end_shib])
            crypto_dict["SHIB"] = shib_value
        else:
            print("Website source code has changed")
    else:
        print("Website source code has changed")

    return crypto_dict


# current date and time
now = datetime.now()
# format
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


def web_page():

    dictt = getPrice()
    doge_price = dictt["DOGE"]
    tel_price = dictt["TEL"]
    shib_price = dictt["SHIB"]
    # 213*doge_price
    ares_dict = {"DOGE": "{:.2f}".format(563*doge_price), "TEL": "{:.2f}".format(4654*tel_price), "SHIB": "{:.2f}".format(6416662*shib_price)}
    deepro_dict = {"DOGE": "{:.2f}".format(548*doge_price), "TEL": "{:.2f}".format(3219*tel_price), "SHIB": "{:.2f}".format(45643431*shib_price)}
    niaz_dict = {"DOGE": "{:.2f}".format(94*doge_price), "TEL": "{:.2f}".format(9832*tel_price), "SHIB": "{:.2f}".format(76893123*shib_price)}
    shourov_dict = {"DOGE": "{:.2f}".format(984*doge_price), "TEL": "{:.2f}".format(12316*tel_price), "SHIB": "{:.2f}".format(3023478*shib_price)}
    sunny_dict = {"DOGE": "{:.2f}".format(356*doge_price), "TEL": "{:.2f}".format(68746*tel_price), "SHIB": "{:.2f}".format(7789431*shib_price)}
    shuvo_dict = {"DOGE": "{:.2f}".format(8945*doge_price), "TEL": "{:.2f}".format(9745.94*tel_price), "SHIB": "{:.2f}".format(1312378*shib_price)}

    file = open('webpage.html', 'w')

    file.write("<html>")
    file.write("<head>")

    file.write(""" <style> """)
    file.write(""" *{box-sizing: border-box;} """)
    file.write(""" .row{margin-left:-5px;margin-right:-5px;} """)
    file.write(""" .row::after{content: "";clear: both;display: table;} """)
    file.write(
        """ table{border-collapse: collapse;border-spacing: 0;width: 100%;border: 0px solid #ddd;} """)
    file.write(""" th, td{text-align: left;padding: 16px;} """)
    file.write(""" tr:nth-child(even){background-color: #f2f2f2;} """)
    file.write(
        """ .box{float:left;background:#007bff;width:23.3333333333333%;height:60px;margin: 5%;border-radius:25px;} """)
    file.write(""" </style> """)

    file.write("""  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">  """)
    file.write(""" <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>   """)
    file.write("<title> Cryptocurrency Distribution </title>")
    file.write("</head>")

    file.write("<body>")
    file.write(""" <div class = "container"> """)
    file.write("""<div class="jumbotron">""")
    file.write("<h2 align = 'center'> Cryptocurrency Distribution at " +
               dt_string + " (local time)" + "</h2>")
    file.write("<hr/>")

    file.write(""" <div class="row"> """)
    file.write(""" <div class="box"><table><tr><th style="color:white"><center>Doge: $""" +
               str(doge_price) + """</center></th></tr></table></div> """)
    file.write(""" <div class="box"><table><tr><th style="color:white"><center>Tel: $""" +
               str(tel_price) + """</center></th></tr></table></div> """)
    file.write(""" <div class="box"><table><tr><th style="color:white"><center>Shib: $""" +
               str(shib_price) + """</center></th></tr></table></div> """)
    file.write(""" </div> """)
    file.write("<hr/>")

    file.write("""<ul class="list-group">""")
    file.write(
        """ <li class="list-group-item active"><center><strong>Ares</strong></center></li> """)

    if float(ares_dict["DOGE"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Doge:</strong> $""" + str(ares_dict["DOGE"]) + "</li> ")
    if float(ares_dict["TEL"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Tel:</strong> $""" + str(ares_dict["TEL"]) + "</li> ")
    if float(ares_dict["SHIB"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Shib:</strong> $""" + str(ares_dict["SHIB"]) + "</li> ")
    file.write("</ul>")
    file.write("<hr/>")

    file.write("""<ul class="list-group">""")
    file.write(
        """ <li class="list-group-item active"><center><strong>Deepro</strong></center></li> """)

    if float(deepro_dict["DOGE"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Doge:</strong> $""" + str(deepro_dict["DOGE"]) + "</li> ")
    if float(deepro_dict["TEL"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Tel:</strong> $""" + str(deepro_dict["TEL"]) + "</li> ")
    if float(deepro_dict["SHIB"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Shib:</strong> $""" + str(deepro_dict["SHIB"]) + "</li> ")
    file.write("</ul>")
    file.write("<hr/>")

    file.write("""<ul class="list-group">""")
    file.write(
        """ <li class="list-group-item active"><center><strong>Niaz</strong></center></li> """)

    if float(niaz_dict["DOGE"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Doge:</strong> $""" + str(niaz_dict["DOGE"]) + "</li> ")
    if float(niaz_dict["TEL"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Tel:</strong> $""" + str(niaz_dict["TEL"]) + "</li> ")
    if float(niaz_dict["SHIB"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Shib:</strong> $""" + str(niaz_dict["SHIB"]) + "</li> ")
    file.write("</ul>")
    file.write("<hr/>")

    file.write("""<ul class="list-group">""")
    file.write(
        """ <li class="list-group-item active"><center><strong>Shourov</strong></center></li> """)

    if float(shourov_dict["DOGE"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Doge:</strong> $""" + str(shourov_dict["DOGE"]) + "</li> ")
    if float(shourov_dict["TEL"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Tel:</strong> $""" + str(shourov_dict["TEL"]) + "</li> ")
    if float(shourov_dict["SHIB"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Shib:</strong> $""" + str(shourov_dict["SHIB"]) + "</li> ")
    file.write("</ul>")
    file.write("<hr/>")

    file.write("""<ul class="list-group">""")
    file.write(
        """ <li class="list-group-item active"><center><strong>Sunny</strong></center></li> """)

    if float(sunny_dict["DOGE"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Doge:</strong> $""" + str(sunny_dict["DOGE"]) + "</li> ")
    if float(sunny_dict["TEL"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Tel:</strong> $""" + str(sunny_dict["TEL"]) + "</li> ")
    if float(sunny_dict["SHIB"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Shib:</strong> $""" + str(sunny_dict["SHIB"]) + "</li> ")
    file.write("</ul>")
    file.write("<hr/>")

    file.write("""<ul class="list-group">""")
    file.write(
        """ <li class="list-group-item active"><center><strong>Shuvo</strong></center></li> """)

    if float(shuvo_dict["DOGE"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Doge:</strong> $""" + str(shuvo_dict["DOGE"]) + "</li> ")
    if float(shuvo_dict["TEL"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Tel:</strong> $""" + str(shuvo_dict["TEL"]) + "</li> ")
    if float(shuvo_dict["SHIB"]) > 0:
        file.write(""" <li class="list-group-item"><strong>Shib:</strong> $""" + str(shuvo_dict["SHIB"]) + "</li> ")
    file.write("</ul>")
    file.write("<hr/>")

    file.write(""" </div> """)
    file.write(""" </div> """)
    file.write(""" </body> """)
    file.write("</html>")

    file.close()


web_page()


url = "webpage.html"


try:
    # Windows
    os.startfile(url)
except AttributeError:
    try:
        # UNIX
        subprocess.call(['open', url])
    except:
        print('Could not open URL')


now = datetime.now()
