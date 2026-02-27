# YouTube Playlist URL Extractor

YouTubeの再生リストURLを入力すると、含まれる動画のURL一覧を取得するWebアプリです。
取得したURLリストをNotebookLMに追加する用途を想定しています。

## 使い方

1. 再生リストのURLを入力
2. 「URLを取得」ボタンをクリック
3. 表示されたURLリストをコピーしてNotebookLMに貼り付け

## ローカル実行

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 技術スタック

- [Streamlit](https://streamlit.io/) — Web UI
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — YouTube再生リスト情報の取得
