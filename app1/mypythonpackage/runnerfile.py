import requests

def download_video(url, save_path):
    """
    Downloads a video from the given URL and saves it to the specified path.
    
    :param url: str - The URL of the video to download.
    :param save_path: str - The path (including filename) where the video will be saved.
    """
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Download complete: {save_path}")
    else:
        print(f"Failed to download video. Status code: {response.status_code}")


download_video("https://youtu.be/kDC4MxBlrIw?si=lXhaB78hPx-Hfa_o", "video.mp4")
