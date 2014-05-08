vim-PYSearch
============
概述:
vim内置的搜索对中文的搜索不太友好, 根据vim的特点, 对中文搜索最易用的方案应该是使用中文拼音首字母缩写进行搜索, 比如输入搜索"中文", 只需要输入zw即可, 插件的实现参考了同类插件https://github.com/ppwwyyxx/vim-PinyinSearch, vim-PinyinSearch的核心部分使用python实现, 因为每次搜索都需要加载拼音表和编码转换以及vim和python之间的转换, 从效率上来说不如使用vim自身的脚本语言, 所以使用vim脚本语言对这款插件进行了重写. 在它原来的基础上加上了对多音字的支持, 另外扩充了对繁体字和生僻字的支持

缺点: 没有使用中文分词功能,所以无法做到精准搜索, 容易受多音字的不同组合影响. 比如搜索yl,可能会搜索到"音乐"

文件说明:
pinyin.txt  为从网上收集的汉字拼音表(http://bbs.unispim.com/forum.php?mod=viewthread&tid=31644),去掉了部分不支持的字符,并格式化了下文件,以方便转换为脚本需要的首字母拼音表
PYTable.txt 转换后的用于脚本查询的汉字首字母拼音表,多音字的多个不同的拼音首字母以tab进行分割
trans.py    用于将pinyin.txt转为PYTable.txt的转换脚本,以方便遇到不支持或错误的拼音时手工添加到pinyin.txt中,从而手工转换使用

使用说明:
插件导出了三个命令给外部使用,分别为:
PYSearch    搜索并高亮和输入的序列匹配的所有汉字或英文字符,可能会有多个匹配的内容,可以使用PYNext依次切换
PYNext  依次设置当前高亮的内容为和输入的序列匹配的汉字或英文字符
PYTest  用于脚本自身功能的测试
g:PYSearchOnlyChinese变量用于设置是否只搜索中文字符,默认为1,设置为0后,可以同时搜索英文和中文拼音首字母缩写匹配的
