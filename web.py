#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import urllib2   
#import urllib.request
#import re   
#from bs4 import BeautifulSoup  
#from distutils.filelist import findall  

import re,sys
import urllib.request
import mysql.connector


def addDb(tt,ptt='ptt',pptt='pptt',cont='cont'):
	conn = mysql.connector.connect(user='root', password='123456', database='kiwitest')
	cursor = conn.cursor()
	cursor.execute('insert into k_docs (title, ptit, pptit, content) values (%s, %s, %s, %s)', ( tt,ptt,pptt,cont))
	conn.commit()
	cursor.close()
	conn.close()
#addDb('兜兜', '兜兜粑粑', '豆豆妈妈', 'dddddddddddddddddddd')

#获取首页的数据
def getIdx():
	#首页
	html = urllib.request.urlopen("http://man.linuxde.net").read().decode('utf-8')
	idx_links = re.findall( '<div id="tags-list" class="clearfix">(.+?)<div class="recent-updates" id="recent-updates-index">', html)
	idx_a = re.findall('<a href="(.+?)" title="(.+?)">(.+?)</a>', idx_links[0]);
	
	_arr = {};
	for val in idx_a:
		_arr[val[1]] = val[0]
	
	return _arr
	
def isIdx():
	return {'常用工具命令': 'http://man.linuxde.net/sub/常用工具命令','常用工具命令2': 'http://man.linuxde.net/sub/常用工具命令/page/2', 'Shell内建命令': 'http://man.linuxde.net/sub/Shell内建命令', '系统安全': 'http://man.linuxde.net/sub/系统安全', '进程和作业管理': 'http://man.linuxde.net/sub/进程和作业管理', '用户和工作组管理': 'http://man.linuxde.net/sub/用户和工作组管理', 'X-Windows': 'http://man.linuxde.net/sub/X-Windows', 'SELinux': 'http://man.linuxde.net/sub/SELinux', '文件系统管理': 'http://man.linuxde.net/sub/文件系统管理', '系统关机和重启': 'http://man.linuxde.net/sub/系统关机和重启', '网络应用': 'http://man.linuxde.net/sub/网络应用', '高级网络': 'http://man.linuxde.net/sub/高级网络', '网络测试': 'http://man.linuxde.net/sub/网络测试', '网络安全': 'http://man.linuxde.net/sub/网络安全', '网络配置': 'http://man.linuxde.net/sub/网络配置', '网络服务器': 'http://man.linuxde.net/sub/网络服务器', '软件包管理': 'http://man.linuxde.net/sub/软件包管理', '编程开发': 'http://man.linuxde.net/sub/编程开发', '打印': 'http://man.linuxde.net/sub/打印', '处理传送进来的文件': 'http://man.linuxde.net/sub/处理传送进来的文件', '文件传输服务': 'http://man.linuxde.net/sub/文件传输服务', '传送文件': 'http://man.linuxde.net/sub/传送文件', '文件传输': 'http://man.linuxde.net/sub/文件传输', '文档编辑': 'http://man.linuxde.net/sub/文档编辑', '文件处理': 'http://man.linuxde.net/sub/文件处理', '文件查找和比较': 'http://man.linuxde.net/sub/文件查找和比较', '文件内容查看': 'http://man.linuxde.net/sub/文件内容查看', '文件编辑': 'http://man.linuxde.net/sub/文件编辑', '目录基本操作': 'http://man.linuxde.net/sub/目录基本操作', '文件权限属性设置': 'http://man.linuxde.net/sub/文件权限属性设置', '文件过滤分割与合并': 'http://man.linuxde.net/sub/文件过滤分割与合并', '文件压缩与解压': 'http://man.linuxde.net/sub/文件压缩与解压', '文件备份和恢复': 'http://man.linuxde.net/sub/文件备份和恢复', '性能监测与优化': 'http://man.linuxde.net/sub/性能监测与优化', '硬件管理': 'http://man.linuxde.net/sub/硬件管理', '内核与模块管理': 'http://man.linuxde.net/sub/内核与模块管理', '磁盘管理': 'http://man.linuxde.net/sub/磁盘管理'}


