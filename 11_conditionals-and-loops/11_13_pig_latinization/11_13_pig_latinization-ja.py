# CodingNomadsのコラボレーションストーリーのテキストを以下から取得します。
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt (英語)
# これをスクリプトの変数に保存します。複数行の文字列を作成する場合は、
# 三重引用符を忘れずに使用してください。
#
# `for`ループを使用してストーリーのテキストを反復処理し、
# 文字列スライシングでピッグラテン(ラテン語風の言葉遊び)に翻訳します。
# このプログラムでは、どのような単語や名前でも、最初の文字を最後に移動し、
# その後に「ay」を続ければ、ピッグラテンに翻訳できることにします。
# 単語の終わりを判断するために、条件文を使用しなければなりません。
#
# 例:You would never guess --> ouyay ouldway evernay uessgay
