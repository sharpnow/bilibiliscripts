from http import cookies
from sqlite3 import Time
from time import sleep, time
from webbrowser import get
import requests

# 记录使用的api
# 短信登录api
# 使用的参数
Account1 = "13056565727"
Account2 = "17683159595"

def GetSubscribeList(mid):
    url = "https://account.bilibili.com/api/member/getCardByMid?mid=" + str(mid)
    r = requests.get(url).json()
    return r['card']['attentions']

def Modify(uids):
    list = []

    for uid in uids:
        headers = {
            'authority': 'api.vc.bilibili.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://t.bilibili.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://t.bilibili.com/',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'buvid3=C023953D-80C7-40CB-AE94-D9B92F6B02A8143102infoc; LIVE_BUVID=AUTO2916075956152105; rpdid=|(k))JRuJlkY0J\'uY|~lml~JJ; pgv_pvi=182343680; AMCV_98CF678254E93B1B0A4C98A5@AdobeOrg=359503849|MCIDTS|18658|MCMID|89005596076711662373238391417866153626|MCAAMLH-1612600909|11|MCAAMB-1612600909|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1612003309s|NONE|vVersion|5.0.1; _ga=GA1.2.2137681814.1613788312; blackside_state=0; CURRENT_BLACKGAP=0; video_page_version=v_old_home; _uuid=10D7ED6F1-22E1-692A-467B-CBB13FF3E2C856824infoc; i-wanna-go-back=-1; b_ut=5; buvid4=6C3EBB50-0C7C-D0E3-0213-4778E51EFCDC37062-022012519-9TO+hWhxQHN5OWpTvoXv2s1myyCfBU+TY1qM0oHQ/ni1nS0Fi1Kt6w==; nostalgia_conf=-1; hit-dyn-v2=1; buvid_fp_plain=undefined; CURRENT_QUALITY=80; bp_article_offset_674053572=696118893378273300; bsource=search_baidu; bp_video_offset_674053572=696867257078251500; DedeUserID=239129100; DedeUserID__ckMd5=47fce8176c4e95d3; fingerprint3=e8487c7a528d7f8650e48262f4e90c70; PVID=1; fingerprint=fb490daaa29a3253a9c86b4b9124f416; innersign=1; b_lsid=1837CB47_182C5590DFC; CURRENT_FNVAL=4048; SESSDATA=ce1bb900,1676723002,39a9e*81; bili_jct=1f979e7cf57b18e67df30f7f154dd0cb; sid=5zjdgzh0; b_timer={"ffp":{"333.1007.fp.risk_C023953D":"182C51068BE","333.1193.fp.risk_C023953D":"182C581EA0E","333.969.fp.risk_C023953D":"182C0AE8363","333.999.fp.risk_C023953D":"182C580DFF7","333.42.fp.risk_C023953D":"182C58165CA","888.2421.fp.risk_C023953D":"182C3BAEBE0","333.337.fp.risk_C023953D":"182C5108177","333.788.fp.risk_C023953D":"182C55B05B1","444.42.fp.risk_C023953D":"182C5169EC1"}}; buvid_fp=fb490daaa29a3253a9c86b4b9124f416'
        }

        data = {
            'fid': str(uid),
            'act': '1',
            're_src': '11',
            'spmid': '333.999.0.0',
            'extend_content': '{"entity":"user","entity_id":'+ str(uid) +',"fp":"0\u0001864,,1536\u0001Win32\u00014\u00018\u000124\u00011\u0001zh-CN\u00011\u00010,,0,,0\u0001Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}',
            'jsonp':'jsonp',
            'csrf': '1f979e7cf57b18e67df30f7f154dd0cb'
        }

        resp = requests.post('https://api.bilibili.com/x/relation/modify', headers=headers, data=data, timeout=200)
        if(resp.status_code == 200):
            print(str(uid) + '关注成功')
            sleep(0.5)
        else:
            print(str(uid) + '关注失败',resp.content['message'].decode())
            list.append(uid)
    
    print(list)


uids = GetSubscribeList(3078223)

Modify(uids)




# 登录老账号
#LoginByIdentcode()
# 记录关注列表
# 退出老账号
#登录新账号
#关注老账号的关注列d
