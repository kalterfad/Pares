import requests

cookies = {
'_2gis_webapi_user': '51333e25-3566-4513-b027-a82174ca7fb9',
'_ym_uid': '1646391910339696623',
'_ym_d': '1653403977',
'_ga': 'GA1.2.1065716343.1653403977',
'ipp_uid': '1653512513691%2FthrciMLeZMpRpgag%2FtXJL4E%2BVq%2Bro%2FeLQoko7Bg%3D%3D',
'_sa': 'SA1.b458abba-2df7-4a6a-ae2e-80b3ced67f96.1656439961',
'_gid': 'GA1.2.1162680033.1659976865',
'_ym_isad': '1',
'_2gis_webapi_session': 'b403f080-342d-4f5b-8aae-521cdd07d009',
'_gat_online5': '1',
}

headers = {
'authority': 'catalog.api.2gis.ru',
'accept': 'application/json, text/plain, */*',
'accept-language': 'ru,en;q=0.9',
# Requests sorts cookies= alphabetically
# 'cookie': '_2gis_webapi_user=51333e25-3566-4513-b027-a82174ca7fb9; _ym_uid=1646391910339696623; _ym_d=1653403977; _ga=GA1.2.1065716343.1653403977; ipp_uid=1653512513691%2FthrciMLeZMpRpgag%2FtXJL4E%2BVq%2Bro%2FeLQoko7Bg%3D%3D; _sa=SA1.b458abba-2df7-4a6a-ae2e-80b3ced67f96.1656439961; _gid=GA1.2.1162680033.1659976865; _ym_isad=1; _2gis_webapi_session=b403f080-342d-4f5b-8aae-521cdd07d009; _gat_online5=1',
'origin': 'https://2gis.ru',
'referer': 'https://2gis.ru/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.148 YaBrowser/22.7.2.899 Yowser/2.5 Safari/537.36',
}

response = requests.get('https://catalog.api.2gis.ru/3.0/items/byid?id=2393065583018885_szBjzr65365H3H3694IGGGG0lfj9lv95G6GB1A4388228B96qEpt7A4483G70G6G1J3JIJ0JvtBnuv195C9B1667B5H2H3JH5d&key=rurbbn3446&locale=ru_RU&fields=items.locale,items.flags,search_attributes,items.adm_div,items.city_alias,items.region_id,items.segment_id,items.reviews,items.point,request_type,context_rubrics,query_context,items.links,items.name_ex,items.org,items.group,items.dates,items.external_content,items.contact_groups,items.comment,items.ads.options,items.email_for_sending.allowed,items.stat,items.stop_factors,items.description,items.geometry.centroid,items.geometry.selection,items.geometry.style,items.timezone_offset,items.context,items.level_count,items.address,items.is_paid,items.access,items.access_comment,items.for_trucks,items.is_incentive,items.paving_type,items.capacity,items.schedule,items.floors,ad,items.rubrics,items.routes,items.platforms,items.directions,items.barrier,items.reply_rate,items.purpose,items...\\[sid\\]=854e7251-d579-4ddb-b493-1e8c7762c76b&stat\\[user\\]=51333e25-3566-4513-b027-a82174ca7fb9&shv=2022-08-05-18&r=2014915632', headers=headers)
c = 0
print(response.json())