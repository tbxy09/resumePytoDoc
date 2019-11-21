
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
        " 公司主要从事服装产业链的智能化，包含各种模型开发和数据库的建立。\
 负责的项目包换 3D虚拟试衣镜的human body tracking/motion capture 和 \
可穿衣的虚拟模特的 animation模块，基于source seq 是 mobile高清摄像头采集的 monocular video stream \
（不包含任何传感数据），同时还负责公司工业机器人部门的基于图像和强化的机械手开发。 "
 }
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
        "这段时间两个角色，一个是parttime私募交易构架的搭建，和策略模型的开发， \
         还有一个是机器算法的学习比赛,参与开源项目.私募的量化模型开发 \
         1.券商数据和交易接口的封装 2.量化主算法模型的建立和模拟盘的测试 3.自动交易模块的优化. \
         参加的比赛列表 kaggle airport scan,kaggle home credit,kaggle fraud detection,kaggle \
         databowl,天池大赛全球调度算法大赛，金融算法挑战大赛上市公司季度营收预测，ICPR MTWI 2018 \
         挑战赛二，网络文字的检测 飞行器航线规划大赛 最好成绩 （112/2116）（118/2724)", \
 }
)
tr_li_history.append({
'work_time':
        "2012.04.01-2015.04.01",
'work_company':
        "摩托罗拉成都研发中心",
'work_industry':
        "通讯/电信/网络设备",
'work_title':
        "嵌入式软件ARM/DSP 开发工程师",
'work_desp':
        "在 ARM/DSP mutlicore linux platform 上进行数字集群语音通讯系统的full-cycle的开发， \
        从产品原型设计，到产品发布后的维护工作，参与到了10多个不同规模的跨site的合作项目。 \
        7个大项目full project cycle involvement \
        , 6个中小项目的开发和测试。涵盖了4个productline DMR/Astro/Bandit/Tetra, \
        3 years DSP工程师，3 years ARM 工程师.Acoustic Model 部门级别的sharing. \
        Oral Presentation and Publication in 摩托罗拉年度技术论坛（拆分之前）",
 })

tr_li_proj = []
tr_li_proj.append({
'proj_name':
        "2019.4-Now 3D虚拟试衣镜的human body tracking 和 可穿衣的虚拟模特的 animation模块",
'proj_desp':
        " 项目是为了实现一套on-device的算法，部署在一个edge系统上，通过从高清相机中采集的video \
                   stream,来对non-Neural body进行 tracking/animation其中主要的工作scope包含以下几点：build and \
                   training body tracking network;build and training body animation/imitation network;build metrics \
                   to measure the loss of both 2d and 3d features;training dataset preparation;AR Location/Fool \
                   detection 方案研究;movement smooth and jitters remove", \
'proj_per':
        "而遇到的挑战主要包含 在model design 方面； model-free/model-base 方案选择,深度信息的模糊性depth ambiguity \
                   of image，dense rotation supervision data generation，location/rotation jitter problem，chest \
                   turn specific movement accuracy ，在 Inference 方面；less dependency to the network \
                   connection，video tracking/animation/clothing all run together in edge device，Inference \
                   latency/performance tradeoff",
 }
)

tr_li_proj.append({
'proj_name':
        "级联编码的语音增强系统",
'proj_desp':
        "应急通讯网络多网络的共存数字/模拟。\
        PSTN/VOIP,客户端的网络，调度作业的网络，调度中心的网络。 \
        每一种网络带有自己的编解码，在多次的编解码的情况下的语音质量的下降。 \
        实现基于16 channels 2kbps Vocoder的前端语音增强",
'proj_per':
        "基于公司现有语料（超过2.5亿小时的无线电传输，来自数万个记录）。\
        设计算法来提取音频波形中最脆弱的语段（通常是清音）作为feature test验证材料-根据人的声学模型，\
        在dsp上实现语音增强的算法。",
 }
)

