try:
    from time import sleep
    from threading import Thread
    from selenium.webdriver import Chrome, ChromeOptions
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    # from seleniumrequests import Chrome
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.common.exceptions import *
    
except ModuleNotFoundError as e:
    print('Module Not Found, Please Install > "pip install selenium" .')

desc='''

What is 'Selenium' ?
    - https://www.selenium.dev/documentation/ja/introduction/the_selenium_project_and_tools/
    - SeleniumはWebブラウザーを制御します。
    - 今回はChromeを使用しています。
    - 
    - https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    - 
'''

class WebAppCmd:

    AppName='Web Application (Auto Application | AI) Test Command by Selenium(WebDriver)'
    Description="""
    - First Program
    app=WebAppCmd(option=['--headless', '--[some option]', '--[some option]'])
    app.command('Dos')
    app.close()
        - or -
    app.quit()
    """

    def __init__(self, option=['--headless']):
        self.options = ChromeOptions()
        self.options.page_load_strategy='none'
        if len(option)>0:
            for o in range(0, len(option)):
                self.options.add_argument(option[o])
        self.driver = Chrome(options=self.options)
    
    def close(self):
        self.driver.close()
    
    def quit(self):
        self.driver.quit()

    def get(self,url):
        self.driver.get(url)
    
    def setUrl(self,url):
        self.url=url
    def getUrl(self):
        return self.url

    def requestPost(self,url,param={}):
        self.driver.request('POST', url, data=param)
    
    def DDos(self):
        # 対象のウェブサイトやサーバーに対して複数のコンピューターから大量に行うこと
        # DDosの場合は複数のAnonymousなコンピュータ群が一斉に攻撃。
        pass

    def Dos(self, num=10):
        # 大量のデータや不正なデータを送り付けること(F5連打)
        self.get(self.getUrl())
        count=0
        while True:
            count+=1
            if count<num:
                self.driver.refresh()
    
    def SqlInjection(self):
        Injection=[
            """
            SELECT * FROM users WHERE name = 't' OR 't' = 't';
            """
            ,
            """
            SELECT * FROM users WHERE name = '\'' OR 1=1 --';
            """
        ]
        pass
    
    def Xss(self):
        # 攻撃対象のWebサイトの脆弱性を突き、攻撃者がそこに悪質なサイトへ誘導するスクリプトを仕掛けることで、
        # サイトに訪れるユーザーの個人情報などを詐取する攻撃のことを指します。
        XssScript=[
            """
                while(true){
                    window.location.href='echo /etc/passwd'
                }
            """
        ]
        pass

    def DirectoryTraversal(self):
        # ファイル名を扱うようなプログラムに対して特殊な文字列を送信することにより、
        # 通常はアクセスできないファイルやディレクトリ（フォルダ）の内容を取得する手法。
        Dt='cd ../|cat /etc/passwd'
        pass

    def BootstrapForm(self):
        pass
    
    def getScript(self, javascript):
        return javascript
    
    def setScript(self, javascript):
        self.javascript=javascript

    def HtmlSelector(self, selector='body'):
        # Initialize Tag='<body> Tag's'
        header=driver.find_element(By.CSS_SELECTOR, selector)
        self.driver.execute_script(self.javascript, header)

    # 耐久系
    def getTable(self):
        return self.tbl

    def sertTable(self, name):
        self.tbl=name

    def AutoInsert(self):
        sql=f'INSERT INTO {self.tbl} VALUES(?, ?, ?, ?, ?, ?,?,?);'


    def AutoSelect(self):
        sql=f'SELECT * FROM {tbl};'

    def AutoUpdate(self):
        pass

    def AutoDelete(self):
        pass
    
    def buttonClick(self, id):
        new_doc=self.driver.find_element(By.ID, id)
        # .clickでは、画面操作が必要のため、下記に変更、JS呼び出し
        self.driver.execute_script("arguments[0].click();", new_doc) 

    def setJS(self, javascript):
        selector='body'
        header=self.driver.find_element(By.CSS_SELECTOR, selector)
        self.driver.execute_script(javascript, header)

    def demo(self):
        # デモンストレーション
        #1. 説明
        #2. 
        pass

# Test:=

# Thread化&Sleepすることで、待機時間を強制的についくる。
# 動作自体は関数化するする。
# A(Thread) - Start
# A(Sleep(Time)) - Aの動作
# B(Thread) - Start
# B(Sleep(Time)) - Bの動作
# 終了後にブラウザを閉じる。


