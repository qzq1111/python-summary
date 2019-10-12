"""
使用前须知：
1. 安装 pip install suds-community
2. 免费的webservice服务网站 http://www.webxml.com.cn/zh_cn/web_services.aspx
"""
from suds import sudsobject
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

# 1. 调用webservice查询国内手机号码归属地查询WEB服务
# 连接到webservice服务，获取服务方法
client = Client('http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl')
# 输出服务方法一共有两个方法 getDatabaseInfo() getMobileCodeInfo(xs:string mobileCode, xs:string userID)
# 具体含义请看 http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx
print(client)

# 查询手机号码归属地
print(client.service.getMobileCodeInfo("18300000000", ""))
# 18300000000：广东 深圳 广东移动全球通卡


# 2. 解决suds.TypeNotFound: Type not found: '(schema, http://www.w3.org/2001/XMLSchema, ) 错误。
# 用浏览器打开webservice服务链接，找到webservice服务中的`targetNamespace`，将它的只添加到过滤的命名空间就能解决问题。
# 但是一旦使用这个方法。速度会变得很慢（原因未知）

imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')
doctor = ImportDoctor(imp)
client = Client('http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl', doctor=doctor)

print(client.service.getSupportCityString("四川"))

# 3. 参数传递使用字典方式，此方法需要找到getSupportCityString服务的参数名，然后传入对应的值
print(client.service.getSupportCityString(**{"theRegionCode": "四川"}))
