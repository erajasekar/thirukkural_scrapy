# -*- coding: utf-8 -*-
import scrapy


class KuralproSpider(scrapy.Spider):
    name = 'kuralpro-kural'

    def start_requests(self):
        urls = self.getUrls();
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def getUrls(self):
        adhigarams = [
            'kadavul-vaazhththu',
            'vaansirappu',
            'neeththaar-perumai',
            'aran-valiyuruththal',
            'ilvaazhkkai',
            'vaazhkkaith-thunainalam',
            'pudhalvaraip-perudhal',
            'anputaimai',
            'virundhompal',
            'iniyavaikooral',
            'seynnandri-aridhal',
            'natuvu-nilaimai',
            'atakkamutaimai',
            'ozhukkamutaimai',
            'piranil-vizhaiyaamai',
            'poraiyutaimai',
            'azhukkaaraamai',
            'veqkaamai',
            'purangooraamai',
            'payanila-sollaamai',
            'theevinaiyachcham',
            'oppuravaridhal',
            'eekai',
            'pukazh',
            'arulutaimai',
            'pulaanmaruththal',
            'thavam',
            'kootaavozhukkam',
            'kallaamai_1',
            'vaaimai',
            'vekulaamai',
            'innaaseyyaamai',
            'kollaamai',
            'nilaiyaamai',
            'thuravu',
            'meyyunardhal',
            'avaavaruththal',
            'oozh',
            'iraimaatchi',
            'kalvi',
            'kallaamai',
            'kelvi',
            'arivutaimai',
            'kutrangatidhal',
            'periyaaraith-thunaikkotal',
            'sitrinanjeraamai',
            'therindhuseyalvakai',
            'valiyaridhal',
            'kaalamaridhal',
            'itanaridhal',
            'therindhudhelidhal',
            'therindhuvinaiyaatal',
            'sutrandhazhaal',
            'pochchaavaamai',
            'sengonmai',
            'kotungonmai',
            'veruvandhaseyyaamai',
            'kannottam',
            'otraatal',
            'ookkamutaimai',
            'matiyinmai',
            'aalvinaiyutaimai',
            'itukkan-azhiyaamai',
            'amaichchu',
            'solvanmai',
            'vinaiththooimai',
            'vinaiththitpam',
            'vinaiseyalvakai',
            'thoodhu',
            'mannaraich-cherndhozhudhal',
            'kuripparidhal_1',
            'avaiyaridhal',
            'avaiyanjaamai',
            'naatu',
            'aran',
            'porulseyalvakai',
            'pataimaatchi',
            'pataichcherukku',
            'natpu',
            'natpaaraaidhal',
            'pazhaimai',
            'thee-natpu',
            'kootaanatpu',
            'pedhaimai',
            'pullarivaanmai',
            'ikal',
            'pakaimaatchi',
            'pakaiththirandheridhal',
            'utpakai',
            'periyaaraip-pizhaiyaamai',
            'penvazhichcheral',
            'varaivinmakalir',
            'kallunnaamai',
            'soodhu',
            'marundhu',
            'kutimai',
            'maanam',
            'perumai',
            'saandraanmai',
            'panputaimai',
            'nandriyilselvam',
            'naanutaimai',
            'kutiseyalvakai',
            'uzhavu',
            'nalkuravu',
            'iravu',
            'iravachcham',
            'kayamai',
            'thakaiyananguruththal',
            'kuripparidhal',
            'punarchchimakizhdhal',
            'nalampunaindhuraiththal',
            'kaadharsirappuraiththal',
            'naanuththuravuraiththal',
            'alararivuruththal',
            'pirivaatraamai',
            'patarmelindhirangal',
            'kanvidhuppazhidhal',
            'pasapparuparuvaral',
            'thanippatarmikudhi',
            'ninaindhavarpulampal',
            'kanavunilaiyuraiththal',
            'pozhudhukantirangal',
            'uruppunalanazhidhal',
            'nenjotukilaththal',
            'niraiyazhidhal',
            'avarvayinvidhumpal',
            'kuripparivuruththal',
            'punarchchividhumpal',
            'nenjotupulaththal',
            'pulavi',
            'pulavi-nunukkam',
            'ootaluvakai'
        ];

        favKurals = [35,36,43,45,50,53,55,56,64,67,69,70,72,79,84,102,103,108,111,114,115,118,120,126,127,128,129,130,138,140,151,156,157,159,160,163,165,167,174,177,178,180,182,184,187,190,195,196,200,203,205,207,208,212,215,216,218,223,225,233,236,237,239,240,241,244,247,248,261,266,267,273,279,280,283,286,291,292,298,305,307,311,312,314,319,321,327,333,335,341,346,355,366,373,376,379,382,385,388,391,396,397,399,406,407,408,409,412,416,420,422,423,424,426,427,429,430,433,437,439,441,442,447,448,449,452,460,461,463,464,466,467,468,469,470,471,472,473,474,475,476,477,478,479,481,482,483,484,485,486,487,489,490,495,496,498,501,502,503,504,505,506,507,510,512,513,514,516,517,520,521,523,524,525,527,528,530,534,537,539,540,541,542,555,569,573,578,580,585,587,589,590,595,597,601,605,610,612,616,618,620,621,627,629,637,640,642,645,646,650,654,655,656,657,659,660,661,662,663,664,666,667,668,669,671,672,673,674,675,676,677,678,679,680,682,691,693,694,695,696,699,700,706,715,718,722,724,725,726,740,754,755,756,773,783,784,791,796,804,812,813,819,820,830,832,833,834,844,852,854,864,866,875,877,879,881,887,890,896,901,906,913,923,925,929,931,938,940,942,944,947,948,949,959,961,962,963,968,969,964,972,974,980,982,983,991,995,998,999,1000,1001,1005,1007,1009,1017,1021,1022,1023,1026,1028,1033,1036,1039,1046,1049,1058,1063,1064,1065,1068,1078,1082,1084,1090,1091,1092,1094,1100,1102,1103,1104,1106,1110,1114,1119,1121,1123,1124,1025,1026,1027,1028,1141,1144,1148,1152,1155,1159,1161,1166,1167,1169,1170,1179,1191,1192,1196,1201,1202,1206,1213,1216,1224,1227,1238,1241,1242,1243,1244,1245,1247,1248,1250,1253,1255,1258,1259,1260,1261,1263,1267,1269,1281,1284,1285,1286,1287,1288,1290,1296,1302,1303,1306,1309,1314,1315,1316,1318,1319,1320,1321,1322,1326,1327,1328,1330];
        urls = [];
        for favKural in favKurals:
            adhigaramIndex = (favKural - 1) / 10;
         #   print (adhigaramIndex)
            adhigaram = adhigarams[adhigaramIndex];
            url = "https://kural.pro/tamil/thirukkural-" + str(favKural) + "-" + adhigaram;
            urls.append(url);
          #  print url;
        return urls[0:1];


    def parse(self, response):
        filename = 'fav-kurals.txt';
        adhigaramName = response.xpath('//meta[@property="position" and @content="5"]/../a/span/text()').get()
        kuralNo = response.xpath('//meta[@property="position" and @content="6"]/../a/span/text()').get()


        with open(filename, 'ab') as f:
            print (adhigaramName);
            print ("\n")
            print (kuralNo);
            print ("\n")
            f.write(adhigaramName.encode("utf-8"))
            f.write("\n");
            f.write(kuralNo.encode("utf-8"))
            f.write("\n");
            for section in (response.xpath('//section[@class="kural"]')):
                for kural in section.xpath('./blockquote/text()').getall():
                    print (kural);
                    print ("\n")
                    f.write(kural.encode("utf-8"))
                print ("----------")
                f.write("\n");
                for meaning in section.xpath('./p[1]/text()').getall():
                    print (meaning);
                    print ("\n")
                    f.write(meaning.encode("utf-8"))

                f.write("\n");