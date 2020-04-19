import requests

url = "http://masslandrecords.com/suffolk/default.aspx"

payload = "ScriptManager1=SearchFormEx1%24UpdatePanel%7CSearchFormEx1%24btnSearch&ScriptManager1_HiddenField=%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3Aeffe2a26%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3A475a4ef5%3A5546a2b%3A497ef277%3Aa43b07eb%3Ad2e10b12%3A37e2e5c9%3A5a682656%3A1d3ed089%3Af9029856%3Ad1a1d569%3B&__VIEWSTATE=&Navigator1%24SearchOptions1%24DocImagesCheck=on&SearchFormEx1%24ACSTextBox_DateFrom=11%2F1%2F2019&SearchFormEx1%24ACSTextBox_DateTo=12%2F31%2F2019&SearchFormEx1%24ACSDropDownList_DocumentType=-2&SearchFormEx1%24ACSDropDownList_Towns=-2&ImageViewer1%24ScrollPos=&ImageViewer1%24ScrollPosChange=&ImageViewer1%24_imgContainerWidth=0&ImageViewer1%24_imgContainerHeight=0&ImageViewer1%24isImageViewerVisible=true&ImageViewer1%24hdnWidgetSize=&ImageViewer1%24DragResizeExtender_ClientState=&CertificateViewer1%24ScrollPos=&CertificateViewer1%24ScrollPosChange=&CertificateViewer1%24_imgContainerWidth=0&CertificateViewer1%24_imgContainerHeight=0&CertificateViewer1%24isImageViewerVisible=true&CertificateViewer1%24hdnWidgetSize=&CertificateViewer1%24DragResizeExtender_ClientState=&DocList1%24ctl03=&DocList1%24ctl05=&DocDetails1%24PageSize=&DocDetails1%24PageIndex=&DocDetails1%24SortExpression=&BasketCtrl1%24ctl01=&BasketCtrl1%24ctl03=&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__ASYNCPOST=true&SearchFormEx1%24btnSearch.x=59&SearchFormEx1%24btnSearch.y=5"
headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'X-MicrosoftAjax': 'Delta=true',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Accept': '*/*',
    'Origin': 'http://masslandrecords.com',
    'Referer': 'http://masslandrecords.com/suffolk/',
    'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
    'Cookie': 'visid_incap_2183455=x6LfP9tZSJqATKZv4GUuH77BmV4AAAAAQUIPAAAAAAAiPMDcl3GzRd/L6m2Kk1NK; incap_ses_530_2183455=D0b7YK+h4zoOeh6xs/FaB77BmV4AAAAA7ox7V/X7spj8Ux/Rocx91w==; ASP.NET_SessionId=b1vouymswnaxjw55ng05qh45; incap_ses_703_2183455=cLClLy7H7Fz576kNHpvBCSLCmV4AAAAAoTCIv4LAUPL4YIn4LeQI3A==; TS015e6998=01651f8bb5c5850666eabbfb555631096297065d41f8359a1a02bc928f7e911d666ffb7cf8ecea4e68e4fae84cd96cb0cdf8dbe8de616f5377723f1b4d9254f492d7c132fc; incap_ses_148_2183455=tbY6UweKUzZIDtW1WtENAuuhnF4AAAAAGgeRG9PQr20DVaaXtIkJ1A==',
    'Content-Type': 'text/plain',
    'Cookie': 'TS015e6998=01651f8bb5c5850666eabbfb555631096297065d41f8359a1a02bc928f7e911d666ffb7cf8ecea4e68e4fae84cd96cb0cdf8dbe8de616f5377723f1b4d9254f492d7c132fc'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
