这是2023年写的一个爬虫, 用于爬取ieee上的数据, 主要利用 selenium 来爬取. 目前实现的功能:
- 根据提供的 链接或文献名或关键词 查找相关信息, 如ris引用, 爬取pdf(在scihub上), 查找与它相似的文献(利用文献末尾的关键词进行查找并晒选).
  - 查找给定文献的相似文献时, 利用摘要文本并生成 tfidf 比较来判断相似度
- 将查找的文献的信息汇总到一个Excel表格中, 包含标题名, 期刊名, 摘要和摘要翻译等


最近整理了一下, 可能存在一些问题
- 移动了一些文件, 可能导致找不到依赖. 比如./test文件夹中的文件可能依赖 ./目录下的py文件.
- python版本和库的更新导致有些代码失效. python的很多第三方库一更新, 接口就变了, 这也是很坑的.
  - 并不是说更新不好, 但是更新有点快了, 我做这个东西时间跨度不到3个星期, 就因为两次更新出问题. 所以放弃使用python了


各种库的版本: 待整理
python版本: 待整理
