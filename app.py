import streamlit as st
import yt_dlp


def extract_video_urls(playlist_url: str) -> list[dict]:
    """再生リストから動画のURL・タイトル一覧を抽出する"""
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)

    if not info:
        return []

    entries = info.get("entries", [])
    videos = []
    for entry in entries:
        if entry is None:
            continue
        video_id = entry.get("id", "")
        title = entry.get("title", "不明")
        url = entry.get("url") or f"https://www.youtube.com/watch?v={video_id}"
        videos.append({"title": title, "url": url})

    return videos


# --- Streamlit UI ---

st.set_page_config(page_title="YT Playlist → URL List", page_icon="📺")

st.title("📺 YouTube Playlist URL Extractor")
st.caption("再生リストのURLを入力すると、含まれる動画のURL一覧を取得します")

playlist_url = st.text_input(
    "YouTube 再生リスト URL",
    placeholder="https://www.youtube.com/playlist?list=PLxxxxxxx",
)

if st.button("URL を取得", type="primary", disabled=not playlist_url):
    with st.spinner("再生リストを読み込み中..."):
        try:
            videos = extract_video_urls(playlist_url)
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
            videos = []

    if videos:
        st.success(f"{len(videos)} 件の動画が見つかりました")

        # URL一覧テーブル
        for i, v in enumerate(videos, 1):
            st.markdown(f"**{i}.** [{v['title']}]({v['url']})")

        # コピー用テキストエリア
        st.divider()
        st.subheader("📋 コピー用 URL リスト")
        url_text = "\n".join(v["url"] for v in videos)
        st.code(url_text, language=None)

        # NotebookLM 向けの説明
        st.divider()
        st.subheader("📓 NotebookLM に追加する方法")
        st.markdown(
            """
1. 上の URL リストをコピー
2. [NotebookLM](https://notebooklm.google.com/) を開く
3. ノートブックの **ソースを追加** → **YouTube** を選択
4. URL を1つずつ貼り付けて追加
"""
        )
    elif playlist_url:
        st.warning("動画が見つかりませんでした。URLが正しいか確認してください。")
