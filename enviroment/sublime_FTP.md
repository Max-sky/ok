Sublime Text 如何连接 FTP/SFTP
2015年08月02日 23:40:48 yuliying 阅读数：11028更多
个人分类： linux/c/c++/杂项
默认的sublime text是没有这个sftp连接功能的，这只是一个文本编辑器，相当于windows下的txt，所以要先装上插件:

1） 安装package control组件:

按Ctrl+`调出console, 粘贴以下代码到底部命令行并回车：

import urllib2,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();os.makedirs(ipp) if not os.path.exists(ipp) else None;open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())
如果是Sublime Text 3执行上述代码会报错，改成如下即可：

import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
2）重启Sublime Text。

如果在Perferences->package settings中看到package control这一项，则安装成功。

3）用Package Control安装sftp插件的方法：

按下Ctrl+Shift+P调出命令面板

输入install 调出 Install Package 选项并回车，然后输入ftp，下拉列表中会出现一些相关的插件，选中sftp进行安装就行了。

4) 对于某项目下的文件上传配置，可按如下配置操作：

右键项目-> SFTP/FTP -> Map to Remote .点击Map to Remote，看到配置文件。编辑完成后保存，在项目目录下可看到多了一个文件sftp-config.json。

普通的ftp连接修改下列配置:

"type":"ftp": ， 

"upload_on_save": true,         //保存文件的时候自动同步到ftp服务器

"sync_skip_deletes": true,     //同步时跳过删除的文件

"host": "192.168.0.148",         //ftp服务器地址

"user": "ftptest",                        //用户名

"password": "yuliying",           //密码

"port":"21" ，                            //端口

"remote_path": "/data",          //ftp服务器项目目录

配置完成后右键项目-> SFTP/FTP , 在这里就可以进行一系列操作了,具体操作菜单写的很清楚了。