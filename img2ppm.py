# 必要なライブラリのインポート
import os
import sys
import glob
import shutil

import cv2

# 引数指定された変換対象のディレクトリの中身を全てリストで取得する
db_path = glob.glob(os.path.join(sys.argv[1] + "/*"))
# 変換対象一覧を表示
print("変換対象:{}".format([os.path.basename(name) for name in db_path]))

# 変換結果の格納先ディレクトリを作成
result_path = "./result/"
if(os.path.isdir(result_path) == True):
    shutil.rmtree(result_path)  # ./result/ が既に存在する場合は削除
os.makedirs(result_path, exist_ok=True)

cnt = 1
# 変換対象を1枚ずつ変換していく
for filename in db_path:
    # 画像を読み込み
    img = cv2.imread(filename)

    # ファイル名(拡張子無し)を抽出
    name = os.path.splitext(os.path.basename(filename))[0]
    # 出力名を作成
    resultname = result_path + name + ".ppm"

    # 画像を書き出し
    cv2.imwrite('{}'.format(resultname), img)
    print("変換結果({}件目):{}".format(cnt,resultname))
    cnt += 1
print("変換完了")