![FindEverything](https://socialify.git.ci/AabyssZG/FindEverything/image?description=1&descriptionEditable=%E5%86%85%E7%BD%91%E6%B8%97%E9%80%8F%E8%BF%87%E7%A8%8B%E4%B8%AD%E6%90%9C%E5%AF%BB%E6%8C%87%E5%AE%9A%E6%96%87%E4%BB%B6%E5%86%85%E5%AE%B9%EF%BC%8C%E4%BB%8E%E8%80%8C%E6%89%BE%E5%88%B0%E7%AA%81%E7%A0%B4%E5%8F%A3%E7%9A%84%E4%B8%80%E6%AC%BE%E5%B0%8F%E5%B7%A5%E5%85%B7&font=Rokkitt&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F54609266%3Fv%3D4&name=1&owner=1&pattern=Charlie%20Brown&stargazers=1&theme=Dark)

## ✈️ 工具概述

当对内网束手无策的时候，入口机器上面说不定藏着突破口，翻找本地的文件和建立的网络连接就是手法

这里也提供一个文件内容敏感词的字典，需要可以自己去整理，如下:

```
jdbc:
user=
password=
key=
ssh-
ldap:
mysqli_connect
sk-
```

通过快速遍历机器文件，去寻找这些关键词，可以找到突破口，这个代码我之前也分享给好几个朋友，在实战阶段效果不错，具体可以看公众号文章：[内网渗透信息搜集骚姿势](https://mp.weixin.qq.com/s/GkK4AgXsqng6OLAGs45MUg)

## 🐉 工具使用

Python3环境

```
python3 FindEverything.py -n .txt,.ini,.yaml,.php,.jsp,.java,.xml,.sql -c "password=" -d D:/
python3 FindEverything.py -n .txt,.ini,.yaml,.php,.jsp,.java,.xml,.sql -c jdbc:mysql
python3 FindEverything.py -n .txt,.ini,.yaml,.php,.jsp,.java,.xml,.sql -c jdbc:mysql -o output.txt
```

Python2环境

```
python2 FindEverything-py2.py -n .txt,.ini,.yaml,.php,.jsp,.java,.xml,.sql -c "password=" -d D:/
python2 FindEverything-py2.py -n .txt,.ini,.yaml,.php,.jsp,.java,.xml,.sql -c jdbc:mysql
python2 FindEverything-py2.py -n .txt,.ini,.yaml,.php,.jsp,.java,.xml,.sql -c jdbc:mysql -o output.txt
```
