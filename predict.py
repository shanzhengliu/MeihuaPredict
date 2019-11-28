
# -*- coding: utf-8 -*-
CODES = ['UTF-8', 'UTF-16', 'GB18030', 'BIG5']
UTF_8_BOM = b'\xef\xbb\xbf'


def string_encoding(b):

    for code in CODES:
        try:
            b.decode(encoding=code)
            if 'UTF-8' == code and b.startswith(UTF_8_BOM):
                return 'UTF-8-SIG'
            return code
        except Exception:
            continue
    return '未知的字符编码类型'

def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]

def change_str(str,pos):
    l=list(str);
    if(l[pos]=="0"):
        l[pos]="1";
    else:
        l[pos] = "0";

    newStr ="".join(l);
    return newStr;


def wuhangshengkepanduan(wuhangshuA,wuhangshuB):
    wuhangzifu = wuhangshuA+wuhangshuB;

    shengkejieguo = wuhangshengke[wuhangzifu];

    return shengkejieguo;

def baguaguaci(baguashuA,baguashuB):
    guaxiang = str(baguashuA)+str(baguashuB);
    result = baguaguaxiang[guaxiang];
    return result;



baguashu = {
    "乾":1,
    "兑":2,
    "离":3,
    "震":4,
    "巽":5,
    "坎":6,
    "艮":7,
    "坤":0

}


baguaguaxiang = {
    "11":"乾为天：乾卦：刚健中正",
    "12":"天泽履：履卦：脚踏实地",
    "13":"天火同人：同人卦：上下和同",
    "14":"天雷无妄：无妄卦：无妄而得",
    "15":"天风姤：姤卦：天下有风",
    "16":"天水讼：讼卦：慎争戒讼",
    "17":"天山遁：遁卦：遁世救世",
    "10":"天地否：否卦：不交不通",
    "21":"泽天夬：夬卦：决而能和",
    "22":"兑为泽：兑卦：刚内柔外",
    "23":"泽火革：革卦：顺天应人",
    "24":"泽雷随：随卦：随时变通",
    "25":"泽风大过：大过卦：非常行动",
    "26":"泽水困：困卦：困境求通",
    "27":"泽山咸：咸卦：相互感应",
    "20":"泽地萃：萃卦：荟萃聚集",
    "31":"火天大有：大有卦：顺天依时",
    "32":"火泽睽：睽卦：异中求同",
    "33":"离卦：离为火：附和依托",
    "34":"火雷噬嗑：噬嗑卦：刚柔相济",
    "35":"火风鼎：鼎卦：稳重图变",
    "36":"火水未济:未济卦：事业未竟",
    "37":"火山旅：旅卦：依义顺时",
    "30":"地火晋：晋卦：求进发展",
    "41":"雷天大壮：大壮卦：状勿妄动",
    "42":"雷泽归妹：归妹卦：立家兴业",
    "43":"雷火丰：丰卦：日中则斜",
    "44":"震为雷：震卦：临危不乱",
    "45":"雷风恒：恒卦：恒心有成",
    "46":"雷水解：解卦：柔道致治",
    "47":"雷山小过：小过卦：行动有度",
    "40":"雷地豫：豫卦：顺时依势",
    "51":"风天小畜：小畜卦：蓄养待进",
    "52":"风泽中孚：中孚卦：诚信立身",
    "53":"风火家人：家人卦：诚威治业",
    "54":"风雷益：益卦：损上益下",
    "55":"巽为风：巽卦：谦逊受益",
    "56":"风水涣：涣卦：拯救涣散",
    "57":"风山渐：渐卦：渐进蓄德",
    "50":"风地观：观卦：观下瞻上",
    "61":"水天需：需卦：守正待机",
    "62":"水泽节：节卦：万物有节",
    "63":"水火既济：既济卦：盛极将衰",
    "64":"水雷屯：屯卦：起始维艰",
    "65":"水风井：井卦：求贤若渴",
    "66":"坎为水：坎卦：行险用险",
    "67":"水山蹇: 蹇卦：险阻在前",
    "60":"水地比：比卦：诚信团结",
    "71":"山天大畜：大畜卦：止而不止",
    "72":"山泽损：损卦：损益制衡",
    "73":"山火贲: 贲卦：饰外扬质",
    "74":"山雷颐: 颐卦：纯正以养",
    "75":"山风蛊：蛊卦：振疲起衰",
    "76":"山水蒙：蒙卦：启蒙奋发",
    "77":"艮为山：艮卦：动静适时",
    "70":"山地剥：剥卦：顺势而止",
    "01":"地天泰：泰卦：应时而变",
    "02":"地泽临：临卦：教民保民",
    "03":"地火明夷：明夷卦：晦而转明",
    "04":"地雷复：复卦：寓动于顺",
    "05":"地风升：升卦：柔顺谦虚",
    "06":"地水师：师卦：行险而顺",
    "07":"地山谦：谦卦：内高外低",
    "00":"坤为地：坤卦：柔顺伸展",

}

bagua = {
    "乾": "111",
    "兑": "011",
    "离": "101",
    "震": "001",
    "巽": "110",
    "坎": "010",
    "艮": "100",
    "坤": "000"

}

wuhangbagua = {
    "乾": "金",
    "兑": "金",
    "离": "火",
    "震": "木",
    "巽": "木",
    "坎": "水",
    "艮": "土",
    "坤": "土"
}