def getAllPages():
	_step = 0;
	_max_arr = []
	for key,value in isIdx().items():
		_step = _step+1;
		if _step < 4000:
			if key == '常用工具命令2':
				list_page = urllib.request.urlopen( 'http://man.linuxde.net/sub/'+urllib.parse.quote('常用工具命令')+'/page/2').read().decode('utf-8');
			else:
				list_page = urllib.request.urlopen( 'http://man.linuxde.net/sub/'+urllib.parse.quote(key) ).read().decode('utf-8');
				
				
			list_page_links = re.findall('<ul id="arcs-list" class="clearfix">(.+?)﻿<div id="footer-wrap">', list_page)
			try:
				detail_link = re.findall('<a class="title" href="(.+?)" title="(.+?)">(.+?)</a>', list_page_links[0])
			except:
				pass
				
				
		
			for dd in detail_link:
				_max_arr.append(dd[0])
	
def allPages():
		return ['http://man.linuxde.net/mattrib', 'http://man.linuxde.net/mmove', 'http://man.linuxde.net/mdel', 'http://man.linuxde.net/linux%e6%96%87%e4%bb%b6%e5%92%8c%e7%9b%ae%e9%8c%84%e7%ae%a1%e7%90%86%e7%9a%84%e5%9f%ba%e6%9c%ac%e5%91%bd%e4%bb%a4', 'http://man.linuxde.net/find-2', 'http://man.linuxde.net/rm-remove', 'http://man.linuxde.net/cd-change-directory', 'http://man.linuxde.net/ls-list', 'http://man.linuxde.net/decompression-bomb', 'http://man.linuxde.net/malicious-source-code', 'http://man.linuxde.net/dd-command', 'http://man.linuxde.net/tar-bomb', 'http://man.linuxde.net/mkfs-command', 'http://man.linuxde.net/rm-rf-command', 'http://man.linuxde.net/mv-folderdevnull-command', 'http://man.linuxde.net/pssh', 'http://man.linuxde.net/screen', 'http://man.linuxde.net/speedtest-cli', 'http://man.linuxde.net/clockdiff', 'http://man.linuxde.net/ntpdate', 'http://man.linuxde.net/rsync', 'http://man.linuxde.net/vdfuse', 'http://man.linuxde.net/ngrep', 'http://man.linuxde.net/tempfile', 'http://man.linuxde.net/xargs', 'http://man.linuxde.net/awk', 'http://man.linuxde.net/yes', 'http://man.linuxde.net/date', 'http://man.linuxde.net/consoletype', 'http://man.linuxde.net/info', 'http://man.linuxde.net/hostid', 'http://man.linuxde.net/clear', 'http://man.linuxde.net/whoami', 'http://man.linuxde.net/users', 'http://man.linuxde.net/sleep', 'http://man.linuxde.net/md5sum', 'http://man.linuxde.net/mesg', 'http://man.linuxde.net/mtools', 'http://man.linuxde.net/login', 'http://man.linuxde.net/stty', 'http://man.linuxde.net/talk', 'http://man.linuxde.net/man', 'http://man.linuxde.net/whatis', 'http://man.linuxde.net/write', 'http://man.linuxde.net/who', 'http://man.linuxde.net/sum', 'http://man.linuxde.net/wall', 'http://man.linuxde.net/dircolors', 'http://man.linuxde.net/gpm', 'http://man.linuxde.net/bc', 'http://man.linuxde.net/cal', 'http://man.linuxde.net/cksum', 'http://man.linuxde.net/pstree-2', 'http://man.linuxde.net/vmstat-2', 'http://man.linuxde.net/xeyes', 'http://man.linuxde.net/fg-bg', 'http://man.linuxde.net/w-2', 'http://man.linuxde.net/sh', 'http://man.linuxde.net/trap', 'http://man.linuxde.net/let', 'http://man.linuxde.net/seq', 'http://man.linuxde.net/tput', 'http://man.linuxde.net/apropos', 'http://man.linuxde.net/set', 'http://man.linuxde.net/command', 'http://man.linuxde.net/dris', 'http://man.linuxde.net/fc', 'http://man.linuxde.net/bind', 'http://man.linuxde.net/readonly', 'http://man.linuxde.net/read', 'http://man.linuxde.net/bg', 'http://man.linuxde.net/ulimit', 'http://man.linuxde.net/enable', 'http://man.linuxde.net/declare', 'http://man.linuxde.net/wait', 'http://man.linuxde.net/builtin', 'http://man.linuxde.net/shopt', 'http://man.linuxde.net/exit', 'http://man.linuxde.net/jobs', 'http://man.linuxde.net/help', 'http://man.linuxde.net/history', 'http://man.linuxde.net/logout', 'http://man.linuxde.net/export', 'http://man.linuxde.net/exec', 'http://man.linuxde.net/env', 'http://man.linuxde.net/unset', 'http://man.linuxde.net/kill', 'http://man.linuxde.net/unalias', 'http://man.linuxde.net/type', 'http://man.linuxde.net/fg', 'http://man.linuxde.net/alias', 'http://man.linuxde.net/echo', 'http://man.linuxde.net/syslog', 'http://man.linuxde.net/openssl', 'http://man.linuxde.net/logwatch', 'http://man.linuxde.net/lastb', 'http://man.linuxde.net/sudo', 'http://man.linuxde.net/lastlog', 'http://man.linuxde.net/logrotate', 'http://man.linuxde.net/chroot', 'http://man.linuxde.net/logsave', 'http://man.linuxde.net/last', 'http://man.linuxde.net/ipcrm', 'http://man.linuxde.net/systemctl', 'http://man.linuxde.net/w', 'http://man.linuxde.net/watch', 'http://man.linuxde.net/pidof', 'http://man.linuxde.net/skill', 'http://man.linuxde.net/pgrep', 'http://man.linuxde.net/renice', 'http://man.linuxde.net/nohup', 'http://man.linuxde.net/ipcs', 'http://man.linuxde.net/pmap', 'http://man.linuxde.net/nice', 'http://man.linuxde.net/service', 'http://man.linuxde.net/pstree', 'http://man.linuxde.net/telint', 'http://man.linuxde.net/killall', 'http://man.linuxde.net/runlevel', 'http://man.linuxde.net/batch', 'http://man.linuxde.net/ps', 'http://man.linuxde.net/init', 'http://man.linuxde.net/crontab', 'http://man.linuxde.net/pkill', 'http://man.linuxde.net/atrm', 'http://man.linuxde.net/atq', 'http://man.linuxde.net/at', 'http://man.linuxde.net/chage', 'http://man.linuxde.net/id', 'http://man.linuxde.net/grpconv', 'http://man.linuxde.net/pwunconv', 'http://man.linuxde.net/pwconv', 'http://man.linuxde.net/nologin', 'http://man.linuxde.net/chpasswd', 'http://man.linuxde.net/grpunconv', 'http://man.linuxde.net/grpck', 'http://man.linuxde.net/groupdel', 'http://man.linuxde.net/chsh', 'http://man.linuxde.net/gpasswd', 'http://man.linuxde.net/pwck', 'http://man.linuxde.net/groupmod', 'http://man.linuxde.net/passwd', 'http://man.linuxde.net/chfn', 'http://man.linuxde.net/newusers', 'http://man.linuxde.net/logname', 'http://man.linuxde.net/groups', 'http://man.linuxde.net/finger', 'http://man.linuxde.net/su', 'http://man.linuxde.net/usermod', 'http://man.linuxde.net/groupadd', 'http://man.linuxde.net/userdel', 'http://man.linuxde.net/useradd', 'http://man.linuxde.net/xclip', 'http://man.linuxde.net/xset', 'http://man.linuxde.net/xlsfonts', 'http://man.linuxde.net/xhost', 'http://man.linuxde.net/xlsatoms', 'http://man.linuxde.net/xauth', 'http://man.linuxde.net/xlsclients', 'http://man.linuxde.net/xinit', 'http://man.linuxde.net/startx', 'http://man.linuxde.net/restorecon', 'http://man.linuxde.net/semanage', 'http://man.linuxde.net/setsebool', 'http://man.linuxde.net/getsebool', 'http://man.linuxde.net/sesearch', 'http://man.linuxde.net/seinfo', 'http://man.linuxde.net/chcon', 'http://man.linuxde.net/linux-fork-bomb-command', 'http://man.linuxde.net/repquota', 'http://man.linuxde.net/e2label', 'http://man.linuxde.net/findfs', 'http://man.linuxde.net/resize2fs', 'http://man.linuxde.net/e2image', 'http://man.linuxde.net/tune2fs', 'http://man.linuxde.net/sync', 'http://man.linuxde.net/swapoff', 'http://man.linuxde.net/swapon', 'http://man.linuxde.net/quota', 'http://man.linuxde.net/quotastats', 'http://man.linuxde.net/edquota', 'http://man.linuxde.net/quotaon', 'http://man.linuxde.net/quotacheck', 'http://man.linuxde.net/quotaoff', 'http://man.linuxde.net/mkfs', 'http://man.linuxde.net/mountpoint', 'http://man.linuxde.net/umount', 'http://man.linuxde.net/e2fsck', 'http://man.linuxde.net/dumpe2fs', 'http://man.linuxde.net/mount', 'http://man.linuxde.net/fsck', 'http://man.linuxde.net/mke2fs', 'http://man.linuxde.net/halt', 'http://man.linuxde.net/ctrlaltdel', 'http://man.linuxde.net/reboot', 'http://man.linuxde.net/shutdown', 'http://man.linuxde.net/poweroff', 'http://man.linuxde.net/axel', 'http://man.linuxde.net/jwhois', 'http://man.linuxde.net/curl', 'http://man.linuxde.net/wget', 'http://man.linuxde.net/telnet', 'http://man.linuxde.net/rexec', 'http://man.linuxde.net/rsh', 'http://man.linuxde.net/rlogin', 'http://man.linuxde.net/mail', 'http://man.linuxde.net/mailstat', 'http://man.linuxde.net/lynx', 'http://man.linuxde.net/elm', 'http://man.linuxde.net/mailq', 'http://man.linuxde.net/lftpget', 'http://man.linuxde.net/elinks', 'http://man.linuxde.net/ipcalc', 'http://man.linuxde.net/lftp', 'http://man.linuxde.net/tcpreplay', 'http://man.linuxde.net/pfctl', 'http://man.linuxde.net/iptraf', 'http://man.linuxde.net/ss', 'http://man.linuxde.net/nstat_rtacct', 'http://man.linuxde.net/lnstat', 'http://man.linuxde.net/arptables', 'http://man.linuxde.net/arpd', 'http://man.linuxde.net/tcpdump', 'http://man.linuxde.net/ip', 'http://man.linuxde.net/ip6tables-restore', 'http://man.linuxde.net/ip6tables-save', 'http://man.linuxde.net/ip6tables', 'http://man.linuxde.net/iptables-restore', 'http://man.linuxde.net/iptables-save', 'http://man.linuxde.net/iptables', 'http://man.linuxde.net/hping3', 'http://man.linuxde.net/iperf', 'http://man.linuxde.net/host', 'http://man.linuxde.net/tracepath', 'http://man.linuxde.net/arpwatch', 'http://man.linuxde.net/nslookup', 'http://man.linuxde.net/arping', 'http://man.linuxde.net/nc_netcat', 'http://man.linuxde.net/dig', 'http://man.linuxde.net/arp', 'http://man.linuxde.net/ping', 'http://man.linuxde.net/traceroute', 'http://man.linuxde.net/netstat', 'http://man.linuxde.net/ssh-copy-id', 'http://man.linuxde.net/ssh-agent', 'http://man.linuxde.net/ssh-add', 'http://man.linuxde.net/nmap', 'http://man.linuxde.net/iptstate', 'http://man.linuxde.net/ssh-keygen', 'http://man.linuxde.net/sftp-server', 'http://man.linuxde.net/sshd', 'http://man.linuxde.net/ssh-keyscan', 'http://man.linuxde.net/sftp', 'http://man.linuxde.net/ssh', 'http://man.linuxde.net/mii-tool', 'http://man.linuxde.net/ethtool', 'http://man.linuxde.net/nisdomainname', 'http://man.linuxde.net/dhclient', 'http://man.linuxde.net/domainname', 'http://man.linuxde.net/ypdomainname', 'http://man.linuxde.net/usernetctl', 'http://man.linuxde.net/dnsdomainname', 'http://man.linuxde.net/hostname', 'http://man.linuxde.net/ifup', 'http://man.linuxde.net/ifcfg', 'http://man.linuxde.net/ifconfig', 'http://man.linuxde.net/ifdown', 'http://man.linuxde.net/route', 'http://man.linuxde.net/mysqlimport', 'http://man.linuxde.net/ftpshut', 'http://man.linuxde.net/ftpcount', 'http://man.linuxde.net/exportfs', 'http://man.linuxde.net/apachectl', 'http://man.linuxde.net/ab', 'http://man.linuxde.net/squid', 'http://man.linuxde.net/mysql', 'http://man.linuxde.net/sendmail', 'http://man.linuxde.net/mysqlshow', 'http://man.linuxde.net/smbpasswd', 'http://man.linuxde.net/squidclient', 'http://man.linuxde.net/smbclient', 'http://man.linuxde.net/showmount', 'http://man.linuxde.net/nfsstat', 'http://man.linuxde.net/mysqladmin', 'http://man.linuxde.net/ftpwho', 'http://man.linuxde.net/mysqldump', 'http://man.linuxde.net/htdigest', 'http://man.linuxde.net/htpasswd', 'http://man.linuxde.net/ftptop', 'http://man.linuxde.net/factor', 'http://man.linuxde.net/dnf', 'http://man.linuxde.net/dpkg-reconfigure', 'http://man.linuxde.net/dpkg', 'http://man.linuxde.net/apt-sortpkgs', 'http://man.linuxde.net/apt-key', 'http://man.linuxde.net/aptitude', 'http://man.linuxde.net/apt-get', 'http://man.linuxde.net/ntsysv', 'http://man.linuxde.net/chkconfig', 'http://man.linuxde.net/rpmsign', 'http://man.linuxde.net/rpmdb', 'http://man.linuxde.net/yum', 'http://man.linuxde.net/dpkg-trigger', 'http://man.linuxde.net/rpm', 'http://man.linuxde.net/rcconf', 'http://man.linuxde.net/rpmbuild', 'http://man.linuxde.net/rpmverify', 'http://man.linuxde.net/rpmquery', 'http://man.linuxde.net/patch', 'http://man.linuxde.net/rpm2cpio', 'http://man.linuxde.net/dpkg-statoverride', 'http://man.linuxde.net/dpkg-preconfigure', 'http://man.linuxde.net/dpkg-split', 'http://man.linuxde.net/dpkg-query', 'http://man.linuxde.net/dpkg-divert', 'http://man.linuxde.net/dpkg-deb', 'http://man.linuxde.net/ldconfig', 'http://man.linuxde.net/readelf', 'http://man.linuxde.net/objdump', 'http://man.linuxde.net/pstack', 'http://man.linuxde.net/indent', 'http://man.linuxde.net/gdb', 'http://man.linuxde.net/gcc', 'http://man.linuxde.net/expr', 'http://man.linuxde.net/test', 'http://man.linuxde.net/php', 'http://man.linuxde.net/protoize', 'http://man.linuxde.net/mktemp', 'http://man.linuxde.net/perl', 'http://man.linuxde.net/make', 'http://man.linuxde.net/ldd', 'http://man.linuxde.net/nm', 'http://man.linuxde.net/unprotoize', 'http://man.linuxde.net/ld', 'http://man.linuxde.net/gcov', 'http://man.linuxde.net/as', 'http://man.linuxde.net/reject', 'http://man.linuxde.net/lpadmin', 'http://man.linuxde.net/cupsenable', 'http://man.linuxde.net/accept', 'http://man.linuxde.net/lpstat', 'http://man.linuxde.net/cupsdisable', 'http://man.linuxde.net/lpc', 'http://man.linuxde.net/cancel', 'http://man.linuxde.net/lp', 'http://man.linuxde.net/lpq', 'http://man.linuxde.net/eject', 'http://man.linuxde.net/lprm', 'http://man.linuxde.net/lpr', 'http://man.linuxde.net/uupick', 'http://man.linuxde.net/uupick', 'http://man.linuxde.net/uucp', 'http://man.linuxde.net/bye', 'http://man.linuxde.net/ftp', 'http://man.linuxde.net/tftp', 'http://man.linuxde.net/scp', 'http://man.linuxde.net/ncftp', 'http://man.linuxde.net/rcp', 'http://man.linuxde.net/mtype', 'http://man.linuxde.net/mattrib', 'http://man.linuxde.net/linux-%e6%96%87%e4%bb%b6%e4%b8%8e%e7%9b%ae%e5%bd%95%e7%ae%a1%e7%90%86', 'http://man.linuxde.net/iconv', 'http://man.linuxde.net/nl', 'http://man.linuxde.net/basename', 'http://man.linuxde.net/unlink', 'http://man.linuxde.net/pathchk', 'http://man.linuxde.net/touch', 'http://man.linuxde.net/rename', 'http://man.linuxde.net/dd', 'http://man.linuxde.net/dirname', 'http://man.linuxde.net/updatedb', 'http://man.linuxde.net/ln', 'http://man.linuxde.net/cat', 'http://man.linuxde.net/strings', 'http://man.linuxde.net/diff', 'http://man.linuxde.net/cmp', 'http://man.linuxde.net/diff3', 'http://man.linuxde.net/locate_slocate', 'http://man.linuxde.net/which', 'http://man.linuxde.net/find', 'http://man.linuxde.net/whereis', 'http://man.linuxde.net/hexdump', 'http://man.linuxde.net/od', 'http://man.linuxde.net/cut', 'http://man.linuxde.net/tail', 'http://man.linuxde.net/head', 'http://man.linuxde.net/less', 'http://man.linuxde.net/more', 'http://man.linuxde.net/nano', 'http://man.linuxde.net/sed', 'http://man.linuxde.net/pico', 'http://man.linuxde.net/emacs', 'http://man.linuxde.net/jed', 'http://man.linuxde.net/joe', 'http://man.linuxde.net/ed', 'http://man.linuxde.net/ex', 'http://man.linuxde.net/vi', 'http://man.linuxde.net/install', 'http://man.linuxde.net/tree', 'http://man.linuxde.net/popd', 'http://man.linuxde.net/pushd', 'http://man.linuxde.net/dirs', 'http://man.linuxde.net/rmdir', 'http://man.linuxde.net/mkdir', 'http://man.linuxde.net/rm', 'http://man.linuxde.net/pwd', 'http://man.linuxde.net/ls', 'http://man.linuxde.net/mv', 'http://man.linuxde.net/cp', 'http://man.linuxde.net/cd', 'http://man.linuxde.net/dos2unix', 'http://man.linuxde.net/setfacl', 'http://man.linuxde.net/umask', 'http://man.linuxde.net/lsattr', 'http://man.linuxde.net/chmod', 'http://man.linuxde.net/chown', 'http://man.linuxde.net/chgrp', 'http://man.linuxde.net/chattr', 'http://man.linuxde.net/stat', 'http://man.linuxde.net/file', 'http://man.linuxde.net/egrep', 'http://man.linuxde.net/fgrep', 'http://man.linuxde.net/split', 'http://man.linuxde.net/grep', 'http://man.linuxde.net/comm', 'http://man.linuxde.net/printf', 'http://man.linuxde.net/expand', 'http://man.linuxde.net/spell', 'http://man.linuxde.net/pr', 'http://man.linuxde.net/look', 'http://man.linuxde.net/tac', 'http://man.linuxde.net/wc', 'http://man.linuxde.net/fmt', 'http://man.linuxde.net/rev', 'http://man.linuxde.net/diffstat', 'http://man.linuxde.net/ispell', 'http://man.linuxde.net/uniq', 'http://man.linuxde.net/tee', 'http://man.linuxde.net/paste', 'http://man.linuxde.net/sort', 'http://man.linuxde.net/unexpand', 'http://man.linuxde.net/csplit', 'http://man.linuxde.net/fold', 'http://man.linuxde.net/join', 'http://man.linuxde.net/col', 'http://man.linuxde.net/tr', 'http://man.linuxde.net/colrm', 'http://man.linuxde.net/lha', 'http://man.linuxde.net/bzcmp', 'http://man.linuxde.net/bzcat', 'http://man.linuxde.net/unarj', 'http://man.linuxde.net/zcat', 'http://man.linuxde.net/znew', 'http://man.linuxde.net/zipsplit', 'http://man.linuxde.net/arj', 'http://man.linuxde.net/gzexe', 'http://man.linuxde.net/bzgrep', 'http://man.linuxde.net/compress', 'http://man.linuxde.net/zfore', 'http://man.linuxde.net/bzless', 'http://man.linuxde.net/bzmore', 'http://man.linuxde.net/zipinfo', 'http://man.linuxde.net/unzip', 'http://man.linuxde.net/bzip2recover', 'http://man.linuxde.net/tar', 'http://man.linuxde.net/bunzip2', 'http://man.linuxde.net/bzdiff', 'http://man.linuxde.net/gunzip', 'http://man.linuxde.net/zip', 'http://man.linuxde.net/bzip2', 'http://man.linuxde.net/gzip', 'http://man.linuxde.net/uncompress', 'http://man.linuxde.net/cpio', 'http://man.linuxde.net/restore', 'http://man.linuxde.net/dump', 'http://man.linuxde.net/inotifywait', 'http://man.linuxde.net/nethogs', 'http://man.linuxde.net/ifstat', 'http://man.linuxde.net/dstat', 'http://man.linuxde.net/ltrace', 'http://man.linuxde.net/iotop', 'http://man.linuxde.net/strace', 'http://man.linuxde.net/fuser', 'http://man.linuxde.net/lsof', 'http://man.linuxde.net/tload', 'http://man.linuxde.net/time', 'http://man.linuxde.net/vmstat', 'http://man.linuxde.net/sar', 'http://man.linuxde.net/mpstat', 'http://man.linuxde.net/iostat', 'http://man.linuxde.net/free', 'http://man.linuxde.net/uptime', 'http://man.linuxde.net/top', 'http://man.linuxde.net/losetup', 'http://man.linuxde.net/dmidecode', 'http://man.linuxde.net/hwclock', 'http://man.linuxde.net/cdrecord', 'http://man.linuxde.net/setpci', 'http://man.linuxde.net/lspci', 'http://man.linuxde.net/lsusb', 'http://man.linuxde.net/arch', 'http://man.linuxde.net/volname', 'http://man.linuxde.net/systool', 'http://man.linuxde.net/lsb_release', 'http://man.linuxde.net/sysctl', 'http://man.linuxde.net/slabtop', 'http://man.linuxde.net/kernelversion', 'http://man.linuxde.net/get_module', 'http://man.linuxde.net/kexec', 'http://man.linuxde.net/dmesg', 'http://man.linuxde.net/uname', 'http://man.linuxde.net/depmod', 'http://man.linuxde.net/bmodinfo', 'http://man.linuxde.net/modprobe', 'http://man.linuxde.net/rmmod', 'http://man.linuxde.net/insmod', 'http://man.linuxde.net/lsmod', 'http://man.linuxde.net/blkid', 'http://man.linuxde.net/du', 'http://man.linuxde.net/lsblk', 'http://man.linuxde.net/vgremove', 'http://man.linuxde.net/lvresize', 'http://man.linuxde.net/lvremove', 'http://man.linuxde.net/lvreduce', 'http://man.linuxde.net/pvs', 'http://man.linuxde.net/pvchange', 'http://man.linuxde.net/pvck', 'http://man.linuxde.net/pvremove', 'http://man.linuxde.net/lvextend', 'http://man.linuxde.net/pvdisplay', 'http://man.linuxde.net/lvdisplay', 'http://man.linuxde.net/pvscan', 'http://man.linuxde.net/lvscan', 'http://man.linuxde.net/lvcreate', 'http://man.linuxde.net/pvcreate', 'http://man.linuxde.net/vgconvert', 'http://man.linuxde.net/blockdev', 'http://man.linuxde.net/mkswap', 'http://man.linuxde.net/vgchange', 'http://man.linuxde.net/mknod', 'http://man.linuxde.net/mkisofs', 'http://man.linuxde.net/mkinitrd', 'http://man.linuxde.net/vgreduce', 'http://man.linuxde.net/hdparm', 'http://man.linuxde.net/vgextend', 'http://man.linuxde.net/partprobe', 'http://man.linuxde.net/vgscan', 'http://man.linuxde.net/vgcreate', 'http://man.linuxde.net/fdisk', 'http://man.linuxde.net/badblocks', 'http://man.linuxde.net/vgdisplay', 'http://man.linuxde.net/mkbootdisk', 'http://man.linuxde.net/grub', 'http://man.linuxde.net/convertquota', 'http://man.linuxde.net/lilo', 'http://man.linuxde.net/df', 'http://man.linuxde.net/parted']
	