tr_li_proj.append({
'proj_name':
        "Motorola 北美集群网络协议的语音/数据传输混合实现",
'proj_desp':
        "集群系统（政府公共部门专属通讯系统，应急通讯）， \
        有它专属的通讯协议，他需求的特殊性要求它具有时效性和极低的容错性。 \
        集群系统的数字化和宽带化。实现整个应急通讯从用户接入，调度网络再到作业网络的宽带数字化。" ,\
'proj_per':
        "快速开发集成架构和工具链条的搭建工作，来应对产品独有的库。\
        第三方库，还有跨产品共享平台的复杂需求。-启用网络协议的voice stack, \
        并基于此stack,开发group call的控制逻辑，实现应急协议的空口到网络段的语音通路  \
        – 运用 off-hardware 的simulation tool 来模拟基站的行为，进行系统级别的验证工作。",\
 }
)

tr_li_proj.append({
'proj_name':
        "DTMF Tone Generation/Encoder",
'proj_desp':
        "DTMF Tone Generation 是 Group call 网络接通 Landline Service 一个 subfeature.\
        DTMF Tone 在 Group call 的调度网络中是没有启用的。\
        而在拨打座机（比如调度中心的办公室电话的时候），为了增加用户的体验，\
        加入 DTMF Tone 的声音。DTMF Encoder需要embeded into the on-call payload 作为一个控制信令，\
        传给远端的Router",
'proj_per':
        "-方案选择。DTMF Tone Encoder 可以通过 DSP Firmware实现，\
        或者通过OEM的on chip circuit 实现。或者通过3rd party Vocoder也可以实现。\
        -DTMF Encoder 的参数Tuning,来获得最佳的DTMF Tone Detection Performance",
 }
)

tr_li_proj.append({
'proj_name':
        "手持对讲设备的低能耗/高兴性能的全频率scan实现",
'proj_desp':
        "嵌入式通讯最重要的优化目标之一：\
        低耗能/高性能的连接方案。Scan 是其中最重要的优化环节。\
        一个具有无线通讯接口的嵌入式设备（包括各种的医疗设备，语音通讯设备，工业控制设备）在开启scan 后，\
        能明显的提高它网络的接入能力，但却同时带来能耗的显著提升，对历史扫描点进行特征提取，\
        从而对未来频率点的预测，最终达到能耗的接近50%的优化", \
'proj_per':
        "原型实现和方案讨论工作，发现dsp的时延导致整个firmware hang,简化option和event 交互机制。\
        满足严格的时间同步。2 Test case design, TEST DRIVEN DEVELOPMENT TDD实践。\
        3. 多个产品线的feature test.performance test, regression test", \
 }
)

tr_li_proj.append({
'proj_name':
        "手持对讲设备的低能耗/高兴性能的全频率scan实现",
'proj_desp':
        "嵌入式通讯最重要的优化目标之一：\
        低耗能/高性能的连接方案。Scan 是其中最重要的优化环节。\
        一个具有无线通讯接口的嵌入式设备（包括各种的医疗设备，语音通讯设备，工业控制设备）在开启scan 后，\
        能明显的提高它网络的接入能力，但却同时带来能耗的显著提升，对历史扫描点进行特征提取，\
        从而对未来频率点的预测，最终达到能耗的接近50%的优化", \
'proj_per':
        "原型实现和方案讨论工作，发现dsp的时延导致整个firmware hang,简化option和event 交互机制。\
        满足严格的时间同步。2 Test case design, TEST DRIVEN DEVELOPMENT TDD实践。\
        3. 多个产品线的feature test.performance test, regression test", \
 }
)

tr_li_proj.append({
'proj_name':
        "bootloader in debug mode 脚本开发",
'proj_desp':
"这是为了解决 early boot hang debug. earlly boot hang 总是很难捕捉。System 总是不能把所有log打印完整。",
'proj_per':
"System Map  analyze tool; auto 提取 tracer log buffer 地址；dump _logbuffer 生成相应的解析文件"
 }
)
tr_li_proj.append({

'proj_name':
        "路由设备中的语音增强",

'proj_desp':
    "把在端到端/网络边缘实现的语音增强模块，移动到中转/路由系统中，\
    由于终端系统的底层硬件和中转路由设备的硬件有很大的区别，\
    主要涉及的工作是 low-level hardware 参数的获取 和 filter tunning",\

'proj_per':
    "滤波器参数重新tuning, 实现real-time on-board filter tuning, \
    省去每次firmware 重新的build和重新的flash, 在 debug mode 中通过脚本注入测试数据，\
    JTAG 连接仿真板后，脚本可以对filter参数做实时的修改和验证" ,\
 }
)
