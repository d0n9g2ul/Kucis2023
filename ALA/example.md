# Kucis2023
---
## Subject: Create Log Analyzer
---
## Version
- Python 3.10.12


import ALA


da = ALA.read_csv('csvfile')
da = ALA.WebParser(dataframe=da)
print(da.total_ip_count())
print(da.ip_count())
print(da.status_count())
print(da.filter_by_status('200').ip_count())


db = ALA.StatParser('filename')
print(db.total_dbte_count())
print(db.file_count())
print(db.filter_by_dbte('2023-11-07'))


dc = ALA.JournalParser('filename')
print(dc.by_dcte())
print(dc.by_time())
print(dc.by_message())
print(dc.by_process())


dd = ALA.LastParser('filename')
print(dd.connect_user())
print(dd.connect_time())


de = ALA.LastbParser('filename')
print(de.failed_attp())
print(de.all_ips())
print(de.attempt_date('2023-11-07'))


df = ALA.NetsParser('filename')
print(df.all_PID())
print(df.local_ips())
print(df.foreign_ips())
print(df.state_count())
print(df.established_ports())
print(df.established_PID())


dg = ALA.TopParser('filename')
print(dg.high_cpu(5))
print(dg.mem_usage())
print(dg.high_memory(5))
print(dg.is_running())