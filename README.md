# turk 
- (26. 3. 23 closing) 上のコードに出てくるSQLを下記のような感じに変えるかも知れません。私がこのような報告をする度に「私が破滅する確率」みたいなものについての情報が更新されているかも知れないとも思います。もしそうだとしたらコードを読める方がそのような予測を行っているのではないかとも思います。ここでの「私の破滅」とはturkがうまく動かずに皆様がこれを手動操縦している私が寝落ちしたのではないかと思うような現象が発生すること等を意味しています。これがうまく動くかは分かりませんが、私は他にもturkの挙動の予測を困難にする為の仕掛けを追加するかも知れません。あと学校等でプログラミングを勉強されているお子様がおられる方はこのコードについて聞いてみて下さい。 
``` sql
select url, title, lang from mixed 
where used = 0 and outlet in ('HBIZ', 'KPOP', 'PBS', 'SDOT', 'MSNBC', 'FOX') 
order by substr(date, 1, 13)+random() DESC
limit 1
```
- (26. 3. 23 Part3) 夜間に聯合ニュースのフィードが枯渇した場合をテストしておきたいのでこの機能をしばらくランダムに呼び出すようにします。実行環境上でのコードの変更点は下記の通りです: 
```python
    cs.execute('''
        select url, title, lang from mixed 
        where used = 0 and outlet in ('HBIZ', 'KPOP', 'PBS', 'SDOT', 'MSNBC', 'FOX') 
        order by random()
    ''')
    feeds_alt = cs.fetchall()
    if (len(feeds_alt) != 0 and random.randint(0, 5) == 0): 
        prefer_alt = True
    else: 
        prefer_alt = False
    if (len(feeds) == 0 or prefer_alt): 
        # if yonhap news is unavailable for us now or, 
        # we feel like using some other news outlets, 
        # then try using one of them. 
        if (len(feeds_alt) == 0): 
            feed = f.entries[0]
            f_url = feed.link
            f_title = feed.title
            f_lang = "ko"
        else: 
            feed = feeds_alt[0]
            f_url = feed[0]
            #f_title = '이걸 대신 사용: ' + feed[1]
            f_title = feed[1]
            f_lang = feed[2]        
            cs.execute('''
                update mixed set used = 1 
                where url = ? 
            ''', 
            (f_url,))
    else: 
        feed = feeds[0]
        f_url = feed[0]
        f_title = feed[1]
        f_lang = feed[2]
        cs.execute('''
            update feeds set used = 1 
            where url = ? 
        ''', 
        (f_url,))
```
- (26. 3. 23 Part2) 画面上部に表示していたNewsisのフィードも停滞することがあったようなので別の方法でニュースを取得するよう変更しました。これに伴い夜間に例の文言が表示されなくなりますが、これは私が義母が悪の根源だと考えていないということを意味するのではありません。 
  - https://github.com/anissatta/turk/commit/0330398641425207cbb3e8c166287ffa3d65fc75
- (26. 3. 23 Part1) 聯合ニュースが新しい記事をあまり出さない時間帯にフィードが枯渇し同じ記事が連続して表示されるケースがまだあるようなのでそれに対する対策を追加しました。今回はヘラルド経済を使用しましたが、この辺のロジックを予告なしに変更する可能性があります。また聯合ニュースが私に協力して下さらない場合にあまり「良くない」ニュースサイトを取得元に追加するかも知れません。 
  - https://github.com/anissatta/turk/commit/d1e2b81c79e930879f49cd0115fb1b81cc4bd837
- (26. 3. 22 closing) 今後dbの古いデータを削除したりするスクリプトを書くかも知れませんが、これに時間を取られるのがあまりに馬鹿馬鹿しいので本レポジトリを一旦アーカイブ化します。私が未だに理解出来ないのは"IT革命"から30余年が経つ今日でもこのような単純なアルゴリズムを理解されず、私が何か滑稽な、いかにも皆様が想像する「発達障害的」な方法でturkを手動操縦しているのではないかと思われているようであることです。皆様にまず考えて頂きたいのは仮に私がこれを手動操縦しているとして、その為に私がどのようなアプリ等を使用しているのかということ(そのアプリは皆様が入手可能かつ簡単に操作できるものであるはずですが)、それとこのことや私について過去に流れていた他の噂(Amazonで無賃労働をしていたのではないかとか、他の現実にはありえないような噂です)が実際の発達障害の特徴に沿ったものなのか、ということです。私が発達障害だという噂のためか私を見に来る方々の中にはそのような方々もおられるのですが(それはお母様を伴った若年男性が多いようです)、私はこのような噂が流れることが発達障害の方々に迷惑をかけているのではないかとも思います。私の意見ですが、このような噂が流れる背景にあるのは集中力の欠如、論理性の欠如、および自らより劣っていると思われる者への寵愛的な執着だと思います。これらはいずれも私の中には見出されないものなのですが(特に3番目については殆どありません)、皆様が私が「発達障害」であるという噂に執着されているのは皆様自身の精神的な弱さのせいだと私は思います。皆様の人生における戦いは、皆様と直接関係ない皆様より劣っている存在(つまりは私)とは無関係に進行しています。私についての噂が流れ始めた頃ならまだしもこの噂はもう7才になります。このturkが皆様が皆様自身の人生を取り戻す機会になることを祈っています。 
- (26. 3. 22 Part3) kiwipiepyという形態素解析器を使った簡単な統計を行うためのコードを追加しました。
  - https://github.com/anissatta/turk/blob/main/bot.py
  - https://github.com/anissatta/turk/blob/main/get-stat1.py
  - https://github.com/anissatta/turk/blob/main/print_mdjson.sh
- (26. 3. 22 Part2) 上部に表示されるニュースについても同様の対策を実施しました。これに伴い日中と夜間とでのフィード取得先の区別が無くなります。 
  - https://github.com/anissatta/turk/blob/main/bot.py
- (26. 3. 22 Part1) 聯合ニュースの同じ記事が連続して表示される事態への対策として下記コードを若干改良しました。
  - https://github.com/anissatta/turk/blob/main/bot.py
- (26. 3. 19) この地域で流れていると思われる噂に対抗するためにボット(bot)のソースコードを公開することにしました。元々公開するつもりの無かったものなので無茶苦茶ですが、大して分量の無いものだとお分かりになるかと思います。これは以前公開していたkamsysのコードを改造したものです。 
- It surprised me to find that, even in 2026 people here seemed to believe that what they saw was in fact something like a [*Mechanical Turk*](https://en.wikipedia.org/wiki/Mechanical_Turk) and I was acting like them... https://youtube.com/shorts/OjmPU9-TvkM