def getNews():
		pages = allPages()
		_pnum = 0;
		for val in pages:
			_pnum = _pnum+1
			if _pnum < 3:
				try:
					html_detail = urllib.request.urlopen( val ).read().decode('utf-8');
					title = re.findall('<h1 class="left">(.+?)</h1>', html_detail)
					content = re.findall('<div id="arc-body">(.+?)</div><div id="ad-arc-bottom">', html_detail, re.S)
						
					ptitle = re.findall('</h1><div class="right"> <a href="(.+?)" rel="tag">(.+?)</a>(.+?)<div id="ad-arc-top', html_detail)
					
					
					pptitle = re.findall('category tag">(.+?)</a>(.+?)title" class="clearfix', html_detail)
					
					print(title[0])
					print(ptitle[0][1])
					#print(pptitle[0][0])
			
					#print('')
					print('')
					addDb(title[0], ptitle[0][1], pptitle[0][0], content[0])
					#abddDb(title[0],ptitle[0][1],pptitle[0][0],content)
				except:
					pass
		
	

#getNews()

def buff():
	keys = 0
	arr_news = []
	for val in idx_a:
		keys = keys+1
		
		#continue
		
		
		if keys < 4:
			print()
			print()
			print()
			print(val[0])
			#获取列表的link( 有的有第二页 )
			list_page = urllib.request.urlopen( 'http://man.linuxde.net/sub/'+urllib.parse.quote(val[1]) ).read().decode('utf-8');
			#list_page_links = re.findall('<ul id="arcs-list" class="clearfix">(.+?)<div class=\'paging clearfix\'>', list_page)
			list_page_links = re.findall('<ul id="arcs-list" class="clearfix">(.+?)﻿<div id="footer-wrap">', list_page)
			
			print(list_page_links)
			
			try:
				#print(page_alllinks[0])
				#获取详情页面的链接
				detail_link = re.findall('<a class="title" href="(.+?)" title="(.+?)">(.+?)</a>', page_alllinks[0])
				#print(detail_link)
				
				#循环list的链接
				for item in detail_link:
					#print(item[0])
					html_detail = urllib.request.urlopen( item[0] ).read().decode('utf-8');
					html_detail_pics_title = re.findall('<h1 class="left">(.+?)</h1>', html_detail)
					html_detail_pics_contetn = re.findall('<div id="arc-body">(.+?)</div><div id="ad-arc-bottom">', html_detail, re.S)
					
					print(html_detail_pics_title)
					print(html_detail_pics_contetn)
					print('')
					print('')
					print('')
					print('')
			except:
				pass
			
			

		keys = keys+1

