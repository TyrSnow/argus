# Argus
Argus项目是一个股票行情分析网站，我们试图使用更简洁的交互设计，让用户可以更快的对股票行情的走势进行分析。
# 项目构成
项目使用tushare作为行情数据源，为了能够更便捷的进行开发，我们使用nodejs实现业务层服务。
在初期，主要接入talib来完成计算工作。
## 功能点
### 股票池
1. 维护股票池数据。从远端更新股票池数据，配置参与计算的股票。
1. 更新各个计算节点的权重。根据各个计算节点的历史正确率，对他们的权重进行重新分配
### 计算公式
管理员可以按照下面的规则创建额外的计算公式：
1. 计算公式需要指定计算公式的数据周期（5分钟|10分钟|日线等）和计算周期（一个月|3个月|6个月等）
1. 当返回多个结果的时候，计算公式需要指定返回结果的含义
1. 计算公式提供一个唯一的main函数作为入口
1. main函数接收一个包含历史行情数据的DataFrame，并支持返回多种值类型（数组|对象|数字）
1. 请注意，main函数返回的是当前时间节点上的结果，而不是一个时间序列，系统调用时会通过滑动时间窗口的方式，获得最终的时间序列结果
