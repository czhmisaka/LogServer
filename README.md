# LogServer

1. 本意是做一个日志服务器，为之后的微服务框架提供日志服务
2. 后来发现与其做一个日志服务模块，不如直接做成节点服务，减少对其他项目的侵入
3. 再后来感觉没必要区分主服务器和节点服务，所有节点服务都可以转化为主服务器，互相之间共同保存日志文件。
4. 但是所有数据都要保存的话不可避免的会遇到数据过大的问题，我就在想要不要给节点做等级或群组区分
5. 毕竟区分完群组and等级之后，可以减少带宽资源的使用（虽然像我这种个人开发也没几个服务需要搭上日志）
6. 但是又会遇到新的问题，比如如何完成日志数据的汇总展示，总不能每次需要的时候都批量的从各个节点获取吧？
7. 所以还是需要一个汇总服务器，提供数据的存储，展示，搜索功能。
8. 数据收集上也是，从一开始的主动式数据收集，改为被动监听所有数据。
9. ~~数据的展示还没开始动工~~
10. 如何辅助接入自由度相对较高的爬虫程序，也是一个很大的问题


### 待定完成的目标（希望这次不会鸽）
1. 节点服务器可动态添加功能
   1. 其他节点的日志数据存储功能
   2. 日志数据展示功能
   3. 其他节点的服务状态功能
   4. 权限管理？这个待定
2. 数据展示功能详解
   1. 批量展示err级别数据

### 如何启动？
1. 还没写完就别想着启动了