def Pattern01():
    url='''data:text/html;charset=utf-8,
    <html contenteditable><head><meta charset='utf-8'><title>Selenium Demo 2021.</title></head>
    <body>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    </body></html>'''
    w=WebAppCmd([])
    w.get(url)

    javascript='''
    /* Javascript Code >>
        - URL部分は[ データURIスキーム ]を使用しています。
        - アドレスバーなどに直接HTMLがかけちゃいます。便利♪
            - sample code => [data:text/html;charset=utf-8,<html>....(Please,You write HTML Codes.)</html>]
        
        ↓ ここから下の行がJavascriptのコードです。Pythonから呼び出されています。
        （DocString形式で書くと、複数行にまたがってかけるので、楽ちん♪♪♪楽ちん♪♪♪）
    */
    message=[
        'こんにちは :)<br><br>',
        'はじめまして<br>',
        'Seleniumって知っていますか？<br>',
        'Seleniumとは、なんでしょうか？？？？？？<br>',
        'Seleniumは、簡単にいうとPytonプログラムからブラウザを操作する(自動化)アプリケーションです。<br>',
        'ドキュメントは、<h href="https://www.selenium.dev/documentation/ja/">https://www.selenium.dev/documentation/ja/</a><br>',
        'このプログラムは自動化したプログラムなのです。<br>',
        'なので、動作をAIにが学習したりで、ブラウザを操作するなんてことも可能かなと感じました。。ただし、学習・認識パターンはたくさんなので、人手がかかりそう（汗）。。。。<br>',
        '今回のデモは自動化の部分とSampleWebApp on Rasberry PI（JITAKU KEIBI）な環境で「えいやっっっ！！！」と仕上げてみました。<br>',
        'ひとりでできるもん！なプロジェクトなので、途中までになっちゃうかもですが、よろしくお願いします。<br>',
        'では、はじめましょう！！！（タブが１個開きますよ〜、自動的だよ。そういうふうにプログラムしました。）<br>',
        'クロスブラウザ・クロスプラットフォームの自動化<br>',
        '対応ブラウザは、Chorme, Firefox, Edge, Opera, Safariのウェブドライバーを利用します。<br>',
        '<a href="https://www.selenium.dev/documentation/ja/webdriver/driver_requuirements/">クイックリファレンス</a>',
        'ドライバーは、実行可能パスに追加します。（環境パス：echo $PATH or echo %PATH%で調べられます。）<br>',
        '実行環境パスを調べるのは忘れないようにしまししょう。また、管理者権限を持っている場合はその方が良いです。<br>',
        '一番苦悩しているのは、Seleniumnの処理待機について。処理待機は現状、Threadでの並列処理を目指しましたが、うまく動作しない。<br>',
        'ネットに繋がっていないので、現状では調査のみ。<br>',
        '体裁を整えて、パワポで出力。<br>',
        ''
    ];
    count=0;
    // 
    // alert(message.length)
    // Text Animation.
    // 
    timer=1500
    setInterval(function(){
        if(count < message.length){
            data=$(document.body).html()+message[count];
            $(document.body).html(data);
        }
        count++;
    }, timer);
    '''

    # w.driver.fullscreen_window()
    w.setJS(javascript)
    print(w.driver.window_handles)

def Pattern02():
    url='http://localhost:50000/'
    # Action: 
    # actions=ActionChains(w.driver)
    # actions.key_down(Keys.CONTROL).click().key_up(Keys.CONTROL).perform()
    # new_window = w.driver.window_handles[-1]
    w=WebAppCmd([])
    w.driver.switch_to.window(w.driver.window_handles[-1])
    # 
    w.get(url)
    # w.driver.refresh()

# UX診断
def Pattern03():
    
    pass


# Thread
Th=[]
Th.append(Thread(target=Pattern01))
Th.append(Thread(target=Pattern02))

for T in range(0, len(Th)):
    # スレッド開始
    Th[T].start()
    # 待ちの発生（30秒）
    sleep(30)

# WebDriverWait(w.driver).until(w.close)
# w.close()

'''
driver=Chrome()
driver.get('http://localhost:50000/')

header=driver.find_element(By.CSS_SELECTOR, 'body')
driver.execute_script(javascript, header)
# print(new_doc)
'''