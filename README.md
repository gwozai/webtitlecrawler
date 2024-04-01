# webtitlecrawler
DeepCrawler是一个以Python编写的强大的网络爬虫工具，不仅可以爬取指定网站的所有链接，还可以进行深度爬取，进一步获取链接的链接。

## 主要功能：

1. **网站链接爬取**：输入网站URL，DeepCrawler将会爬取该网站的所有链接。
2. **深度爬取**：继续对获取的链接进行爬取，获取更多级别的链接，以便进行更深层次的数据抓取。
3. **数据导出**：DeepCrawler支持将爬取的链接导出为CSV或JSON格式，方便后续的数据分析和处理。

## 安装方式：

1. 克隆此仓库到本地。
2. 进入项目文件夹，运行`pip install -r requirements.txt`安装所需依赖。
3. 运行`python deepcrawler.py`启动DeepCrawler。

## 使用示例：

在命令行中键入以下指令，将对目标网站进行爬取：

```
python deepcrawler.py --url "https://www.targetsite.com"
```

DeepCrawler将爬取该网站的所有链接，还会进行深度爬取。

以上信息仅为DeepCrawler的基本概述，详细的使用方法请参阅我们的用户手册。

## 维护者:

DeepCrawler维护团队: [联系我们](mailto:sun584257191@gmail.com)

## 反馈：

对于任何问题或疑问，欢迎向我们发送邮件，我们将尽快回复。同时，也欢迎在GitHub上提交issue。

## 许可证

本项目在MIT许可下发布。详情请参阅[LICENSE](LICENSE)文件。



实用flask做服务器，vue做前端
vue 打包可以在flask中运行


flask 调用抓取，因为接口时间太长，是否有其他方法持续传入数据，会给前端传入数据  后端提交完成返回任务id，通过任务id可以停止或进行，
       /status 判断id状态
flask 调用数据库获取信息的数据，
      检测数据库是否有表信息，没有的话从sqlit导入
      对sql进行增删改查的操做
- 把表封装为sql文件
- 判断是否有表，没有的话用sql创建
- 增删改查代码



controller层 接口
service 层 redis minio mysql  业务，实现类
mapper 层 redis minio mysql


替换为数据库操作

把深度可控制，抓够了就返回。 默认为3层， 继续抓取  填入任务id, websit,抓取深度
website 1
website 2
website 3
输入 网址，或网址页，然后加队列进行抓取。

可以有rabbitmq的集成

登录操作

- [ ] 数据库查询操作 使用sql 
- [ ] 前端展示
- [ ] rabbitmq集成flask


输入输出： 从接口输入，从接口输出，然后加权限


pip install Flask
pip install flask_sqlalchemy
pip install flask_migrate

flask db init
flask db migrate -m "Initial migration."
flask db upgrade

python run.py