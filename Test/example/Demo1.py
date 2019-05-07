# -*- coding:utf-8 -*-


from util import getSQLResult

sql = "select * from t_tn_online_bind_flow a where a.account_no = '6222020200097521997'"
res = getSQLResult(sql)  # [0][1:2:3]
print(res)
