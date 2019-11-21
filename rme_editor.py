import collections
import sys
from rme_table4_text import tr_li_proj
from rme_table4_text import tr_li_history

table= collections.namedtuple(
    "compu", ["values", "indices", "dense_shape"])

with open('./resume_template.doc') as f:
    file_bone = f.read()

with open('./rme_head') as f:
    fh = f.read()

with open('./rme_table01') as f:
    file_t1 = f.read()
with open('./rme_table02') as f:
    file_t2 = f.read()
with open('./rme_table03') as f:
    file_t3 = f.read()
with open('./rme_table04') as f:
    file_t4 = f.read()

with open('./rme_table05') as f:
    file_t5 = f.read()

with open('./rme_table_template.doc') as f:
    file_tb = f.read()

with open('./rme_table04_template.doc') as f:
    file_tb04 = f.read()
with open('./rme_table05_template.doc') as f:
    file_tb05 = f.read()

class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'

final = open('./rme_final.doc','w')
lines = []

def format_table(file_tb,tb_wd, tr_li):
    lines = []
    tr_li_iter=iter(tr_li)
    for ix,line in enumerate(file_tb.split('\n')):
        if '{tb}' in line:
        # if kw1 in line:
            line = line.format_map(SafeDict(tb=tb_wd))
        if '{tr}' in line:
        # if kw2 in line:
            line = line.format_map(SafeDict(tr=next(tr_li_iter)))
        lines.append(line)
    ret = '\n'.join(lines)
    return ret

def format_table_04(file_tb,tr_li):
    lines = []
    if 'work_time' in tr_li.keys():
        work_time = tr_li['work_time']
    if 'work_company' in tr_li.keys():
        work_company = tr_li['work_company']
    if 'work_title' in tr_li.keys():
        work_title = tr_li['work_title']
    if 'work_industry' in tr_li.keys():
        work_industry = tr_li['work_industry']
    if 'work_desp' in tr_li.keys():
        work_desp = tr_li['work_desp']
    if 'proj_name' in tr_li.keys():
        proj_name = tr_li['proj_name']
    if 'proj_per' in tr_li.keys():
        proj_per = tr_li['proj_per']
    if 'proj_desp' in tr_li.keys():
        proj_desp = tr_li['proj_desp']
    for ix,line in enumerate(file_tb.split('\n')):
        if '{work_time}' in line:
            line = line.format_map(SafeDict(work_time=work_time))
        if '{work_company}' in line:
            line = line.format_map(SafeDict(work_company=work_company))
        if '{work_desp}' in line:
            line = line.format_map(SafeDict(work_desp=work_desp))
        if '{work_title}' in line:
            line = line.format_map(SafeDict(work_title=work_title))
        if '{work_industry}' in line:
            line = line.format_map(SafeDict(work_industry=work_industry))
        if '{proj_name}' in line:
            line = line.format_map(SafeDict(proj_name=proj_name))
        if '{proj_per}' in line:
            line = line.format_map(SafeDict(proj_per=proj_per))
        if '{proj_desp}' in line:
            line = line.format_map(SafeDict(proj_desp=proj_desp))
        lines.append(line)
    ret = '\n'.join(lines)
    return ret

tb_wd = '个人简历网站'
tr_li= []
tr_li.append(
'www.oneyardline.cn')
tr_li=tr_li + ['']*10
# file_t6=format_table(file_tb,tb_wd, tr_li)

def gen_table04(file_t4,file04_template,tr_li_history):
    lines = []
    file_history=[]
    [file_history.append(format_table_04(file04_template, history)) for history in tr_li_history]
    itr = iter(file_history)
    for ix,line in enumerate(file_t4.split('\n')):
        if '{tb}' in line:
            print(line)
            line = line.format_map(SafeDict(tb=next(itr)))
        lines.append(line)
    ret = '\n'.join(lines)
    return ret

# file_t1=format_table(file_t1, '{info}', tr_li)
file_t4 = gen_table04(file_t4,file_tb04,tr_li_history)
file_t5 = gen_table04(file_t5,file_tb05,tr_li_proj)
file_tl=[file_t1,file_t2,file_t3,file_t4,file_t5]
file_tl=file_tl+['']*10
# print(file_tl[0])

# for line in file_bone.split('\n'):
file_tl_iter=iter(file_tl)
for ix,line in enumerate(file_bone.split('\n')):

    if '{file_head}' in line:
        print(line)
        line = line.format_map(SafeDict(file_head=fh))
    if '{ft}' in line:
        print(line)
        line = line.format_map(SafeDict(ft=next(file_tl_iter)))
    # if 'ft1' in line:
    #     print('get ft1')
    #     line = line.format_map(SafeDict(ft1=file_t2))
    # if 'ft2' in line:
    #     print('get ft2')
    #     line = line.format_map(SafeDict(ft2=file_t3))
    # if 'ft3' in line:
    #     print('get ft3')
    #     line = line.format_map(SafeDict(ft3=file_t4))

    # line = line.format_map(SafeDict(file_head='file_head'))
    lines.append(line)

final.writelines(lines)

