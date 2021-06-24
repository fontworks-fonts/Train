[English](https://github.com/fontworks-fonts/Train) /[日本語](README-JP.md) 

![TrainOne-Regular](./image_Train.png)

## トレイン One-Regular

「トレイン」（GoogleFonts提供名称）は、アウトラインの内側と外側の二重のラインで形成されるゴシック系書体です。そのままロゴやタイトルとしても使用できるほど、インパクトがあり、快活でオープンなイメージを与えるデザインです。  
（Fontworksがリリースしている書体名称は「レイルウェイ」です。）  
このフォントについての詳しい情報は[こちら](https://fontworks.co.jp/fontsearch/RailwayStd-B/)をご覧ください。


### フォントのダウンロード

以下のページより、ビルド済みのTrueTypeフォントをダウンロードできます。  

[最終リリース](https://github.com/fontworks-fonts/Train/tree/master/fonts/ttf)


### ソースからのフォントのビルド手順

#### 要件

* [python3](https://www.python.org/)  
* [fontmake](https://github.com/googlefonts/fontmake/)
* [fonttools](https://github.com/fonttools/fonttools/)
* [ttfautohint](https://www.freetype.org/ttfautohint/doc/ttfautohint.html)  


#### フォントのビルド

ワーキングディレクトリ(カレントディレクトリ)を「Train」フォルダへ変更し、**build.py**を実行します。

    $ python build.py

**--autohinting**コマンドラインオプションを指定すると、ttfautohintを使用してヒントを付与します。

    $ python build.py --autohinting

### ライセンス

* 個人利用・商用利用にかかわらずどなたでも無料でお使いいただけます。
* ゲームやアプリなどへの組み込みやwebフォントとしての利用も可能です。
* このフォントを使用し、派生フォントを作ることもできます。ただし、配布の際はSIL Open Font Licenseに基づいてリリースする必要があります。
* SILライセンスについて詳しくは[SIL Open Font License 1.1 日本語訳](https://licenses.opensource.jp/OFL-1.1/OFL-1.1.html)または同梱の「OFL.txt」(英語)をご確認ください。


### 収録文字

* カタカナ、ひらがな、英数字、記号類、JIS第一水準漢字など
* [GF Latin Core](https://github.com/googlefonts/gftools/tree/master/Lib/gftools/encodings/GF%20Glyph%20Sets#gf-latin-core)  


### 禁止行為

* 「SIL Open Font License Version 1.1」以外のライセンスで再配布すること。
* フォントファイル自体を単体で販売すること。
