#!/usr/bin/env python
# coding:utf8
import sys
import json
import codecs
import os
import datetime
import shutil
from properties import Properties

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 读取config.json，并将配置文件中的目录列表存入rootdirdict
rootdirdict = {}
backupdirstr = ''
templates = []


def mycopytree(src, dst, symlinks=False, ignore=None):
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    if not os.path.exists(dst):
        os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                mycopytree(srcname, dstname, symlinks, ignore)
            else:
                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
    try:
        shutil.copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)


def init():
    print '开始解析配置文件config.json'
    config = {}
    errmsg = ''
    with codecs.open("config.json", "rb", "UTF-8") as f:
        config = json.loads(f.read())
    if not config:
        errmsg = '配置文件config.json不存在'
        return errmsg

    rootdirs = config.get("rootdirs")
    if rootdirs:
        for x in rootdirs:
            rootdirdict[x['name']] = x['rootdir']
            if not os.path.exists(x['rootdir']):
                print x['name'] + x['rootdir']
                errmsg = '配置文件config.json中的根目录配置不正确'
                return errmsg
    else:
        errmsg = '配置文件config.json中rootdirs没有配置'
        return errmsg

    backupdir = config.get("backupdir")
    global backupdirstr
    backupdirstr = backupdir
    if not backupdir or not os.path.exists(backupdir):
        errmsg = '配置文件config.json中backupdir配置不正确'
        return errmsg

    print '配置文件config.json解析完成...'
    return errmsg


def inittemplate(templatefile):
    print '开始解析模板文件'+templatefile
    config = {}
    errmsg = ''
    with codecs.open(templatefile, "rb", "UTF-8") as f:
        config = json.loads(f.read())
    if not config:
        errmsg = '模板文件不存在'
        return errmsg

    global templates
    templates = config.get("templates")
    if templates:
        # for x in templates:
        #     print x
        pass
    else:
        errmsg = '模板文件中templates没有配置'
        return errmsg

    print '模板文件解析完成...'
    return errmsg


def backup(source, target):
    print '开始backup...'
    print 'source : ' + source
    print 'target : ' + target
    mycopytree(source, target)
    print '...backup结束'


def backupfile(source, target):
    print '开始backup...'
    print 'source : ' + source
    print 'target : ' + target
    path = os.path.split(target)
    if not os.path.exists(path[0]):
        os.makedirs(path[0])
    shutil.copy2(source, target)
    print '...backup结束'


def replacefile(source, target, propname, propcontent):
    # 如果target不存在，就先将source复制到target中
    print '开始替换...'
    print 'source : ' + source
    print 'target : ' + target
    print '属性名' + propname
    print '属性内容' + propcontent
    path = os.path.split(target)
    if not os.path.exists(path[0]):
        os.makedirs(path[0])
    shutil.copy2(source, target)
    targetfile = Properties(target)
    targetfile.put(propname, propcontent)
    print '...backup结束'


def backupall():
    print '开始全部backup...'
    backupname = backupdirstr + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    os.makedirs(backupname)
    print "备份目录创建成功 ：" + backupname
    for x in rootdirdict:
        targetdir = backupname + '/' + x
        print '开始备份 : ' + x + '...'
        backup(rootdirdict.get(x), targetdir)
        print '...' + x + '备份结束'
    print '...全部backup结束'


def gettarget(xsource, xtarget):
    target = {}
    if len(xtarget) == 0:
        for y in rootdirdict:
            if y != xsource:
                target[y] = rootdirdict.get(y)
    else:
        for y in xtarget:
            target[y] = rootdirdict.get(y)
    return target


def deploy(filename):
    print '开始deploy...' + filename
    for x in templates:
        print '******开始进行第'+str(x['id']) + '项操作****** '
        if x.has_key('sourcedir'):
            # 如果是dir，则进行复制
            target = gettarget(x.get('source'), x.get('target'))
            for y in target:
                for z in x.get('sourcedir'):
                    # 将sourcedir中所有的目录复制到target中
                    sourcedirt = rootdirdict.get(x.get('source'))+z
                    targetdirt = target[y]+z
                    backup(sourcedirt, targetdirt)
        elif x.has_key('sourcefile'):
            # 如果是文件，需要分析是替换还是复制
            target = gettarget(x.get('source'), x.get('target'))
            updatetype = x.get('update_type')
            if updatetype == 'update_line':
                updatename = x.get('update_name')
                if updatename and len(x.get('sourcefile')) == 1:
                    for y in target:
                        for z in x.get('sourcefile'):
                            # 将sourcedir中所有的目录复制到target中
                            sourcet = rootdirdict.get(x.get('source'))+z
                            targett = target[y]+z
                            updatecontent = x.get('update_content')
                            propcontent = Properties(sourcet).get(updatename)
                            if updatecontent:
                                if updatecontent.get(y):
                                    replacefile(
                                        sourcet, targett, updatename, updatecontent.get(y))
                                else:
                                    replacefile(sourcet, targett,
                                                updatename, propcontent)
                            else:
                                replacefile(sourcet, targett,
                                            updatename, propcontent)
                else:
                    print '模板中update_type是逐行替换，则update_name必须有值，且sourcefile数量只能为1'
            else:
                for y in target:
                    for z in x.get('sourcefile'):
                        # 将sourcedir中所有的目录复制到target中
                        sourcet = rootdirdict.get(x.get('source'))+z
                        targett = target[y]+z
                        backupfile(sourcet, targett)
        else:
            print '模板错误：id为' + x['id']
    print '...deploy结束'


msg = '''
一、配置文件：
1、config.json : 配置各省项目的根目录
2、template20180409.json ： 配置替换模板

二、使用方法
python tools.py [backup]|[deploy *.json]
backup : 备份全部目录
deploy : 按照*.json文件中的要求进行文件的批量修改替换，每次执行前会将当前的所有目录进行备份
'''


def main():
    args = sys.argv
    a = init()
    if a == '':
        if len(args) == 1:
            backupall()
        elif len(args) == 2:
            if args[1] == 'backup':
                backupall()
            else:
                print msg
        elif len(args) == 3:
            # 在更新之前先进行备份
            backupall()
            if args[1] == 'deploy':
                b = inittemplate(args[2])
                if b == '':
                    deploy(args[2])
                else:
                    print '模板文件有错误，请检查'
                    print b
            else:
                print msg
        else:
            print msg
    else:
        print '配置文件有错误，请检查'
        print a


if __name__ == '__main__':
    main()
