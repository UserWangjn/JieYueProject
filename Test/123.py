# -*- coding:utf-8 -*-


from util import getSQLResult

sql = "select * from t_tn_online_bind_flow a where a.account_no = '6222020200097521997'"
print(getSQLResult(sql))
