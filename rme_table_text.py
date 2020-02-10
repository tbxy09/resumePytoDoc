tr_li_history=[]
tr_li_history.append({
'work_time':
        "2019.1-Now",
'work_company':
        " 真玫智能 ",
'work_industry':
        "边缘计算/VR/AR/机器人",
'work_title':
        " 机器学习算法工程师",
'work_desp':
        "
公司主要从事服装产业链的智能化，包含各种模型开发和数据库的建立。负责的项目包换 3D虚拟试衣镜的human body tracking/motion capture 和 可穿衣的虚拟模特的 animation模块，基于source seq 是 mobile高清摄像头采集的 monocular video stream （不包含任何传感数据），同时还负责公司工业机器人部门的基于图像和强化的机械手开发。 "  }
)

tr_li_history.append({
'work_time':
        "2015.04-2018.12",
'work_company':
        " 私募量化基金 ",
'work_industry':
        "基金/证券/期货/投资",
'work_title':
        " 量化工程师",
'work_desp':
"这段时间两个角色，一个是parttime私募交易构架的搭建，和策略模型的开发，  还有一个是机器算法的学习比赛,参与开源项目.私募的量化模型开发  1.券商数据和交易接口的封装 2.量化主算法模型的建立和模拟盘的测试 3.自动交易模块的优化.  参加的比赛列表 kaggle airport scan,kaggle home credit,kaggle fraud detection,kaggle  databowl,天池大赛全球调度算法大赛，金融算法挑战大赛上市公司季度营收预测，ICPR MTWI 2018  挑战赛二，网络文字的检测 飞行器航线规划大赛 最好成绩 （112/2116）（118/2724)",  }
)
tr_li_history.append({
'work_time':
        "2009.04.01-2015.04.01",
'work_company':
        "摩托罗拉成都研发中心",
'work_industry':
        "通讯/电信/网络设备",
'work_title':
        "嵌入式软件ARM/DSP 开发工程师",
'work_desp':
"在 ARM/DSP mutlicore linux platform 上进行数字集群语音通讯系统的full-cycle的开发， 从产品原型设计，到产品发布后的维护工作，参与到了10多个不同规模的跨site的合作项目。 7个大项目full project cycle involvement , 6个中小项目的开发和测试。涵盖了4个productline DMR/Astro/Bandit/Tetra, 3 years DSP工程师，3 years ARM 工程师.Acoustic Model 部门级别的sharing. Oral Presentation and Publication in 摩托罗拉年度技术论坛（拆分之前）",  })

tr_li_proj = []
tr_li_proj.append({
'proj_name':
        "2019.4-Now 3D虚拟试衣镜的human body tracking 和 可穿衣的虚拟模特的 animation模块",
'proj_desp':
" 项目是为了实现一套on-device的算法，部署在一个edge系统上，通过从高清相机中采集的video stream,来对non-Neural body进行 tracking/animation其中主要的工作scope包含以下几点：build and training body tracking network;build and training body animation/imitation network;build metrics to measure the loss of both 2d and 3d features;training dataset preparation;AR Location/Fool detection 方案研究;movement smooth and jitters remove",
'proj_per':
"而遇到的挑战主要包含 在model design 方面； model-free/model-base 方案选择,深度信息的模糊性depth ambiguity of image，camera 外参estimation(纠正camera俯视角度造成的3D节点估计的腿部弯曲), dense rotation supervision data generation，location/rotation 防抖算法(jitter problem)，chest turn specific movement accuracy ， 在 Inference 方面；less dependency to the network connection，video tracking/animation/clothing all run together in edge device，Inference latency/performance tradeoff",
})

tr_li_proj.append({
'proj_name':
        "级联编码的语音增强系统",
'proj_desp':
"应急通讯网络多网络的共存数字/模拟。 PSTN/VOIP,客户端的网络，调度作业的网络，调度中心的网络。 每一种网络带有自己的编解码，在多次的编解码的情况下的语音质量的下降。 实现基于16 channels 2kbps Vocoder的前端语音增强",
'proj_per':
"基于公司现有语料（超过2.5亿小时的无线电传输，来自数万个记录）。 设计算法来提取音频波形中最脆弱的语段（通常是清音）作为feature test验证材料-根据人的声学模型， 在dsp上实现语音增强的算法。",
})

tr_li_proj.append({
'proj_name':
        "Motorola 北美集群网络协议的语音/数据传输混合实现",
'proj_desp':
"集群系统（政府公共部门专属通讯系统，应急通讯）， 有它专属的通讯协议，他需求的特殊性要求它具有时效性和极低的容错性。 集群系统的数字化和宽带化。实现整个应急通讯从用户接入，调度网络再到作业网络的宽带数字化。" ,
'proj_per':
"快速开发集成架构和工具链条的搭建工作，来应对产品独有的库。 第三方库，还有跨产品共享平台的复杂需求。-启用网络协议的voice stack, 并基于此stack,开发group call的控制逻辑，实现应急协议的空口到网络段的语音通路  – 运用 off-hardware 的simulation tool 来模拟基站的行为，进行系统级别的验证工作。",  }
)

tr_li_proj.append({
'proj_name':
        "DTMF Tone Generation/Encoder",
'proj_desp':
"DTMF Tone Generation 是 Group call 网络接通 Landline Service 一个 subfeature. DTMF Tone 在 Group call 的调度网络中是没有启用的。 而在拨打座机（比如调度中心的办公室电话的时候），为了增加用户的体验， 加入 DTMF Tone 的声音。DTMF Encoder需要embeded into the on-call payload 作为一个控制信令， 传给远端的Router",
'proj_per':
"-方案选择。DTMF Tone Encoder 可以通过 DSP Firmware实现， 或者通过OEM的on chip circuit 实现。或者通过3rd party Vocoder也可以实现。 -DTMF Encoder 的参数Tuning,来获得最佳的DTMF Tone Detection Performance",  }
)

# tr_li_proj.append({
# 'proj_name':
#         "手持对讲设备的低能耗/高兴性能的全频率scan实现",
# 'proj_desp':
#         "嵌入式通讯最重要的优化目标之一：
#         低耗能/高性能的连接方案。Scan 是其中最重要的优化环节。
#         一个具有无线通讯接口的嵌入式设备（包括各种的医疗设备，语音通讯设备，工业控制设备）在开启scan 后，
#         能明显的提高它网络的接入能力，但却同时带来能耗的显著提升，对历史扫描点进行特征提取，
#         从而对未来频率点的预测，最终达到能耗的接近50%的优化",
# 'proj_per':
#         "原型实现和方案讨论工作，发现dsp的时延导致整个firmware hang,简化option和event 交互机制。
#         满足严格的时间同步。2 Test case design, TEST DRIVEN DEVELOPMENT TDD实践。
#         3. 多个产品线的feature test.performance test, regression test",
#  }
# )

tr_li_proj.append({
'proj_name':
        "手持对讲设备的低能耗/高兴性能的全频率scan实现",
'proj_desp':
"嵌入式通讯最重要的优化目标之一： 低耗能/高性能的连接方案。Scan 是其中最重要的优化环节。 一个具有无线通讯接口的嵌入式设备（包括各种的医疗设备，语音通讯设备，工业控制设备）在开启scan 后， 能明显的提高它网络的接入能力，但却同时带来能耗的显著提升，对历史扫描点进行特征提取， 从而对未来频率点的预测，最终达到能耗的接近50%的优化",
'proj_per':
"原型实现和方案讨论工作，发现dsp的时延导致整个firmware hang,简化option和event 交互机制。 满足严格的时间同步。2 Test case design, TEST DRIVEN DEVELOPMENT TDD实践。 3. 多个产品线的feature test.performance test, regression test",  }
)

tr_li_proj.append({
'proj_name':
        "bootloader in debug mode 脚本开发",
'proj_desp':
"这是为了解决 early boot hang debug. earlly boot hang 总是很难捕捉。System 总是不能把所有log打印完整。",
'proj_per':
"System Map  analyze tool; auto 提取 tracer log buffer 地址；dump _logbuffer 生成相应的解析文件"}
)
tr_li_proj.append({
'proj_name':
        "路由设备中的语音增强",

'proj_desp':
"把在端到端/网络边缘实现的语音增强模块，移动到中转/路由系统中， 由于终端系统的底层硬件和中转路由设备的硬件有很大的区别， 主要涉及的工作是 low-level hardware 参数的获取 和 filter tunning",
'proj_per':
"滤波器参数重新tuning, 实现real-time on-board filter tuning, 省去每次firmware 重新的build和重新的flash, 在 debug mode 中通过脚本注入测试数据， JTAG 连接仿真板后，脚本可以对filter参数做实时的修改和验证" ,  }
)
tr_li_intro= []
tr_li_intro.append(
"10 年的软件开发经验，拥有多个领域产品的开发项目经验， 包括human body detection and tracking,motion capture/pose estimation and 3D virtual character animation， 服装工业机器人的前沿领域研究，基于动作视频学习的强化模型开发， 排料系统的智能化模型开发（强化方向），语音编解码/增强,语音通讯协议层开发， low-latence vocoder ，ARM/DSP/SoC,real-time on-device software development 。 一直在信号处理领域进行探索和学习。在团队中扮演多个角色，可以是植根于代码， 也可以lead team to achieve high standard goal of production, 帮助business leader更好的理解机器学习开发落地的难点和痛点。")

tr_li_intro=tr_li_intro + ['']*10
tr_li_skill=[]

tr_li_skill.append({
'proj_name':
        "天池大赛全球调度算法大赛-solo参赛（112/2116）",

'proj_desp':
'这个调度问题是一个 bin-packing 问题，我的方案是强化学习，因为它具备的以下三个条件：1. Input where Policy network can build on 2. Action 3. Rewards ,seqtoseq combination optimization的问题， 也属于动态规划问题的范畴,对于seq里面每一步来说, 是对每一幅图像进行 map 到 Action 的分类， 而依据 machine id 的数量，这是个 high dimension {state,action}问题 （action数目达到了 6000）有 15000 台的 app 应用需要部署， 有 4 个类别的约束条件需要满足。Platform 选取: Pytorch， Pytorch 具有 dynamic graph 的 feature, 对于模型建立中数据分析很方便 通过阿里云的 12 核 CPU 服务器实现',
'proj_per':
' gradient explode, 通过在每一层的 conv layer 后面增加 ReLu 解决 - gradient vanish 的问题（是因为过大的 weight 的初始化让其中一个非线性的部件（Relu)得 backward 通路断了），即使我不断调小 weight 的 initialization, 对输入进行 BatchNormalization 操作，仍然最终还是 gradient vanish, - 解决方案 将 action 对应成 step(这相当与对action space 进行了降维处理,因为转化成step之后,会更倾向于临近的machine,对state space的explore并没有太大影响),machine id 进行排序之后，step= the next choose id- right now id, 梯度消失的问题得到了解决。 - 解决 bug，Empty Array Constructor 的操作，导致 internal memory leak,使得整个程序异常缓慢。 - 基于多 cpu 并行 search,async search ,我选用的是多核 cpu 的硬件方案（基 于经济的考虑角度） code 地址：https://github.com/tbxy09/tianchi_text_detection_dev_log' }
)

tr_li_comp=[]

tr_li_comp.append({

'proj_name':
        "天池大赛全球调度算法大赛-solo参赛（112/2116）",

'proj_desp':
'这个调度问题是一个 bin-packing 问题，我的方案是强化学习，因为它具备的以下三个条 件。 1. Input where Policy network can build on 2. Action 3. Rewards ,seqtoseq combination optimization的问题， 也属于动态规划问题的范畴,对于seq里面每一步来说, 是对每一�图像进行 map 到 Action 的分类， 而依据 machine id 的数量，这是个 high dimension {state,action}问题 （action数目达到了 6000）有 15000 台的 app 应用需要部署， 有 4 个类别的约束条件需要满足。Platform 选取: Pytorch， Pytorch 具有 dynamic graph 的 feature, 对于模型建立中数据分析很方便 通过阿里云的 12 核 CPU 服务器实现',
'proj_per':
' gradient explode, 通过在每一层的 conv layer 后面增加 ReLu 解决 - gradient vanish 的问题（是因为过大的 weight 的初始化让其中一个非线性的部件（Relu)得 backward 通路断了），即使我不断调小 weight 的 initialization, 对输入进行 BatchNormalization 操作，仍然最终还是 gradient vanish, - 解决方案 将 action 对应成 step(这相当与对action space 进行了降维处理,因为转化成step之后,会更倾向于临近的machine,对state space的explore并没有太大影响),machine id 进行排序之后，step= the next choose id- right now id, 梯度消失的问题得到了解决。 - 解决 bug，Empty Array Constructor 的操作，导致 internal memory leak,使得整个程序异常缓慢。 - 基于多 cpu 并行 search,async search ,我选用的是多核 cpu 的硬件方案（基 于经济的考虑角度） code 地址：https://github.com/tbxy09/tianchi_text_detection_dev_log' } )

tr_li_comp.append({
'proj_name':
        "2018/07-2018/07 比赛项目的总结-金融算法挑战大赛上市公司季度营收预测-Solo 参赛(118/2724)",

'proj_desp':
"这场比赛我用了外部的数据和自己的 domain knowledge，而且当时和调度的比赛有点冲突，只用了三天，最 主要的外部数据的使用是上市公司有没有进行收购和合并 ",
'proj_per':
"Feature engineering,特征工程 Feature preprocessing 特征的预处理， Hyper Parameter Tuning 超参数的调整 Ensemble 了两套模型",  }
)

tr_li_comp.append({
'proj_name':
        "2018/06-2018/06 比赛项目的总结-ICPR MTWI 2018 挑战赛二,网络图像文本检测",
'proj_desp':
"图像文本检测，总共 20000 张，来自淘宝商家的图片数据 目标数据：是一个 box 框形的二维坐标，box 不一 定是水平，是可以根据文本方向倾斜 实现平台：Pytorch",
'proj_per':
" 1. 图像的预处理, 一开始加入了 Gray 的处理，但 Gray 处理后，Unet 的训练效果并不理想 2. Box Regression 算法的实现，由于 box 方向是倾斜的,需要基于state-of-the-art 算法作相应的改进 code 地址 https://github.com/tbxy09/tianchi_text_detection_dev_log"  }
)

tr_li_hub = []
tr_li_hub.append({
'proj_name':
        "2015/06-now Github 总结",
'proj_desp':
"https://github.com/tbxy09/mindmap2 javascript 实现的单向的知识图谱，通过 markup   的脚本语言绘制,后端是   mongodb 是实现 - Copyme and Jump   https://github.com/tbxy09/moreIPython ipynb 的   nbextension,它解决的   问题主要是,在 notebook 的运行环境下以 pipeline 的方式写出来了很多 code   的基本单元，希望写进具体的代码文件中，作为以后能使用的基本模块，于是我利用一个文件作为 ipython   与 IDE 之间的 clipboard,通过   ipython magic command CLI 方式，和 IDE 共享。而我们在 IDE 里头浏览和查找定位到的 code   line,也和可以通过'copyme from',从 IDE 中获得   https://github.com/tbxy09/pcloud   是一个集中管理阿里云和腾讯云（稍后加入华为云的）综合管理平台,包括调试各种平台的API   Request,React+Flask的框架做数据的可视化   ",
'proj_per':"na"}
)

