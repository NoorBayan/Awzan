import pandas as pd
p=pd.read_csv('corpus/awzan.csv',sep='\t',encoding='utf-16')
sea = pd.read_csv('corpus/Seas_info.csv', sep='\t', encoding='utf-16')
seas = dict(zip(sea['Snum'], sea['Sname']))
seas={i:seas[i] for i in set(p.Sid)}
seas = dict([(0, 'الكل')] + list(seas.items()))
revers_seas = {value: key for key, value in seas.items()}
################
topics=dict(pd.read_csv('corpus\Topics.csv',sep='\t',encoding='utf-16').Topic)
topics={i:topics[i] for i in set(p.Topic)}
topics = dict([(0, 'الكل')] + list(topics.items()))
revers_topics = {value: key for key, value in topics.items()}
#########
rhymes=dict(pd.read_csv('corpus\Rhymes.csv',sep='\t',encoding='utf-16').Qafih)
rhymes={i:rhymes[i] for i in set(p.Rid) if i!=-1}
rhymes = dict([(0, 'الكل')] + list(rhymes.items()))
revers_rhymes = {value: key for key, value in rhymes.items()}
periods=dict(pd.read_csv('corpus\Periods.csv',sep='\t',encoding='utf-16').Period)
periods={i:periods[i] for i in set(p.Fid) if i!=-1}
periods = dict([(0, 'الكل')] + list(periods.items()))
revers_periods = {value: key for key, value in periods.items()}
#########
authers=dict(pd.read_csv('corpus\Authers.csv',sep='\t',encoding='utf-16').Auther)
authers={i:authers[i] for i in set(p.Aid) if i!=-1}
authers = dict([(0, 'الكل')] + list(authers.items()))
revers_authers = {value: key for key, value in authers.items()}