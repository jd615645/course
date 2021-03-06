# NCHU-python-Parser (中興大學課程爬蟲)[![Build Status](https://travis-ci.org/Stufinite/Crawler-NCHU-course.svg?branch=master)](https://travis-ci.org/NCHUSG/Python-Crawler)

興大的計資中心有按照我的需求產出一份**類似**json的東西  但時常會出現不合法的字元,使得整份json噴掉，且計中提供的格式是format過的，所以這個parser可以將它minify、過濾資料內空白、空行，倘若學校資料來源不幸無法運作，請採用替代方案：
  * 使用自製的[Crawler](fallback)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

```
sudo apt-get update
sudo apt-get install python3 python3-dev
```

### Installing

```
git clone git@github.com:NCHUSG/Python-Crawler.git
pip3 install -r requirements.txt
```

## Deployment

Add additional notes about how to deploy this on a live system

1. Use Crontab to make crawler automatically run in background

  * `crontab -e`

2. Paste the command below into the bottom of the crontab file :

  (1).  Change your directory to this project

    * `cd /path/to/project`

  (2). Use Crontab to make crawler automatically run in background

    * `crontab -e`

  (3). Paste the command below into the bottom of the crontab file :

    *  `* * * * * python3 CoursePickingHelperCrawler.py #獲得全部課程 ( For all Course )`

### Result

預設會將json存在這個路徑底下:

    os.chdir('/var/www/html/Python-Crawler/nchu/json')

若沒有這個資料夾會產生exception 並直接將json儲存在當前目底下
輸出 JSON 格式

    {
      "course": [
        {
          "class": "1",
          "code": "1032",
          "credits": "2",
          "credits_parsed": 2,
          "department": "環境工程學系學士班",
          "discipline": "",
          "enrolled_num": "0",
          "for_dept": "環境工程學系學士班",
          "hours": "2",
          "hours_parsed": "2",
          "intern_location": [
            ""
          ],
          "intern_time": "",
          "language": "中文",
          "location": [
            "C405"
          ],
          "note": "",
          "number": "52",
          "number_parsed": 52,
          "obligatory": "選修",
          "obligatory_tf": false,
          "prerequisite": "",
          "professor": "望熙榮",
          "time": "412",
          "time_parsed": [
            {
              "day": 4,
              "time": [
                1,
                2
              ]
            }
          ],
          "title": "R程式在環工之應用 `Application of R Program on Environmental Engineering",
          "title_parsed": {
            "en_US": "Application of R Program on Environmental Engineering",
            "zh_TW": "R程式在環工之應用"
          },
          "url": "1415",
          "year": "半"
        },
        ...
      ]
    }

## Built With

* python3.4

## Versioning

For the versions available, see the [tags on this repository](https://github.com/NCHUSG/Python-Crawler/tags).

## Contributors

* **邱冠喻** - *Initial work* - [Pastleo](https://github.com/chgu82837)
* **戴均民** - *Initial work* - [taichunmin](https://github.com/taichunmin)
* **黃川哲** - *Initial work* - [CJHwong](https://github.com/CJHwong)
* **張泰瑋** [david](https://github.com/david30907d)

## Acknowledgments

* 感謝中興大學計資中心提供
    * [學士班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=U)
    * [通識加體育課](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=O)
    * [進修部](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=N)
    * [在職專班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=W)
    * [碩班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=G)
    * [博士班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=D)
    
* 感謝[黃川哲](https://github.com/CJHwong)大大開的坑，讓學弟學了不少的Python，學長們的 code 也讓我受益良多~
* 感謝[Pastleo](https://github.com/chgu82837)大大開的坑，讓學弟學了不少的Python，學長們的 code 也讓我受益良多~

## License

This project is licensed under the **GNU 3.0** License - see the [LICENSE.md](LICENSE.md) file for details
