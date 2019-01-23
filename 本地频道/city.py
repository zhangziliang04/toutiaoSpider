# coding=utf-8

city_info = [["安阳","A Y"],["鞍山","A S"],["安庆","A Q"],["安康","A K"],["阿坝","A B"],["阿拉善","A L S"],["阿克苏","A K S"],
    ["阿勒泰","A L T"],["阿里","A L"],["安顺","A S"],["澳门","A M"],["北京","B J"],["蚌埠","B B"],["保定","B D"],["本溪","B X"],
    ["包头","B T"],["亳州","B Z"],["滨州","B Z"],["白城","B C"],["百色","B S"],["白山","B S"],["白银","B Y"],["宝鸡","B J"],
    ["保山","B S"],["巴彦淖尔","B Y N E"],["巴中","B Z"],["北海","B H"],["毕节","B J"],["博尔塔拉","B E T L"],["巴音郭楞","B Y G L"],
    ["成都","C D"],["长春","C C"],["长沙","C S"],["承德","C D"],["常州","C Z"],["滁州","C Z"],["巢湖","C H"],["沧州","C Z"],
    ["常德","C D"],["昌都","C D"],["昌吉","C J"],["长治","C Z"],["朝阳","C Y"],["潮州","C Z"],["郴州","C Z"],["楚雄","C X"],["赤峰","C F"],
    ["池州","C Z"],["崇左","C Z"],["大连","D L"],["东莞","D G"],["德州","D Z"],["丹东","D D"],["大理","D L"],["大庆","D Q"],["大同","D T"],
    ["大兴安岭","D X A L"],["达州","D Z"],["德宏","D H"],["德阳","D Y"],["定西","D X"],["迪庆","D Q"],["东营","D Y"],["鄂州","E Z"],
    ["鄂尔多斯","E E D S"],["恩施","E S"],["福州","F Z"],["阜阳","F Y"],["佛山","F S"],["抚州","F Z"],["防城港","F C G"],["抚顺","F S"],
    ["阜新","F X"],["广州","G Z"],["贵阳","G Y"],["桂林","G L"],["赣州","G Z"],["广元","G Y"],["甘南","G N"],["甘孜","G Z"],["广安","G A"],
    ["贵港","G G"],["果洛","G L"],["固原","G Y"],["杭州","H Z"],["合肥","H F"],["哈尔滨","H E B"],["海口","H K"],["衡阳","H Y"],["邯郸","H D"],
    ["呼和浩特","H H H T"],["黄冈","H G"],["黄石","H S"],["湖州","H Z"],["衡水","H S"],["呼伦贝尔","H L B E"],["黄山","H S"],["海北","H B"],
    ["海东","H D"],["海南","H N"],["海西","H X"],["哈密","H M"],["汉中","H Z"],["鹤壁","H B"],["河池","H C"],["鹤岗","H G"],["黑河","H H"],
    ["和田","H T"],["河源","H Y"],["菏泽","H Z"],["贺州","H Z"],["红河","H H"],["淮安","H A"],["淮北","H B"],["怀化","H H"],["淮南","H N"],
    ["黄南","H N"],["惠州","H Z"],["葫芦岛","H L D"],["吉林","J L"],["济南","J N"],["九江","J J"],["揭阳","J Y"],["酒泉","J Q"],["荆州","J Z"],
    ["锦州","J Z"],["佳木斯","J M S"],["吉安","J A"],["江门","J M"],["焦作","J Z"],["嘉峪关","J Y G"],["金昌","J C"],["晋城","J C"],
    ["景德镇","J D Z"],["荆门","J M"],["金华","J H"],["济宁","J N"],["晋中","J Z"],["鸡西","J X"],["济源","J Y"],["昆明","K M"],["开封","K F"],
    ["喀什","K S"],["克拉玛依","K L M Y"],["克孜勒苏","K Z L S"],["兰州","L Z"],["廊坊","L F"],["六安","L A"],["乐山","L S"],["来宾","L B"],
    ["柳州","L Z"],["聊城","L C"],["莱芜","L W"],["拉萨","L S"],["洛阳","L Y"],["凉山","L S"],["连云港","L Y G"],["辽阳","L Y"],["辽源","L Y"],
    ["丽江","L J"],["临沧","L C"],["临汾","L F"],["临夏","L X"],["临沂","L Y"],["林芝","L Z"],["丽水","L S"],["六盘水","L P S"],["陇南","L N"],
    ["龙岩","L Y"],["娄底","L D"],["漯河","L H"],["泸州","L Z"],["吕梁","L L"],["绵阳","M Y"],["马鞍山","M A S"],["茂名","M M"],["眉山","M S"],
    ["梅州","M Z"],["牡丹江","M D J"],["南京","N J"],["南昌","N C"],["南宁","N N"],["宁波","N B"],["南通","N T"],["南充","N C"],["南平","N P"],
    ["南阳","N Y"],["那曲","N Q"],["内江","N J"],["怒江","N J"],["宁德","N D"],["莆田","P T"],["濮阳","P Y"],["盘锦","P J"],["攀枝花","P Z H"],
    ["平顶山","P D S"],["平凉","P L"],["萍乡","P X"],["普洱","P E"],["青岛","Q D"],["秦皇岛","Q H D"],["泉州","Q Z"],["衢州","Q Z"],["曲靖","Q J"],
    ["黔东南","Q D N"],["黔南","Q N"],["黔西南","Q X N"],["庆阳","Q Y"],["清远","Q Y"],["钦州","Q Z"],["齐齐哈尔","Q Q H E"],["七台河","Q T H"],
    ["日照","R Z"],["曰喀则","Y K Z"],["上海","S H"],["深圳","S Z"],["沈阳","S Y"],["石家庄","S J Z"],["三门峡","S M X"],["商洛","S L"],
    ["商丘","S Q"],["苏州","S Z"],["汕头","S T"],["汕尾","S W"],["十堰","S Y"],["遂宁","S N"],["上饶","S R"],["山南","S N"],["绍兴","S X"],
    ["邵阳","S Y"],["双鸭山","S Y S"],["朔州","S Z"],["四平","S P"],["松原","S Y"],["绥化","S H"],["随州","S Z"],["宿迁","S Q"],["宿州","S Z"],
    ["石嘴山","S Z S"],["韶关","S G"],["天津","T J"],["太原","T Y"],["唐山","T S"],["台州","T Z"],["塔城","T C"],["泰安","T A"],["铁岭","T L"],
    ["台湾","T W"],["泰州","T Z"],["天水","T S"],["铜川","T C"],["通化","T H"],["通辽","T L"],["铜陵","T L"],["铜仁","T R"],["吐鲁番","T L F"],
    ["武汉","W H"],["温州","W Z"],["无锡","W X"],["乌鲁木齐","W L M Q"],["芜湖","W H"],["潍坊","W F"],["威海","W H"],["渭南","W N"],["文山","W S"],
    ["乌海","W H"],["乌兰察布","W L C B"],["武威","W W"],["吴忠","W Z"],["梧州","W Z"],["西安","X A"],["厦门","X M"],["湘潭","X T"],["徐州","X Z"],
    ["许昌","X C"],["信阳","X Y"],["西宁","X N"],["咸阳","X Y"],["宣城","X C"],["新乡","X X"],["湘西","X X"],["襄阳","X Y"],["咸宁","X N"],
    ["孝感","X G"],["锡林郭勒","X L G L"],["兴安","X A"],["邢台","X T"],["新余","X Y"],["忻州","X Z"],["西双版纳","X S B N"],["香港","X G"],
    ["扬州","Y Z"],["银川","Y C"],["宜昌","Y C"],["岳阳","Y Y"],["榆林","Y L"],["烟台","Y T"],["雅安","Y A"],["延安","Y A"],["延边","Y B"],
    ["盐城","Y C"],["阳江","Y J"],["阳泉","Y Q"],["宜宾","Y B"],["伊春","Y C"],["宜春","Y C"],["伊犁","Y L"],["营口","Y K"],["鹰潭","Y T"],
    ["益阳","Y Y"],["永州","Y Z"],["玉林","Y L"],["运城","Y C"],["云浮","Y F"],["玉树","Y S"],["玉溪","Y X"],["珠海","Z H"],["肇庆","Z Q"],
    ["张家口","Z J K"],["中山","Z S"],["淄博","Z B"],["驻马店","Z M D"],["奉庄","F Z"],["张家界","Z J J"],["张掖","Z Y"],["漳州","Z Z"],
    ["湛江","Z J"],["昭通","Z T"],["郑州","Z Z"],["镇江","Z J"],["中卫","Z W"],["周口","Z K"],["舟山","Z S"],["株洲","Z Z"],["自贡","Z G"],
    ["资阳","Z Y"],["遵义","Z Y"]]