wuhangshu = {
    "金":"1",
    "木":"2",
    "水":"3",
    "土":"4",
    "火":"5"
}
wuhangshengke = {
    "11":"比和",
    "12":"克",
    "13":"生",
    "14":"被生",
    "15":"被克",
    "21":"被克",
    "22":"比和",
    "23":"被生",
    "24":"克",
    "25":"生",
    "31":"被生",
    "32":"生",
    "33":"比和",
    "34":"被克",
    "35":"克",
    "41":"生",
    "42":"被克",
    "43":"克",
    "44":"比和",
    "45":"被生",
    "51":"克",
    "52":"被生",
    "53":"被克",
    "54":"生",
    "55":"比和"
}

yuanshubagua = {
    "乾": "天",
    "兑": "泽",
    "离": "火",
    "震": "雷",
    "巽": "风",
    "坎": "水",
    "艮": "山",
    "坤": "地"
}


shanggua = input("输入上卦数:")
xiagua    =input("输入下卦数:")
dongyao  = input("请输入动爻数:")

shanggua = shanggua%8;
xiagua = xiagua%8;
dongyao = dongyao%6;
shangbenguawuhang = wuhangbagua[get_key(baguashu,shanggua)[0]];
xiabenguawuhang = wuhangbagua[get_key(baguashu,xiagua)[0]];

shangbengua = get_key(baguashu,shanggua)[0]+" 五行为:" +shangbenguawuhang;
xiabengua = get_key(baguashu,xiagua)[0]+" 五行为:" +xiabenguawuhang;


bengua = bagua[get_key(baguashu, shanggua)[0]] + bagua[get_key(baguashu, xiagua)[0]];
# bagua[get_key(bagua,get_key(baguashu,xiagua)[0])[0]];

shanghuguawuhang = wuhangbagua[get_key(bagua, bengua[1:4])[0]];
xiahuguawuhang = wuhangbagua[get_key(bagua, bengua[2:5])[0]];
shanghuguaguaming = get_key(bagua, bengua[1:4])[0];
xiahuguaguaming = get_key(bagua, bengua[2:5])[0]
shanghugua = get_key(bagua, bengua[1:4])[0]+" 五行为:"+shanghuguawuhang;
xiahugua = get_key(bagua, bengua[2:5])[0]+" 五行为:"+xiahuguawuhang;


changpos = 6-dongyao;
if(changpos==6):
    changpos=0;



biangua = change_str(bengua, changpos);
shangbianguawuhang = wuhangbagua[get_key(bagua, biangua[0:3])[0]];
xiabianguawuhang = wuhangbagua[get_key(bagua, biangua[3:6])[0]];
shangbianguaguaming = get_key(bagua, biangua[0:3])[0];
xiabianguaguaming =get_key(bagua, biangua[3:6])[0];
shangbiangua = get_key(bagua, biangua[0:3])[0]+" 五行为:"+shangbianguawuhang;
xiabiangua = get_key(bagua, biangua[3:6])[0]+" 五行为:"+xiabianguawuhang;



shangtiyong = "";
if(shangbengua == shangbiangua):
    shangtiyong = "体";
    xiatiyong = "用";
    print "上体下用"
else:
    shangtiyong = "用";
    xiatiyong = "体";
    print "下体上用"


dingbenguawuhang = "";
dingbengua = "";
Yongbengua = "";
Yongbenguawuhang = "";

if (shangtiyong == "体"):
    dingbenguawuhang = shangbenguawuhang;
    dingbengua = shangbengua;
    Yongbengua = xiabengua;
    Yongbenguawuhang = xiabenguawuhang;
else:
    dingbenguawuhang = xiabenguawuhang;
    dingbengua = xiabengua;
    Yongbengua = shangbengua;
    Yongbenguawuhang = shangbenguawuhang;

print "本卦如下：";
print "上卦为："+shangbengua+"  "+shangtiyong;

print "下卦为："+xiabengua+"  "+xiatiyong;

print  "体用关系："+wuhangshengkepanduan(wuhangshu[dingbenguawuhang],wuhangshu[Yongbenguawuhang])
print  "六十四卦卦辞："+baguaguaci(shanggua,xiagua)+"\n"

print "互卦如下：";

print "上互卦为："+shanghugua+"  "+"用";

print "体用关系: "+wuhangshengkepanduan(wuhangshu[dingbenguawuhang],wuhangshu[shanghuguawuhang]);


print "下互卦为："+xiahugua+"  "+"用";

print "体用关系: "+wuhangshengkepanduan(wuhangshu[dingbenguawuhang],wuhangshu[xiahuguawuhang]);




print  "六十四卦卦辞："+baguaguaci(baguashu[shanghuguaguaming],baguashu[xiahuguaguaming])+"\n"

print "变卦如下: ";

print  "上变卦为："+shangbiangua+"  "+shangtiyong;
if(shangtiyong == "用"):
    print "体用关系: "+wuhangshengkepanduan(wuhangshu[dingbenguawuhang],wuhangshu[shangbianguawuhang]);

print  "下变卦为："+xiabiangua+"  "+xiatiyong;
if(xiatiyong == "用"):
    print "体用关系: "+wuhangshengkepanduan(wuhangshu[dingbenguawuhang],wuhangshu[xiabianguawuhang]);

print  "六十四卦卦辞："+baguaguaci(baguashu[shangbianguaguaming],baguashu[xiabianguaguaming])+"\n"


